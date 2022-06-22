https://docs.flutter.dev/get-started/install/macos  에서 sdk 다운로드 

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




//Widget Tree 
// MaterialApp > Scaffold > Center 와 같이 화면상에 나타나는 widget들의 연결고리
// Project 1 
//main.dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,        //debug banner 없애기
      home: HomeScreen(),
    ),
  );
}

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
/////////////////////////////////////////////////////////////////////////


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

1. 만일 Widget의 파라미터가 뭐가 있는 알고 싶으면, 위젯 오른쪽 클릭 > Go to > declaration or Usages