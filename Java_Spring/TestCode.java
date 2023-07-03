// Unit Test Code 작성 원칙 FIRST 
Fast : 유닛 테스트는 빨라야함 
Isolated : 다른 테스트에 종속적인 테스트 금지 , 특정 테스트의 결과에 따라 다른 테스트의 결과가 바뀌어서는 안됨.
Repeatable : 매번 같은 결과를 만들어야함 
Self-validating : 테스트는 스스로 결과를 검증할 수 있어야 함. 
Timely : 테스트는 적시에 작성해야함 

// 통합 테스트는 실제 환경을 가져와서 테스트해보는 것을 말함. 몇몇 Mocking을 섞어서 테스트함.


// @WebMvcTest : Controller 테스트 
// @DataJpaTest : jpa 레포지토리 테스트 
// @RestclientTest : 클라이언트의 요청을 서버가 정상적으로 수행하는지 테스트 
// @JsonTest : json 직렬화 역직렬화 테스트

// @BeforeEach : @Test 코드가 실행되기 전에 실행되는 메소드. 테스트메소드마다 반복되는 객체의생성과 set메서드를 하나의 메소드로 통일시켜놓는것.

// assert 문법
// assertEquals(expected, actual)
// assertNotNull(object) : 객체가 null인지 
// assertTrue(result>0) : result가 0보다 큰지 판별 
// assertFalse(result.isEmpty())
// assertArrayEquals(expected, result)
// assertThrows(RuntimeException.class, ()-> someMethod())
// assertThat
    // assertThat(actualValue).isEqualTo(42);
    // assertThat(actualValue).isPositive();
    // assertThat(actualValue).isNotZero();
    // assertThat(actualValue).isBetween(0, 50);
    // assertThat(actualValue).isGreaterThan(30);
    // assertThat(actualValue).isLessThanOrEqualTo(100);
    // assertThat(actualValue).isInstanceOf(Integer.class);
    // assertThat(actualValue).isNotNegative();
    // assertThat(actualString).startsWith("Hello");
    // assertThat(actualString).endsWith("!");
    // assertThat(actualString).contains("World");
    // assertThat(actualString).hasSize(13);
    // assertThat(actualString).isNotEmpty();
    // assertThat(actualString).isEmpty();



