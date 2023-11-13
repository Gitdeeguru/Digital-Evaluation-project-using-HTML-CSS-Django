from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect #, get_object_or_404
#from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.core.validators import FileExtensionValidator, MaxValueValidator
from scriptofstd.models import Scriptofstd
from staff.models import Staff
from service.models import Service
from django.contrib.auth import authenticate
from django.http import FileResponse
from django.http import Http404
from django.conf import settings
from django.urls import reverse
import os
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from math import ceil
#from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, "index.html")

def studentResult(request):
    return render(request, "studentResult.html")

def studentlogin(request):
    if request.method == 'POST':
        script_usn = request.POST['student-usn']
        script_usn = str(script_usn).upper()
        try:
            script = Scriptofstd.objects.filter(script_usn=script_usn)
            context = {'script_usn': script_usn, 'scripts': script}
            return render(request, 'studentResult.html', context)
            #return redirect('studentResult', script)
        except Scriptofstd.DoesNotExist:
            return redirect('index')
    #return render(request, 'facultylogin.html')
    return render(request, "studentlogin.html") # check here

def errorPage(request):
    return render(request, "errorPage.html")

def staff(request):
    return render(request,"staff.html")

def evaluator(request):
    return render(request,"evaluator.html")

def controller(request):
    return render(request,"controller.html")

def userform(request):
    return render(request, "userform.html")

#@login_required
def script(request):
    return render(request, "script.html")

def facultylogin(request):
    return render(request, "facultylogin.html")

def stafflogin(request):
    return render(request, "stafflogin.html")

def anzarProfile(request):
    return render(request, "anzarProfile.html")

def shaymSirProfile(request):
    return render(request, "shaymSirProfile.html")

def deepakProfile(request):
    return render(request, "deepakProfile.html")

def nagaprasadProfile(request):
    return render(request, "nagaprasadProfile.html")

def evaluationInterface(request, script_id):
    scripts = Scriptofstd.objects.filter(script_id=script_id)
    return render(request, 'evaluationInterface.html', {'scripts': scripts})



#def evaluationInterface(request):
#    return render(request, "evaluationInterface.html")

#def evaluatorInterface(request):
 #   return render(request, "evaluatorInterface.html")
 
def evaluatorInterface(request, script_evaluated_by):
    scripts = Scriptofstd.objects.filter(script_evaluated_by=script_evaluated_by)
    btnEvaluate= request.POST.get('btn-evaluate')
    #btnEvaluate.enabled= False
    #scripts = Scriptofstd.objects.all()
    #scripts = Scriptofstd.objects.filter(script_subject_code='ENG101')
    return render(request, 'evaluatorInterface.html', {'scripts': scripts})

#upload pdf

def view_pdf(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def generate_script_id():
    while True:
        new_id = str(random.randint(1000, 9999))
        if not Scriptofstd.objects.filter(script_id=new_id).exists():
            return new_id

# script upload


import random

from django.contrib import messages

def upload_file(request):
    if request.method == "POST":
        # Extract form data
        usnofstd = request.POST.get('usn')
        subcode = request.POST.get('subject-code')
        myfile = request.FILES['file-upload']
    
        # Convert usnofstd and subcode to uppercase
        usnofstd = str(usnofstd).upper()
        subcode = str(subcode).upper()

    #check whether script is already uploaded aganist the USN
        if Scriptofstd.objects.filter(script_usn=usnofstd, script_subject_code=subcode).exists():
            messages.error(request, 'Script Already Exists!!')
            return render(request, 'script.html')
    
    #checkScriptExistance = 

        # Check file size
        if myfile.size > 7340032:
            messages.error(request, 'File size must be no more than 7 MB.')
            return render(request, 'script.html')

        # Save file
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        # Save Scriptofstd object
        sc = Scriptofstd(
            script_usn=usnofstd, 
            script_subject_code=subcode, 
            script_id=generate_script_id(), 
            script_ist_marks=0, 
            script_second_marks=0, 
            script_final_marks=0, 
            script_progress="Yet to Distribute", 
            script_pdf=filename, 
            script_upload_datetime=timezone.now(),  
            script_evaluated_by=0
        )
        sc.save()

        # Show success message
        messages.success(request, 'Script Uploaded Successfully')
        return render(request, 'script.html')

    return render(request, 'script.html')



#staff login

# def staffloginform(request):
#     if request.method=="POST":
#         idofstaff = request.POST.get('staff-id"')
#         passwordofstaff = request.POST.get('password')
#     data = Staff.objects.all()
#     #print(data.staff_name)
#     # staffids = data.staff_id
#     # for a in staffids:
#     #     if idofstaff == a:
#     #         return render(request, "script.html")
#     #     else:
#     #         return render(request, "stafflogin.html")

#     return render(request, "script.html")


def staffloginform(request):
    if request.method == 'POST':
        staff_id = request.POST['staff-id']
        staff_password = request.POST['password']
        try:
            staff = Staff.objects.get(staff_id=staff_id, staff_password=staff_password)
            #request.session['authenticated'] = True
            #next_url = request.POST.get('next', '/script/')
            return redirect('script')
            
            #return redirect('script')
        except Staff.DoesNotExist:
            return redirect('errorPage')
    return render(request, 'stafflogin.html')



#  faculty login

# def facultyloginform(request):
#     if request.method == 'POST':
#         faculty_id = request.POST['faculty-id']
#         faculty_password = request.POST['faculty-password']
#         try:
#             faculty = Service.objects.get(faculty_id=faculty_id, faculty_password=faculty_password)
#             #return redirect(reverse('evaluator', kwargs={'script_evaluated_by': faculty.faculty_id}))
#             #return redirect('evaluator', script_evaluated_by=faculty.faculty_id)
#             return redirect(reverse('evaluator', kwargs={'script_evaluated_by': faculty.faculty_id}))


            
#         except Staff.DoesNotExist:
#             return redirect('index')
#     return render(request, 'facultylogin.html')


def facultyloginform(request):
    if request.method == 'POST':
        faculty_id = request.POST['faculty-id']
        faculty_password = request.POST['faculty-password']
        try:
            faculty = Service.objects.get(faculty_id=faculty_id, faculty_password=faculty_password)
            return redirect('evaluator', script_evaluated_by=faculty.faculty_id)
        except Service.DoesNotExist:
            return redirect('errorPage')
    return render(request, 'facultylogin.html')


def save_script_ist_marks(request, script_id):
    if request.method == 'POST':
        #script_id = request.POST.get('script_id')
        script_ist_marks = request.POST.get('totalmarks')
        #print(f"Retrieved script object with script_id={script_id}: {script}")
        script = Scriptofstd.objects.get(script_id=script_id) # make it dynamic
        script.script_ist_marks = script_ist_marks
        script.script_progress = "Completed"
        evaluatorofscript = script.script_evaluated_by
        script.script_evaluation_date = timezone.now()
        script.save()
        
        #print(f"Saved script object with updated script_ist_marks={script_ist_marks}")
        return redirect('evaluator', evaluatorofscript)
    else:
        return redirect('errorPage')
    




def distribute(request):
    # Handle form submission
    if request.method == 'POST':
        evaluator_id = request.POST.get('initialevaluatorid')
        script_subject_codes = request.POST.get('subject_value')
        scripts = Scriptofstd.objects.filter(script_subject_code=script_subject_codes, script_progress="Yet to Distribute")# ,script_progress="Yet to Distribute"
        script_count = scripts.count()
        return render(request, 'controller.html', {'scripts': scripts, 'evaluator_id': evaluator_id, 'script_subject_codes':script_subject_codes, 'script_count': script_count})
        

    # Fetch data from database
    
    faculty_names = Service.objects.all()
    script_subject_code = Scriptofstd.objects.order_by('script_subject_code').values('script_subject_code').distinct()
    script_subject_codes = request.POST.get('subject-value') #"18CS55"
    #evaluator_id = request.POST.get('initialevaluatorid')
    scripts = Scriptofstd.objects.filter(script_subject_code=script_subject_codes)
    
    return render(request, 'controller.html', {'faculty_names': faculty_names, 'script_subject_code': script_subject_code, 'scripts': scripts })

    # Render the template with the data

def distributeScriptsOfStds(request):
    try:
        if request.method == 'POST':
            script_ids = request.POST.get('scriptids')
            evaluator_id = request.POST.get('evaluatorid')
            for script_id in script_ids.split(','):
                script = Scriptofstd.objects.get(script_id=script_id)
                script.script_evaluated_by = evaluator_id
                script.script_progress = "Distributed"
                script.save()
            messages.success(request, 'Sucessfully Distributed!! ')
            return redirect('distribute')
    except:
        messages.error(request, 'Nothing to Distribute!! ')
        return redirect('distribute')






def getScriptsBasedOnSubjectCode(request, script_subject_code):
    scripts = Scriptofstd.objects.filter(script_subject_code=script_subject_code)
    #btnEvaluate= request.POST.get('btn-evaluate')
    #btnEvaluate.enabled= False
    #scripts = Scriptofstd.objects.all()
    #scripts = Scriptofstd.objects.filter(script_subject_code='ENG101')
    return render(request, 'controller.html', {'scripts': scripts})



def faculty_profiles(request):
    faculty_data = Service.objects.all()
    context = {'faculty_data': faculty_data}
    #faculty_scriptDetails = Scriptofstd.objects.filter()
    return render(request, 'evaluatorProfiles.html', context)





""" if request.method == 'POST' and request.FILES:
        myfile = request.FILES['file-upload']
        if myfile.size > 7340032:  # 7 MB in bytes
            return render(request, 'script.html', {'error_message': 'File size must be no more than 7 MB.'})
        usn = request.POST.get('usn')
        subCode = request.POST.get('subject-code')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        sc = Scriptofstd(script_usn=usn, script_subject_code=subCode, script_pdf=filename)
        sc.save()
        return redirect('success') #redirect
    return render(request, 'script.html') # USE ANOTHER page """

   