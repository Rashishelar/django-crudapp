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
from .views import offices,employees,customers,productlines,products,orders,orderdetails,payments
from .views import logout
urlpatterns = [
  
    path('offices',offices,name='offices'),
    path('employees',employees,name='employees'),
    path('customers',customers,name='customers'),
    path('productlines',productlines,name='productlines'),
    path('products',products,name='products'),
    path('orders',orders,name='orders'),
    path('orderdetails',orderdetails,name='orderdetails'),
    path('payments',payments,name='payments'),

    path('logout',logout,name='logout'),
    
]
