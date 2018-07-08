from calendar import month

from django.db.models.functions import Extract
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import generic, View
from .forms import PostForm

from users.models import CustomUser

from .models import Post


def birthdaylist(request):
    if(request.user.is_authenticated):




        users=CustomUser.objects.annotate(
           birth_date_month=Extract('birth_date', 'month'),
           birth_date_day=Extract('birth_date', 'day')
        ).order_by('birth_date_month', 'birth_date_day').all()


        #users=CustomUser.objects.order_by(Extract('birth_date','month'))[:]
        # or this
        #users=CustomUser.objects.order_by('birth_date')[:]

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

def new_posts(request):
    if request.method== 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()

            return redirect('dashboard:post_detail',pk= post.pk)
    else:
        form = PostForm()
        return render(request, 'dashboard/post_edit.html', {'form': form})


def postdetail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context={
        'post':post
    }
    return render(request,'dashboard/posts.html',context=context)


class posts(generic.ListView):
    template_name = 'dashboard/posets.html'
    def get_queryset(self):
        return Post.objects.all()
