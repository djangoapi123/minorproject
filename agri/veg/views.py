from django.shortcuts import render 
import requests

from datetime import date
# Create your views here.


from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.models import User , auth
from .models import product , reconfigure ,ls , lsre     , vl   , vm
# Create your views here.



def reg(request):
    if(request.method == "POST"):
        fn=request.POST['fn']
        sdn=request.POST['sdn']
        un=request.POST['un']
        em=request.POST['em']
        p=request.POST['p']
        cp=request.POST['cp']
        if(p==cp):
            a= User.objects.filter(username=un).first()
            if(a is not  None):
                print("already registred ")
            else:


                print(p)
                User.objects.create_user(username=un,email=em,password=p).save()
                aa=User.objects.filter(username=un,password=p).first()
                print(aa)
                print("registered successfully the {}".format(un))
                return redirect(login)
        else:
            print("password didn't match")
    return render (request,'reg.html',{})



def login(request):
    if(request.method=="POST"):
        un=request.POST['nqw']
        p=request.POST['p']
        aa=User.objects.filter(username=un,password=p).first()
        print(un,p,aa)
        if(aa is not None):
            return redirect(home)
        else:
            print("invalid")    
    return render(request,'login.html',{})


def home(request):
    today = date.today()
    products = product.objects.filter(p_da__gte=today)
    expired_products = product.objects.filter(p_da__lt=today)        
    count = expired_products.count()  
    expired_products.delete()
    return render(request,'home.html',{'product':products})



def form(request):
    if(request.method=="POST"):
        
        na=request.POST['na']
        da=request.POST['da']
        qa=request.POST['qa']
        loc=request.POST['loc']
        sn=request.POST['sn']
        ph=request.POST['ph']
        pr=request.POST['pr']
        
        reconfigure(na=na,dis=qa,loc=loc,sn=sn,pr=pr,ph=ph,da=da).save()
        return redirect (home)
    return render(request,'form.html',{})


def verify(request):
    
    products=reconfigure.objects.all()
    if(request.method=="POST"):
        name=request.POST['name']
        na=request.POST['na']
        qa=request.POST['qa']
        loc=request.POST['loc']
        sn=request.POST['sn']
        ph=request.POST['ph']
        pr=request.POST['pr']
        da=request.POST['da']
       
        a=reconfigure.objects.filter(na=na,dis=qa,loc=loc,sn=sn,pr=pr,ph=ph).first()
        
        if a is not None:
            product(p_na=na,p_dis=qa,p_loc=loc,p_sn=sn,p_pr=pr,p_ph=ph,p_da=da).save()  

            a.delete()
        else:
            return render(request,'verify.html' ,{'product':products,'key':"no products "})

        
    

    return render(request,'verify.html' ,{'product':products})





def detail(request, id=None): # < here
    flower = get_object_or_404(product , p_id=id)
    return render(request, 'detail.html', {'flower': flower})



def verifydelete(request):
    if(request.method=="POST"):
       
        na=request.POST['na']
        qa=request.POST['qa']
        loc=request.POST['loc']
        sn=request.POST['sn']
        ph=request.POST['ph']
        pr=request.POST['pr']
        da=request.POST['da']
        a=reconfigure.objects.filter(na=na,dis=qa,loc=loc,sn=sn,pr=pr,ph=ph).first()
        
        if a is not None:
            # product(p_na=na,p_dis=qa,p_loc=loc,p_sn=sn,p_pr=pr,p_ph=ph,p_da=da).save()  

            a.delete()
        else:
            return render(request,'verifydetete.html' ,{'key':"no products "})

        

    return render(request,'verifydetete.html')




def weather_view(request):
    if(request.method=="POST"):
        na=request.POST['na']
        # Retrieve the location from the request, e.g. request.GET.get('location')
        location = na 
        api_key = "37d7001c033c224d47c330f1e5b4d9a8"

        # Make an HTTP GET request to the OpenWeatherMap API endpoint       
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}')

        # Parse the JSON response data to extract the weather information
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            temperature=temperature-273
            temperature=round(temperature,1)
            description = data['weather'][0]['description']
            # Render a template with the weather information
            return render(request, 'weather.html', {'temperature': temperature, 'description': description,'name':na})
        else:
            # Handle the error case, e.g. by rendering an error page
            return render(request, 'error.html')



    return render(request, 'weather.html')




def leasrform(request):
    if(request.method=="POST"):
        
        na=request.POST['name']
        da=request.POST['email']
        qa=request.POST['start-date']
        loc=request.POST['end-date']
        pr=request.POST['pr']
        print(na,da,qa,loc,pr)
        lsre(na=na,de=da,da=qa,eda=loc,pr=pr).save()
        return redirect (home)
    return render(request,'leaseform.html',{})



def leaseverify(request):
    
    products=lsre.objects.all()
    if(request.method=="POST"):
        na=request.POST['name']
        da=request.POST['email']
        qa=request.POST['start-date']
        loc=request.POST['end-date']
        pr=request.POST['pr']
        print(na,da,qa,loc,pr)
        a=lsre.objects.filter(na=na,de=da,da=qa,eda=loc,pr=pr)
        
        
        if a is not None:
            ls(na=na,de=da,da=qa,eda=loc,pr=pr).save()

            a.delete()
        else:
            return render(request,'leaseverify.html' ,{'product':products,'key':"no products "})

        
    

    return render(request,'leaseverify.html' ,{'product':products})





def lease(request):
    today = date.today()
    products = ls.objects.filter(eda__gte=today)
    expired_products = ls.objects.filter(eda__lt=today)        
    count = expired_products.count()  
    expired_products.delete()
    return render(request,'lease.html',{'product':products})


def leasedetail(request, id=None): # < here
    flower = get_object_or_404(ls,id=id)
    return render(request,'leasedetail.html' , {'flower': flower})


def main(request):
    return render(request,'main.html')




def verla(request):
    if(request.method=="POST"):
        un=request.POST['un']
        p=request.POST['p']
        a=vl.objects.filter(un=un,p=p).first()
        if a is not None:
            return redirect(leaseverify)
        else:
            return render(request,'verla.html',{'key':"not valid user"})
    return render ( request,'verla.html')


def verimarit(request):
    if(request.method=="POST"):
        un=request.POST['un']
        p=request.POST['p']
        a=vm.objects.filter(un=un,p=p).first()
        if a is not None:
            return redirect(verify)

        else:
            return render(request,'verimarit.html',{'key':"not valid user"})
    return render ( request,'verimarit.html')