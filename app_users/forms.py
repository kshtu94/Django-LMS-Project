from django import forms
from django.contrib.auth.models import User
from app_users.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

# Now we going to use feature of django which is very helpful for user creation
# & Django has a user creation form , which will be very useful for user creation

# As we know first we need to create a user instance and then we can use our custom based model to give extra information

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ("username","first_name","last_name","email","password1","password2")

        labels = {
            'password1':"Password",
            "password2": "Confirm Password"
        }


# After this we will use custom based user profile info model that is extended from the User
class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    teacher = "teacher"
    student = "student"
    parent = "parent"
    user_types = [
        (student,"student"),
        (parent,"parent"),

    ]
    user_type = forms.ChoiceField(required=True , choices=user_types)

    # We are giving here choices of Student and Parents bcoz we don't want anyone to be registering on our website as a teacher
    # Only admin can give the privilege of teacher on the website
    class Meta():
        model = UserProfileInfo
        fields = ('bio','profile_pic','user_type')


        