from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.admin.templatetags import log


@staff_member_required(login_url='login')
def index(request):
    return render(request, 'administration/index.html')
