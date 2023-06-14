@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Entity
// @AuditOverride(forClass=BaseEntity.class)
// 위에꺼 쓰려면 implementation 'org.springframework.data:spring-data-envers' 해줘야함.
// 그리고 config에서 JpaAuditing 없어도 됨.
public class Account extends BaseEntity {
    @Id
    @GeneratedValue
    private Long id;

    @ManyToOne // FK 설정, AccountUser테이블의 PK값이 들어오게 된다.
    private AccountUser accountUser;

    private String accountNumber;

    @Enumerated(EnumType.STRING) // DB에 저장될때 ENUM의 순서번호가 아닌, 실제 STRING값으로 저장된다.
    private AccountStatus accountStatus;
    private Long balance;

    private LocalDateTime registeredAt;
    private LocalDateTime unRegisteredAt;

    // 잔고를 변경시키는 중요한 로직은 domain 내에서 구현하는 것이 좋음. 왜냐면 service에서 로직을 구현할때 balance를 호출하는
    // 일이 없어지기 때문.
    public void useBalance(Long amount) {
        if (amount > balance) {
            throw new AccountException(ErrorCode.AMOUNT_EXCEED_BALANCE);
        }
        balance -= amount;
    }

    public void cancelBalance(Long amount) {
        if (amount < 0) {
            throw new AccountException(ErrorCode.INVALID_REQUEST);
        }
        balance += amount;
    }
}
