"""ask_rogachev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from ask_rogachev import views

urlpatterns = [
	url(r'^$', views.newQuestions, name = 'new'),
    url(r'^hot/$', views.hot, name = 'hot'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^signup/$', views.signup, name = 'signup'),
    url(r'^ask/$', views.ask, name = 'ask'),
    url(r'^question/(?P<questionId>[0-9]+)/$', views.question, name = 'question'),
    url(r'^question/(?P<questionId>[0-9]+)/?page=(?P<pageNumber>[0-9]+)/$', views.question, name = 'question'),
    url(r'^tag/(?P<tagName>[-\w]+)/$', views.tag, name = 'tag'),
    url(r'^admin/', admin.site.urls),
    url(r'^settings/', views.settings, name = 'settings'),
    url(r'^logout/', views.logout, name = 'logout'),
    url(r'^like_question/$', views.like_question, name = 'like_question'),
    url(r'^like_answer/$', views.like_answer, name = 'like_answer'),
    url(r'^correct/$', views.correct_answer, name = 'correct')
]
