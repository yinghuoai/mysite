from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import User

# Create your views here.

def index(request):

    try:
        user_list=User.objects.all()
    except User.DoesNotExist:
        raise Http404("用户不存在，还没有创建")

    template = loader.get_template(('user/index.html'))
    context ={
        'user_list':user_list,

    }
    return HttpResponse(template.render(context,request))







