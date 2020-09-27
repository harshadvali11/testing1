from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
import datetime
# Create your views here.
def Form_validate(request):
    form=Form()
    if request.method=='POST':
        form_data=Form(request.POST)
        if form_data.is_valid():
            return HttpResponse('data is validated successfully')
    return render(request,'form.html',context={'form':form})




def filter_html(request):
    dates=datetime.datetime.now()
    d={'data':'hai Hello HOW R u','dates':dates,'count':1}
    return render(request,'filter.html',context=d)