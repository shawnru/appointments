from __future__ import unicode_literals
from django.db import models
import datetime
import re
import bcrypt

password_regex = re.compile(r'^[a-zA-Z0-9.+_!@#$%^&*()={}[]|~`,<>?/;:"-]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User_manager(models.Manager):
    def register(self, postdata):
        error = []
        response_to_views = {}
        if postdata:
            if len(postdata['name']) < 3 and not re.search(r'^\w+$', postdata['name']):
                error.append('Please use three or more letters to write your name.')
            if re.search(r' ', postdata['email']):
                error.append('Don\'t use spaces or random character in your email.')
            if not EMAIL_REGEX.match(postdata['email']):
                error.append('Please use a correct email address.')
            if len(postdata['password']) < 8:
                error.append('Please use 8 or more characters to write your password.')
            elif not password_regex.match(postdata.get('password')):
                error.append('Please dont use foreign characters and keep your special characters to a minimum.')
            if postdata.get('password') != postdata.get('confirmpw'):
                error.append('Both passwords must match.')
            if User.objects.filter(email=postdata['email']):
                error.append('This email already exists, please choose another one.')
            if User.objects.filter(email=postdata['email']):
                error.append('This email already exists, please choose another one.')
            if error == []:
                password = bcrypt.hashpw(postdata['password'].encode(), bcrypt.gensalt())
                self.create(email=postdata['email'],password=password,name=postdata['name'],birthdate=postdata['birthdate'])
                error.append('Thank you for registering, please log-in with your new username and password!')
        response_to_views['errors'] = error
        return response_to_views

    def signin(self, postdata):
        response_to_signin = {}
        idea = []
        user = User.objects.filter(email=postdata['email'])
        if postdata:
            if user:
                if bcrypt.hashpw(postdata['password'].encode(), user[0].password.encode()) == user[0].password.encode():
                    for z in user:
                        idea.append(z)
                    response_to_signin['id'] = idea
        return response_to_signin

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    birthdate = models.CharField(max_length=50, default=datetime.date.today())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = User_manager()
