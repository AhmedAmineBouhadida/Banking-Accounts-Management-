from django.urls import path 
from .views import *
from .ui_views import *

urlpatterns = [
 path('',bank_soap_app),
 path('home/', home , name='add_account'),
 path('add-account/', add_account_view, name='add_account'),
 path('account_details/', account_details_view, name='account_details'),
 path('all-accounts/', all_accounts_view, name='all_accounts'),


]
