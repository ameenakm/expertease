from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse

from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    return render(request,'signup.html')
def clientsignup(request):
    return render(request,'clientsignup.html')
def freelancersignup(request):
    categories = category.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        place = request.POST['place']
        cat_name = request.POST['category']
        subcat_name = request.POST.get('subcategory', '')  
        ys = request.POST['ys']
        bi = request.POST['bi']
        ima = request.FILES['ima']
        wi = request.POST['wi']
        wimg = request.FILES['wimg']
        cn = request.POST['cn']

       
        cat_obj = category.objects.filter(categoryname=cat_name).first()
        subcat_obj = subcategory.objects.filter(subcategorynm=subcat_name, categorynm=cat_obj).first()

 
        data = freelancers(
            name=name,
            email=email,
            password=password,
            place=place,
            categoryname=cat_obj,
            subcategoryname=subcat_obj,
            specilization=ys,
            bi=bi,
            image=ima,
            wi=wi,
            wimage=wimg,
            cn=cn
        )
        data.save()
        return HttpResponse("Successfully registered!")

    return render(request, 'freelancersignup.html', {'data': categories})
def addcategory(request):
    if request.method=='POST':
        cname=request.POST['name']
        data=category(categoryname=cname)
        data.save()
        return HttpResponse("suucessfully added")
    return render(request,'addcategory.html')
def userindex(request):
    categories = category.objects.all()
    subcategories = subcategory.objects.all()  

    
    category_map = {}
    for cat in categories:
        category_map[cat] = subcategories.filter(categorynm=cat)
    return render(request, 'userindex.html', {'category_map': category_map})
def categorylist(request):
    data=category.objects.all()
    return render(request,'categorylist.html',{'data':data})
def addsubcategory(request,id):
    data=category.objects.get(id=id)
    if request.method=='POST':
        catid=request.POST['catid']
        subcat=request.POST['name']
        p=category.objects.get(id=catid)
        data=subcategory(categorynm=p,subcategorynm=subcat)
        data.save()
        return HttpResponse("suucessfully added")
    return render(request,'addsubcategory.html',{'data':data})
def freelancer_profile(request, freelancer_id):
    freelancer = Freelancer.objects.get(id=freelancer_id)
    return render(request, 'freelancer_display.html', {'freelancer': freelancer})
def get_subcategories(request):
    category_name = request.GET.get('category')
    subcategories_list = []
    try:
        cat_obj = category.objects.get(categoryname=category_name)
        subcategories = subcategory.objects.filter(categorynm=cat_obj)
        subcategories_list = [sub.subcategorynm for sub in subcategories]
    except category.DoesNotExist:
        pass
    return JsonResponse(subcategories_list, safe=False)
def freelancerdisplay(request):
    categoryname = request.GET.get('category')
    subcategoryname = request.GET.get('subcategory')
    cat_obj = category.objects.filter(categoryname=categoryname).first()
    subcat_obj = subcategory.objects.filter(subcategorynm=subcategoryname, categorynm=cat_obj).first()
    freelancerss = freelancers.objects.filter(categoryname=cat_obj,subcategoryname=subcat_obj)
    return render(request,'freelancerdisplay.html',{'freelancerss':freelancerss})
def viewfreelancer(request,id):
    data=freelancers.objects.get(id=id)
    return render(request,'viewfreelancres.html',{'freelancer':data})