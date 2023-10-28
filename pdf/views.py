from django.shortcuts import render,redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
def Profile_view(request):
    if request.method=='POST':
        name=request.POST.get("name","")
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        summary=request.POST.get('summary','')
        degree=request.POST.get('degree','')
        school=request.POST.get('school','')
        university=request.POST.get('university','')
        previous_work=request.POST.get('previous_work','')
        skills=request.POST.get('skills','')
        linkedin_url=request.POST.get('linkedin_url','')
        portfolio_url=request.POST.get('portfolio_url','')
        github_url=request.POST.get('github_url','')
        projects=request.POST.get('projects','')
        hobbies=request.POST.get('hobbies','')
        certications=request.POST.get('certications','')
        obj=Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,previous_work=previous_work,skills=skills,university=university,certications=certications,hobbies=hobbies,projects=projects,linkedin_url=linkedin_url,github_url=github_url,portfolio_url=portfolio_url)
        obj.save()
        return redirect(f'/resume/{obj.id}')
    return render(request,'pdf/accept.html')


def resume(request,id):
    profile=Profile.objects.get(id=id)
    # return render(request,'pdf/resume.html',{'user_profile':profile})
    template=loader.get_template('pdf/resume.html')
    html=template.render({'profile':profile})
    options={
        'page-size':'Letter',
        'encoding':"ÜTF-8",
    }
    pdf=pdfkit.from_string(html,False,options)
    resp=HttpResponse(pdf,content_type='application/pdf')
    resp['Content-Disposition']='attachment'
    filename='resume.pdf'
    return resp