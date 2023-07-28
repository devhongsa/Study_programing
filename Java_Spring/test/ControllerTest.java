@WebMvcTest(TransactionController.class)
class TransactionControllerTest {
    // 실제 transactionService를 주입하면 객체가 무거워지니까, 가짜로 주입받는 것임.
    // 그래서 실제 transactionService의 메소드가 실행되는 것이 아니기 때문에, 메소드의 리턴값을 우리가 임의로 설정해줘야함
    // given을 통해서 transactionService의 메소드가 실행됬을때 리턴값을 우리가 설정을 해줌.
    @MockBean
    private TransactionService transactionService;

    @Autowired
    private MockMvc mockMvc;
    @Autowired
    private ObjectMapper objectMapper; //json->String, String->json

    @Test
    void successUseBalance() throws Exception {
        //given
        given(transactionService.useBalance(anyLong(), anyString(), anyLong()))
                .willReturn(TransactionDto.builder()
                        .accountNumber("1234567890")
                        .transactedAt(LocalDateTime.now())
                        .amount(1234L)
                        .transactionId("txsId")
                        .transactionResultType(S)
                        .build());

        //when
        //then
        mockMvc.perform(post("/transaction/use")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(
                                new UseBalance.Request(1L, "1111111111", 3000L)
                        ))
                ).andExpect(status().isOk())
                .andExpect(jsonPath("$.accountNumber").value("1234567890"))
                .andExpect(jsonPath("$.transactionResult").value("S"))
                .andExpect(jsonPath("$.transactionId").value("txsId"))
                .andExpect(jsonPath("$.amount").value(1234))
                .andDo(print());
    }

    @Test
    void successCancelBalance() throws Exception {
        //given
        given(transactionService.cancelBalance(anyString(), anyString(), anyLong()))
                .willReturn(TransactionDto.builder()
                        .accountNumber("1234567890")
                        .transactedAt(LocalDateTime.now())
                        .amount(1000L)
                        .transactionId("txsId")
                        .transactionResultType(S)
                        .build());

        //when
        //then
        mockMvc.perform(post("/transaction/cancel")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(
                                new CancelBalance.Request("txsId", "1111111111", 3000L)
                        ))
                ).andExpect(status().isOk())
                .andExpect(jsonPath("$.accountNumber").value("1234567890"))
                .andExpect(jsonPath("$.transactionResult").value("S"))
                .andExpect(jsonPath("$.transactionId").value("txsId"))
                .andExpect(jsonPath("$.amount").value(1000))
                .andDo(print());
    }

    @Test
    void successQueryTransaction() throws Exception {
        //given
        given(transactionService.queryTransaction(anyString()))
                .willReturn(TransactionDto.builder()
                        .accountNumber("1234567890")
                        .transactionType(TransactionType.USE)
                        .transactionResultType(S)
                        .transactionId("txsId")
                        .amount(1000L)
                        .transactedAt(LocalDateTime.now())
                        .build());
        //when

        //then
        mockMvc.perform(get("/transaction/12345"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.accountNumber").value("1234567890"))
                .andExpect(jsonPath("$.transactionType").value("USE"))
                .andExpect(jsonPath("$.transactionResult").value("S"))
                .andExpect(jsonPath("$.transactionId").value("txsId"))
                .andExpect(jsonPath("$.amount").value(1000))
                .andDo(print());
    }
}