from django.shortcuts import render
from django.http import HttpResponse
from .models import Food, Room, Order, Menu,Sweet,Chat,Bevage
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail

@login_required
def welcome(request):
    return render(request,'hotelapp/index.html',{})
    # return HttpResponse('welcome to hotel mangemanagement application')

@login_required
def listfood(request):
    foods=Food.objects.all()
    #nv=NorthIndianVeg.objects.all()
    #nn = NorthIndianNonveg.objects.all()
    #sv =South_Indian_Veg .objects.all()
    #sn =South_Indian_Nonveg .objects.all()
    #return render(request,'hotelapp/food.html',{'nv':nv,'nn':nn,'sv':sv,'sn':sn})
    return render(request, 'hotelapp/food.html', {'foods':foods})

def updatefood(request):
    updatefoods=Food.objects.create()

@login_required
def listroom(request):
    rooms=Room.objects.all()
    return render(request,'hotelapp/rooms.html',{'rooms':rooms})

#@login_required
def liststarter(request):
    sweets=Sweet.objects.all()
    chats=Chat.objects.all()
    bevages=Bevage.objects.all()
    return render(request,'hotelapp/starters.html',{'sweets':sweets,'chats':chats,'bevages':bevages})

#def takeorder(request):
#if request.method=='GET':
#render the template where form is there
@login_required
def contact(request):
    #contacts=Contact.objects.all()
    return render(request,'hotelapp/contact.html',{})

def sign_in(request):
    if request.method=='GET':
        users=User.objects.all()
        return render(request, 'hotelapp/sign-in.html', {'users':users})
    elif request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        emailid=request.POST['emailid']
        newuser=User.objects.create_user(email=emailid,username=username,password=password)
        newuser.save()
        print newuser.id
        return render(request, 'hotelapp/sign-in.html', {})

def loginuser(request):
    if request.method=='GET':
        return render(request,'hotelapp/login.html',{})

    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            print 'login success'
            login(request,user)
            #Login is successful
            return render(request, 'hotelapp/index.html', {})
        else:
            print 'login failure'
            #Login Fail Send some message
            return render(request, 'hotelapp/login.html', {'error':'Username or password Wrong'})




def about(request):
    return render(request,'hotelapp/about.html',{})

@login_required
def order(request):
    if request.method=='GET':
        foods=Food.objects.all()
        #nv = NorthIndianVeg.objects.all()
        #nn = NorthIndianNonveg.objects.all()
        #sv = South_Indian_Veg.objects.all()
        #sn = South_Indian_Nonveg.objects.all()
        rooms = Room.objects.all()
        #return render(request,'hotelapp/order.html',{'nv':nv,'nn':nn,'sv':sv,'sn':sn,'rooms':rooms})
        return render(request, 'hotelapp/order.html', {'foods':foods, 'rooms': rooms,'ordercomplete':False})

    elif request.method=='POST':
        foodid=request.POST['food']
        fooditem=Food.objects.get(pk=foodid)
        #fooditem1 = NorthIndianVeg.objects.get(pk=foodid)
        #fooditem2 = NorthIndianNonveg.objects.get(pk=foodid)
        #fooditem3 = South_Indian_Veg.objects.objects.get(pk=foodid)
        #fooditem4 = South_Indian_Nonveg.objects.objects.get(pk=foodid)

        roomid=request.POST['rooms']
        roomitem=Room.objects.get(pk=roomid)

        now=datetime.now()
        print request.user
        user_id=request.user.id
        print user_id
        #user_id=1
        neworder=Order(food_item=fooditem,room_type=roomitem,user_id=user_id,order_timestamp=now,status='In Progress')
        neworder.save()
        print neworder.id
        #send an email with order id to customer
        message='Order has been placed with order id: '+str(neworder.id)
        emailcustomers('order','vidya.s099@gmail.com',[request.user.email],'Order Placed',message)
        orders = Order.objects.all()

        return render(request, 'hotelapp/order.html', {'orders': orders,'ordercomplete':True})
        #return HttpResponse('YOu called the post method with food id'+str(foodid),)

def user(request):
    user1 = User.objects.create_user(email='vidhya2@gmail.com', username='test2', password='test@12345')
    user1.save()
    # user1.password = 'test'
    # user1.save()
    return HttpResponse('user created succcessfully')

def sendSimpleEmail(request):
   res = send_mail('Subject here', 'Here is the message.', 'vidya.s099@gmail.com', ['vidya.s099@gmail.com'], fail_silently=False)
   return HttpResponse('%s'%res)

def emailcustomers(emailtype,fromemail,to,subject,message):
    res = send_mail(subject,message,fromemail,to,fail_silently=False)
    return True



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/hotelapp/')