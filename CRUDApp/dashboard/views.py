from django.shortcuts import render,HttpResponseRedirect
# here import form
from dashboard.forms.form_Offices import Form_Offices
from dashboard.forms.form_Employees import Form_Employees
from dashboard.forms.form_Customers import Form_Customers
from dashboard.forms.form_Productlines import Form_Productlines
from dashboard.forms.form_Products import Form_Products
from dashboard.forms.form_Orders import Form_Orders
from dashboard.forms.form_Orderdetails import Form_Orderdetails
from dashboard.forms.form_Payments import Form_Payments
from dashboard.forms.form_ChangePassword import Form_ChangePassword

# here import model
from dashboard.models.offices import Offices
from dashboard.models.employees import Employees
from dashboard.models.customers import Customers
from dashboard.models.productlines import Productlines
from dashboard.models.orders import Orders
from dashboard.models.products import Products
from dashboard.models.orderdetails import Orderdetails
from dashboard.models.payments import Payments
from dashboard.models.admin import Admin

# import password hasher
from argon2 import PasswordHasher

# import here message
from django.contrib import messages
# Create your views here.


def offices(request):
    if request.method=='POST':
        fm=Form_Offices(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/offices')
    else:
        fm=Form_Offices()
        display_offices=Offices.objects.all()
        return render(request,'dashboard/offices.html',{'forms':fm,'display_offices':display_offices})

def update_offices(request,id):
    officeCode=Offices.objects.get(pk=id)
    if request.method=='POST':
        fm=Form_Offices(request.POST,instance=officeCode)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/offices')
    else:
        fm=Form_Offices(instance=officeCode)
        return render(request,'dashboard/update_offices.html',{'forms':fm})

def delete_offices(request,id):
    try:
        officeCode=Offices.objects.get(pk=id)
        officeCode.delete()
        return HttpResponseRedirect('/dashboard/offices')
    except Exception as e:
        messages.add_message(request,messages.ERROR,"Can't delete record")
        return HttpResponseRedirect('/dashboard/offices')

def employees(request):
    if request.method=='POST':
        fm=Form_Employees(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/employees')
    else:
        fm=Form_Employees()
        display_employees=Employees.objects.all()
        return render(request,'dashboard/employees.html',{'forms':fm,'display_employees':display_employees})

def update_employees(request,id):
    employeeNumber=Employees.objects.get(pk=id)
    if request.method=='POST':
        fm=Form_Employees(request.POST,instance=employeeNumber)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/employees')
    else:
        fm=Form_Employees(instance=employeeNumber)
        return render(request,'dashboard/update_employees.html',{'forms':fm})

def delete_employees(request,id):
    try:
        employeeNumber=Employees.objects.get(pk=id)
        employeeNumber.delete()
        return HttpResponseRedirect('/dashboard/employees')
    except Exception as e:
        messages.add_message(request,messages.ERROR,"Can't delete record")
        return HttpResponseRedirect('/dashboard/employees')


def customers(request):
    if request.method=='POST':
        fm=Form_Customers(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/customers')
    else:
        fm=Form_Customers()
        # this is sql query 
        display_customers=Customers.objects.all()
        return render(request,'dashboard/customers.html',{'forms':fm,'display_customers':display_customers})

def update_customers(request,id):
    customerNumber=Customers.objects.get(pk=id)
    if request.method=='POST':
        fm=Form_Customers(request.POST,instance=customerNumber)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/customers')
    else:
        fm=Form_Customers(instance=customerNumber)
        return render(request,'dashboard/update_customers.html',{'forms':fm})

def delete_customers(request,id):
    try:
        customerNumber=Customers.objects.get(pk=id)
        customerNumber.delete()
        return HttpResponseRedirect('/dashboard/customers')
    except Exception as e:
        messages.add_message(request,messages.ERROR,e)
        return HttpResponseRedirect('/dashboard/customers')

def productlines(request):
    if request.method=='POST':
        fm=Form_Productlines(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/productlines')
    else:
        fm=Form_Productlines()
        display_productlines=Productlines.objects.all()
        return render(request,'dashboard/productlines.html',{'forms':fm,'display_productlines':display_productlines})

def update_productlines(request,id):
    productLine=Productlines.objects.get(pk=id)
    if request.method=='POST':
        fm=Form_Productlines(request.POST,instance=productLine)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/productlines')
    else:
        fm=Form_Productlines(instance=productLine)
        return render(request,'dashboard/update_productlines.html',{'forms':fm})

def delete_productlines(request,id):
    try:
        productLine=Productlines.objects.get(pk=id)
        productLine.delete()
        return HttpResponseRedirect('/dashboard/productlines')
    except Exception as e:
        messages.add_message(request,messages.ERROR,e)
        return HttpResponseRedirect('/dashboard/productlines')
    
def products(request):
    if request.method=='POST':
        fm=Form_Products(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/products')
    else:
        fm=Form_Products()
        display_products=Products.objects.all()
        return render(request,'dashboard/products.html',{'forms':fm,'display_products':display_products})

def update_products(request,id):
    productCode=Products.objects.get(pk=id)
    if request.method=='POST':
        fm=Form_Products(request.POST,instance=productCode)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/products')
    else:
        fm=Form_Products(instance=productCode)
        return render(request,'dashboard/update_products.html',{'forms':fm})

def delete_products(request,id):
    try:
        productCode=Products.objects.get(pk=id)
        productCode.delete()
        return HttpResponseRedirect('/dashboard/products')
    except Exception as e:
        messages.add_message(request,messages.ERROR,e)
        return HttpResponseRedirect('/dashboard/products')

def orders(request):
    if request.method=='POST':
        fm=Form_Orders(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/orders')
    else:
        fm=Form_Orders
        display_orders=Orders.objects.all()
        return render(request,'dashboard/orders.html',{'forms':fm,'display_orders':display_orders})

def update_orders(request,id):
    orderNumber=Orders.objects.get(pk=id)
    if request.method=='POST':
        fm=Form_Orders(request.POST,instance=orderNumber)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/orders')
    else:
        fm=Form_Orders(instance=orderNumber)
        return render(request,'dashboard/update_orders.html',{'forms':fm})
    
def delete_orders(request,id):
    try:
        orderNumber=Orders.objects.get(pk=id)
        orderNumber.delete()
        return HttpResponseRedirect('/dashboard/orders')
    except Exception as e:
        messages.add_message(request,messages.ERROR,e)
        return HttpResponseRedirect('/dashboard/orders')

def orderdetails(request):
    if request.method=='POST':
        fm=Form_Orderdetails(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/orderdetails')
    else:
        fm=Form_Orderdetails()
        display_orderdetails=Orderdetails.objects.all()
        return render(request,'dashboard/orderdetails.html',{'forms':fm,'display_orderdetails':display_orderdetails})

def update_orderdetails(request,id):
    orderdetails_id=Orderdetails.objects.get(pk=id)
    if request.method=='POST':
        fm=Form_Orderdetails(request.POST,instance=orderdetails_id)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/orderdetails')
    else:
        fm=Form_Orderdetails(instance=orderdetails_id)
        return render(request,'dashboard/update_orderdetails.html',{'forms':fm})

def delete_orderdetails(request,id):
    try:
        orderdetails_id=Orderdetails.objects.get(pk=id)
        orderdetails_id.delete()
        return HttpResponseRedirect('/dashboard/orderdetails')
    except Exception as e:
        messages.add_message(request,messages.ERROR,e)
        return HttpResponseRedirect('/dashboard/orderdetails')
    

def payments(request):
    if request.method=='POST':
        fm=Form_Payments(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/payments')
    else:
        fm=Form_Payments()
        display_payments=Payments.objects.all()
        return render(request,'dashboard/payments.html',{'forms':fm,'display_payments':display_payments})
    
def update_payments(request,id):
    paymentID=Payments.objects.get(pk=id)
    if request.method=='POST':
        fm=Form_Payments(request.POST,instance=paymentID)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/dashboard/payments')
    else:
        fm=Form_Payments(instance=paymentID)
        return render(request,'dashboard/update_payments.html',{'forms':fm})

def delete_payments(request,id):
    try:
        paymentID=Payments.objects.get(pk=id)
        paymentID.delete()
        return HttpResponseRedirect('/dashboard/payments')
    except Exception as e:
        messages.add_message(request,messages.ERROR,e)
        return HttpResponseRedirect('/dashboard/payments')
    
def changepassword(request):
    if request.method=='POST':
        ph=PasswordHasher()
        old_username=request.POST['old_username']
        old_password=request.POST['old_password']
        new_password=request.POST['new_password']
        user=Admin.objects.get(username=old_username)
        if user.username==old_username and ph.verify(user.password,old_password):
            password=ph.hash(new_password)
            user.password=password
            user.save()
            return HttpResponseRedirect('/dashboard/changepassword')
        else:
            return HttpResponseRedirect('/dashboard/changepassword')
    else:
        fm=Form_ChangePassword()
        return render(request,'dashboard/changepassword.html',{'forms':fm})
    
def logout(request):
    return HttpResponseRedirect('/')
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