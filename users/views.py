from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token, forgot_password_token
# from .forms import RegisterForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect




@login_required
def dashboard(request):
    student = request.user
    return render(request=request, template_name='dashboard.html', context={"student": student})


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('users:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'Form1/Register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             print('okkk')
#             username = form.cleaned_data.get('username1')
#             print(username)
#             password1 = form.cleaned_data.get('password1')
#             password2 = form.cleaned_data.get('password2')
#             user = User.objects.get(username=username)
#             print(user)
#             email_sliced = user.email[0:5]
#             if password1==password2:

#                 user.set_password(password1)
#                 user.is_active = False
#                 user.save()


#                 # current_site = get_current_site(request)
#                 # print(account_activation_token.make_token(user))
#                 # to_email = user.email
#                 #
#                 # print(to_email)
#                 # print("1234567890-")
#                 # mail_subject = 'Aaaa'
#                 # message = render_to_string('pass_reset_email.html', {
#                 #     'user': user,
#                 #     'domain': current_site.domain,
#                 #     'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
#                 #     'token': account_activation_token.make_token(user),
#                 # })
#                 # email = EmailMessage(
#                 #     mail_subject, message, to=[to_email]
#                 # )
#                 # email.send()
#                 # print(message)
#                 print(user.email)

#                 return render(request, 'Form1/account_activation_email.html', context={'user_name':username, "email_sliced":email_sliced})
#             else:
#                 return render(request, 'Form1/Register.html', {'form': form,"error":"Password does not matched","email_sliced":email_sliced})
#         else:
#             return render(request, 'Form1/Register.html', {'form': form, "error": "Form is not valid"})
#     else:
#         form = RegisterForm()

#     return render(request, 'Form1/Register.html', {'form': form})

# def email_authen(request):
#     if request.method == 'POST':
#         username=request.POST.get('username')
#         user = User.objects.get(username=username)
#         get_email=request.POST.get('email')
#         print("before email check")
#         if get_email.lower() == str(user.email).lower():
#             print("after email check")
#             return render(request, 'Form1/account_activation_dob.html', context={'user_name': username})
#         else:
#             return render(request, 'Form1/account_activation_email.html', context={'error': "Email does not matched with the our database",'user_name':username})
#     else:
#         return render(request, 'Form1/account_activation_email.html')

# def pass_reset(request, uidb64, token):
#     User = get_user_model()
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         print("after login")
#         return redirect('users:create_profile')

# def dob_authen(request):
#     print("enter dob_authen")
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         print("enter request.method")
#         # username=request.POST.get('username')
#         print(username)
#         user = User.objects.get(username=username)
#         print(user)
#         First_Name = user.first_name
#         dep_slice=str(user.username)[2:4]
#         get_dob=request.POST.get('dob')
#         if get_dob.lower() == str(user.last_name).lower():
#             user.is_active=True
#             user.save()
#             login(request, user)
#             return render(request, 'Form1/index.html',context={'user_name': username,'First_Name':First_Name,'dep_slice':dep_slice})
#         else:
#             return render(request,'Form1/account_activation_dob.html',context={'error':"Your date of birth does not matched with the our database",'user_name':username})
#     else:
#         return render(request, 'Form1/account_activation_dob.html')


# def create_profile(request):

#     print("before post")
#     dep_slice = str(request.user.username)[2:4]

#     if request.method == "POST":

#         print("after post")
#         form = ProfileForm(request.POST, request.FILES)
#         print("form invalid")
#         First_Name = request.user.first_name
#         username = request.user.username
#         if form.is_valid():
#             print("form valid")
#             user=request.user
#             print(user)
#             print(form)

#             dob = form.cleaned_data.get('dob')
#             contact_no = form.cleaned_data.get('contact_no')
#             image = form.cleaned_data.get('image')
#             room_no = form.cleaned_data.get('room_no')
#             profile=Profile(contact_no=contact_no,dob=dob,image=image,room_no=room_no)
#             profile.username=user


#             print("previous save")
#             profile.save()

#             print("previous redirect")
#             return redirect("users:dashboard")

    #     else:
    #         print(form.errors)
    #         return render(request, 'Form1/index.html', {'form': form,'user_name': username,'First_Name':First_Name,'dep_slice':dep_slice})

    # else:
    #     form = ProfileForm()
    #     return render(request, 'Form1/index.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('users:dashboard')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next'):
                    print('reached')
                    return HttpResponseRedirect(request.GET.get('next'))
                else:
                    print('not')
                    return redirect('users:dashboard')
            else:
                return render(request, 'Form1/login.html', {'errors': 'Your account is not active'})
        else:
            return render(request, 'Form1/login.html', {'errors': 'Invalid login, You do not have an account'})
    else:
        return render(request, 'Form1/login.html')


def logout_user(request):
    logout(request)
    return redirect('website')
