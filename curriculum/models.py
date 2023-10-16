from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import os

# So we have used relations with Users in our Lessons model which is created_by
# So we need to import User
# as we are using Inbuilt user Model we will use Auth.Models to import User

# Create your models here.

# First we need to create standard of class Model 
# Slug will be name of our chapter with which we can go into the url path
# The url path with dash - or flash % for eg i%am%cool is called slug
# Or we can say a slug is the string that can only include character , numbers , dashes and underscores.
# It is part of a url that identifies a particular page on a website , in human-
# friendly form.


# We will be using the same method that will use the slugify function to convert the name of standard into slug 
class Standard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True , blank=True)
    description = models.TextField(max_length=500 , blank=True)

    def __str__(self):
        return self.name
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        # Slug will basically the name of the Chapter in which we can go to the Url Path
        super().save(*args , **kwargs)


# Now lets create our method as well to upload our image to a particular assigned folder for this subject model
# As we have already created our media folder and we want it to be saved under Images folder under Subject_Pictures , with
# a filename
def save_subject_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.subject_id:
        filename = 'Subject_Pictures/{}.{}'.format(instance.subject_id,ext)
    return os.path.join(upload_to,filename)

# We will use standard here . bcoz we want to use one to many relation with standard
# Our standard may have multiple subjects 
# But this particular subject may belong to one subject only
# So we use Foreign Key here
# We are also giving related_name = Subjects , which means this subject is related to standard with the name subjects


class Subject(models.Model):
    subject_id = models.CharField(max_length=100 , unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True , blank=True)
    standard = models.ForeignKey(Standard , on_delete=models.CASCADE , related_name='subjects')
    image = models.ImageField(upload_to=save_subject_image , blank=True , verbose_name='Subject Image')
    descritpion = models.TextField(max_length=500 , blank=True)

    # We are also using Standard bcoz we want o have one to many relation with the standard as in a standard may have different
    # subjects , but this particular subjeftc should belong to one satndard only
    # so we are using the foreign key and on delete models.cascade , and related name = subjects
    # which means this subjects is related to standard with a name subjects.

    """
    We need to define a method which will save our save our Image to a new folder 
    Where we will upload it to media director under Images Folder Inside specific folder subject Pirctures
    and then we require name of the file
    
    """

    def __str__(self):
        return self.name
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.subject_id)
        super().save(*args , **kwargs)


"""
Now to save our Videos , PPT's & Notes inside Our Folder Save_Lesson_Files , we use this Method or Function over here
"""

def save_lesson_files(instance  , filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.lesson_id:
        filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id, instance.lesson_id, ext)
        if os.path.exists(filename):
            # we will check if the file is already exists , if it exists then we will provide the Integer 1 and we will upload
            new_name = str(instance.lesson_id) + str('1')
            filename = 'lesson_images/{}/{}.{}'.format(instance.lesson_id,new_name ,ext)
    return os.path.join(upload_to ,filename)


# Now lets create lesson Model that will be connected to subject and standard or class 

class Lesson(models.Model):
    lesson_id = models.CharField(max_length=100 , unique=True)
    Standard = models.ForeignKey(Standard , on_delete=models.CASCADE)
    created_by = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE , related_name='lessons')
    # Here Subject has many lessons and one lesson is connected to One Subject
    name = models.CharField(max_length=250)
    position = models.PositiveSmallIntegerField(verbose_name='Chapter no.')
    slug  = models.SlugField(null=True , blank=True)
    video = models.FileField(upload_to=save_lesson_files , verbose_name='Video' , blank=True , null=True)
    ppt = models.FileField(upload_to=save_lesson_files , verbose_name="Presentations" , blank=True)
    Notes = models.FileField(upload_to=save_lesson_files , verbose_name="Notes" , blank=True)
    """
    We should have Videos for our Lesson or e, we should have ppts , we should have Note's as well for our lesson
    """
    """
    We will also define a function to store all these things inside the Folder using upload_to = save_lesson_files
    """

    class Meta:
        ordering = ['position']
        # Positiion is basically chapter no , from where it stands in all the chapter
        """
        WE are using class Meta for the Ordering , so i wan to order Lessons using the Position , which means Chapter
        So we want Chapter 4 on Top and Chapter 7 & 8 at the Bottom.
        """

    """
    A String method which will return the Name and save method  which will slugify the name 
    """
    def __str__(self):
        return self.name
    
    def save(self, *args , **kwargs):
        self.slug = slugify(self.name)
        super().save(*args , **kwargs)

#  Lets Create a Subject Model and Subject Class

# if We have google.com/i%am%cool , so we sometimes use Percentile % , Dash - or Underscore _ Symbol is known as Slug
# We  are going to use the same method which will use the Slugify function to convert name of standard into slug.