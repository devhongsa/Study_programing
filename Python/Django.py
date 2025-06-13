# https://lucky516.tistory.com/52?category=1010534 장고로 웹페이지 만들기 튜토리얼 
## https://docs.djangoproject.com/ko/4.1/intro/tutorial01/  장고 docs
## https://www.django-rest-framework.org/tutorial/1-serialization/ 장고 rest framework docs

# pip install django
# python3 -m pip install Django (mac os)
###### 작업폴더를 만들 위치에 가서 django-admin startproject 프로젝트이름  작업폴더 생성됨
###### django-projects 안에 django-venv(python -m venv venvName), 작업폴더를 생성하자
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
### pip install django 
### python3 -m pip install Django (mac os)
### django-admin startproject myprojectname  :  기본 프로젝트 개발환경 구성. 
### settings.py 에서 DB뭐 쓸건지, timezone 뭔지, 어떤 웹앱을 탑재할건지 기본 세팅
### python manage.py startapp mywebappname  : 웹앱 개발을 위한 기본 환경 구성.
### settings.py에서 installed_app부분에 mywebapp apps.py에 있는 Config클래스 탑재 'polls.apps.PollsConfig'
### mywebapp의 models.py 에서 db 테이블 정의
import datetime
from django.db import models
from django.utils import timezone ## django에서는 datetime이 아닌 timezone을 사용함.

#Question 테이블 정의
class Question(models.Model):       
    # id 컬럼은 만들지 않아도 장고가 알아서 생성해줌.   
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True) # auto_now 는 업데이트 될때마다 바뀜(updatedAt 컬럼에 적절)
    
    ## Question객체를 리턴했을때 객체표현이아닌 실제 값이 나오도록 하는 함수
    ## admin url로 들어갔을때 테이블을 보면 Questions.objects(1) 이렇게 나오는게 아닌 question_text 내용으로 보이게 된다.
    def __str__(self):
        if self.was_published_recently():
            new_badge = "NEW!!"
        else:
            new_badge = ""
            
        return self.question_text
        # return f'{new_badge} 질문: {self.question_text}, 날짜: {self.pub_date}'
    
    ## custom 함수. 특정 Question 객체의 pub_date가 만들어진지 하루가 지났냐 안지났냐 여부를 true false 리턴
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#Choice 테이블 정의
class Choice(models.Model):
    # 이 fk설정으로 choice.quenstion으로 Question객체불러오기 가능 
    # Question 과 Choice는 OneToMany 관계임. 그래서 question.choice_set.all() 하면 특정 question에 대한 모든 choice들을 불러올수있음.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
    
    
    
### python manage.py makemigrations mywebbappname  : db 테이블 migration -> migrations폴더에 intial파일 생성됨
### python manage.py migrate : mywebbapp에서 migration된 내용들 실제 db에 적용 장고는 sqlite를 기본적으로 사용하게끔 설정하게 되어있음(db.sqlite3 생성).
### sqlite db 접속법 : sqlite3 db.sqlite3 (db접속) > .tables (테이블목록보기) > .schema tableName (테이블생성 sql문 보기) > ctrl + d (db종료)
### migrate 할때마다 polls.migrations 폴더에 migrate기록들이 있음. 그래서 python manage.py migrate polls 0001(migrate번호)를 치면 그때 상태로 되돌아감. 잘못 migrate했던 파일들은 삭제하면됨. models.py 코드에서도 그 전상태로 되돌려줘야함.
### project폴더 urls.py에서 mywebapp 경로설정.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls')), ## polls경로로 오면 polls.urls에서 알아서 처리해라
    path('admin/', admin.site.urls),
]




### mywebapp폴더 에서 urls.py 만들고 api 개발 시작. 이러한 url요청이오면 views.py의 어떤 함수를 실행시켜라라는 로직구현.
from django.urls import path 
from .. import views

app_name = 'polls' # app_name을 정해주면 templates html에서 href를 사용할때 'polls:detail' 이런식으로 써줘야함 여기서 detail은 밑에 path에서 name부분
urlpatterns = [
    path('',views.index, name='index'),  # polls/ 뒤에 오는 url값에 따라서 이동. 여기서는 '' 빈문자열이니까 /polls 로 요청이 오면 views.index 로드
    path('<int:question_id>/', views.detail, name='detail'),  # polls/1  이런식으로 오면 views.detail에 1을 인자값으로 전달
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'), #polls/1/result 로 왔을때
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'), #polls/1/vote 로 왔을때
]




### views.py에서 특정 url로 요청이 왔을때 어떤 작업을 할 건지 메인로직 구현. 여기서 얻어진 유의미한 데이터들을 template html에 context로 전달하고 리스폰스.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.utils import timezone ## django에서는 datetime이 아닌 timezone을 사용함.

def index(request):
    ### CRUD
    ## Create
    # q1 = Question(question_text="커피 vs 녹차")
    # q1.pub_date = timezone.now()
    # q1.save()
    # q1.choice_set.create(choice_text='a') #질문에 대한 선택데이터 choice테이블에 create, 이거는 save()가 필요없음.
    
    ## Update
    # q1 = Question.objects.last()
    # q1.question_text += '???'
    # q1.save()
    # Choice.objects.filter(votes__gt=0).update(votes=0) # votes값이 0보다 큰 애들이 있으면 모두다 votes값을 0으로 업데이트 시킴, update한 데이터 갯수 리턴
    
    ## Delete
    # c1 = Choice.objects.last()
    # c1.delete()
    # Choice.objects.filter(votes__gt=0).delete() # 지운 데이터 갯수 리턴
    
    ## Read
    # Question.objects.get(id=1)
    # Question.objects.get(question_text__startswith='휴가를') 
    # Question.objects.get(pub_date__second=59) #조건에 맞는거 하나만 가져워
    # Question.objects.filter(pub_date__year=59) #조건에 맞는 모든 값 가져옴 QuerySet return
    # Question.objects.exclude(pub_date__year=59) #조건에 맞는 값을 제외한 모든값을 가져옴 QuerySet return
    # Question.objects.filter(pub_date__year=59).count() #조건에 맞는게 몇개있는지
    # Question.objects.filter(pub_date__year=59).query #print해보면 query어떻게 보내는지 확인 가능
    # Choice.objects.filter(question__question_text__startswith='휴가') 
    # startswith, endswith, contains, gt: greater than >, gte: >=, lt: less than <, lte: <=
    
    # 구버전 response
    # latest_question_list = Question.objects.order_by('pub_date')[:5]  # -pub_date는 decs(최신 data먼저나오게), 그냥 pub_date는 asc
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
    # 구버전 response
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # shortcut render() 위에 코드랑 동일하지만 코드를 조금 짧게 해줌.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # request 내용과 context를 함께 템플릿으로 넘겨줌 데이터 전달.

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")  # question없으면 이 에러 실행시키고 끝남.
    # return render(request, 'polls/detail.html', {'question': question}) # question있으면 이코드 실행, 없으면 실행안됨.

    # 위코드와 동일한 shortcut 버전
    question = get_object_or_404(Question, pk=question_id)
    # for choice in question.choice_set.all():      #choice_set.all()은 question의 fk키를 가지고 있는 테이블의 데이터를 다 가져와줌.
    #     print(choice)
    return render(request, 'polls/detail2.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  #여기서 choice는 detail.html에서 form으로 제출된 input의 name임.
    except (KeyError, Choice.DoesNotExist):     #만약 post요청으로 받은 choice가 없으면 keyerror가 일어남.
        # Redisplay the question voting form.
        return render(request, 'polls/detail2.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F('votes') + 1   ## F()함수는 경쟁상태 문제를 방지할 수 있는 기능임.
        selected_choice.save()
        selected_choice.refresh_from_db()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  #다른 url로 redirecting





### mywebapp/templates/mywebapp 에서 template html 파일 작성. views.py에서 받아온 데이터들을 html에 표현하여 사용자에게 전달
#detail.html
<form action="{% url 'polls:vote' question.id %}" method="post">
  {% csrf_token %}
  <fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}
    <p><strong>{{ error_message }}</strong></p>
    {% endif %} {% for choice in question.choice_set.all %}
    <input
      type="radio"
      name="choice"
      id="choice{{ forloop.counter }}"
      value="{{ choice.id }}"
    />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label
    ><br />
    {% endfor %}
  </fieldset>
  <input type="submit" value="Vote" />
</form>

#results.html
<h1>{{ question.question_text }}</h1>

<ul>
  {% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }} -- {{ choice.votes }} vote</li>
  {% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>



### AWS에 배포시 EC2 퍼블릭 dns 주소를 settings.py ALLOWED_HOSTS 에 추가해줘야함.

### python manage.py createsuperuser : admin 계정을 만들고 (계정이름, 비밀번호 입력, 이메일은 없어도 됨.) mywebapp admin.py에서 DB 테이블 등록하면, 웹페이지에서 쉽게 DB조작가능.
from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
### /admin url로 접속하면 됨. User 목록에서 관리자 계정 추가 가능 superuser 권한도 줄 수 있음.



### django shell 이용하기 : manage.py가 있는 폴더로 가서. python manage.py shell 실행
### from polls.models import * > Question.objects.all()

# cookie 
# 원리 :
    # 클라이언트가 페이지를 요청
    # 서버에서 쿠키생성
    # 브라우저에 쿠키 저장. 
    # http헤더에 쿠키를 포함 시켜 응답
    # 클라이언트가 같은 요청을 할 경우 Http헤더에 쿠키를 함께 보냄
# session 
# 원리 :
    # 클라이언트가 서버 접속시 서버가 세션 ID 발급
    # 클라이언트는 세션ID를 쿠키를 사용해서 저장하고 가지고 있음
    # 클라이언트는 서버에 요청할때, 이 쿠키의 세션ID를 서버에 전달해서 사용 
    # 서버는 세션ID를 전달 받아서 서버에 저장된 세션ID와 비교해서 맞으면 해당 클라이언트의 정보를 가지고 로직 수행
    # 클라이언트 정보를 가지고 서버 요청을 처리하여 클라이언트에 응답