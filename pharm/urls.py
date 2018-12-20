"""pharm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from pharmacy import views, apis

from django.contrib.auth.views import LoginView, LogoutView 

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('pharmacy/sign-in/', LoginView.as_view(template_name='pharmacy/sign_in.html'),
        name='pharmacy-sign-in'),
    path('pharmacy/sign-out/', LogoutView.as_view(next_page='/'), 
        name='pharmacy-sign-out'),
    path('pharmacy/', views.pharmacy_home, name='pharmacy-home'),
    
    path('pharmacy/sign-up/', views.pharmacy_sign_up, name='pharmacy-sign-up'),

    path('pharmacy/account/', views.pharmacy_account, name='pharmacy-account'),
    path('pharmacy/drug/', views.pharmacy_drug, name='pharmacy-drug'),
    path('pharmacy/drug/add/', views.pharmacy_add_drug, name='pharmacy-add-drug'),
    path('pharmacy/drug/edit/<int:drug_id>', views.pharmacy_edit_drug, name='pharmacy-edit-drug'),

    # APIS
    path('api/client/pharmacys/', apis.client_get_pharmacys),
    path('api/client/drugs/<int:pharmacy_id>/', apis.client_get_drugs),

    # Sign In / Sign Up / Sign Out
    path('api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token (sign in / sign up)
    # /revoke-token (sign out)


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
