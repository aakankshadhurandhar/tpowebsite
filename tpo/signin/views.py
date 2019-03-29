import pyrebase
from django.shortcuts import render

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
auth=firebase.auth()
def signin(request):
    return render(request,'signin.html')


def postsignin(request):
    return render(request,'welcome.html')





