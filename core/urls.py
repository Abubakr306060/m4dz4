"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from posts.views import hello, IndexView , about , contacts , PostDetailView , PostCreateView , PostDeleteView , PostUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello, name='hello'),
    path("", IndexView.as_view(), name="main-page"),
    path("about/",about, name="about-page"),
    path("contacts/",contacts, name="contacts-page"),
    path("post/<int:pk>/", PostDetailView.as_view(),name="post-detail" ),
    path("post/create", PostCreateView.as_view(), name="post-create"),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete" ),
    path("post/update/<int:pk>", PostUpdateView.as_view(), name="post_update")
  

]
