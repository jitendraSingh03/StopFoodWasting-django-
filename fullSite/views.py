import smtplib
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth  # w1e import User and auth for create user in database
from .models import userpost,orderBook,moneyRefund,account,feedback,contect
from django.utils import timezone

# Create your views here.
def home(request):
    post=userpost.objects.all()
    return render(request,'fullSite/home.html',{"Posts":post})



def about(request):
    return render(request,'fullSite/join.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['email']
        password=request.POST['password1']
        user = auth.authenticate(username=username,password=password)   # auth.authenticate() use for checking username or passwaord
        if user is not None:
            orderbook=orderBook.objects.all()   
            return render(request,'fullSite/workPlace.html',{'user':user,'order':orderbook})
        else:
            return render(request,'fullSite/login.html',{'error':'please check email'})
    return render(request,'fullSite/login.html')

def logout(request):
    auth.logout(request)   # use for log out ....
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():  # checking weather  username it is exist or not if exists return true ....
                 return render(request,'fullSite/signup.html',{"error":"Username already exists"})
            elif User.objects.filter(email=email).exists():
                 return render(request,'fullSite/signup.html',{"error":"Email already exists"})
            else:
                # con=smtplib.SMTP('smtp.gmail.com',587)
                # con.ehlo()
                # con.starttls()
                # con.login('bukh.foodwastage@gmail.com','up80db8192')
                # con.sendmail('bukh.foodwastage@gmail.com',email,'Subject:congratulation \n\n you are success fully join our team, also thanks for joining us.We thing you work hard with us .')
                # con.quit()
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=fname)
                user.save()
                orderbook=orderBook.objects.all()   
            return render(request,'fullSite/workPlace.html',{'user':user,'order':orderbook})
        else:
            return render(request,'fullSite/signup.html',{"error":"password does't match"})
    else:
        return render(request,'fullSite/registration.html')


def help(request):

    return render(request,'fullSite/help.html')


def order(request):
    if request.method =="POST":
        person=request.POST['name']
        phone1=request.POST['phone']
        phone2=request.POST['phone2']
        address=request.POST.get('add')
        date=request.POST['date']
        time=request.POST['time']
        city=request.POST['city']
        landmark=request.POST['landmark']
        orderbook=orderBook(personname=person,personphone=phone1,othernumber=phone2,eventdate=date,eventtime=time,eventcity=city,eventlandmark=landmark,eventaddress=address)
        orderbook.save()
        return render(request,'fullSite/thanks.html',{"name":person,"message":"Thanks for giving your support with us . We contect you as soon as possible."})
 
    return render(request,'fullSite/order.html')


def thanks(request):
    if request.method == "POST":
        orid=request.POST['orid']
        amount=request.POST['amount']
        image1=request.FILES['image1']
        image2=request.FILES['image2']
        username=request.POST['username']
        date=str(timezone.datetime.now())
        
        user=orderBook.objects.filter(orderid=orid)
        user.update(completedBy=username)
        complete=moneyRefund(completedBy=username,orderId=orid,amount=amount,image1=image1,image2=image2,date=date)
        complete.save()
        return render(request,'fullSite/thanks.html',{"message":"thanks for completing order","name":username})
    return render(request,'fullSite/thanks.html')

def workplace(request):
    if request.method == "POST":
        name=request.POST.get('username')
        desc=request.POST.get('description')
        img=request.FILES['img']
        vote=0
        post=userpost(person=name,desc=desc,vote=vote,image=img)
        post.save()
        orderbook=orderBook.objects.all()
        return render(request,'fullSite/workPlace.html',{"order":orderbook,"user":name})
    
    return render(request,'fullSite/thanks.html',{"name":"you con't access from here","message":"go at home page."})

def userposted(request):
    if request.method == "POST":
        username=request.POST['username']
        return render(request,'fullSite/userpost.html',{'user':username})

    return render(request,'fullSite/thanks.html',{"name":"you con't access from here","message":"go at home page."})




def connect(request):
    if request.method == 'POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        query=request.POST['query']
        contected=contect(name=name,quary=query,phone=phone,email=email)
        contected.save()
        return render(request,'fullSite/thanks.html',{"name":name,"message":"your query is send."})    
    return render(request,'fullSite/contect.html')


def registration(request):
    if request.method == "POST":
        name=request.POST['name']
        phone=request.POST['phone']
        city=request.POST.get('city')
        state=request.POST['state']
        landmark=request.POST['landmark']
        address=request.POST.get('address')
        accountNo="nono"
        totolorder=0
        account_create=account(username=name,phone=phone,city=city,State=state,landmark=landmark,address=address,accountNo=accountNo,totalOrder=totolorder)
        account_create.save()
        return render(request,'fullSite/signup.html',{"fname":name})
    return render(request,'fullSite/registration.html')

def feedbacker(request):
    feed=request.POST.get('Feedback')
    feedus=feedback(response=feed)
    feedus.save()
    return render(request,'fullSite/home.html')