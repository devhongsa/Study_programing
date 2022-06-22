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
preference 가서 sdk 검색 후 sdk tools에 4가지 선택하고 OK 버튼
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
안드로이드 스튜디오에서 이미지파일 쓰려면
pubspec.yaml 파일에서 flutter : 부분에 
asset :    //여기서 asset은 폴더이름
    - asset/img/  //경로 
추가해준다.





//Widget Tree 
// MaterialApp > Scaffold > Center 와 같이 화면상에 나타나는 widget들의 연결고리
//main.dart
import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.black,
        body: Center(
          child: Text(
              'Hello World',
              style: TextStyle(
                color: Colors.white,
                fontSize: 20.0,
              ),
          ),
        ),
      ),
    ),
  );
}
