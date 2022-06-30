https://docs.flutter.dev/get-started/install/macos  에서 sdk 다운로드 
https://blog.codefactory.ai/    //볼만한 강의들 많이 있음 

pub.dev 들어가서 패키지 검색. webview / flutter.dev 팀이 만든 패키지가 신뢰성있음.
클릭해서 들어간다음에 제목옆에 복사 / project 폴더 pubspec.yaml 에 dependencies 밑쪽에 버전적혀져있는 패키지 밑에 붙여넣기
버전앞에 ^ 표시는 ^3.0.0 일때 앞에 3을 제외하고 뒷쪽 버전이 업데이트가 되면 자동으로 업데이트하겠다는 뜻임. 맨 앞자리가 바뀌면 크게 바뀌는 업데이트이기 떄문에
자동으로 업데이트하지 않겠다는 뜻 / 그리고 android/app/build.gradle 로 가서 defaultconfig > minsdkversion 20 으로 변경, webview readme 참고
그리고 중요한거는 main.dart를 run 중지시키고 terminal에서 flutter clean 입력해준다음에 다시 실행해야함. 그래야 적용완료 

/////////////////////flutter 시작을 위한 환경세팅 /////////////////////////
terminal 열고 
echo $SHELL  =>  /bin/zsh 
ls  => 현재 폴더경로에 있는 폴더들 목록

이 경로 중요함 
/Users/hongseungmin/Documents/libraries/flutter/bin

이 경로에서
vi ~/.zshrc
i => INSERT 
export PATH="$PATH:/Users/hongseungmin/Documents/libraries/flutter/bin" 입력후 esc 누르면 INSERT 사라지는데 이때 :wq 입력후 엔터(나가기)
terminal 종료후 다시 실행 vi ~/.zshrc 해보면 경로가 추가되어있음

m1 계열 apple chip 맥북일때 
터미널에 
sudo softwareupdate --install-rosetta --agree-to-license

xcode 다운로드 
터미널에 
sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
sudo xcodebuild -runFirstLaunch
sudo xcodebuild -license

android studio 다운로드
plugin에서 flutter 다운
flutter project 생성
preference 가서 sdk 검색 후 android SDK에서  sdk tools에 4가지 선택하고 OK 버튼
Android SDK Build-Tools 
Android SDK Command-line Tools 
Android Emulator 
Android SDK Platform-Tools 

터미널에서 
flutter doctor --android-license 
flutter doctor > Flutter, Android toolchain, Xcode, Android Studio  정상체크 확인. 
정상체크안되어있으면, 뭐 설치해야된다 알려주니까 그대로 설치 

homebrew 설치후에
brew install cocoapods

IOS 실기기 사용위한 작업 
android studio 에서 작업한 프로젝트로 가서 ios/runner/info.plist 가보면 오른쪽 위에 open ios module in Xcode 클릭
Xcode Runner 클릭후 signing%capabilities 클릭
add account로 계정 추가하면 내 아이폰으로 테스트가능 
/////////////////////////////////////////////////////////////////////////
preference > key map > 기능 검색 > 더블클릭후 단축키 지정
/////////////////////////////////////////////////////////////////////////
안드로이드 스튜디오에서 이미지파일 쓰려면
pubspec.yaml 파일에서 flutter : 부분에 
asset :    //여기서 asset은 폴더이름
    - asset/img/  //경로 
추가해준다. 그리고 나서 오른쪽 위에 Pub get 을 꼭 클릭해줘야함.


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//////tips////////

//만일 Widget의 파라미터가 뭐가 있는 알고 싶으면, 위젯 오른쪽 클릭 > Go to > declaration or Usages
//import하기 쉬운방법, 위젯이름 오른쪽 클릭 show action , import 
//꼭 override 해줘야하는 함수 찾는거는 부모클래스 오른쪽 클릭후 show action 에서 찾을 수 잇음

//// 패키지 다운받기 ////
// pub.dev 들어가서 패키지 검색. webview / flutter.dev 팀이 만든 패키지가 신뢰성있음.
// 클릭해서 들어간다음에 제목옆에 복사 / project 폴더 pubspec.yaml 에 dependencies 밑쪽에 버전적혀져있는 패키지 밑에 붙여넣기
// 버전앞에 ^ 표시는 ^3.0.0 일때 앞에 3을 제외하고 뒷쪽 버전이 업데이트가 되면 자동으로 업데이트하겠다는 뜻임. 맨 앞자리가 바뀌면 크게 바뀌는 업데이트이기 떄문에
// 자동으로 업데이트하지 않겠다는 뜻 / 그리고 android/app/build.gradle 로 가서 defaultconfig > minsdkversion 20 으로 변경, webview readme 참고
// 그리고 중요한거는 main.dart를 run 중지시키고 terminal에서 flutter clean 입력해준다음에 다시 실행해야함. 그래야 적용완료 


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

///widget 기능 관련 ///
StatefulWidget?   stful 로 간편생성. 상태변할때 위젯을 아예없애지 않고 업데이트함. 상태저장O
StatelessWidget?   stless로 간편생성. 상태변할때 아예 위젯을 삭제해버림 상태저장 X

CircularProgressIndicator? 로딩표시하기

mainAxisAlignment? Coulmn이면 세로방향이 mainAxis이고 정렬
CrossAxisAlignment? 나와 반대되는 방향 정렬
MainAxisSize? 내 방향으로의 사이즈 
Expanded?    컨테이너 자리 차지하는거 관련
MediaQuery?  핸드폰 너비 사이즈 관련
SafeArea?  핸드폰 위쪽 시간있고 배터리표시있는 부분 범위침범안하게 해주는 기능 
Boxfit?   사진같은거를 화면에 어떤식으로 맞출거냐 

WebViewController? 웹뷰를 가져왔을 때 웹페이지를 컨트롤할 수 있게 해주는 기능
AppBar?   앱의 위쪽에 bar 만들기 기능
IconButton?   버튼
WebView?    웹페이지를 그대로 핸드폰으로 들고 와서 볼 수 있는 패키지 
Timer?      Timer 설정해서 일정시간 간격으로 기능을 반복하게 할 수 있는 기능 
PageController?   페이지를 컨트롤 할 수 있게 하는 기능
PageView?         여러 페이지 설정하는 기능 1페이지에는 뭐, 2페이지에는 뭐  리스트형태로 
setSystemUIOverlayStyle?  핸드폰 위에 배터리, 시간 부분 색깔 조정 
Image?    이미지 불러오는 기능


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



//Widget Tree 
// MaterialApp > Scaffold > Center 와 같이 화면상에 나타나는 widget들의 연결고리
// Project 1 
//main.dart
import 'package:flutter/material.dart';
import 'package:flutter_project/screen/home_screen.dart';   //이 파일 찾을때 밑에 HomeScreen 오른쪽 클릭 하고 show action 누르면 있음

void main() {
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      home: HomeScreen(),
    ),
  );
}

///// /////

StatelessWidget은 라이프 사이클 동안 단 한번만 build함수를 실행한다.
class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFFF99231),   //hex code 직접입력 , 아니면 Colors.white 이런식으로 
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,        //정렬
        children: [
          Image.asset('asset/img/logo.png'),
          CircularProgressIndicator(                //로딩표시 
            color: Colors.white,
          ),
        ],
      ),
    );
  }
}


1.MaterialApp 은 꼭 있어야함 html태그라고 생각 
2.Scaffold 도 꼭 있어야함 body라고 생각
3.HomeScreen 같은 class 위젯을 만들어서 MaterialApp에 넣어주는 방식으로 해야 됨. 안그러면 나중에 코드가 엄청 보기 힘들어지기 때문
4.HomeScreen 오른쪽 클릭해서 show context action을 보면 꼭 override 해줘야하는 함수가 나옴. 
5.hot reload는 StatelessWidget의 build 함수의 내용이 바뀔때 알아서 화면을 바꿔줌. build안에 내용이 아니라면 hot restart를 눌러줘야함.
6.특정 위젯을 제거하고 싶을때, Center 에서 option + enter 누르면 기능들이 나오는데 remove widget 해주면 편하게 제거할수있음.
반대로 위젯을 생성할때는 Wrap with Column 기능이나 다른 위젯기능을 눌러주면 됨.






/////////////////////////////////////////////////////////////////////////
//////////////////////////정렬, 화면차지하는 비율 //////////////////////////////
////// /////////
//home_screen.dart

import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        bottom: false,            //밑에 Container 에서 wrap with widget 누르고 SafeArea로 변경, 핸드폰 화면범위침범안하게 해주는기능
        child: Container(          //Container는 div 라고 생각
          color: Colors.black,
          width: MediaQuery.of(context).size.width,     //size는 핸드폰사이즈 width 핸드폰 너비 사이즈 불러오기
          //height: MediaQuery.of(context).size.height  //Row일때는 이렇게 해줘야함
          child: Column(            //Row로 바꾸면 가로로
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.max,
            children: [
              // Expanded / Flexible 은 clildren 안에서만 사용가능
              Expanded(     //남은공간 차지할만큼 다 차지해라
                flex: 2,    //공간 나눠먹는 비율 정해주기
                child: Container(
                  color: Colors.red,
                  width: 50.0,
                  height: 50.0,
                ),
              ),
              Expanded(     //Expanded가 여러개면 나눠서 먹음
                child: Container(
                  color: Colors.blue,
                  width: 50.0,
                  height: 50.0,
                ),
              ),
              Container(
                color: Colors.green,
                width: 50.0,
                height: 50.0,
              ),
              Container(
                color: Colors.yellow,
                width: 50.0,
                height: 50.0,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
//만일 Widget의 파라미터가 뭐가 있는 알고 싶으면, 위젯 오른쪽 클릭 > Go to > declaration or Usages





/////// container 안에 column, row 조합으로 화면 구현하기 /////
///// //////
////// home_screen.dart   ////// 
import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        bottom: false,            //밑에 Container 에서 wrap with widget 누르고 SafeArea로 변경, 범위침범안하게 해주는기능
        child: Container(          //Container는 div 라고 생각
          color: Colors.black,
          width: MediaQuery.of(context).size.width,     //size는 핸드폰사이즈 width 핸드폰 너비 사이즈 불러오기
          //height: MediaQuery.of(context).size.height,  //Row일때는 이렇게 해줘야함
          child: Column(            //Row로 바꾸면 가로로
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Container(
                    height: 50.0,
                    width: 50.0,
                    color: Colors.red,
                  ),
                  Container(
                    height: 50.0,
                    width: 50.0,
                    color: Colors.orange,
                  ),
                  Container(
                    height: 50.0,
                    width: 50.0,
                    color: Colors.yellow,
                  ),
                  Container(
                    height: 50.0,
                    width: 50.0,
                    color: Colors.green,
                  ),
                ],
              ),
              Container(
                height: 50.0,
                width: 50.0,
                color: Colors.orange,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  Container(
                    height: 50.0,
                    width: 50.0,
                    color: Colors.red,
                  ),
                  Container(
                    height: 50.0,
                    width: 50.0,
                    color: Colors.orange,
                  ),
                  Container(
                    height: 50.0,
                    width: 50.0,
                    color: Colors.yellow,
                  ),
                  Container(
                    height: 50.0,
                    width: 50.0,
                    color: Colors.green,
                  ),
                ],
              ),
              Container(
                height: 50.0,
                width: 50.0,
                color: Colors.green,
              ),
            ]
          ),
        ),
      ),
    );
  }
}





///////////////////////////////////////////////////////////////////////////////////////////
////// 웹페이지 url 을 가져와서 폰화면에 그대로 띄워주는 패키지 사용 ///////
///// ///////
//// WebView /////
pub.dev 들어가서 패키지 검색. webview / flutter.dev 팀이 만든 패키지가 신뢰성있음.
클릭해서 들어간다음에 제목옆에 복사 / project 폴더 pubspec.yaml 에 dependencies 밑쪽에 버전적혀져있는 패키지 밑에 붙여넣기
버전앞에 ^ 표시는 ^3.0.0 일때 앞에 3을 제외하고 뒷쪽 버전이 업데이트가 되면 자동으로 업데이트하겠다는 뜻임. 맨 앞자리가 바뀌면 크게 바뀌는 업데이트이기 떄문에
자동으로 업데이트하지 않겠다는 뜻 / 그리고 android/app/build.gradle 로 가서 defaultconfig > minsdkversion 20 으로 변경, webview readme 참고
그리고 중요한거는 main.dart를 run 중지시키고 terminal에서 flutter clean 입력해준다음에 다시 실행해야함. 그래야 적용완료 
// home_screen.dart //
import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

class HomeScreen extends StatelessWidget {
  WebViewController? controller;                //webview를 통해 불러온 웹사이트를 이 컨트롤러로 바꿔줄수있음
  final homeUrl = 'https://blog.codefactory.ai';
  HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(                   //appBar는 Scaffold 에서 생성가능
        backgroundColor: Colors.orange,
        title: Text('Code Factory'),
        centerTitle: true,
        actions: [
          IconButton(
              onPressed: (){
                if(controller == null) {return;}
                controller!.loadUrl(homeUrl);     // !를 넣어줘서 controller가 null값이 아니다라는걸 알려줘야 함.
              },
              icon: Icon(
                Icons.home,
              ),
          )
        ],
      ),
      body: WebView(
        onWebViewCreated: (WebViewController controller){ // webview가 생성될때 작동
          this.controller = controller;                 //web을 컨트롤 할 수 있는 controller를 HomeScreen 클래스 내에서
                                                        // 사용할 수 있게끔 보내주는 역할
        },
        initialUrl: homeUrl,      //website를 앱화면으로 불러올 수 있음
        javascriptMode: JavascriptMode.unrestricted,    //javascript 언어 사용가능하게 하는 설정.
      )
    );
  }
}








///////////////////////////////////////////////////////////////////////////////////////////
//// 페이지 넘기기, 타이머 설정해서 자동으로 페이지 넘어가는 기능 구현 /////
//
//// StatefulWidget? /////
//// home_screen.dart
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  Timer? timer;                 //일정시간마다 특정 로직을 실행시키기 위해 변수 생성 initState에서 로직구현
  PageController controller = PageController(     //페이지를 컨트롤 하기위한 컨트롤러 생성
    initialPage: 0,   //처음 시작 페이지 설정, 0이 1페이저
  );

  @override
  void initState() {
    super.initState();

    timer = Timer.periodic(Duration(seconds: 4), (timer) {      //Timer 로직 구현 부분
      int currentPage = controller.page!.toInt();               // 현재페이지 불러오기, page는 0.5페이지도 존재 넘어갈랑말랑할때
      int nextPage = currentPage + 1;

      if(nextPage > 4){
        nextPage = 0;
      }

      controller.animateToPage(nextPage, duration: Duration(milliseconds: 1000), curve: Curves.linear);
      //animateToPage 는 페이지 넘기는 기능, (몇페이지로 넘길것인지, 넘어가는 속도, 넘어갈때 애니메이션)
    });
  }

  @override
  void dispose() {
    controller.dispose();       //컨트롤러와 타이머는 위젯이 삭제될때 꼭 같이 없애줘야 메모리 leak을 방지할 수 있음 
    if(timer != null){
      timer!.cancel();
    }
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle.dark); //위에 시간과 배터리,와이파이 표시의 색깔 조정 
    return Scaffold(
      body: PageView(           //PageView는 children의 리스트에 각 페이지를 설정할 수 있다.
        controller: controller,     //PageView 부분을 컨트롤하기 위한 controller 적용/ 우선 homescreenState클래스에서 변수선언해주고
                                    // initState 함수에서 로직구현을 해주면 로직대로 페이지가 반응함.
        children: [1,2,3,4,5].map((e) =>
          Image.asset('asset/img/image_$e.jpeg', fit: BoxFit.cover,) //cover같은 경우 화면을 맞추기 위해 그림이 짤릴수있음
        ).toList()     //map같은 경우 리스트가 아닌 iterable 객체를 반환하기 때문에 리스트로 변환해줘야함
      ),
    );
  }
}
