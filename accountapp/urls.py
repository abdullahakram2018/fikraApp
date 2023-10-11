from django.urls import path
from accountapp import views
urlpatterns = [
    path('typedoc',views.typeDoc_api,name='create_typedoc'),
    path('typeDoc/<int:pk>/', views.typeDoc_detail,name='typeDoc_detail'),
    path('currency',views.currency_api,name='create_currency'),
    path('currency/<int:pk>/', views.currency_detail,name='currency_detail'),
    path('account',views.account_api,name='create_account'),
    path('account/<int:pk>/', views.account_detail,name='account_detail'),
    path('create_unit',views.unit_api,name='create_unit'),
    path('unit/<int:pk>/', views.unit_detail,name='unit_detail'),
    path('item',views.item_api,name='create_item'),
    path('item/<int:pk>/', views.item_detail,name='item_detail'),
    path('create_store',views.store_api,name='create_store'),
    path('store/<int:pk>/', views.store_detail,name='store_detail'),
    path('entry',views.entry_api,name='entry'),
    path('entry/<int:pk>/', views.entry_detail,name='entry_detail'),
    path('account_entry/<int:pk>/', views.account_entry_detail,name='account_entry_detail'),
    path('detail_entry/<int:pk>/', views.detail_entry_detail,name='detail_entry_detail'),
    path('account_book',views.account_book,name='account_book'),
    path('bill',views.bill,name='bill'),
    path('trial_balance',views.trial_balance,name='trial_balance'),
]