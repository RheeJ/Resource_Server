# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, detail_route
from rest_framework.response import Response
from authapp.models import *
import requests
# Create your views here.

@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def login(r):
    """
    Input: User Email and User Password (str, str)
    Output: Access Credentials as Payload
    Login using email and password to generate a user access token. Using the access_token header, user can access certain features.
    """
    email, password  = r.POST.get('email'), r.POST.get('password')
    payload = (('grant_type', 'password'), ('username', email), ('password', password), ('client_id', 'kb2oCM69TqC7rOHzUQKn3mkDiSOgnE6TITBJTjsN'), ('client_secret', 'kgNZRelRLHNZHWO0kfl55FQq6s8tfamCGG04RTmTLOZxSfrcXbDex2ZulRWXuyoEwJF68QSjGjSdCQT3sw2N9HHjvVbB3YQinwlyJCWGKyD893dRIcie1R2TUes5iHo1'))
    resp = requests.post('http://ec2-34-230-22-130.compute-1.amazonaws.com:8000/oauth/token/', data=payload)
    if resp.status_code == 200:
        try:
        	q = QuarkX_User.objects.get(email=email)
                return Response(resp.json(), 200)
        except Exception as e:
            print e
            q = QuarkX_User.objects.create(email=email)
            return Response(resp.json(), 200)
    else:
        return Response('',401)

def verify(access_token):
    resp = requests.get('http://ec2-34-230-22-130.compute-1.amazonaws.com:8000/verify/', headers={'Authorization': 'Bearer {}'.format(access_token)})
    if resp.status_code == 200:
        return (True, resp.text)
    else:
        return (False, '')

@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def Print_Roles(r):
    authorized, email = verify(r.POST.get('access_token'))
    print email
    if authorized:
        q = QuarkX_User.objects.get(email=str(email))
        result = "QUARKX CLIENT\nROLES: "
        result += "SUPER_USER( {0} ), REPORT_USER( {1} ), NORMAL_USER( {2} )".format(q.isSuper, q.isReport, q.isNormal)
        return Response(result, 200)
    else:
        return Response('Unauthorized', 401)
