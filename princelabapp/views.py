from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Student
from .forms import StudentForm
from .serializers import StudentSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
def addandshow(request):
    form=StudentForm
    stu=Student.objects.all()
    if request.method=="POST":
        name=request.POST.get('name'),
        name=name[0]
        age=request.POST.get('age'),
        age=age[0]
        address=request.POST.get('address'),
        address=address[0]
        grade=request.POST.get('grade'),
        grade=grade[0]
        major=request.POST.get('major'),
        major=major[0]
        stu=Student(name=name,age=age,address=address,grade=grade,major=major)
        stu.save()
        return HttpResponseRedirect("/")
       
    else: 
        context={'form':form,'stu':stu}
        return render(request,'show.html',context) 

def updatedata(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        fm=StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect("show")

    else:
        pi=Student.objects.get(pk=id)
        fm=StudentForm(instance=pi)

    return render(request,'updatestudent.html' ,{'form':fm})    

def delete_data(request,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")

@api_view(['GET', 'POST'])
def studentapi(request):
    if request.method == 'GET':
        prod=Student.objects.all()
        serial=StudentSerializer(prod,many=True)
        return JsonResponse(serial.data,safe=False)        


