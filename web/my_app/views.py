from django.shortcuts import render,redirect
# from django.http import HttpResponse
# Create your views here.
# from .form import calculator #userform

def index(request):
    context={
        'title':'home'
    }
    return render(request,"index.html",context)

def home(request):
    '''c=''
    if request.method=='POST':
        val1=int(request.POST.get('v1'))
        val2=int(request.POST.get('v2'))
        OPR=request.POST.get('opr')
        if OPR=="+":
            c=val1+val2 
        elif OPR=="-":
            c=val1-val2
        elif OPR=="*":
            c=val1*val2
        elif OPR=="/":
            c=val1/val2
    context={
        'title':'home page',
        'c':c,
    }'''
    c=''
    if request.method=="POST":
        n1=int(request.POST.get('info'))
        if n1%2==0:
            c='It\'s even'
        else:
            c='It\'s odd'
    return render(request,"home.html",{'c':c})

def regis(request):
    a= request.method=="POST"
    data={}
    if a:
        data={
            'fname':request.POST.get("first"),
            'mname':request.POST.get("mid"),
            'lname':request.POST.get("last"),
            'date':request.POST.get("date"),
            'roll_no':request.POST.get("roll"),
            'phone_no':request.POST.get("phone"),
            'college_email':request.POST.get("College_email"),
            'personal_email':request.POST.get("Personal_email"),
            'pass':request.POST.get("password"),
            'cpass':request.POST.get("cpassword"),
            'value':a
        }
        url=(f"/?value:{a}")
        return redirect(url)
    
    return render(request,'reg.html',data)
    
# def about(request):
#     return HttpResponse("hi this is about us page") 
# def aboutus(request,aboutusid):
#     return HttpResponse(aboutusid)
    