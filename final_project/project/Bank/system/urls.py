from django.urls import path
from . import views

app_name = 'system'
urlpatterns = [
    path('',views.system,name='system'),
    path('account-list',views.account_list,name='account_list'),
    path('create_account_list',views.create_account_list,name='create_account_list'),
    # path('create_account_list1',views.create_account_list1,name='create_account_list1'),
    path('signup',views.signup,name='signup'),
    path('account_log',views.account_log,name='account_log'),
    path('account_owener',views.account_owener,name='account_owener'),
    path('close',views.close,name='close'),
    path('block',views.block,name='block'),
    path('retrive_account',views.retrive_account,name='retrive_account'),
    path('retrive_owner',views.retrive_owner,name='retrive_owner'),
    path('transaction',views.transaction,name='transaction'),
    path('transaction_get',views.transaction_get,name='transaction_get'),
]