from django.shortcuts import render,redirect
from myapp.models import Categrory,Product,User,Customer,Cart
from django.views import generic
# Create your views here.

class CustomerRegistration(generic.View):
    def get(self,req):
        return render(req,"register.html")

    def post(self,req):
        cname=req.POST.get("cname")
        city=req.POST.get("city")
        gender=req.POST.get("gender")
        email=req.POST.get("email")
        pwd=req.POST.get("pwd")
        User.objects.create(userid=email,uname=cname,pwd=pwd,role='customer')
        Customer.objects.create(cname=cname,email=email,gender=gender,city=city)
        req.session["msg"]="Customer Registered Successfully"
        return redirect('allcusts')

class CustomerLogin(generic.View):
    def get(self,req):
        if req.session.get("msg") is not None:
            msg=req.session.get("msg")
            req.session.pop("msg")
        return render(req,"login.html",locals())
    
    def post(self,req):
        email=req.POST.get("email")
        pwd=req.POST.get("pwd")
        user=User.objects.filter(userid=email,pwd=pwd).first()
        if user is None:
            req.session["msg"]="Invalid username or password"
            return redirect('login')
        else:
            req.session["userid"]=user.userid
            req.session["uname"]=user.uname
            req.session["role"]=user.role
            return redirect('home')
        

class ProductDetail(generic.View):
    def get(self,req,id):
        p=Product.objects.get(id=id)
        return render(req,"pdetail.html",locals())
    
    def post(self,req,id):
        pid=req.POST.get("pid")
        qty=req.POST.get("qty")
        userid=req.session.get("userid")
        product=Product.objects.get(id=pid)
        customer=Customer.objects.get(email=userid)
        Cart.objects.create(product=product,customer=customer,qty=qty)
        req.session["msg"]="Product Added to Cart"
        return redirect('home')

    
class MyCart(generic.View):
    def get(self,req):
        userid=req.session.get("userid")
        customer=Customer.objects.get(email=userid)
        cart=Cart.objects.filter(customer=customer)
        return render(req,"cartpage.html",locals())
        

class AllCustomers(generic.View):
    def get(self,req):
        all=Customer.objects.all()
        if req.session.get("msg") is not None:
            msg=req.session.get("msg")
            req.session.pop("msg")
        return render(req,"allcustomer.html",locals())


class Logout(generic.View):
    def get(self,req):
        req.session.flush() # delete all session variables
        return redirect('home')


class HomePage(generic.View):
    def get(self,req):
        cats=Categrory.objects.all()
        prods=Product.objects.all()
        return render(req,"home.html",locals())

class CategoryView(generic.View):
    def get(self,req):
        all=Categrory.objects.all()
        return render(req,"categories.html",locals())

    def post(self,req):
        cname=req.POST.get("cname")
        Categrory.objects.create(cname=cname)
        return redirect('cats')

        
class ProductView(generic.View):
    def get(self,req):
        cats=Categrory.objects.all()
        prods=Product.objects.all()
        return render(req,"products.html",locals())

    def post(self,req):
        pname=req.POST.get("pname")
        catid=req.POST.get("pcat")
        pcat=Categrory.objects.get(id=catid)
        price=req.POST.get("price")
        photo=req.FILES.get("photo")
        Product.objects.create(pname=pname,pcat=pcat,price=price,photo=photo)
        return redirect('products')
    