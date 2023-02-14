from django.urls import path,include
from django.contrib import admin
from blog import views

urlpatterns = [
    path('',views.PostView.as_view(), name='home'),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail")
]