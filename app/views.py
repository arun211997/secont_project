from django.shortcuts import render,redirect
from app.models import Product
from imgcrude.settings import STATIC_URL

# Create your views here.
def home(request):
    return render(request,'homepage.html')
    
def add(request):
    if request.method == 'POST':  # Correct the method comparison to uppercase
        pname = request.POST.get("name")
        price = request.POST.get("price")
        qty = request.POST.get("quantity")
        image = request.FILES.get("file")

        if pname and price and qty:  # Check if all required fields are present
            p = Product(
                productname=pname,
                price=price,
                quantity=qty,
                image=image
            )
            p.save()
            print("Product saved successfully")
            return redirect('show')
        else:
            print("Invalid data provided")
    
    # You may want to add a response for GET requests or form errors
    # ...
    return redirect('show')

def show(request):
    products=Product.objects.all()
    return render(request,'showp.html',{'products':products})

def edit(request,pk):
    pro=Product.objects.get(id=pk)
    return render(request,'edit.html',{'pro':pro})

def editfun(request,pk):
    if request.method=='POST':
        pro=Product.objects.get(id=pk)
        pro.productname=request.POST["name"]
        pro.price=request.POST["price"]
        pro.quantity=request.POST["quantity"]
        pro.image=request.FILES.get("file")
        pro.save()
        return redirect('show')
    return render(request,'edit.html')

def delete(request,pk):
    pro=Product.objects.get(id=pk)
    pro.delete()
    return redirect('show')