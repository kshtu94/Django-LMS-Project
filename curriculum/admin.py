from django.contrib import admin
from models import Standard , Subject , Lesson

# Register your models here.
# Now we need to register all this in our Admin.py 

admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Lesson)