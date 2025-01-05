from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import View


class Main(View):
    def get(self,request:HttpRequest):
        return render(request,'chat/main.html')

class Home(View):
    def get(self,request):
        return render(request, 'chat/home.html')

class ChatPerson(View):
    def get(self,request):
        return render(request, 'chat/chat_person.html')

class Login(View):
    def get(self,request):
        return render(request, 'chat/login.html')

class Logout(View):
    def get(self, request):
        pass

class Register(View):
    def get(self,request):
        return render(request, 'chat/register.html')