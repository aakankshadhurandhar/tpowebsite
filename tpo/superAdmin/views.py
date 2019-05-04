#from django.shortcuts import render

# Create your views here.

import pyrebase
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse

# Create your views here.
config={



    'apiKey': "AIzaSyCeXV4CNWlcGanHtJ7dk0CasgBVqww3Ixg",
    'authDomain': "bitdurgtpo-48593.firebaseapp.com",
    'databaseURL': "https://bitdurgtpo-48593.firebaseio.com",
    'projectId': "bitdurgtpo-48593",
    'storageBucket': "bitdurgtpo-48593.appspot.com",
    'messagingSenderId': "1040969843907"
  }

firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()
def signin(request):
    return render(request,'admin_signin.html')

def xyz(request):
    return HttpResponse("hello world")

def sign(request):
        email=request.POST.get('email')
        passw=request.POST.get('pass')
        if email== 'admin@gmail.com' and passw == 'admin':
            return render(request,'admin_dashboard.html')
        else:
            message="invalid credencials"
            return render(request,"admin_signin.html", {'mess':message})



