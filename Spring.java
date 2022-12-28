// jdk download 검색 후 설치 : java SE , java EE 따로있음. SE는 standard edition, ee는 enterprise edition. EE버전이 SE위에 더 기능을 추가한 버전이라고 생각하면 됨.
// java EE 설치 : temurin 검색후 lts 버전 설치 
// tomcat : WAS  tar파일 받은후 bin폴더 경로로 가서  ./startup.sh 실행 localhost:8080 으로 접속가능 // ./shutdown.sh 으로 종료
// gradle : brew install gradle (npm과 같은 패키지,빌드 매니저 )
// start.spring.io
// intellij settings에서 gradle 검색후 build and run을 inellij 로 변경하면 더 빨리 빌드하고 실행됨.

// TestCode 관련
// implementation 'ch.qos.logback:logback-classic:1.2.3'
// testImplementation 'org.assertj:assertj-core:3.23.1'
// testImplementation 'org.junit.jupiter:junit-jupiter-params:5.8.2'

// DB관련
// implementation 'org.springframework:spring-jdbc:5.3.22'
// implementation 'com.zaxxer:HikariCP:5.0.1'
// testImplementation 'com.h2database:h2:2.1.214'

//import static org.assertj.core.api.Assertions.*;


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

// resources.static에 index.html 파일 올리면 알아서 spring boot가 index.html을 welcome page로 렌더링함.
// static 폴더에 hello-static.html 를 만들고 localhost:8080/hello-static.html 하면 spring boot cointainer가 처음에는
// hello-static.html 컨트롤러를 찾고 없으면, static폴더의 hello-static.html파일을 찾아서 렌더링 해줌.
// file - project structure에서 jdk 버전 변경 가능.
// settings에서 gradle 검색후 gradle의 jdk 버전도 변경 가능.
// 빌드하기 : 프로젝트폴더 경로에서 ./gradlew build, 빌드하면 /build/libs 경로에 jar파일 생성됨.
// ./gradlew clean build 하면 build 폴더 싹 지웠다가 다시 빌드함.
// /build/libs 경로에서 java -jar 파일이름.jar 하면 서버가 실행됨.

// MVC (Model, View, Controller) 방식 : html 정적파일에 동적데이터들을 합쳐서 렌더링
// API 방식 : json데이터를 리턴해주는 방식

// TDD : Test code를 먼저 구현하고, 그에 맞춰 로직을 구현하는 방식.

// Controller -> Service -> Repository : 정형화된 DI(Denpendency Injection) 관계
// Controller에서 Service기능을 써야하고, Service에서는 Repository 기능을 써야함.
// Ex) service.MemberService 클래스는 회원가입서비스가 구현되어있고, repository.MemoryMemberRepository 에는 회원정보를
// DB에 저장하는 기능 구현되어있음. MemberService의 회원가입서비스에는 Repository의 DB저장기능을 가져와서 쓰고 있고,
// controller.MemberController 에서는 client에서 온 요청에 따라 MemberService의 회원가입 기능을 가져와서 씀.
// 즉 Controller -> Service -> Repository는 DI 관계가 형성되어있고 Spring boot는 @Controller @Service 클래스의
// 생성자에 @Autowired 태그를 달아서 자동의존관계로 연결을 해줌.(스프링 빈 등록)


// 일급 컬렉션(클래스) : object(딕셔너리) 라고 생각하면됨. key,value를 인스턴스변수로 갖는 클래스 A를 List<A> 변수로 가지고 있는 클래스
