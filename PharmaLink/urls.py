"""
URL configuration for PharmaLink project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main import views as mainv
from users import views as userv
from invtry import views as invv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , mainv.index , name='homepage'),
    path('login/' , userv.loginreq , name='login'),
    path('logout/' , userv.logoutreq , name='logout'),
    path('inv/' , invv.inventory , name='inv'),
    path('api/add_drug' , invv.add_drug , name='add_drug'),
    path('api/delete_drug/', invv.delete_drug, name='delete_drug'),
    path('api/update_drug/', invv.update_drug, name='update_drug'),
    path('api/list_drugs/', invv.drug_list, name='list_drugs'),
    path('dashboard/' , invv.dashboard , name='dashboard')
]
