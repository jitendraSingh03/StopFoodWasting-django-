from django.urls import path
from . import views
from django.conf import settings       #setting file ko import karne ke lia
from django.conf.urls.static import static

urlpatterns =[
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('help/',views.help,name="help"),
    path('order/',views.order,name="order"),
    path('thanks/',views.thanks,name="thanks"),
    path('workplace/',views.workplace,name="workplace"),
    path('userposted/',views.userposted,name="userpost"),
    path('contect/',views.connect,name="contect"),
    path('registration/',views.registration,name="registration"),
    
    path('feedback/',views.feedbacker,name="feedback"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 