from django.conf.urls import url

from . import views

urlpatterns = [

    # /user/
    #url(r'^$'),

    # /user/create/
    url(r'^create/$', views.UserCreateView.as_view(), name="UserCreate"),

    # /user/login/
   	# url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'users/user_login.html'}, name="UserLogin"),

    # /user/username/
    #url(r'(?P<username>[0-9a-zA-Z]+)/$'),

    # /user/username/
    url(r'^(?P<username>[0-9a-zA-Z]+)/$', views.profile, name="ProfileView"),

    # /user/add_friend/pk
    url(r'^add_friend/(?P<pk>[0-9]+)/$', views.add_friend, name="AddFriend")
]
