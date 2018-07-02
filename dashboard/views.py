
from django.shortcuts import render, redirect, get_object_or_404


from users.models import CustomUser



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