"""Evaluation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Evaluation import views
from django.conf import settings
from django.conf.urls.static import static

from .views import upload_file

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name="index"),
    path('staff/', views.staff, name='staff'),
    path('evaluator/', views.evaluator),
    #path('controller/',views.controller),
    path('userform/',views.userform),
    #path('script/',views.script, name="script"),
    path('script/',views.script, name="script"),
   # path('upload/', upload_file, name='upload'), #can b commented
    path('upload_file/',views.upload_file, name="upload_file"),
   # path('facultylogin/',views.facultylogin),
    #path('stafflogin/',views.stafflogin),
    #path('staffloginform/',views.staffloginform, name="staffloginform"),
    path('stafflogin/', views.staffloginform, name='stafflogin'),
    #path('evaluationInterface/',views.evaluationInterface),
    path('evaluationInterface/<int:script_id>/', views.evaluationInterface, name="evaluationInterface"),

    path('pdf/<str:file_name>/', views.view_pdf, name='view_pdf'), # for pdf

    path('evaluatorInterface/<int:script_evaluated_by>/', views.evaluatorInterface, name="evaluator"),

    path('facultylogin/', views.facultyloginform, name='facultyloginform'),

    # path('save-marks/', views.save_script_ist_marks, name='save_script_ist_marks'),

    path('save_script_ist_marks/<int:script_id>/', views.save_script_ist_marks, name='save_script_ist_marks'),
    
    path('studentResult/', views.studentResult, name='studentResult'),

    path('studentlogin/', views.studentlogin, name='studentlogin'),

    path('errorPage/', views.errorPage, name='errorPage'),

    path('shaymSirProfile/', views.shaymSirProfile, name='shaymSirProfile'),
    path('anzarProfile/', views.anzarProfile, name='anzarProfile'),
    path('deepakProfile/', views.deepakProfile, name='deepakProfile'),
    path('nagaprasadProfile/', views.nagaprasadProfile, name='nagaprasadProfile'),


    path('controller/', views.distribute, name='distribute'),
    path('controller/distribute_scripts/', views.distributeScriptsOfStds, name='distributeScriptsOfStds'),

    path('evaluatorProfiles/', views.faculty_profiles, name="evaluatorProfiles"),
    path('evaluatorProfiles/faculty_scriptDetails/', views.faculty_scriptDetails, name='faculty_scriptDetails'),
    
    #check here
    path('unassign_Scripts', views.unassign_Scripts, name="unassign_Scripts"),

   # path('evaluatorInterface/<int:faculty_id>/index', views.index, name='indes'),


    

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)











"""
previous code




from django.contrib import admin
from django.urls import path
from Evaluation import views
from django.conf import settings
from django.conf.urls.static import static

from .views import upload_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('staff/', views.staff),
    path('evaluator/', views.evaluator),
    path('controller/',views.controller),
    path('userform/',views.userform),
    path('script/',views.script),
]

#if settings.DEBUG:
  #  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



urlpatterns = [
    path('upload/', upload_file, name='upload'),
]
"""

