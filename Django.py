# https://lucky516.tistory.com/52?category=1010534 장고로 웹페이지 만들기 튜토리얼 
## https://docs.djangoproject.com/ko/4.1/intro/tutorial01/  장고 docs

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




### DDD 