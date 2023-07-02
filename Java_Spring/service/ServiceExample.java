// Example 1
@Service
@RequiredArgsConstructor
public class AccountService {
    private final AccountRepository accountRepository;
    private final AccountUserRepository accountUserRepository;

    /**
     * 유저있는지 확인
     * 유저의 계좌 갯수 확인
     * 계좌번호 생성
     * 저장 후, 정보 넘기기
     */
    @Transactional
    public AccountDto createAccount(Long userId, Long initialBalance) {
        AccountUser accountUser = accountUserRepository.findById(userId)
                .orElseThrow(() -> new AccountException(ErrorCode.USER_NOT_FOUND));

        String newAccountNumber = accountRepository.findFirstByOrderByIdDesc()
                .map(account -> (Integer.parseInt(account.getAccountNumber())) + 1 + "")
                .orElse("1000000000");

        validateCreateAccount(accountUser, newAccountNumber);

        return AccountDto.fromEntity(
                accountRepository.save(
                        Account.builder()
                                .accountUser(accountUser)
                                .accountStatus(IN_USE)
                                .accountNumber(newAccountNumber)
                                .balance(initialBalance)
                                .registeredAt(LocalDateTime.now())
                                .build()));
    }

    @Transactional
    public AccountDto deleteAccount(Long userId, String accountNumber) {
        AccountUser accountUser = accountUserRepository.findById(userId)
                .orElseThrow(() -> new AccountException(ErrorCode.USER_NOT_FOUND));
        Account account = accountRepository.findByAccountNumber(accountNumber)
                .orElseThrow(() -> new AccountException(ErrorCode.ACCOUNT_NOT_FOUND));

        validateDeleteAccount(accountUser, account);

        account.setAccountStatus(AccountStatus.UNREGISTERED);
        account.setUnRegisteredAt(LocalDateTime.now());

        accountRepository.save(account); // 원래 여기서 sava안해도 위에 Set할때 자동으로 업데이트됨. 이거는 테스트코드를 위해서 넣은거임.

        return AccountDto.fromEntity(account);
    }

    private void validateCreateAccount(AccountUser accountUser, String newAccountNumber) {
        if (accountRepository.findByAccountNumber(newAccountNumber).isPresent()) {
            throw new AccountException(ErrorCode.ACCOUNT_ALREADY_EXIST);
        }
        if (accountRepository.countByAccountUser(accountUser) >= 10) {
            throw new AccountException(ErrorCode.MAX_ACCOUNT_PER_USER_10);
        }
    }

    private void validateDeleteAccount(AccountUser accountUser, Account account) {
        if (!Objects.equals(accountUser.getId(), account.getAccountUser().getId())) {
            throw new AccountException(ErrorCode.USER_ACCOUNT_UN_MATCH);
        }
        if (account.getAccountStatus() == AccountStatus.UNREGISTERED) {
            throw new AccountException(ErrorCode.ACCOUNT_ALREADY_UNREGISTERED);
        }
        if (account.getBalance() > 0) {
            throw new AccountException(ErrorCode.BALANCE_NOT_EMPTY);
        }
    }

    @Transactional
    public List<AccountDto> getAccountsByUserId(Long userId) {
        AccountUser accountUser = accountUserRepository.findById(userId)
                .orElseThrow(() -> new AccountException(ErrorCode.USER_NOT_FOUND));

        List<Account> accounts = accountRepository.findByAccountUser(accountUser);

        return accounts.stream()
                .map(AccountDto::fromEntity)
                .collect(Collectors.toList());
    }

}




// Example 2 
@Slf4j
@Service
@RequiredArgsConstructor
@Transactional
public class CustomerService {

    private static final int MINUTES_PRIOR_TO_VISIT = 10;
    private static final int RESERVATION_LIMIT = 50;

    private final ReservationRepository reservationRepository;
    private final UserRepository userRepository;
    private final StoreRepository storeRepository;
    private final ReviewRepository reviewRepository;

    /*
        예약하기
        1. Customer 유저 확인
        2. 예약하려는 상점 유무 확인
        3. validateReservationTime : 예약이 가능한 시간인지 체크
        4. 예약
     */
    public Reservation addReservation(ReservationDto.Reserve reserve) {

        User user = userRepository.findByUsername(reserve.getUserName())
                .orElseThrow(() -> new CustomException(CustomErrorCode.USER_NOT_FOUND));

        Store store = storeRepository.findById(reserve.getStoreId())
                .orElseThrow(() -> new CustomException(CustomErrorCode.STORE_NOT_FOUND));

        validateReservationTime(reserve.getReservationTime(), user.getId(), store.getId());

        return reservationRepository.save(reserve.toEntity(user, store));
    }

    /*
        예약시간 유효성 체크
        1. 현재시간이 만약 예약시간 10분전(도착해야하는 시간)보다 뒤라면 예약불가,
        2. 유저가 해당시간에 이미 예약했으면 예약 불가,
        3. 해당 예약시간에 예약건수가 50건 이상일때 예약불가
     */
    private void validateReservationTime(String reservationTime, Long userId, Long storeId) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        LocalDateTime formattedDateTime = LocalDateTime.parse(reservationTime, formatter);

        if (LocalDateTime.now().isAfter(formattedDateTime.minusMinutes(MINUTES_PRIOR_TO_VISIT))) {
            throw new CustomException(CustomErrorCode.UNABLE_TO_RESERVATION);
        }

        if (reservationRepository.existsByUserIdAndStoreIdAndReservationTime(
                userId, storeId, formattedDateTime)) {
            throw new CustomException(CustomErrorCode.RESERVATION_ALREADY_EXISTS);
        }

        if (reservationRepository.countByStoreIdAndIsCanceledAndReservationTime(
                storeId, false, formattedDateTime) >= RESERVATION_LIMIT) {
            throw new CustomException(CustomErrorCode.RESERVATION_IS_FULL);
        }
    }

    /*
        리뷰 추가
        1. 유저, 상점 유무 확인
        2. 리뷰를 쓸 수 있는 지 유효성 검증
        3. 리뷰 DB에 저장, 저장한 Review 엔티티 리턴
     */
    public Review addReview(ReviewDto.ReviewRequest request) {
        User user = userRepository.findByUsername(request.getUsername())
                .orElseThrow(() -> new CustomException(CustomErrorCode.USER_NOT_FOUND));
        Store store = storeRepository.findById(request.getStoreId())
                .orElseThrow(() -> new CustomException(CustomErrorCode.STORE_NOT_FOUND));

        validateReview(user, store);

        return reviewRepository.save(request.toEntity(user, store));
    }

    /*
        리뷰 유효성 검증
        1. 실제 방문을 한 상점인지 확인
     */
    private void validateReview(User user, Store store) {
        if (!reservationRepository.existsByUserAndStoreAndIsVisited(user, store, true)) {
            throw new CustomException(CustomErrorCode.REVIEW_NOT_ALLOWED);
        }
    }
}



///// return Entity or DTO ??
// Spring의 @Service에서 Controller에 객체를 반환할 때, Entity를 반환하는 것이 좋은지 아니면 DTO를 만들어서
// 반환하는 것이 좋은지에 대해서는 일반적인 가이드라인이 있지만, 최종 결정은 상황과 요구사항에 따라 다를 수 있습니다.

// 일반적으로는 DTO를 만들어서 반환하는 것이 좋습니다. 이는 다음과 같은 이유로 권장됩니다:

// 엔티티와 비즈니스 로직의 분리: 엔티티 클래스는 데이터베이스와 직접적으로 연관되어 있으며, 비즈니스 로직에 집중되어야 합니다. 엔티티
// 클래스를 그대로 노출하면, 비즈니스 로직과 데이터베이스 스키마가 결합되어 유지 보수와 테스트에 어려움을 초래할 수 있습니다. DTO를
// 사용하면 엔티티와 컨트롤러 간의 분리를 유지할 수 있습니다.

// 보안 및 데이터 노출 제어: DTO를 사용하면 필요한 데이터만을 전송할 수 있으며, 민감한 정보를 숨길 수 있습니다. 클라이언트에 불필요한
// 정보를 노출하지 않고, 보안 및 개인 정보 보호를 위해 필요한 필드만을 제공할 수 있습니다.

// API 설계 및 확장성: DTO를 사용하면 API 인터페이스를 명확하게 정의할 수 있습니다. 클라이언트가 필요한 데이터를 명확하게 알고
// 있을 때, 필요한 필드만을 DTO에 포함시킬 수 있습니다. 또한, 엔티티 구조가 변경되더라도 DTO 구조는 유지되므로 API와 클라이언트
// 간의 결합도를 낮출 수 있습니다.

// 그러나 몇 가지 상황에서는 Entity를 직접 반환하는 것이 적절할 수도 있습니다:

// 간단한 애플리케이션: 간단한 애플리케이션의 경우, 별도의 비즈니스 로직이 없을 수 있으며, DTO를 생성하고 관리하는 비용이 불필요할 수
// 있습니다. 이러한 경우에는 Entity를 직접 반환해도 문제가 되지 않을 수 있습니다.

// 성능 및 부하 문제: DTO를 생성하고 변환하는 과정이 성능에 영향을 미칠 수 있습니다. 대량의 데이터를 다루거나, 빠른 응답이 필요한
// 경우에는 Entity를 직접 반환하는 것이 성능 측면에서 유리할 수 있습니다. 그러나 이는 특정 상황에서의 최적화로서, 성능 테스트와 함께
// 신중하게 결정해야 합니다.

// 요약하면, 대부분의 경우 DTO를 사용하여 엔티티와 컨트롤러 간의 분리를 유지하는 것이 권장됩니다. DTO를 통해 보안, API 설계,
// 유지 보수 등 다양한 이점을 얻을 수 있습니다. 그러나 간단한 애플리케이션이나 성능에 민감한 상황에서는 Entity를 직접 반환하는 것이
// 효율적일 수 있습니다. 최종적인 결정은 애플리케이션의 요구사항, 복잡성, 확장성 등을 고려하여 적절한 방식을 선택해야 합니다.