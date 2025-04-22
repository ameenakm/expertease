"""
URL configuration for pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from expertease import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('signup/',views.signup),
    path('clientsignup/',views.clientsignup),
    path('freelancersignup/',views.freelancersignup),
    path('addcategory/',views.addcategory),
    path('userindex/',views.userindex),
    path('categorylist/',views.categorylist),
    path('addsubcategory/<int:id>',views.addsubcategory,name="addsubcategory"),
    path('get-subcategories/', views.get_subcategories, name='get_subcategories'),
    path('freelancerdisplay/',views.freelancerdisplay),
    path('viewfreelancer/<int:id>',views.viewfreelancer,name="viewfreelancer"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)