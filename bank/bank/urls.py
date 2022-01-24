"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from bank.app.forms.login import LoginForm
from bank.app.views import index, register, profile
from bank.system.views import index as index_system, \
    add_account as add_account_system, \
    add_transaction as add_transaction_system, \
    add_category as add_category_system, \
    list_transactions as list_transactions_system, \
    change_account as change_account_system, \
    delete_account as delete_account_system, \
    ajax_get_account as ajax_get_account_system, \
    admin_account_list, \
    admin_account_change, \
    admin_account_delete, \
    admin_account_add
from bank.administration.views import index as admin_index
urlpatterns = [
    path('django/', admin.site.urls),
    path('', index, name="index"),
    path('login', auth_views.LoginView.as_view(
        template_name='app/user/login.html',
        authentication_form=LoginForm,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('account/', index_system, name='index_system'),
    path('account/add', add_account_system, name='add_account_system'),
    path('account/<int:id>/add', add_transaction_system, name='add_transaction_system'),
    path('category/add', add_category_system, name='add_category_system'),
    path('account/<int:id>', list_transactions_system, name='list_transactions_system'),
    path('account/<int:id>/change', change_account_system, name='change_account_system'),
    path('api/account/<int:id>', ajax_get_account_system, name='ajax_get_account_system'),
    path('account/<int:id>/delete', delete_account_system, name='delete_account_system'),
    path('admin/', admin_index, name='admin_index'),
    path('admin/account/', admin_account_list, name='admin_account_list'),
    path('admin/account/add', admin_account_add, name='admin_account_add'),
    path('admin/account/<int:id>/change', admin_account_change, name='admin_account_change'),
    path('admin/account/<int:id>/delete', admin_account_delete, name='admin_account_delete'),
]

