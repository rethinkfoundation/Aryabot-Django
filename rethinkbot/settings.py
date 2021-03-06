"""
Django settings for rethinkbot project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$crgcj_8@zzu@v^fapdi&a9$_5or!j2gh+zti+5dg6lcy*3sk5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['139.59.6.15']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chatterbot.ext.django_chatterbot',
    'aryabot',
]

# ChatterBot settings

CHATTERBOT = {
    'name': 'Django ChatterBot Example',
    #'trainer': 'chatterbot.trainers.ChatterBotCorpusTrainer',
    'trainer': 'chatterbot.trainers.ListTrainer',
    'training_data': [
        #'chatterbot.corpus.english.greetings'
    "Hi there!",
    "Hello",
    "Hello",
    "Hello",
    "Name",
    "Aryabot",
    "Who are you?",
    "I am Aryabot :)",
    "Father of Rethink",
    "Sijo Kuruvilla George",
    "Who is the father",
    "Sijo Kuruvilla George",
    "What is the address of rethink",
    "Rethink Technology Foundation, No.21/536A, AMS Building, CUSAT P.O, Thrikkakara North, Ernakulam, Kerala, India - 682022",
    "What is the address",
    "Rethink Technology Foundation, No.21/536A, AMS Building, CUSAT P.O, Thrikkakara North, Ernakulam, Kerala, India - 682022",
    "Where is office?",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "How to reach Rethink",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "Get to rethink",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "Get there",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "How to get there",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "Google maps link of Rethink",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "Google maps link",
    "Here is the link to follow : http://www.bit.ly/gettorethink",
    "What is the wiki link",
    "Here you go : http://wiki.rethinkfoundation.in",
    "Rethink wiki",
    "Here you go : http://wiki.rethinkfoundation.in",
    "Rethink website",
    "Here you go : http://rethinkfoundation.in",
    "Website",
    "Here you go : http://rethinkfoundation.in",
    "Blog",
    "Here you go : http://blog.rethinkfoundation.in",
    "Rethink blog",
    "Here you go : http://blog.rethinkfoundation.in",
    "Opportunity",
    "Here you go : http://wiki.rethinkfoundation.in/opportunities",
    "Opportunities",
    "Here you go : http://wiki.rethinkfoundation.in/opportunities",
    "Who is the contact person",
    "You can send email to this email id http://volunteers@rethinkfoundation.in",
    "What are the projects?",
    "Here you go http://wiki.rethinkfoundation.in/Projects",
    "What is rethink foundation",
    "Rethink foundation is a non profit organization",
    "Team members",
    "Sijo, Arya, Aby",
    "Founders of rethink",
    "Sijo, Arya, Aby",
    "Founder of rethink",
    "Sijo, Arya, Aby",
    "Thank you",
    "You are welcome :)",
    "Thanks",
    "You are welcome",
    "Bye",
    "Bye :) Have a good day!",
    "Who is your creator?",
    "Zac!",
    "Who invented you?",
    "Zac!",
    "Who is the inventor",
    "Zac!",
    "How to join rethink",
    "Rethink is a non profit organisation and not an incubator / accelerator / coworking space. There is no process to join / register. Currently the space is provided to volunteers who are working on Rethink focused projects.",
    "What is Rethink",
    "Rethink is a non profit organisation and not an incubator / accelerator / coworking space. There is no process to join / register. Currently the space is provided to volunteers who are working on Rethink focused projects."
    ],
    'django_app_name': 'django_chatterbot'
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rethinkbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rethinkbot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
