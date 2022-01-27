import email
from email import message
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.core.mail import send_mail
from app.models import cat1,cate2,item

from Jade.settings import EMAIL_HOST_USER
# Create your views here.
def index(request):
    return render(request,'index.html')
def hello(request):
    return render(request,'home.html')
def ahome(request):
    return render(request,'admin/home.html')
def categ(request):
    return render(request,'admin/addcategoryone.html')


def vcat1(request):
    return render(request,'admin/viewcat1.html')
def vcat2(request):
    return render(request,'admin/viewcat2.html')

def boys(request):
    return render(request,'boys.html')
def girls(request):
    return render(request,'girls.html')
def kids(request):
    return render(request,'kids.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['txt_fname']
        last_name = request.POST['txt_lname']
        username = request.POST['txt_uname']
        email = request.POST['txt_email']
        password1 = request.POST['txt_password']
        password2 = request.POST['txt_conpassword']
        if password1== password2:
            if User.objects.filter(username=username).exists():
                print('hai')
                messages.info(request,'mail not')
                return render(request,'register.html')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                print("user created")


                member = User(email=request.POST['txt_email'],)
                subject = 'WELCOME TO JADE SHOPPING'
                message ='hai'
                print(member.email)
                recepient = str(member.email)
                print(member.email)
                send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
               
                
                return render(request, 'Login.html')
        else:
            messages.info(request,'password not')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['txt_uname']
        password = request.POST['txt_password']
        user= auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
        else:
            messages.info(request,'email taken')
            return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')

def logout(request):
    auth.logout(request)
    return render (request, 'register.html')

def savecat1(request):
    if request.method == "POST":
        cat1_name = request.POST.get("txt_c1name")
       
        try:
            member = cat1(cat1_name=cat1_name)
            member.save()
            return redirect('categ')
            
        except:
            print('haiaa')
            return redirect('/')
    else:
        return redirect('home')
def cat2(request):
    datas=cat1.objects.all()
    return render(request,'admin/addcategorytwo.html',{'datascat':datas})
def vcat1(request):
    datas=cat1.objects.all()
    return render(request,'admin/viewcat1.html',{'datascat':datas})
def vitem(request):
    datas=item.objects.all()
    return render(request,'admin/viewitem.html',{'datasitem':datas})


def savecat2(request):
    data=cate2(cat2_name=request.POST['txt_c2name'],cat1_id_id=request.POST['sel'])
    data.save()    
    return redirect('cat2')

def deletecat1(request,cat1_id):
    vars1=cat1.objects.get(cat1_id=cat1_id)
    vars1.delete()
    return redirect('/app/vcat1')
def editcat1(request,cat1_id):
    vars=cat1.objects.get(cat1_id=cat1_id)
    return render(request,'admin/cat1edit.html',{'var':vars})

def updatecat1(request,cat1_id):
    vars=cat1.objects.get(cat1_id=cat1_id)
    vars.cat1_name=request.POST.get('txt_c1name')    
    vars.save()
    return redirect('/app/vcat1')



def saveitem(request):
    data=item(i_categ=request.POST['txt_icat'],i_name=request.POST['txt_iname'],i_desc=request.POST['txt_idesc'],i_price=request.POST['txt_iprice'],i_offerprice=request.POST['txt_iofferprice'],i_pic=request.POST['txt_ipic'])
    data.save()    
    return redirect('items')

def items(request):
    return render(request,'admin/additem.html')

def deleteitem(request,i_id):
    vars1=item.objects.get(i_id=i_id)
    vars1.delete()
    return redirect('/app/vitem')
def edititem(request,i_id):
    vars=item.objects.get(i_id=i_id)
    return render(request,'admin/cat1edit.html',{'var':vars})

def updateitem(request,i_id):
    vars=item.objects.get(i_id=i_id)
    vars.cat1_name=request.POST.get('txt_c1name')    
    vars.save()
    return redirect('/app/vitem')
