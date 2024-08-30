
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, PostCreationForm



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html',{'form':form})






def create_post(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = PostCreationForm()
    return render(request, 'create_post.html', {'form': form})
