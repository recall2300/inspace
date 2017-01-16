"""
Django settings for inspace project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*wf3g-f)=h*^53yt&ioo660ypc$z8-99ji4tgojf4x&*c2rc-r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'approval',
    'rest_framework',
    'rest_framework_swagger',
    'haystack',
    # python-social-auth
    'social_django',
]

AUTH_USER_MODEL = 'approval.Employee'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# REST Framework
# Use Django's standard `django.contrib.auth` permissions,
# or allow read-only access for unauthenticated users.
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'PAGE_SIZE': 10
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # python-social-auth
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'inspace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'approval', 'templates', 'approval'), ]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # python-social-auth
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'inspace.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Modified Time Zone UTC->Asia/Seoul
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
# Added Static_root

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}

# python-social-auth
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend', # 장고 기본 로그인
)
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1031012446497-o4jnm4ij9bvd7sug7qdk0flq8sv1tt3v.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'fanDeQmrBF2WKY9vepP_DlLt'

AUTH_USER_MODEL = 'approval.Employee'

# 확장 가능한 기능
# 개발자가 인증, 연결, 연결해제 흐름 중 기능을 추가수정제거할수 있음.
# 모든 함수는 예기치 않은 인수에 대한 오류를 피하기 위해 **kwargs를 정의하는 것이 좋음
# 반환 형태는 dict or None. dict 리턴값은 {}형태가 아닌 **kwargs 형태의 인수로 넘겨줍니다.
# 기본적으로 선언하지 않아도 되나, 별도로 덮어씌울땐 기존것을 재정의합니다.

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',  # 공급자의 인증 읍답 일부(간단한 사용자 정보)
    'social.pipeline.social_auth.social_uid',  # 공급자에서 주어진 사용자 고유 식별자
    'social.pipeline.social_auth.auth_allowed',  # 프로젝트, 이메일 및 허용 목룍이 적용되는 곳
    'social.pipeline.social_auth.social_user',  # 현재 소셜계정이 사이트에 이미 연결되어있는지 확인
    # 'social.pipeline.mail.mail_validation', 이메일 주소를 검증하기 위해 사용자에게 메일을 보냅니니다.
    # 'social.pipeline.social_auth.associate_by_email',  # 이메일이 같은것들끼리 연결시킵니다.
    # 'social.pipeline.user.create_user',  # 사용자 계정을 찾지 못했다면, 사용자 계정을 만듭니다.
    # 'path.to.save_profile',  # <--- set the path to the function
    'social.pipeline.social_auth.associate_user',  # 소설계정을 사용자의 계정과 연결합니다.
    'social.pipeline.social_auth.load_extra_data',  # access_token과 같은 기본설정을 extra_data 필드에 채웁니다.
    'social.pipeline.user.user_details',  # 인증 서비스에서 정보가 변경될 경우 정보를 업데이트합니다.
)



# print (social.pipeline.user.user_details)
