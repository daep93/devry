# 가상환경 설정

- 가상환경 생성

```bash
$ python -m venv venv
```

- 실행
  - 완료 후에는 (venv)와 같이 지정했던 가상환경의 이름이 나옴으로 가상환경이 구동되고 있다는 것을 알 수 있습니다.

```bash
$ source venv/Scripts/activate
(venv)
```



# Django 서버 구동

- Django 및 라이브러리 설치
  - 디렉토리 내의 `requirements.txt`를 통해 패키지들을 한 번에 설치할 수 있습니다.
  - 현재 `django-rest-knox`를 설치 시도하면 오류를 출력하는데, pip의 버전이 낮아 발생하는 문제로 보입니다. 패키지 설치 이전에 pip를 업그레이드해야 오류 없이 설치됩니다.

```bash
$ python -m pip install --upgrade pip

$ pip install -r requirements.txt
```

- Django 프로젝트 생성
  - 만약 다른 디렉터리에서 Django 프로젝트를 새로 생성하려는 경우 다음의 명령어를 입력해야 합니다.
  - `.`을 뒤에 붙이는 경우 현재 디렉터리에 `manage.py`를 생성합니다.

```bash
$ django-admin startproject project_name [.]
```

- Django app 생성
  - 어플리케이션을 새로 만드는 경우 다음의 명령어를 입력합니다.

```bash
$ python manage.py startapp app_name
```

- Django app 등록
  - 만들어진 어플리케이션을 프로젝트의 `settings.py`에 등록해줍니다.
  - `settings.py`에는 생성한 어플리케이션의 이름과 설치한 라이브러리의 이름을 작성합니다.

```python
# settings.py
INSTALLED_APPS = [
    'accounts',

    'rest_framework',
    'knox',
    'django_rest_passwordreset',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

