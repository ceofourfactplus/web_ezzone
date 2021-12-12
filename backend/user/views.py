from django.core import exceptions
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class RegisterUserAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        can_save = True

        if User.objects.filter(username=username).exists():
            can_save = False
            return Response('Username or password is taken, choose another one', status=400)

        if User.objects.filter(email=email).exists():
            can_save = False
            return Response('Username or password is taken, choose another one', status=400)

        if can_save:
            user = User.objects.create_user(username, email, password)
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.is_active = False
            user.save()
            html_content = render_to_string('user/send_verify_mail.html',{'token':default_token_generator.make_token(user),'user_id':user.id,'name':user.first_name,})
            plain_content = strip_tags(html_content)
            send_mail(
                'testezzone',
                plain_content,
                'testezzone@gmail.com',
                [user.email],
                fail_silently=False,
                html_message=html_content,
            )
            data = UserSerializer(user)
            return Response(data.data, status=201)

        return Response(status=400)


class UserInfo(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class activate(APIView):
    def put(self, request,):
        user = User.objects.get(id=request.data['id'])
        if default_token_generator.check_token(user, request.data['token']):
            serializer = UserSerializer(user,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('Thank you for your email confirmation.',status=200)
            return Response('bad request',status=400)
        return Response('Activation link is invalid!',status=400)


class ConfirmPass(APIView):
    def post(self, pk,request):
        user = User.objects.get(id=request.data['id'])
        if user.check_password(request.data['password']):
            return Response('password correct', status=200)
        return Response('password Incerrect', status=400)

class IsActive(APIView): 
    def post(self, request):
        user = User.objects.get(username=request.data['username'])
        if user.check_password(request.data['password']):
            if user.is_active:
                return Response('is_active')
            return Response('is_not_active', status=400)
        return Response('your password is incorrect', status=400)
        
