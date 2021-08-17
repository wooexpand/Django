"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.shortcuts import HttpResponse, render, redirect
def login(request):
    #return HttpResponse('abddksafk')
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        u = request.POST.get('user')
        p = request.POST.get('pass')
        if u == "root" and p == "123123":
            return redirect('http://google.com')
        else:
            return render(request, 'login.html', {'msg': 'username or password are invalid!'})
def showlist(request):


    return render(request, 'showList.html', {'myUserList':[
        {'id':'1', 'username':'Kondo',  'email':'jun.kondo@yaho.coo.jp'},
        {'id':'2', 'username':'Tanaka', 'email':'yuusuke.tanaka@yaho.coo.jp'},
        {'id':'3', 'username':'Yito',   'email':'hitomi.yito@yaho.coo.jp'}]})
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', login),
    path('showlist/', showlist),

]
