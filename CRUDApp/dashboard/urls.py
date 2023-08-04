"""
URL configuration for CRUDApp project.

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

from django.urls import path

from .views import offices,update_offices,delete_offices
from .views import employees,update_employees,delete_employees
from .views import customers,update_customers,delete_customers
from .views import productlines,update_productlines,delete_productlines
from .views import products,update_products,delete_products
from .views import orders,update_orders,delete_orders
from .views import orderdetails,update_orderdetails,delete_orderdetails
from .views import payments,update_payments,delete_payments
from .views import logout,changepassword
urlpatterns = [
  
    path('offices',offices,name='offices'),
    path('update_offices/<int:id>',update_offices,name='update_offices'),
    path('delete_offices/<int:id>',delete_offices,name='delete_offices'),

    path('employees',employees,name='employees'),
    path('update_employees/<int:id>',update_employees,name='update_employees'),
    path('delete_employees/<int:id>',delete_employees,name='delete_employees'),

    path('customers',customers,name='customers'),
    path('update_customers/<int:id>',update_customers,name='update_customers'),
    path('delete_customers/<int:id>',delete_customers,name='delete_customers'),

    path('productlines',productlines,name='productlines'),
    path('update_productlines/<str:id>',update_productlines,name='update_productlines'),
    path('delete_productlines/<str:id>',delete_productlines,name='delete_productlines'),

    path('products',products,name='products'),
    path('update_products/<str:id>',update_products,name='update_products'),
    path('delete_products/<str:id>',delete_products,name='delete_products'),

    path('orders',orders,name='orders'),
    path('update_orders/<int:id>',update_orders,name='update_orders'),
    path('delete_orders/<int:id>',delete_orders,name='delete_orders'),

    path('orderdetails',orderdetails,name='orderdetails'),
    path('update_orderdetails/<int:id>',update_orderdetails,name='update_orderdetails'),
    path('delete_orderdetails/<int:id>',delete_orderdetails,name='delete_orderdetails'),

    path('payments',payments,name='payments'),
    path('update_payments/<int:id>',update_payments,name='update_payments'),
    path('delete_payments/<int:id>',delete_payments,name='delete_payments'),

    path('logout',logout,name='logout'),
    path('changepassword',changepassword,name='changepassword'),
    
]
