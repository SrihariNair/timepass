from calendar import month

from django.db.models.functions import Extract
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import generic, View
from .forms import PostForm

from users.models import CustomUser

from .models import Post, Announcement


def birthdaylist(request):
    if(request.user.is_authenticated):

        users=CustomUser.objects.annotate(
           birth_date_month=Extract('birth_date', 'month'),
           birth_date_day=Extract('birth_date', 'day')
        ).order_by('birth_date_month', 'birth_date_day').all()

        Months={
            1:'January',
            2: 'February',
            3:'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December',
        }
        context={
            'users':users,
            'month':Months
        }
        return render(request,'dashboard/birthdaylist.html',context=context)
    else:
        return redirect('login')


class detailview(generic.DetailView):
    model = CustomUser
    template_name = "dashboard/detailview.html"

def detailview(request):
    if request.user.is_authenticated:
            return render(request,'dashboard/detailview.html')
    else:
        return redirect('login')

def home(request):
    announces = Announcement.objects.order_by('-date').all()
    if(request.user.is_authenticated):
        context={
            'announcements' : announces,
        }
        return render(request,'dashboard/home.html',context=context)
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
        return render(request, 'dashboard/new_post.html', {'form': form})


def postdetail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    context={
        'post':post
    }
    return render(request,'dashboard/postdetail.html',context=context)


class PostList(generic.ListView):
    template_name = 'dashboard/postlist.html'
    def get_queryset(self):
        return Post.objects.order_by('-date').all()




def approval(request):
    leaves = request.user.leaveapplication_set.all().order_by('-created_date')
    context = {
        'leaves': leaves,
    }
    if (request.user.is_authenticated):
        return render(request, 'dashboard/approval.html', context=context)
    else:
        return redirect('home')


def applyleave(request):
    if request.method== 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('dashboard:approval')
    else:
        form = PostForm()
        return render(request, 'dashboard/applyleave.html', {'form': form})



