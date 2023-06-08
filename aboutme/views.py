from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse,FileResponse
from .forms import AboutForm,VideoForm
from .models import About,Videos
from django.core.mail import send_mail
from django.contrib import messages
from .pdf import html2pdf



# Create your views here.
def pdf(request):
    return render(request,'pdf.html')



def home(request):
    return render(request,'home.html')


def about(request):
    result = About.objects.get(id=1)
        
    return render(request,'about.html',{'result':result})



def editabout(request,pk):
    data = About.objects.get(id=pk)
    if request.method=="POST":       
        result = AboutForm(request.POST,instance =data)
        if result.is_valid():            
            result.save()
            return redirect('/about')

    else:       
        result = AboutForm(instance=data)    
    return render(request,'editabout.html',{'form':result})


# this is to contact me message from one account to another 
def contact(request):
    if request.method=="POST":
            form_data = request.POST
            name = form_data['Name']
            from_email = form_data['Email']        
            subject = form_data['Subject']
            message =form_data ['Message']
            if not name:
                messages.error(request,'please fill completely  ')
                return redirect('contact')
            if not from_email:
                messages.error(request,'please fill completely  ')

                return redirect('contact')
            if not subject:
                messages.error(request,'please fill completely  ')

                return redirect('contact')
            if not message:
                messages.error(request,'please fill completely  ')

                return redirect('contact')
            data = f'name= {name},  email={from_email} ,and message={message} '
            send_mail( subject, data, 'testingchitwan@gmail.com', ['rajanbhandari939@gmail.com'],fail_silently=False)
            messages.info(request,'message send sucessfull ')
            return redirect('contact')
    else:
       
        return render(request,'contact.html')



def project_video(request):
    data = Videos.objects.all()
    return render(request,'video.html',{'data':data})

def submit_video(request):    
    if request.method=="POST":        
        data = VideoForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return redirect('/video')
    else:
        data = VideoForm()
    return render(request,'submitvideo.html',{'form':data})


def edit_video(request,pk):
    data = Videos.objects.get(id=pk)
    if request.method=="POST":
        result = VideoForm(request.POST,request.FILES,instance=data)
        if result.is_valid():
            print('hello')
            result.save()
            return redirect('video')
    else:
        result = VideoForm(instance=data)
    return render(request,'submitvideo.html',{'form':result})


def delete_video(request,pk):
    data = Videos.objects.get(id=pk)
    data.delete()
    return redirect('video')


def cv(request):
    return render(request,'cv.html')


def pagenotfound(request,exception):
    return render(request,'notfound.html')


# def siteundercons(request):
#     return render(request,'siteundercons.html')


from .pdf import html2pdf  
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def generatepdf(request):
    pdf = html2pdf('pdf.html')
    return HttpResponse(pdf,content_type='application/pdf')


