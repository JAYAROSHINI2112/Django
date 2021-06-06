from contactform.forms import contactformemail
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import render

# Create your views here.
def contactsendmail(request):
    if request.method=="GET":
        form=contactformemail()
    else:
        form=contactformemail(request.POST)
        if form.is_valid():
             fromemail=form.cleaned_data['fromemail']
             subject=form.cleaned_data['subject']
             message=form.cleaned_data['message'] 
             send_mail(subject,message,fromemail,['roshinicandy2112@gmail.com',fromemail])

    return render(request,'contact.html',{'form':form})