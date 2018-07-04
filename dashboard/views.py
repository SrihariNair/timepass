
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import PostForm

from users.models import CustomUser

from .models import Userpost


def birthdaylist(request):
    if(request.user.is_authenticated):

        users=CustomUser.objects.order_by('birth_date')[:]
    # ignore the line below
    #   users= CustomUser.objects.extra(select={'birthmonth':'birth_date'},order_by=['birthmonth'])
        context={
            'users':users
        }
        return render(request,'dashboard/birthdaylist.html',context=context)
    else:
        return redirect('login')


def detailview(request,customuser_id):
    users=get_object_or_404(CustomUser,pk=customuser_id)
    context={
        'users':users
    }
    return render(request,'dashboard/detailview.html',context=context)


def home(request):
    if(request.user.is_authenticated):
        return render(request,'dashboard/home.html')
    else:
        return redirect('login')


def leaveapplications(request):
    leaves = Userpost.objects.all()
    context = {
        'leaves': leaves
    }
    if (request.user.is_authenticated):
        return render(request, 'dashboard/leaveapplications.html', context=context)
    else:
        return redirect('login')

class userposts(generic.CreateView):
    form_class = PostForm
    template_name = 'dashboard/posts.html'