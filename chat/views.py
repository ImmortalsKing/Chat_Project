from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import View
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class Main(View):
    def get(self,request):
        #region comments
        # data = {
        #         'type' : 'receiver_function',
        #         'message' : 'this is MR chatroom',
        #         'website' : 'MR chat'
        #     }
        # request.session['get_me_from_the_consumer'] = 'this is python'
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)('MR_chat',data)
        #endregion
        if request.user.is_authenticated:
            return redirect('home')
        return render(request,'chat/main.html')

class Home(View):
    def get(self,request):
        if request.user.is_authenticated:
            users = User.objects.all()
            context = {
                'users' : users
            }
            return render(request, 'chat/home.html',context)
        else:
            return redirect('main')

class ChatPerson(View):
    def get(self,request,id):
        person:User = User.objects.filter(id=id).first()
        me = request.user
        context = {
            'person':person,
            'me':me
        }
        return render(request, 'chat/chat_person.html',context)

class Login(View):
    def get(self,request):
        return render(request, 'chat/login.html')

    def post(self,request):

        context = {}
        data = request.POST.dict()

        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username__iexact=username).first()
        if user is not None:
            is_password_correct = user.check_password(password)
            if is_password_correct:
                login(request,user)
                return redirect('home')
            else:
                context = {'error':'the user name or password is wrong'}
        else:
            context = {'error':'the user name or password is wrong'}

        return render(request, 'chat/login.html',context)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class Register(View):
    def get(self,request):
        return render(request, 'chat/register.html')

    def post(self,request):

        context = {}
        data = request.POST.dict()
        print(data)

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        try:
            new_user = User()
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.username = username
            new_user.email = email
            new_user.set_password(password)
            new_user.save()
            user = authenticate(request=request, username=username, email=email)

            if user != None:
                login(request, user)
                return redirect('home')

        except:
            context = {
                'error' : 'the data is wrong'
            }

        return render(request, 'chat/register.html',context)
