from django.shortcuts import render,HttpResponseRedirect

#import here forms
from dashboardadmin.forms.form_Login import Form_Login
#import here model
from dashboard.models.admin import Admin

#from argon2 import PasswordHasher
# Create your views here.
def index(request):
    if request.method=='POST':
        # form user data
        #ph=PasswordHasher()
        form_username=request.POST['username']
        form_password=request.POST['password']
        try:
            user=Admin.objects.get(username=form_username)
            if user.username==form_username and user.password==form_password:
                return HttpResponseRedirect('/dashboard/offices')
        except Exception as e:
            return HttpResponseRedirect('/')
    else:
        fm=Form_Login()
        return render(request,'dashboardadmin/index.html',{'forms':fm})
        
'''
def savepassword(request):
    ph=PasswordHasher()
    password=ph.hash('raju@123')
    #save the password
    username='raju'
    save_admin=Admin(username=username,password=password)
    save_admin.save()
    return HttpResponseRedirect('/')
'''
def savepassword(request):
    username='raju'
    password='raju@123'
    save_admin=Admin(username=username,password=password)
    save_admin.save()
    return HttpResponseRedirect('/')
