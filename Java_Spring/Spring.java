객체지향(OOP):방대한 양의 코드를 잘 분류(클래스화)하고 교체를 할 수 있는 방법
SOLID 원칙 SRP:단일 책임 원칙(분류)-클래스 하나에 여러기능들을 다 넣지 마라,기능별로 클래스를 나눠라 OCP:개방 폐쇄 원칙(교체)-확장에는 열려있고 변경에는 닫혀있다.즉 수정하지말고 클래스를 추가해서 기능을 추가해라 LSP:리스코프 치환 법칙(교체)-상속받은 클래스는 부모클래스와 동일한 동작을 해야 재활용 가능성이 높아진다.(부모클래스를 인터페이스처럼 생각),실무에서는 상속을 최대한피함.ISP:인터페이스 분리 원칙(분류)-인터페이스를 기능별로 좀더 잘게 분리하자 DIP:의존성 역전 원칙(교체)-어떤 외부라이브러리를 사용하고 있다가,갑자기 그 라이브러리를 바꿔야할 일이 생기면 그 라이브러리를 직접적으로 사용한 클래스들을 모두 수정해줘야함.이를 방지하기 위해 인터페이스를 통해서 라이브러리 어답터코드만 바꾸면 되는 방식으로 해야함.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// implementation 'org.springframework.boot:spring-boot-starter-aop'
// implementation 'org.springframework.boot:spring-boot-starter-validation'
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// start.spring.io
// intellij settings에서 gradle 검색후 build and run을 inellij 로 변경하면 더 빨리 빌드하고 실행됨.
// Spring

// @SpringBootApplication : spring boot application으로 설정
// @Controller : View를 제공하는 controller로 설정, 응답값이 기본적으로 html임. 백엔드와 프로튼엔드가 구별이 거의
// 없던 시절 쓰였고 지금은 거의 안쓰임
// @RestController : REST API를 제공하는 controller로 설정, 응답을 주로 json으로 함. 백엔드에서는 이제
// 이거를 씀. 클래스에 붙임.
// @RequestMapping : URL 주소를 맵핑, RestController클래스안에 있는 메서드에 맵핑
// @GetMapping, PostMapping, PutMapping, DeleteMapping, : api method 설정
// @PathVariable : /1 이런식으로 url 뒤에 붙는 정보를 받는 방법
// @RequestParam : URL query parameter 맵핑. url에 ?ordierId=1 이런식으로 오는 요청에서 파라미터
// 정보를 받는 방법, required나 defaultValue 설정가능
// @RequestBody : Http Body를 parsing 맵핑. client가 body에 json형식의 큰데이터를 실어서 보내면,
// 백엔드에서 이 body를 받을때 사용
// @RequestHeader : 마찬가지로 client가 보낸 header정보를 받을때 사용
// @Valid : 객체 유효성 검증. @RequestBody와 함께 쓰여서 client로부터 온 데이터가 내가만든 DTO객체와 적합한지
// 판단함.
// @Configration : 1개 이상의 Bean을 등록할때 설정
// @Component : 1개의 Class 단위로 등록할때 사용
// @Bean : 1개의 외부 library로부터 생성한 객체를 등록 시 사용 , 메소드에 사용
// @Autowired : DI를 위한 곳에 사용
// @Qualifier : @Autowired 사용시 bean이 2개 이상 일때 명시적 사용, 구현체가 2개일때 하나의 bean을 우선적으로
// 사용
// @Primary : 역시 인터페이스의 구현체가 다수일때 한 구현체를 Primary로 지정해서 이 구현체를 우선적으로 사용
// @Resource : @Autowired + @Qualifier 의 개념으로 이해
// @ExceptionHandler : Controller 클래스 안에서 구현됨. Controller안에있는 특정API가 에러를 일으키면
// catch해서 처리
// @ResponseStatus : 예외가 일어났을때 Status code를 변경함
// @RestControllerAdvice : 어플리케이션의 전역적 예외 처리 클래스를 만들어서 사용. 현재 실무에서 가장많이 쓰임 클래스에
// 붙이고, 클래스안에서 @ExceptionHandler 구현
// @Transactional : 클래스나 메소드에 달아서 트랜잭션 생성, 보통 service 클래스에 붙여준다.
    Transactional 세부 설정들
    1. isolation (격리수준)
        DEFAULT : db의 종류에 따라 db가 택하고 있는 격리수준을 선택하겠다.
        READ_UNCOMMITTED : Dirty Read 발생
        READ_COMMITTED : Dirty Read 방지
        REPEATABLE_READ : Non-Repeatable Read 방지
        SERIALIZABLE : Phantom Read 방지
    2. propagation (전파수준) : 한 트랜잭셔널 메소드 안에서 다른 트랜잭셔널 메소드를 호출할때, 어떤 트랜잭셔널로 설정을 할지 결정하는 단계
        REQUIRED : default 속성. 부모트랜잭션이 실행중에 자식트랜잭션이 들어오면 자식트랜잭션은 부모트랜잭션에 그냥 참여함. 단독으로 실행될때도 트랜잭션으로 실행
        SUPPORTS : 부모트랜잭션에 참여할때만 참여하고 단독으로 실행될때는 트랜잭션없이 실행함.
        REQUIRES_NEW : 부모트랜잭션과 별개로 자식트랜잭션 자기만의 트랜잭션으로 실행함.
        NESTED : 부모가 실패한 경우 자식도 실패하지만, 부모트랜잭션은 성공했는데 자식트랜잭션이 실패한 경우, 부모트랜잭션은 커밋하고 자식트랜잭션만 롤백함. 
            NESTED 예) 일기작성 관련해서 로그를 DB에 저장하는 상황 
                로그 저장(자식)이 실패한다고 해서, 일기 작성(부모)까지 실패하면 안됨
                일기작성(부모)가 실패하면, 로그(자식)는 당연히 실패해야함.
    3. readOnly : 트랙잭션을 읽기 전용 속성으로 지정
        true로 설정하면, 이 트랜잭션으로 설정된 메소드에서 만약 Read가 아닌 Create, update , delete를 하려고하면 예외를 일으킴
        그리고 이걸 설정하면 트랜잭션 메소드 동작이 더 빨라짐.
    4. 트랜잭션 롤백 예외 설정
        @Transactional(noRollbackFor=Exception.class) : 특정 예외상황에서는 롤백하지않고 그냥 커밋함.
        @Transactional(rollbackFor=Exception.class) : 특정 예외상황이 일어나면 롤백함.
    5. timeout : 일정 시간 이내에 트랜잭션을 끝내지 못하면 롤백시킴 
    // @Transactional(prpagation = Required) : Required가 실무에서 가장 많이 쓰이고,
// Required-New가 가끔 쓰일수 있다.
// New는 Transactional메소드안에 다른 메소드가 존재하고 그 메소드를 Transactional New로 설정해주면 그 메소드만
// 따로 독립적인 Transaction을 갖게된다.
// @EnableTransactionManagement : Application class에 붙여서 전체프로젝트에 transactional을 적용시킴.
// @EnableScheduling : Application class에 붙여서 스케쥴작업을 할 수 있게 함.
// @Query(value = "select b from Book b where name = :name and createdAt >=
// :createdAt and updatedAt >= :updatedAt and category is null") :
// Query는 Repository 객체에서 쿼리메소드에 대한 어노테이션으로 붙는다. 쿼리메소드 naming이 너무 길어질때 쓴다.
// jpql문에서 :name은 쿼리메소드의 파라미터에서
// List<Book> findByNameRecently(@Param("name") String name, ...) 이렇게 Param
// 어노테이션을 사용해줘야지 쓸수 있다. 안그러면 ?1 이런식으로 파라미터 순서번호로 jpql에 넣어줘야한다.

// cascade : orphanRemoval vs Remove vs Soft deleted(soft는 deleted컬럼을 생성후 이데이터가
// 삭제된 데이터인지 true false 표시, 이후 데이터를 지우려고 할때 deleted false인 데이터만 지우게 한다.)

// jdk download 검색 후 설치 : java SE , java EE 따로있음. SE는 standard edition, ee는
// enterprise edition. EE버전이 SE위에 더 기능을 추가한 버전이라고 생각하면 됨.
// java EE 설치 : temurin 검색후 lts 버전 설치
// tomcat : WAS tar파일 받은후 bin폴더 경로로 가서 ./startup.sh 실행 localhost:8080 으로 접속가능 //
// ./shutdown.sh 으로 종료
// gradle : brew install gradle (npm과 같은 패키지,빌드 매니저 )
// start.spring.io
// talend API tester : 크롬웹스토어에서 다운
// intellij settings에서 gradle 검색후 build and run을 inellij 로 변경하면 더 빨리 빌드하고 실행됨.

// TestCode 관련
// implementation 'ch.qos.logback:logback-classic:1.2.3'
// testImplementation 'org.assertj:assertj-core:3.23.1'
// testImplementation 'org.junit.jupiter:junit-jupiter-params:5.8.2'

// DB관련
// implementation 'org.springframework:spring-jdbc:5.3.22'
// implementation 'com.zaxxer:HikariCP:5.0.1'
// testImplementation 'com.h2database::2.1.214'

// import static org.assertj.core.api.Assertions.*;

// new project 생성 , gradle 기반
// TDD
// ex) 학점 계산기 도메인
// 1. 도메인을 구성하는 객체에는 어떤 것들이 있는지 고민
// 이수한 과목, 학점 계산기
// 2. 객체들 간의 관계를 고민
// 학점계산기 객체가 이수한 과목들을 인스턴스 변수로 갖고 그것들을 통해 학점평균계산?
// 3. 동적인 객체를 정적인 타입으로 추상화해서 도메인 모델링 하기
// 동적인 객체 : 과목종류(자료구조, 객체지향프로그래밍, 코딩테스트) --> 정적인 타입: 과목(코스) 클래스로 구현
// 4. 협력을 설계
// 5. 객체들을 포괄하는 타입에 적절한 책임을 할당.
// 6. 구현하기

// tomcat : was, 요청올때 쓰레드를 늘려서 요청을 처리하는 방식.
// 요청이 올때마다 쓰레드를 늘리면 대규모 트래픽 상황에서 서버의 과부화가 심해진다.
// 그래서 쓰레드 갯수를 제한해놓고 쓰레드 풀을 형성하여 쓰레드를 재활용하는 방식으로 운영된다.

// CGI(Common Gateway Interface)
// 웹 서버와 was 사이에 데이터를 주고받는 규약
// 인터프리터 방식 : 웹서버 <--> script engine <--> script 파일
// 서블릿 방식 : 웹서버 <--> servlet Container <--> servlet 파일
// servlet? : 자바에서 웹 애플리케이션을 만드는 기술, 동적인 웹 페이지를 구현하기 위한 표준이다.

// JDBC
// 커넥션 풀 : 미리 디비와의 커넥션들을 연결해놓고 풀로 형성해놓음. client요청이 있을때 마다 커넥션을 사용
// Was 스레드 수와 커넥션 수를 함께 고려해야함.
// 커넥션 수를 많이 설정하면 많은 접속자의 요청을 처리할 수 있지만 메모리 소모가 큼.

// settings
// inlay - code vision - usages 해제
// gradle - build and run : intellij 사용, jdk 버전 변경

// resources.static에 index.html 파일 올리면 알아서 spring boot가 index.html을 welcome
// page로 렌더링함.
// static 폴더에 hello-static.html 를 만들고 localhost:8080/hello-static.html 하면 spring
// boot cointainer가 처음에는
// hello-static.html 컨트롤러를 찾고 없으면, static폴더의 hello-static.html파일을 찾아서 렌더링 해줌.
// file - project structure에서 jdk 버전 변경 가능.
// settings에서 gradle 검색후 gradle의 jdk 버전도 변경 가능.
// 빌드하기 : 프로젝트폴더 경로에서 ./gradlew build, 빌드하면 /build/libs 경로에 jar파일 생성됨.
// ./gradlew clean build 하면 build 폴더 싹 지웠다가 다시 빌드함.
// /build/libs 경로에서 java -jar 파일이름.jar 하면 서버가 실행됨.

// MVC (Model, View, Controller) 방식 : html 정적파일에 동적데이터들을 합쳐서 렌더링
// API 방식 : json데이터를 리턴해주는 방식

// TDD : Test code를 먼저 구현하고, 그에 맞춰 로직을 구현하는 방식.
// debug 모드 사용 : 브레이크포인트 찍고, debug모드로 test코드 실행.

// Controller -> Service -> Repository : 정형화된 DI(Denpendency Injection) 관계
// Controller에서 Service기능을 써야하고, Service에서는 Repository 기능을 써야함.
// Ex) service.MemberService 클래스는 회원가입서비스가 구현되어있고,
// repository.MemoryMemberRepository 에는 회원정보를
// DB에 저장하는 기능 구현되어있음. MemberService의 회원가입서비스에는 Repository의 DB저장기능을 가져와서 쓰고 있고,
// controller.MemberController 에서는 client에서 온 요청에 따라 MemberService의 회원가입 기능을
// 가져와서 씀.
// 즉 Controller -> Service -> Repository는 DI 관계가 형성되어있고 Spring boot는 @Controller
// @Service 클래스의
// 생성자에 @Autowired 태그를 달아서 자동의존관계로 연결을 해줌.(스프링 빈 등록)

// 일급 컬렉션(클래스) : object(딕셔너리) 라고 생각하면됨. key,value를 인스턴스변수로 갖는 클래스 A를 List<A> 변수로
// 가지고 있는 클래스

// jpa auditing : Entity에서 데이터타입이 localDatetime인 컬럼에 자동으로 시간 넣어주는 기능
// https://webcoding-start.tistory.com/53
// @EnableJpaAuditing, @EntityListeners(AuditingEntityListener.class) 으로 사용한다.

// StringBuilder
// StringBuilder는 문자열을 + 연산할때 쓰인다.
// 그냥 보통 "a" + "b" 를 써도 되지만 이렇게 하면 메모리 낭비가 심해지기때문에 StringBulider를 쓴다.
// StringBuilder로 생성된 객체에 append를 사용하여 합친후 .toString()으로 출력가능

// IoC, DI
// Ioc(Inversion of Control) : 제어의 역전. java 객체를 개발자가 new로 생성하여 관리하는 것이 아닌 Spring
// Container에 모두 맡김.
// DI(Dependency Injection) : 객체간의 결합성을 낮춰주고, 유지보수가 좋은 코드로 만들어줌. 의존성으로 부터 격리시켜
// 코드 테스트에 용이하다. Mock
// 예를 들어 DB를 연결하는 기능의 객체를 만들려고하는데, 하나는 mysql, 하나는 postgresql이 있다고 한다면 두 객체에서 모두
// connect라는 method를 만들어야함. 그러면 이때 connect method를 가진 Idb 객체를 만들고. mysql과
// postgresql 객체에서는 각자 connect 메서드를 오버라이드해서 구현을 한다.
// 그리고 DbConnector라는 DI 객체를 만들어서 DbConnector connertor = new DbConnector(new
// mysql()), connector.connect(mysql) 이렇게사용
// 즉 DbConnector라는 객체안에서 new mysql()으로 객체를 생성하는 것이 아니라 밖에서 생성한 객체를 파라미터로 전달해
// 주입하는 형태를 말함.
// Ioc 는 @Component 어노테이션으로 spring에게 객체를 관리해달라는 뜻임. Component 등록된 객체는 Spring
// container에서 관리하는 Bean이 됨.
// @Controller, RestController, Service, Component, Repository 어노테이션은 모두 자동으로
// bean으로 등록됨.
// 원래 옛날에는 xml파일에 직접 모든 클래스를 bean으로 등록해줬어야했음.
//

// AOP : 로그관련 기능 @Aspect, @Pointcut, @Before, @After

// JPA
// ORM (Object Relational Mapping) : Database의 테이블과, java에서의 객체 간의 관계를 정의해줌.
// JPA는 ORM역할을 하는 표준라이브러리라고 생각하면됨.
// Hibernate : JPA의 실제 구현체들을 말함.
// Spring data jpa : Hibernate에서 자주쓰는 기능들을 좀더 사용하기 쉽게 Spring에서 제공해주는 라이브러리
// @Entity : database의 table과 java의 객체를 이어주기 위해서 자바 객체에 선언
// @Id : table의 아이디로 설정
// @GeneratedValue : auto increment

// Lombok
// @Getter
// @Setter
// @ToString // User라는 객체를 println 했을때, User의 멤버변수에 대한 값들을 출력해줌.
// @NoArgsConstructor // 인자가 없는 생성자 생성, 필수적으로 넣어줘야함
// @AllArgsConstructor // 모든 멤버변수를 인자로 갖는 생성자 생성
// @RequiredArgsConstructor // NonNull(final) 멤버변수를 인자로 갖는 생성자 생성, 멤버변수에
// @Autowired를 하는대신, 멤버변수를 final로 생성해주고
// @RequiredArgsConstructor를 클래스에 선언해서 final로 선언된 멤버변수가 포함된 생성자를 자동으로 생성해준다.
// @EqualsAndHashCode // 객체끼리의 비교연산을 위한 어노테이션
// @Data // Getter + Setter + ToString + RequiredArgsConstructor +
// EqualsAndHashCode
// @Builder // User.builder().name("martin").email("11@gs").build(); 이런식으로
// 이어쓰기위한 어노테이션s
// @Slf4j : 해당 클래스의 logger를 자동생성.
// @UtilityClass : static method만 재공하는 유틸리티 성격의 클래스들의 생성자를 private으로 만들어서 객체 생성을
// 못하게 막아놓음.

// 프로젝트 구조
// package
// controller : API 로직 구현 부분. GET POST DELETE UPDATE 로직 구현
// domain : DB에서의 테이블 내용이라고 생각하면 됨.
// repository : domain과 실제 DB를 연결. CRUD를 할때 이 repository를 통해 사용함. Interface로 작성
