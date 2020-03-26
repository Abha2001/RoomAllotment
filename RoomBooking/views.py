from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
    return render(request,'../templates/index.html')

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('bookRoom')
    else:
        form=UserCreationForm()
    return render(request,'../templates/signup.html',{'form':form})

def login_view(request):
    message=False
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            message="Invalid Username or Password"
    return render(request,'../templates/login.html',{'message':message})

def logout_view(request):
    logout(request)
    return redirect('index')

def bookRoom(request):
    roomList=getRoomList()
    message2=False
    message=False
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid:
            Date=request.POST['Date']

            availableObject=Available.objects.get(id=(request.POST['Time']))
            
            startTime=availableObject.startTime
            
            endTime=availableObject.endTime
            
            roomAvailable=availableObject.roomNo
            
            roomNo=request.POST['roomNo']
            
            if int(str(roomAvailable))==int(str(roomNo)):
                isVacant=checkVacancy(Date,startTime,endTime,roomNo)
                if isVacant==True:
                    form.save()
                    return render(request,'../templates/thanks.html')
                else:
                    message='The room is  booked! Please make a different choice!'
                   
            else:
                message2="The room you want is not available in the desired slot. Please choose from the given list"
    else:
        form=BookingForm()
    return render(request,'../templates/bookingForm.html',{'form':form,
    'message':message,
    'roomList':roomList,
    'message2':message2})

def checkVacancy(Date,startTime,endTime,roomNo):
    sameRoom=Guest.objects.filter(roomNo=roomNo)
    
    sameDate=sameRoom.filter(Date=Date)
    
    sameTime=sameDate.filter(Time__startTime= startTime,Time__endTime=endTime) 
    
    if sameTime:
        return False
    return True

def addSlot(request):
    if request.method=='POST':
        form=SlotsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('bookRoom')
    else:
        form=SlotsForm()
        return render(request,'../templates/addSlots.html',{'form':form})
    
def getRoomList():
    message=Available.objects.all()
    
    startTimeList=[i.startTime.strftime('%H:%M:%S') for i in message]
    
    endTimeList=[i.endTime.strftime('%H:%M:%S') for i in message]
    
    roomNoList=[str(i.roomNo) for i in message]
    
    roomList=[{'roomNo':roomNoList[i], 'startTime':startTimeList[i],
    'endTime':endTimeList[i]} for i in range (len(roomNoList))]

    return roomList