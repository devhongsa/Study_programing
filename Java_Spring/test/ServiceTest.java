// @BeforEach에서 given으로 설정해줬던것들이 모든 테스트메소드에서 필요한것이 아니기 때문에, 이 설정을 넣어줘야 테스트돌릴때 경고메세지가 안뜸 
@MockitoSettings(strictness = Strictness.LENIENT) 
@ExtendWith(MockitoExtension.class) // @Mock 어노테이션 사용가능 
class TransactionServiceTest {
    @Mock
    TransactionRepository transactionRepository;
    @Mock
    private AccountUserRepository accountUserRepository;
    @Mock
    private AccountRepository accountRepository;

    // 위에 @Mock으로 생성했던 Repository객체들을 transactionService객체에 주입한다.
    // transactionService의 메소드에서 repository를 사용하기때문에 의존성 주입을 해주는 것임.
    // 그래야 transactionService의 메소드들을 테스트해볼 수 있게 됨.
    @InjectMocks 
    private TransactionService transactionService;

    @Test
    @DisplayName("잔액사용 성공")
    void successUseBalance() {
        //given
        // given 부분은 테스트 메소드마다 반복되게 때문에 @BeforeEach로 빼는 것이 좋음
        AccountUser user = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();

        Account account = Account.builder()
                .accountUser(user)
                .accountStatus(AccountStatus.IN_USE)
                .balance(10000L)
                .accountNumber("1111111111")
                .build();

        // TransactionService의 useBalance메소드에서 Repository관련 실행한 모든메소드를 given으로 줘야함.
        given(accountUserRepository.findById(anyLong()))
                .willReturn(Optional.of(user));
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.of(account));
        given(transactionRepository.save(any()))
                .willReturn(Transaction.builder()
                        .account(account)
                        .transactionType(TransactionType.USE)
                        .transactionResultType(TransactionResultType.S)
                        .transactionId("txsId")
                        .transactedAt(LocalDateTime.now())
                        .amount(1000L)
                        .balanceSnapshot(9000L)
                        .build());

        // save() 검증할때 save의 인자로 들어갈 Transaction 객체를 captor로 설정, save 인자에 Transaction 객체가 들어가는지 검증함.
        ArgumentCaptor<Transaction> captor = ArgumentCaptor.forClass(Transaction.class);

        //when
        TransactionDto transactionDto = transactionService.useBalance(1L, "1111111111", 200L);

        //then
        // verify는 행위에 대한 테스트임.
        // times(1) : save() 함수가 1번 실행됬다는걸 검증 , atLeastOnce()랑 동일, never()는 한번도 실행 안됐다.
        // 여기서 transactionRepository는 Mock객체이다.
        // 만약 @Mock으로 객체주입을 안해줬으면, TransactionRepository mock = mock(TransactionRepository.class) 를 선언해주고 사용해야함
        // captor.capture()은 테스트를 진행하면서 save()에 어떤 실제 어떤 인자가 들어갔는지 capture함. 즉 위에 given으로 주어진 정보들을 토대로 메소드를 거치면서
        // save() 안에 어떤 인자가 들어갔는지 검증하기 위한 작업임. 즉 인자 검증 테스트임.
        verify(transactionRepository, times(1)).save(captor.capture());
        assertEquals(200L,captor.getValue().getAmount());
        assertEquals(9800L,captor.getValue().getBalanceSnapshot());

        // 상태 테스트 
        assertEquals(9000L, transactionDto.getBalanceSnapshot());
        assertEquals(TransactionType.USE, transactionDto.getTransactionType());
        assertEquals(TransactionResultType.S, transactionDto.getTransactionResultType());
        assertEquals(1000L, transactionDto.getAmount());
    }

    @Test
    @DisplayName("잔액 사용 실패 - 해당 유저 없음")
    void failUseBalance_UserNotFound() {
        //given
        given(accountUserRepository.findById(anyLong()))
                .willReturn(Optional.empty());

        //when
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.useBalance(1L, "1111111111",100L));

        //then
        assertEquals(ErrorCode.USER_NOT_FOUND, exception.getErrorCode());

        // 위에 when, then을 합쳐놓은 거 
        assertThatThrownBy(() -> transactionService.useBalance(1L, "1111111111", 100L)).isInstanceOf(AccountException.class).hasFieldOrPropertyWithValue("errorCode", ErrorCode.USER_NOT_FOUND);
    }

    @Test
    @DisplayName("잔액 사용 실패 - 해당 계좌 없음")
    void failUseBalance_AccountNotFound() {
        //given
        AccountUser user = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();

        given(accountUserRepository.findById(anyLong()))
                .willReturn(Optional.of(user));
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.empty());

        //when
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.useBalance(1L, "1111111111",100L));

        //then
        assertEquals(ErrorCode.ACCOUNT_NOT_FOUND, exception.getErrorCode());
    }

    @Test
    @DisplayName("잔액 사용 실패 - 계좌 소유주 다름")
    void failUseBalance_UserAccountUnMatch() {
        //given
        AccountUser pobi = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();

        AccountUser harry = AccountUser.builder()
                .id(13L)
                .name("Harry").build();

        given(accountUserRepository.findById(anyLong()))
                .willReturn(Optional.of(pobi));
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.of(Account.builder()
                        .accountUser(harry)
                        .balance(0L)
                        .accountNumber("1000000012").build()));

        //when
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.useBalance(1L, "1111111111",100L));

        //then
        assertEquals(ErrorCode.USER_ACCOUNT_UN_MATCH, exception.getErrorCode());
    }

    @Test
    @DisplayName("잔액 사용 실패 - 계좌가 이미 해지되었음")
    void failUseBalance_AccountAlreadyUnregistered() {
        //given
        AccountUser user = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();

        given(accountUserRepository.findById(anyLong()))
                .willReturn(Optional.of(user));
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.of(Account.builder()
                        .accountUser(user)
                        .balance(0L)
                        .accountStatus(AccountStatus.UNREGISTERED)
                        .accountNumber("1000000012").build()));

        //when
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.useBalance(1L, "1111111111",100L));

        //then
        assertEquals(ErrorCode.ACCOUNT_ALREADY_UNREGISTERED, exception.getErrorCode());
    }

    @Test
    @DisplayName("잔액 사용 실패 - 거래금액이 잔고보다 많음.")
    void failUseBalance_AmountExceedBalance() {
        //given
        AccountUser user = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();
        Account account = Account.builder()
                .accountUser(user)
                .accountStatus(AccountStatus.IN_USE)
                .balance(1000L)
                .accountNumber("1111111111")
                .build();
        // TransactionService의 useBalance메소드에서 Repository관련 실행한 모든메소드를 given으로 줘야함.
        given(accountUserRepository.findById(anyLong()))
                .willReturn(Optional.of(user));
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.of(account));

        //when
        //then
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.useBalance(1L, "1111111111",1500L));

        //then
        assertEquals(ErrorCode.AMOUNT_EXCEED_BALANCE,exception.getErrorCode());
        verify(transactionRepository, times(0)).save(any());
    }

    @Test
    @DisplayName("잔액사용 실패 테스트 ")
    void successSaveFailedTransaction() {
        //given
        AccountUser user = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();
        Account account = Account.builder()
                .accountUser(user)
                .accountStatus(AccountStatus.IN_USE)
                .balance(10000L)
                .accountNumber("1111111111")
                .build();
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.of(account));
        given(transactionRepository.save(any()))
                .willReturn(Transaction.builder()
                        .account(account)
                        .transactionType(TransactionType.USE)
                        .transactionResultType(TransactionResultType.F)
                        .transactionId("txsId")
                        .transactedAt(LocalDateTime.now())
                        .amount(1000L)
                        .balanceSnapshot(9000L)
                        .build());

        ArgumentCaptor<Transaction> captor = ArgumentCaptor.forClass(Transaction.class);

        //when
        transactionService.saveFailedTransaction("1111111111", 200L);

        //then
        verify(transactionRepository, times(1)).save(captor.capture());
        assertEquals(200L,captor.getValue().getAmount());
        assertEquals(10000L,captor.getValue().getBalanceSnapshot());
        assertEquals(TransactionResultType.F,captor.getValue().getTransactionResultType());
    }

    @Test
    void successCancelBalance() {
        //given
        AccountUser user = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();
        Account account = Account.builder()
                .accountUser(user)
                .accountStatus(AccountStatus.IN_USE)
                .balance(10000L)
                .accountNumber("1111111111")
                .build();
        Transaction transaction = Transaction.builder()
                .account(account)
                .transactionType(TransactionType.USE)
                .transactionResultType(TransactionResultType.S)
                .transactionId("txsId")
                .transactedAt(LocalDateTime.now())
                .amount(1000L)
                .balanceSnapshot(10000L)
                .build();

        given(transactionRepository.findByTransactionId(anyString()))
                .willReturn(Optional.of(transaction));
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.of(account));

        given(transactionRepository.save(any()))
                .willReturn(Transaction.builder()
                        .account(account)
                        .transactionType(TransactionType.CANCEL)
                        .transactionResultType(TransactionResultType.S)
                        .transactionId("txsId2")
                        .transactedAt(LocalDateTime.now())
                        .amount(1000L)
                        .balanceSnapshot(11000L)
                        .build());

        ArgumentCaptor<Transaction> captor = ArgumentCaptor.forClass(Transaction.class);

        //when
        TransactionDto transactionDto = transactionService.cancelBalance("txsId", "1111111111", 1000L);

        //then
        verify(transactionRepository, times(1)).save(captor.capture());
        assertEquals(1000L,captor.getValue().getAmount());
        assertEquals(11000L,captor.getValue().getBalanceSnapshot());

        assertEquals(11000L, transactionDto.getBalanceSnapshot());
        assertEquals(TransactionType.CANCEL, transactionDto.getTransactionType());
        assertEquals(TransactionResultType.S, transactionDto.getTransactionResultType());
        assertEquals(1000L, transactionDto.getAmount());
    }

    @Test
    @DisplayName("거래 취소 실패 - 해당 계좌 없음")
    void failCancelBalance_AccountNotFound() {
        //given
        given(transactionRepository.findByTransactionId(anyString()))
                .willReturn(Optional.of(Transaction.builder().build()));
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.empty());

        //when
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.cancelBalance("txsId", "1111111111",100L));

        //then
        assertEquals(ErrorCode.ACCOUNT_NOT_FOUND, exception.getErrorCode());
    }

    @Test
    @DisplayName("거래 취소 실패 - 해당 거래 없음")
    void failCancelBalance_TransactionNotFound() {
        //given
        given(transactionRepository.findByTransactionId(anyString()))
                .willReturn(Optional.empty());

        //when
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.cancelBalance("txsId", "1111111111",100L));

        //then
        assertEquals(ErrorCode.TRANSACTION_NOT_FOUND, exception.getErrorCode());
    }

    @Test
    @DisplayName("거래 취소 실패 - 거래가 해당계좌에 존재하지 않습니다.")
    void failCancelBalance_TransactionAccountUnMatch() {
        //given
        AccountUser user = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();
        Account account = Account.builder()
                .id(1L)
                .accountUser(user)
                .accountStatus(AccountStatus.IN_USE)
                .balance(10000L)
                .accountNumber("1111111111")
                .build();
        Account accountNotUse = Account.builder()
                .id(2L)
                .accountUser(user)
                .accountStatus(AccountStatus.IN_USE)
                .balance(10000L)
                .accountNumber("1111111112")
                .build();
        Transaction transaction = Transaction.builder()
                .account(account)
                .transactionType(TransactionType.USE)
                .transactionResultType(TransactionResultType.S)
                .transactionId("txsId")
                .transactedAt(LocalDateTime.now())
                .amount(1000L)
                .balanceSnapshot(10000L)
                .build();

        given(transactionRepository.findByTransactionId(anyString()))
                .willReturn(Optional.of(transaction));
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.of(accountNotUse));

        //when
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.cancelBalance("txsId", "1111111112",1000L));

        //then
        assertEquals(ErrorCode.TRANSACTION_ACCOUNT_UN_MATCH, exception.getErrorCode());
    }

    @Test
    @DisplayName("거래 취소 실패 - 거래금액과 취소금액이 다름")
    void failCancelBalance_CancelMustFully() {
        //given
        AccountUser user = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();
        Account account = Account.builder()
                .accountUser(user)
                .accountStatus(AccountStatus.IN_USE)
                .balance(10000L)
                .accountNumber("1111111111")
                .build();
        Transaction transaction = Transaction.builder()
                .account(account)
                .transactionType(TransactionType.USE)
                .transactionResultType(TransactionResultType.S)
                .transactionId("txsId")
                .transactedAt(LocalDateTime.now())
                .amount(1000L)
                .balanceSnapshot(10000L)
                .build();

        given(transactionRepository.findByTransactionId(anyString()))
                .willReturn(Optional.of(transaction));
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.of(account));

        //when
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.cancelBalance("txsId", "1111111112",1500L));

        //then
        assertEquals(ErrorCode.CANCEL_MUST_FULLY, exception.getErrorCode());
    }

    @Test
    @DisplayName("거래 취소 실패 - 1년이 지난 거래는 취소가 불가능합니다.")
    void failCancelBalance_TooOldTransaction() {
        //given
        AccountUser user = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();
        Account account = Account.builder()
                .accountUser(user)
                .accountStatus(AccountStatus.IN_USE)
                .balance(10000L)
                .accountNumber("1111111111")
                .build();
        Transaction transaction = Transaction.builder()
                .account(account)
                .transactionType(TransactionType.USE)
                .transactionResultType(TransactionResultType.S)
                .transactionId("txsId")
                .transactedAt(LocalDateTime.now().minusYears(2))
                .amount(1000L)
                .balanceSnapshot(10000L)
                .build();

        given(transactionRepository.findByTransactionId(anyString()))
                .willReturn(Optional.of(transaction));
        given(accountRepository.findByAccountNumber(anyString()))
                .willReturn(Optional.of(account));

        //when
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.cancelBalance("txsId", "1111111112",1000L));

        //then
        assertEquals(ErrorCode.TOO_OLD_TRANSACTION_TO_CANCEL, exception.getErrorCode());
    }

    @Test
    void successQueryTransaction(){
        //given
        AccountUser user = AccountUser.builder()
                .id(12L)
                .name("Pobi").build();
        Account account = Account.builder()
                .accountUser(user)
                .accountStatus(AccountStatus.IN_USE)
                .balance(10000L)
                .accountNumber("1111111111")
                .build();
        Transaction transaction = Transaction.builder()
                .account(account)
                .transactionType(TransactionType.USE)
                .transactionResultType(TransactionResultType.S)
                .transactionId("txsId")
                .transactedAt(LocalDateTime.now().minusYears(2))
                .amount(1000L)
                .balanceSnapshot(10000L)
                .build();
        given(transactionRepository.findByTransactionId(anyString()))
                .willReturn(Optional.of(transaction));

        //when
        TransactionDto transactionDto = transactionService.queryTransaction("12345");

        //then
        assertEquals(TransactionType.USE,transactionDto.getTransactionType());
        assertEquals(TransactionResultType.S,transactionDto.getTransactionResultType());
        assertEquals(1000,transactionDto.getAmount());
        assertEquals("txsId",transactionDto.getTransactionId());
    }

    @Test
    @DisplayName("거래 조회 실패 - 해당 거래 없음")
    void failQueryTransaction() {
        //given
        given(transactionRepository.findByTransactionId(anyString()))
                .willReturn(Optional.empty());

        //when
        AccountException exception = assertThrows(AccountException.class,
                () -> transactionService.queryTransaction("txsId"));

        //then
        assertEquals(ErrorCode.TRANSACTION_NOT_FOUND, exception.getErrorCode());
    }
}