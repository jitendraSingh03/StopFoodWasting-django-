from django.db import models

# Create your models here.
class account(models.Model):
    customer_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    phone=models.CharField(max_length=14,default="")
    email=models.CharField(max_length=30)
    landmark=models.CharField(max_length=20)
    city=models.CharField(default="",max_length=20)
    State=models.CharField(default="",max_length=20)
    address=models.CharField(default="",max_length=200)
    totalOrder=models.IntegerField(default=0)
    accountNo=models.CharField(default="",max_length=20)
    def __str__(self):
        return str(self.username)
    def accountID(self):
        return self.customer_id

        
class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    person_name=models.CharField(max_length=30)
    person_phone=models.CharField(max_length=30)
    other_number=models.CharField(max_length=20)
    event_date=models.CharField(max_length=30)
    event_time=models.CharField(max_length=30)
    event_city=models.CharField(max_length=30)
    event_landmark=models.CharField(max_length=50)
    event_address=models.CharField(max_length=200)

    def __str__(self):
        return self.person_name


class userpost(models.Model):
    person=models.CharField(max_length=30)
    desc=models.TextField()
    vote=models.IntegerField(default=0)
    image=models.ImageField(upload_to="fullSite/image")
    date=models.DateField( default="1999-11-23")

    def __str__(self):
        return self.person 


class orderBook(models.Model):
    orderid=models.AutoField(primary_key=True)
    personname=models.CharField(max_length=30)
    personphone=models.CharField(max_length=30)
    othernumber=models.CharField(max_length=20)
    eventdate=models.CharField(max_length=30)
    eventtime=models.CharField(max_length=30)
    eventcity=models.CharField(max_length=30)
    eventlandmark=models.CharField(max_length=50)
    eventaddress=models.CharField(max_length=200)
    completedBy=models.CharField(max_length=30,default="unknown")
    def __str__(self):
        return self.personname


class moneyRefund(models.Model):
    completedBy=models.CharField(max_length=30)
    orderId=models.CharField(max_length=20)
    amount=models.CharField(max_length=20)
    image1=models.ImageField(upload_to='fullSite/image')
    image2=models.ImageField(upload_to='fullSite/image')
    date=models.CharField(max_length=20)

    def __str__(self):
        return self.orderId



class contect(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    quary=models.CharField(max_length=300)

    def __str__(self):
        return self.name
    

class feedback(models.Model):
    response=models.CharField(max_length=300,default="None")