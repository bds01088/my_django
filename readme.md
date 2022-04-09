# Project 05

## Django - CRUD



### 알게된 주의사항 !!

- post후 페이지를 가져올때에는 redirect(import해야함)를 사용하자

- redirect시에는 'appname:name' 형태로 사용한다

- ```python
  if request.method == 'POST'
  ```

  를 이용하여 한 페이지에서 get할 때와 post할때를 구분하여 코딩하면 쓸데없는 html파일 하나를 줄일 수 있다. __또한 더 편하다!__

- variable routing 할때는 \<int:var_name> 형태로 사용한다

- variable routing이 적용된 주소를 부를때는 반드시 var_name에 들어갈 값을 같이 넣어주어야 한다

- 같은 구조를 가진 html들은 통합시킬 수 있다.

  if request.resolver_match.url_name == 'url_name'을 통해 html이 불러져온 위치의 url_name(views.py에 설정된 이름)이 무엇인지에 따라 입력될 html 문구를 정할 수 있다.

- form의 post 시 csrf_token 반드시 작성
- 수정 시 이전의 값들을 미리 입력된 상태로 가져오려면 value에 값을 너어준다
- 초기값으로 되돌리는 reset은 type 자체가 `reset`이다
- 날짜 형식 변경은 var|date:"날짜형식(문서참조)"

- 스크롤 리스트에서 값 고르는 태그는 select, 그 안에 옵션은 option태그

- 소수점 입력 방법은 \<input type="number" step="0.1"> 사용

  step을 이용하여 소수점 표시개수를 조절

- 모델에 데이터를 기입할 때, modelname.objects.create를 사용해도되지만

  업데이트할 때에는 save()를 사용하는게 올바르다.

- delete는 post로 올때만 작동하도록 코딩하며, 해당 개체를 받아온 다음 개체.delete()로 삭제한다

- delete할때에는 따로 html파일이 필요하지 않다. 삭제만 하면 끝이기 때문

- 하지만 urls과 views에는 작성해야 활용이 가능하다



### Django 기본 실행 바탕

1. 가상환경 설치 

   `python -m venv venv`

2. 가상환경 실행

   `source venv/Scripts/Activate`

3. 장고 설치 (requirements.txt로 설치방법)

   `pip install -r requirements.txt`

4. 프로젝트 생성

   `django-admin startproject pjtname .`

5. 앱 생성

   `python manage.py startapp appname`



### django 기본 세팅

1. pjt.setting 에서 app 추가

2. pjt.setting에 TEMPLATES, DIRS에 BASE_DIR / 'templates' 기입

   -> base.html을 불러올 수 있게 하도록 만드는 것

3. pjt와 동일 선상에 templates 폴더 만들고 그 안에 base.html 생성
4. pjt.urls에 import include 추가
5. urlpatterns에 path('appname/', include('appname.urls'))로 작성
6. app폴더에 urls.py 새로 생성
7. from django.urls import path 및 from . import views
8. app_name 지정
9. urlpatterns 생성
10. app폴더의 templates 생성시, templates폴더 안에 movies폴더 추가 생성 후 안에 템플릿 작성



### 모델 세팅

1. models.py에 모델 생성

   ```python
   class modelname(models.Model):
       속성이름 = models.속성성질field()
   ```

2. migrations 생성하기

   `python manage.py makemigrations`

3. showmigration으로 현재 migrate 적용상태 확인가능

4. migrate하기

5. views.py에 모델을 사용할 수 있도록 하기

   `from .models import modelname`

6. 모델 사용하기

   `modelname.objects.orm함수`

   orm함수 자체는 여러가지가 있으니 참조하자

7. admin 페이지에 추가하기

   1. admin.py에 from .model import modelname

   2. admin.py에 클래스 생성

      ```python
      class modelnameAdmin(admin.ModelAdmin):
          list_display=('pk'....)
      ```

      표현할 속성 이름들 리스트로 추가

   3. admin.py에 아싸리 추가

      `admin.site.register(modelname, modelnameAdmin)`



