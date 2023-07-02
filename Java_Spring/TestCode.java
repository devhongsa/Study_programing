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



