# https://lucky516.tistory.com/52?category=1010534 장고로 웹페이지 만들기 튜토리얼 
## https://docs.djangoproject.com/ko/4.1/intro/tutorial01/  장고 docs
## https://www.django-rest-framework.org/tutorial/1-serialization/ 장고 rest framework docs

# pip install django
# python3 -m pip install Django (mac os)
###### 작업폴더를 만들 위치에 가서 django-admin startproject 프로젝트이름  작업폴더 생성됨
###### 웹앱만들기 : python manage.py startapp 웹앱이름   작업폴더 생성됨
###### python manage.py runserver    서버실행   http://127.0.0.1:8000/ 

# settings.py 에서 Time_zone을 Asia/Seoul 로 변경 

###### python manage.py migrate  :  INSTALLED_APPS 의 설정을 탐색하여, mysite/settings.py 의 데이터베이스 설정과 app 과 함께 제공되는 
# database migrations(나중에 다루겠습니다) 에 따라, 필요한 데이터베이스 테이블을 생성합니다.

# polls/models.py  에서 db관련 테이블 정의 
# settings.py 의 intalled_apps 에서 내가 만든 앱 추가. 'polls.apps.PollsConfig',
###### python manage.py makemigrations polls  : migrate와 비슷한 기능이지만 실제 db를 조작하지는 않음. polls앱에서 수정한 사항들 save 하는 기능
# python manage.py sqlmigrate polls 0001 : db migration할때 실제 어떤 sql 쿼리가 실행되었는지 보여줌.
###### python manage.py migrate : 이후 이 명령어를 실행하면 여러앱들에서 migrations로 save된 내용들을 실제로 migrate함. db조작


#### 코딩을 통해 연결된 db테이블들 조작해보기
# python manage.py shell
# >>> from polls.models import Choice, Question
# >>> Question.objects.all()
# >>> from django.utils import timezone
# >>> q = Question(question_text="What's new?", pub_date=timezone.now())
# >>> q.save()

# >>> q.id
# >>> q.question_text
# >>> q.pub_date

# >>> q.question_text = "What's up?"
# >>> q.save()

# >>> q = Question.objects.get(pk=1)    
# >>> q.was_published_recently()      ## custom 함수 : Question 테이블에서 pk가 1인 pub_date가 create된지 1일이 됐냐 안됐냐 체크


#### 관리자 생성하기 
#https://docs.djangoproject.com/ko/4.1/intro/tutorial02/
# python manage.py createsuperuser
# 관리자 계정 생성후에   url주소 /admin 으로 들어가면 계정 인증요청이 뜸.
# polls/admin.py  파일에서 db테이블을 코딩시켜놓으면 admin전용 웹사이트에서 쉽게 db를 조작할 수 있음


#{% csrf_token %} : 모든 post 요청에 대해서 위조방지를 위한 보안기능. post요청은 무조건 이거를 써야함.
### DDD 



##### 장고 개발 로드맵 
# pip install django 
# python3 -m pip install Django (mac os)
# django-admin startproject myprojectname  :  기본 프로젝트 개발환경 구성. 
# settings.py 에서 DB뭐 쓸건지, timezone 뭔지, 어떤 웹앱을 탑재할건지 기본 세팅
# python manage.py startapp mywebappname  : 웹앱 개발을 위한 기본 환경 구성.
# settings.py에서 installed_app부분에 mywebapp 탑재 
# mywebapp의 models.py 에서 db 테이블 정의
# python manage.py makemigrations mywebbappname  : db 테이블 migration -> migrations폴더에 intial파일 생성됨
# python manage.py migrate : mywebbapp에서 migration된 내용들 실제 db에 적용.
# project urls.py에서 mywebapp 경로설정.
# mywebapp 에서 urls.py 만들고 api 개발 시작. 이러한 url요청이오면 views.py의 어떤 함수를 실행시켜라라는 로직구현. 실제 메인로직부분은 views.py에서 담당. 
# views.py에서 특정 url로 요청이 왔을때 어떤 작업을 할 건지 메인로직 구현. 여기서 얻어진 유의미한 데이터들을 template html에 context로 전달하고 리스폰스.
# mywebapp/templates/mywebapp 에서 template html 파일 작성. views.py에서 받아온 데이터들을 html에 표현하여 사용자에게 전달

# python manage.py createsuperuser : admin 계정을 만들고 mywebapp admin.py에서 DB 테이블 등록하면, 웹페이지에서 쉽게 DB조작가능.
# /admin url로 접속하면 됨.