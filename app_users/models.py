from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#If we want our Application to be organised better , we can use one function that will take the images and 
# save it to a particular folder with a particular name 
import os

# We will use this line of code to orgainze our images in a better way
# so to organize our data or images properly we are using this function to organize our images in a better way
def path_and_rename(instance,filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username,ext)
    return os.path.join(upload_to,filename)

class UserProfileInfo(models.Model):
    # This user will have all the functionality that the default Custom User Model has and you can also add some extra information 
    # Based on the user to user.
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    # If don't want to give any bio then blank =True
    bio = models.CharField(max_length=150,blank=True)

    # This image file will uploaded to a media file using this upload to
    # Now it will automatically search for Media Folder and If the folder is not inside it it will create one folder and save the files inside it.
    profile_pic = models.ImageField(upload_to=path_and_rename,verbose_name="Profile Picture",blank=True)

    # Giving the user option of choosing what type of user they are either teacher , parents or students
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'


    # Creating a list of options
    user_types = [
        (teacher , 'teacher'),
        (student ,'student'),
        (parent , 'parent'),
    ]

    # & creating a list of choices so that user can choose between the option available
    user_type = models.CharField(max_length=10 , choices = user_types , default=student)


    def __str__(self):
        return self.user.username
    
    