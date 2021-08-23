from django.shortcuts import render
from django import forms
from PIL import Image
from .forms import RegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Registration
from django.contrib.auth.decorators import login_required



# Create your views here.
class deleteform(forms.Form):
    first= forms.CharField(max_length= 64, label="First Name")
    last= forms.CharField(max_length= 64, label= "last name")
    mobile= forms.CharField(max_length=12, min_length= 10)

class modifyform(forms.Form):
    prevfirst=forms.CharField(max_length=60)
    prevlast= forms.CharField(max_length=60)
    prevmobile=forms.CharField(max_length=12)
    firstname=forms.CharField(max_length=60)
    middlename= forms.CharField(max_length=60, required= False)
    lastname= forms.CharField(max_length=60)
    mobilenum= forms.CharField(max_length=12)
    studentphoto= forms.ImageField(required=False)
    studentaadhar_photo= forms.ImageField(required= False)
    emailid= forms.EmailField(max_length=200)

def index(request):
    return render(request, "home/index.html")

@login_required
def registration(request):
    if request.method == 'POST':  # data sent by user
        form = RegistrationForm(request.POST, request.FILES)
        try:
            form.ipAddress=request.META['HTTP_X_FORWARDED_FOR']
        except:
            form.ipAddress= request.META['REMOTE_ADDR']

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:  # display empty form
        form = RegistrationForm()

    return render(request, 'home/registration.html', {'reg_form': form})

@login_required
def update(request):
    if request.method=="GET":
        #form= (request.GET)
        #if form.is_valid():

                firstname= request.GET.get("first_name")
                lastname= request.GET.get("last_name")
                mobile= request.GET.get("mobile_num")
                #candidate= Registration.objects.get(first_name= firstname, last_name= lastname, mobile_num= mobile)

                try:
                    candidate= Registration.objects.get(first_name= firstname, last_name= lastname, mobile_num= mobile)

                    return render(request, 'home/update.html',
                    {
                    "candidate": candidate, "form": modifyform()
                    })
                except:

                    return render(request, 'home/search.html', {
                    "message": "****You will be get back to this page again if your record doesn't exist****"
                    })

        #else:
        #    return render(request, "home/index.html",{
        #    "message": "Not Found!!! Create a New registration by clicking on the Registration button"
        #    })
    if request.method=="POST":

        uform= modifyform(request.POST, request.FILES)
        if uform.is_valid():
            prev_first=uform.cleaned_data["prevfirst"]
            prev_last=uform.cleaned_data["prevlast"]
            prev_mobile= uform.cleaned_data["prevmobile"]
            form= Registration.objects.get(first_name= prev_first,  last_name= prev_last , mobile_num= prev_mobile)
            #uform= modifyform(request.POST)
            form.first_name= uform.cleaned_data["firstname"]
            form.middle_name= uform.cleaned_data["middlename"]
            form.last_name= uform.cleaned_data["lastname"]
            form.mobile_num= uform.cleaned_data["mobilenum"]
            form.student_photo= uform.cleaned_data["studentphoto"]
            form.student_aadhar_photo= uform.cleaned_data["studentaadhar_photo"]
            form.email= uform.cleaned_data["emailid"]
            form.save()
            return render(request, 'home/search.html', {
            "msg1":"UPDATED SUCCESSFULLY!!"
            })


    return render(request, 'home/search.html')

@login_required
def delete(request):
    if request.method=="POST":
        form= deleteform(request.POST)
        if form.is_valid():

                firstname= form.cleaned_data["first"]
                lastname= form.cleaned_data["last"]
                mobile= form.cleaned_data["mobile"]
                #candidate= Registration.objects.get(first_name= firstname, last_name= lastname, mobile_num= mobile)

                try:
                    candidate= Registration.objects.get(first_name= firstname, last_name= lastname, mobile_num= mobile)
                    candidate.delete()
                    return render(request, 'home/delete.html', {
                    "msg": "DELETED SUCCESSFULLY!!", "form": deleteform()
                    })

                except:
                    return render(request, 'home/delete.html', {
                    "message": "** NO SUCH RECORD EXISTS!! PLEASE TRY AGAIN", "form": form
                    })

    return render(request, 'home/delete.html', {
    "form": deleteform()
    })
