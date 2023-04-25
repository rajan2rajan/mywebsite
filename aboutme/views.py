from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .forms import AboutForm,ContactForm,VideoForm
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
        data = ContactForm(request.POST)
        if data.is_valid():
            name = data.cleaned_data['Name']
            from_email = data.cleaned_data['Email']        
            subject = data.cleaned_data['Subject']
            message = data.cleaned_data['Message']
            data = f'name= {name},  email={from_email} ,and message={message} '
            send_mail( subject, data, 'testingemailmsg@gmail.com', ['rajanbhandari939@gmail.com'])
            messages.info(request,'message send sucessfull ')
    else:
        data = ContactForm()
    return render(request,'contact.html',{'result':data})



def project_video(request):
    data = Videos.objects.all()
    return render(request,'video.html',{'data':data})

def submit_video(request):    
    if request.method=="POST":        
        data = VideoForm(request.POST)
        if data.is_valid():
            print('hellow')
            data.save()
            return redirect('/video')
    else:
        data = VideoForm()
    return render(request,'submitvideo.html',{'form':data})


def edit_video(request,pk):
    data = Videos.objects.get(id=pk)
    if request.method=="POST":
        result = VideoForm(request.POST,instance=data)
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


from .pdf import html2pdf  

def generatepdf(request):
    pdf = html2pdf('pdf.html')
    return HttpResponse(pdf,content_type='application/pdf')








