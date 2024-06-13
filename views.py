
from django.shortcuts import render,redirect,HttpResponse
# from .models import*
from django.contrib.auth.models import User
from .forms import ProductForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout

# from loginpro import settings
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_text
# from . tokens import generate_token
# from django.core.mail import EmailMessage, send_mail

# Create your views here.

# def index(request):
#     return render(request,"index.html")

def index(request):
    uid = Product.objects.all()
    context = {
        'uid': uid,

    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def cart(request):
    return render(request,'cart.html')


def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

# def shop(request):
#     return render(request,'shop.html')

def thankyou(request):
    return render(request,'thankyou.html')

def register(request, messages=messages) :

    if request.POST:
        # username=request.POST.get('usernsem')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! please try some other username")
            return redirect('register')

        if User.objects.filter(email=email):
            messages.error(request,"Email already registered!")
            return redirect('register')

        if len(username)>10 :
            messages.error(request,"Username must be under 10 character")

        if password != cpassword :
            messages.error(request,"Password didn't match!")

        if not username.isalnum():
            messages.error(request,"Username must be Alpha-Numeric!")
            return redirect('register')



        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.save()

        # messages.success(request,"Your account has been successfully created.")


        # Welcome Email
        #
        # subject = "Welcome to AAV - Django Login!!"
        # messages = "Hello " + myuser.first_name + "!! \n" + "Welcom to AAV!! \n Thank you for visiting our website\n We have also sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thanking You \n Akshar Vaghasiya"
        # from_email= settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, messages, from_email, to_list, fail_silently=True)
        #
        # # Email address Configration Email
        # current_site = get_current_site(request)
        # email_subject = 'Confirm your email @ AAV - Django Login!!'
        # message2 = render_to_string('email_confirmation.html', {
        #     'name' : myuser.first_name,
        #     'domain' : current_site.domain,
        #     'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token' : generate_token.make_token(myuser),
        # })
        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()

        return redirect('/logIn/')

    return render(request,"register.html")
def logIn(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None :

            login(request, user)
            return redirect('/index/')
            # fname=user.first_name
            # print(fname)
            # return render(request, "index.html", {'fname':fname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('/logIn/')

    return render(request, "login.html")

def logOut(request):
    logout(request)
    # messages.success(request,"Logged Out Successfully")
    return redirect("/index/")

# def activate(request, uidb64, token):
#     try :
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pk=uid)
#
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist) :
#         myuser = None
#
#     if myuser is not None and generate_token.check_token(myuser, token):
#         myuser.is_active = True
#         myuser.save()
#         login(request,myuser)
#         return redirect('index')
#     else:
#         return render(request,"activation_failed.html")


def addproduct(request):
    if request.POST:
        name = request.POST['name']
        price = request.POST['price']
        pic = request.FILES['pic']
        c_name = request.POST['name']

        uid = Product.objects.create(
            name=name,
            price=price,
            pic=pic,
        )
        return redirect('product_list')

    else :
        catid = Category.objects.all()
        con={
            'cat': catid
        }
        return render(request, 'addproduct.html',con)

def product_list(request):
    uid = Product.objects.all()
    cat = Category.objects.all()
    context = {
        'uid': uid,
        'cat': cat,
    }
    return render(request, "product_list.html", context)

def update(request):
    pass


def add_cart(request,id):
    uid = Product.objects.get(id=id)
    if Add_Cart.objects.filter(p_id=uid):
        product_id = Add_Cart.objects.get(p_id=uid)
        product_id.quantity += 1
        product_id.total_price = product_id.price * product_id.quantity
        product_id.save()

    else :
        Add_Cart.objects.create(
            p_id=uid,
            name=uid.name,
            price=uid.price,
            pic=uid.pic,
            quantity=uid.quantity,
            total_price = uid.price * uid.quantity,
        )

    return redirect('cart')

def cart(request) :
    pass
    cid = Add_Cart.objects.all()

    p_quantites = {}

    for i in cid:
        product_id = i.p_id
        if product_id in p_quantites:
            p_quantites[product_id] += i.quantity
        else:
            p_quantites[product_id] = i.quantity
    subtotal = sum(item.price * item.quantity for item in cid)
    total_total = subtotal
    if request.POST:
        code = request.POST['coupon_code']
        cou = coupon.objects.get(code=code)
        discount=cou.discount
        # dp= (total_total*discount) / 100
        total_total=total_total-((total_total*discount)/100)

    context = {
        'cid': cid,
        'p_quantites': p_quantites,
        'subtotal': subtotal,
        'total_total': total_total,
        'disc' : total_total,
        # 'dp' : dp,
    }
    return render(request, 'cart.html', context)

def deleteproduct(request,id):
    dpid = Add_Cart.objects.get(id=id)
    dpid.delete()
    return redirect('cart')

def change_qty(request,id):
    cid = Add_Cart.objects.get(id=id)
    print(cid)
    quantity = request.POST['quantity']
    print(quantity)
    if cid.quantity == 0:
        cid.delete()
        return redirect('cart')
    else:
        cid.quantity = quantity
        cid.total_price = cid.price * int(quantity)
        cid.save()
        return redirect('cart')

def read_cat(request,id):
    cats=Category.objects.get(id=id)
    image=Product.objects.filter(cat=cats)
    cate = Category.objects.all()
    uid = Product.objects.all()
    cat = Category.objects.all()

    return render(request, 'cat_product.html', { 'cats' : cats, 'image' : image, 'cate': cate,'uid': uid, 'cat': cat,})

def checkout(request, dp=None):
    cid = Add_Cart.objects.all()

    p_quantites = {}

    for i in cid:
        product_id = i.p_id
        if product_id in p_quantites:
            p_quantites[product_id] += i.quantity
        else:
            p_quantites[product_id] = i.quantity
    subtotal = sum(item.price * item.quantity for item in cid)
    total_total = subtotal
    if request.POST:
        code = request.POST['coupon_code']
        cou = coupon.objects.get(code=code)
        discount = cou.discount
        dp = discount
        total_total = total_total - ((total_total * discount) / 100)

    context = {
        'cid': cid,
        'p_quantites': p_quantites,
        'subtotal': subtotal,
        'total_total': total_total,
        'disc': total_total,
        'dp' : dp,
    }
    return render(request,'checkout.html',context)

def bill(request):
    if request.POST:
        c_countryname = request.POST['c_countryname']
        c_fname = request.POST['c_fname']
        c_lname = request.POST['c_lname']
        c_companyname = request.POST['c_companyname']
        c_address = request.POST['c_address']
        c_full_address = request.POST['c_full_address']
        c_state_country = request.POST['c_state_country']
        c_email = request.POST['c_email']
        c_phone = request.POST['c_phone']

        uid = Billing.objects.create(
            c_countryname=c_countryname,
            c_fname=c_fname,
            c_lname=c_lname,
            c_companyname=c_companyname,
            c_address=c_address,
            c_full_address=c_full_address,
            c_state_country=c_state_country,
            c_email=c_email,
            c_phone=c_phone,
        )
        return redirect('billing')
    else:
        return render(request,"checkout.html")

def billing(request):
    uid = Billing.objects,all()
    did = Add_Cart.objects.all()
    did.objects.delete()
    context = {
        'uid':uid
    }
    return render(request,"thankyou.html",context)
