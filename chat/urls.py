from django.urls import path

from chat import views

urlpatterns = [
    path('',views.Main.as_view(),name='main'),
    path('home',views.Home.as_view(),name='home'),
    path('chat-person',views.ChatPerson.as_view(),name='chat_person'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('register',views.Register.as_view(),name='register'),
]