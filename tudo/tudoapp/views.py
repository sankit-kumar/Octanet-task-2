from django.shortcuts import render,HttpResponseRedirect
from .form import regi
from .models import tudoapp


def tudos(request):
    if request.method=='POST':
        data=regi(request.POST)
        if data.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            mob=request.POST.get('mob')
            all=tudoapp(name=name,email=email,mob=mob,password=password)
            all.save()
            return HttpResponseRedirect('/project/show/')
    else:
        data=regi()
    return render(request,"tudo.html",{'form':data})


def show(request):
    data=tudoapp.objects.all()
    return render(request,"show.html",{'all':data})

def delete(request,pk):
    data=tudoapp.objects.get(id=pk)
    data.delete()
    return HttpResponseRedirect('/project/show/')

def update(request,pk):
     if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        mob=request.POST.get('mob')
        all=tudoapp(id=pk,name=name,email=email,mob=mob,password=password)
        all.save()
        return HttpResponseRedirect('/project/show/')
     else:
        all=tudoapp.objects.get(id=pk)
        return render(request,"update.html",{'data':all})



# Create your views here.
