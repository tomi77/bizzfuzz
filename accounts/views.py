from django.shortcuts import render, redirect

from accounts.models import UserProfile


def index(request):
    users = UserProfile.objects.all()

    message = request.session.get('message', None)
    info = request.session.get('info', None)
    warning = request.session.get('warning', None)
    alert = request.session.get('alert', None)
    request.session['message'] = None
    request.session['info'] = None
    request.session['warning'] = None
    request.session['alert'] = None

    return render(request, 'accounts/index.html', {
        'users': users,
        'message': message,
        'info': info,
        'warning': warning,
        'alert': alert
    })


def add(request):
    if request.method == 'POST':
        user = UserProfile(username=request.POST.get('username'),
                           birthday=request.POST.get('birthday'))
        user.save()

        return redirect('/')

    return render(request, 'accounts/add.html')


def edit(request, pk):
    user = UserProfile.objects.get(pk=pk)

    if request.method == 'POST':
        user.username = request.POST.get('username', user.username)
        user.birthday = request.POST.get('birthday', user.birthday)
        user.save()

        return redirect('/')

    return render(request, 'accounts/edit.html', {
        'user': user
    })


def details(request, pk):
    user = UserProfile.objects.get(pk=pk)

    return render(request, 'accounts/details.html', {
        'user': user
    })


def delete(request, pk):
    try:
        user = UserProfile.objects.get(pk=pk)
        user.delete()
        request.session['message'] = 'User has been deleted'
    except UserProfile.DoesNotExist:
        request.session['alert'] = 'User does not exist'

    return redirect('/')
