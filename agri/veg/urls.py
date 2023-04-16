
from django.urls import path
from . import views
urlpatterns = [
    
    path('reg/',views.reg,name="reg"),
    path('',views.login,name="login"),
    path('home/',views.home,name="home"),
    path("form/",views.form,name="form"),
    path("verify",views.verify,name="verify"),
    path('veg/<int:id>/',views.detail, name='detail'),
    path('verifydelete',views.verifydelete, name='verifydelete'),
    path('te/',views.weather_view,name="wheather"),
    path('lefo/',views.leasrform,name="lefo"),
    path('levr',views.leaseverify,name="levr"),
    path('le',views.lease,name="le"),
    path('ls/<int:id>/',views.leasedetail, name='leasedetail'),
    path('main/',views.main,name="main"),
    path('verla',views.verla,name="verla"),
    path('verimarit',views.verimarit,name="verimarit"),
]
