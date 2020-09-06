from django.shortcuts import render
from django.http import HttpResponse
from shop.models import products,Contact
from math import ceil
from django.contrib import messages
# Create your views here.
def index(request):

    # pd=products.objects.all()
   
    # n=len(pd)
    # nslides=n//4+ceil((n/4)-(n//4))
    # params={'product':pd,'no_ofslides':(1,nslides),'range':range(nslides)}
    # allproducts=[[pd,range(1,nslides),nslides],[pd,range(1,nslides),nslides]]
    allproduct=[]
    cats=products.objects.values('category','id')
    cat={item['category']for item in cats}
    # here values is stored in the form of set{'clothing','electronics'}
    for cats in cat:
        prod=products.objects.filter(category=cats)
        # print(prod.values('id'))
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        allproduct.append([prod,range(1,nslides),nslides])
     
    params={'product':allproduct}
    
    return render(request,'shop/index.html',params)

        
    # print(allproducts[0][0])
    # params={'product':allproducts}
   
    
    # return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if request.method=='GET':
      return render(request,'shop/contact.html')
    else:
      username=request.POST.get('Username')
      email=request.POST.get('Email')

      description=request.POST.get('Desc')
      phone=request.POST.get('Phone')
      checked=request.POST.get('Check',default="off")

      if checked=='on':
           contact=Contact(Username=username,Email=email,Desc=description,Phone=phone)
           contact.save()

      else:
         messages.info(request,'Please fill all the forms field')
         return render(request,'shop/contact')
def tracker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return render(request,'shop/search.html')
def productview(request,mid):
    # fetch the product using the id
    product=products.objects.filter(id=mid)
    
    print(product)
    # params={'pructdetail':product}
    # print(pructdetail[0])
   
    return render(request,'shop/productview.html',{'prod':product[0]})
def checkout(request):
    return render(request,'shop/checkout.html')