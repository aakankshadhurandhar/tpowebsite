import pyrebase
from django.shortcuts import render
from django.contrib import auth

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
    return render(request,'signin.html')


def postsign(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:


        user=authe.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credencials"
        return render(request,"signin.html",{'mess':message})

    print(user['idToken'])

    session_id=user['idToken']
    request.session['uid']=str(session_id)

    return render(request,'dashboard.html',{'e':email})
def logout(request):
    auth.logout(request)
    return render(request,'signin.html')
def signup(request):
    return render(request,'signup.html')
def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    unirn=request.POST.get('unirollno')
    branch=request.POST.get('branch')
    semester=request.POST.get('semester')
    classrollno=request.POST.get('crn')
    try:
        user=authe.create_user_with_email_and_password(email,passw)

    except:
        message='unable to create account '
        return render(request,'signup.html',{"messg":message})
    uid = user['localId']
    data = {"universityrollno":unirn,"name": name,"branch":branch,"semester":semester,"classrollno":classrollno,'email': email}
    database.child("users").child(uid).child("details").set(data)
    return render(request,'signin.html')

