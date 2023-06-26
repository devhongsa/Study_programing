@RestController // 그냥 @Controller와 다른점은 RestController는 서버응답코드를 자동으로 설정해서 응답해줌.
@RequiredArgsConstructor
public class AccountController {
	private final AccountService accountService;

	@PostMapping("/account")
	public CreateAccount.Response createAccount(
			@RequestBody @Valid CreateAccount.Request request) {
		return CreateAccount.Response.from(
				accountService.createAccount(request.getUserId(), request.getInitialBalance()));
	}

	@DeleteMapping("/account")
	public DeleteAccount.Response deleteAccount(
			@RequestBody @Valid DeleteAccount.Request request) {
		return DeleteAccount.Response.from(
				accountService.deleteAccount(request.getUserId(), request.getAccountNumber()));
	}

	@GetMapping("/account")
	public List<AccountInfo> getAccountsByUserId(
			@RequestParam("user_id") Long userId) {
		return accountService.getAccountsByUserId(userId)
				.stream().map(accountDto -> AccountInfo.builder()
						.accountNumber(accountDto.getAccountNumber())
						.balance(accountDto.getBalance()).build())
				.collect(Collectors.toList());
	}
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@Slf4j
@RestController
@RequiredArgsConstructor
public class TransactionController {
	private final TransactionService transactionService;

	@PostMapping("/transaction/use")
	@AccountLock
	public UseBalance.Response UseBalance(
			@Valid @RequestBody UseBalance.Request request) throws InterruptedException {
		try {
			// Thread.sleep(6000L);
			return UseBalance.Response.from(
					transactionService.useBalance(request.getUserId(),
							request.getAccountNumber(),
							request.getAmount()));
		} catch (AccountException e) {
			log.error("Failed to use balance. ");

			transactionService.saveFailedTransaction(
					request.getAccountNumber(), request.getAmount());

			throw e;
		}
	}

	@PostMapping("/transaction/cancel")
	@AccountLock
	public CancelBalance.Response cancelBalance(
			@Valid @RequestBody CancelBalance.Request request) {

		try {
			return CancelBalance.Response.from(transactionService.cancelBalance(request.getTransactionId(),
					request.getAccountNumber(), request.getAmount()));
		} catch (AccountException e) {
			log.error("Failed to cancel balance. ");

			transactionService.saveFailedCancelTransaction(
					request.getAccountNumber(), request.getAmount());

			throw e;
		}
	}

	@GetMapping("/transaction/{transactionId}")
	public QueryTransactionResponse queryTransaction(
			@PathVariable String transactionId) {
		return QueryTransactionResponse.from(transactionService.queryTransaction(transactionId));
	}
}

// Dto객체로 response/ResponseEntity<?> 객체로 맵핑해서 response/엔티티객체를 바로 response하는것은안좋음
// @RequestMapping
// @RequestParam : url 뒤에 ? 으로 오는 요청
// @PathVariable : /{var}
// @RequestBody : 헤더 바디에 오는 요청
// @ModelAttribute : RequestParam을 여러번쓰는대신 Dto를 만들어서 한번에 Dto객체에 파라미터들을 맵핑해줌.