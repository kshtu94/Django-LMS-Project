from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from app_users.forms import UserForm , UserProfileInfoForm
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
# Instead of just giving a small message we want it to show a template
def index(request):
    return render(request,'home.html')



def register(request):

    # We will use the boolean value which is reqgistered which will tell us if the user is registered on the website or not
    registered = False

    if request.method =="POST":
        print("Yes")
        user_form = UserForm(data=request.POST)
        profile_form  = UserProfileInfoForm(data=request.POST)

        # Use these lines of code to check the validation
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            # In the profile form we had to link it to the user , so we will take the above user and link it
            # to the profile we are getting here.
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Once everthing above is done we will make registered  =True  , whcih means that our user is now registered with us
            registered = True

            # Now if forms not valid we will print the error we get with the forms
        else:
            print(user_form.errors , profile_form.errors)

        # So the above whole if else statement is if the user is writing anything inside the forms
        # And if the user is not writing anything inside the form or leaving it blank and then submitting it
        # The below else condition takes care of that

    else :
        user_form = UserForm()
        profile_form = UserProfileInfoForm()




    # As this overall is function it should return something 
    # Now we return the forms we have created 
    return render(request , 'app_users/registration.html' ,          
        {'registered':registered,
        'user_form' : user_form,
        'profile_form' : profile_form})



# Now the User is registered on the website , now we need to create a login function for the user to login
# On th webpage we will be asking user the user name and the password and we will use that to authenticate our user
def user_login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Now we have usename and password so, we need to authenticate the user and login if the user is authenticated 
        # SO we will use some inbuilt libraries (authenticate , login and logout  form django.contrib.auth)
        user = authenticate(username=username , password=password)

        # If user authenticated we'll login the user otherwise raise error
        # If user is authencticated it will be true so we used if user
        if user:
            # If user is active or not
            # & if user is active and is on the website login the user with the authenticate and the request 
            if user.is_active:
                login(request, user)
                # Now we want to sent to the user to the required page we want to show 
                # So we'll use this reverse function and we will redirect this user to the index
                # Index is basically namephrase for our home page
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is Deactivated")
            
        # If the username and password is incorrect or wrong 
        else:
            return HttpResponse("Please use correct id and password")
        
        # SO all the above things were if user is logging IN

        # Otherwise if the user is directly visitinbg something , we'll give the user template for logging
    else:
        return render(request , 'app_users/login.html')
    

# Now lets make a function for logout
# We are using decorator login required that is given by django to check if the user is logged in or not
@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    # if not request.user.is_authenticated:
    #     return redirect(f"{settings.LOGIN_URL}")
        
        # return HttpResponseRedirect(reverse('index'))
        # logout(request)

    
    

    
    # else:
    #     logout(request)
        


# We can use  the logout function to logout the user , similar to login if the user is logged out succesfully 
# We'll redirect him on the home page

# We know currently logout is always available , but we want it to be seen only when user is logged in.