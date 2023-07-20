"""
URL configuration for redmi_project project.

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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from headphones import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mathoperation/<str:operationType>/',views.mathoperation,name='mathoperation'),
    path('primenumber/',views.primenumber,name='primenumber'),
    path('factorial/',views.factorial,name='factorial'),
    path('simplehtmlpage/',views.simplehtmlpage,name='simplehtmlpage'),
    path('forpage/',views.forpage,name='forpage'),
    path('block/',views.block,name='block'),
    path('variable/',views.variable,name='variable'),
    path('simpleform/',views.simpleform,name='simpleform'),
    path('multiplemath/',views.multiplemath,name='multiplemath'),
    path('palindrome/',views.palindrome,name='palindrome'),
    path('studentregistrationform/',views.studentregistrationform,name='studentregistrationform'),
    path('calculator/',views.calculator,name='calculator'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
