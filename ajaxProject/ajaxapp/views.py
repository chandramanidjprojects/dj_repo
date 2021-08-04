from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .forms import StudentForm
from django.db.models import Q,Sum,Avg,Min,Max,Count
#from django.views.decorators.csrf import csrf_exempt

def like_request(request):
   stuid=request.GET.get('sid')
   stu=Student.objects.get(pk=stuid)
   stu.marks=stu.marks+1
   up=Student(id=stu.id,name=stu.name,marks=stu.marks)
   up.save()
   return JsonResponse({'status':'success','likes':stu.marks})
def home_page(request):
  stu=Student.objects.all()
  form=StudentForm()
  return render(request,'ajaxapp/base.html',{'stu':stu,'form':form})

def ajax_request(request):
  if request.method=='POST':
     form=StudentForm(request.POST) 
     if form.is_valid():
        nm=form.cleaned_data['name']
        mk=form.cleaned_data['marks']
        sid=request.POST.get('s')
        if sid=='':
          stu=Student(name=nm,marks=mk)
        else:
          stu=Student(id=sid,name=nm,marks=mk)  
        stu.save()
        std=Student.objects.values()
        return JsonResponse({'status':'success','std_data':list(std)}) 
     else:
        return JsonResponse({'status':'failed'}) 
def delete_request(request):
  if request.method=='POST':
    print(request.POST.get('sid'))
    data=Student.objects.get(pk=request.POST.get('sid'))
    data.delete()
    stu_data=Student.objects.values()
    return JsonResponse({'status':1,'stu_data':list(stu_data)})    
def edit_request(request):   
  if request.method=='POST':
    stu=Student.objects.get(pk=request.POST.get('sid'))
    dict={'id':stu.id,'name':stu.name,'marks':stu.marks}
    return JsonResponse ({'status':'ok','dict':dict})
   
   
   
   
