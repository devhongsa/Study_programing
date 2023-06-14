@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class AccountException extends RuntimeException {
    private ErrorCode errorCode;
    private String errorMassage;

    public AccountException(ErrorCode errorCode) {
        this.errorCode = errorCode;
        this.errorMassage = errorCode.getDescription();
    }
}
