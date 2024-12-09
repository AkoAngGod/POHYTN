#apps/urls.py
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #ADMIN LANG
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addaccount/', views.profile_loob, name='addaccount'),
    path('editprofile/', views.edit_profile, name='edit_profile'),
    path('creditpayment/', views.credit_payment, name='credit_payment'),    

    path('billing/', views.billing, name='billing'),

    #DRIVER LANG
    path('driverdashboard/', views.driverdashboard, name='driverdashboard'),
    path("addaccount/", views.driverprofile_loob, name="addaccount"),
    path('drivereditprofile/', views.driveredit_profile, name='driveredit_profile'),
    path('driverbilling/', views.driverbilling, name='driverbilling'),

    #PARA SA LAHAT
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.profile_creation, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('receipt/<int:receipt_id>/', views.receipt, name='receipt'),
    path('deleteprofile/<int:user_id>/', views.delete_profile, name='delete_profile'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

