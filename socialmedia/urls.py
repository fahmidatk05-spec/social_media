"""
URL configuration for socialmedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from socialmedia_app.views import *
from rest_framework.authtoken.views import obtain_auth_token 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',SignUpView.as_view()),
    path('token',obtain_auth_token),
    path('post',PostCreateListView.as_view()),
    path('post/<int:pk>',PostRetrieveUpdateDestroyView.as_view()),
    path('post-list',CommonPostwallView.as_view()),
    path('comment',CommentCreateListView.as_view()),
    path('comment/<int:pk>',CommentRetrieveDestoryView.as_view()),
    path('like',LikeCreateListView.as_view()),
    path('unlike/<int:pk>',UnLike.as_view()),
    path('following',FollowingView.as_view()),
    path('following/<int:pk>',UnFollowView.as_view())
]
