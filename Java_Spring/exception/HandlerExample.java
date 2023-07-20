// Example 1 
@Slf4j
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(AccountException.class)
    public ErrorResponse handleAccountException(AccountException e) {
        log.error("{} is occurred.", e.getErrorCode());
        return new ErrorResponse(e.getErrorCode(), e.getErrorMassage());
    }

    // DataBase관련 오류들은 은근히 자주 등장하기 때문에 errorhandler 추가
    @ExceptionHandler(DataIntegrityViolationException.class)
    public ErrorResponse handleDataIntegrityViolationException(DataIntegrityViolationException e) {
        log.error("DataIntegrityViolationException is occurred.", e);

        return new ErrorResponse(INVALID_REQUEST, INVALID_REQUEST.getDescription());
    }

    @ExceptionHandler(Exception.class)
    public ErrorResponse handleAccountException(Exception e) {
        log.error("Exception is occurred.", e);

        return new ErrorResponse(INTERNAL_SERVER_ERROR, INTERNAL_SERVER_ERROR.getDescription());
    }
}


// Example 2 
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@Slf4j
@RestControllerAdvice
public class GlobalExceptionHandler {

    /*
        커스텀 exception 발생시 핸들러
     */
    @ExceptionHandler(CustomException.class)
    public ResponseEntity<ErrorResponse> handleAccountException(CustomException e) {
        ErrorResponse response = ErrorResponse.builder()
                .statusCode(e.getStatus().value())
                .errorCode(e.getErrorCode())
                .errorMessage(e.getErrorMessage())
                .build();
        log.error("{} is occurred.",e.getErrorCode());
        return new ResponseEntity<>(response, e.getStatus());
    }

    /*
        api 접근 권한 설정으로 요청 제한이 되었을때 핸들러
     */
    @ExceptionHandler(AccessDeniedException.class)
    public ResponseEntity<ErrorResponse> handleAccessDeniedException(AccessDeniedException e) {
        ErrorResponse response = ErrorResponse.builder()
                .statusCode(HttpStatus.FORBIDDEN.value())
                .errorCode(CustomErrorCode.ACCESS_DENIED)
                .errorMessage(CustomErrorCode.ACCESS_DENIED.getErrorMessage())
                .build();
        log.error("Access Denied: {}", e.getMessage());
        return new ResponseEntity<>(response, HttpStatus.FORBIDDEN);
    }
}