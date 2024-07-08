from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Contact_Us_Feedback,Contact_Us_Issues,Contact_Us_Quiry

# Create your views here.
def Home(request):
    return render(request,'index.html')
def Signin(request):
    return render(request,'signin.html')
def About(request):
    return render(request,'about_us.html')
def Contact(request):
    selector={}
    if request.method=='POST':
        selector={
            'selected':request.POST.get('contacting_for')
        }
        value=False
        if selector['selected']=='Feedback':
            details=Contact_Us_Feedback.objects.create(
            info_type=request.POST['contacting_for'],
            Fullname_ursername=request.POST['Name_username'],
            Email=request.POST['Email'],
            Issue_quriy=request.POST['issue_quiry_feedback']
            )
            details.save()
        elif selector['selected']=='Quiry':
            details=Contact_Us_Quiry.objects.create(
            info_type=request.POST['contacting_for'],
            Fullname_ursername=request.POST['Name_username'],
            Email=request.POST['Email'],
            Issue_quriy=request.POST['issue_quiry_feedback']
            )
            details.save()
            value=True
        elif selector['selected']=='Issues':
            details=Contact_Us_Issues.objects.create(
            info_type=request.POST['contacting_for'],
            Fullname_ursername=request.POST['Name_username'],
            Email=request.POST['Email'],
            Issue_quriy=request.POST['issue_quiry_feedback']
            )
            details.save()
        return render(request,'contact_us.html',{'submission':True,'selected':request.POST.get('contacting_for'),'selector':value})

    return render(request,'contact_us.html')
    
def Browse(request):
    return render(request,'search.html')