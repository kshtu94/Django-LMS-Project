"""
URL configuration for teaching_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_users/',include("app_users.urls")),
]


# Now we need to set the Media file in the url patterns
# Make sure that you use this in the testing phase not in the production

# Its always recommended you created a folder of the media files in a seperate url or seperate server

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL , 
                         document_root=settings.MEDIA_ROOT)
