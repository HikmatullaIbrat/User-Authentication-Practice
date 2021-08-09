from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required # this is for users if they are logged in

def home(request):
    return render(request, 'index.html')
@login_required # if he/she is logged in
def treasure(request):
    return render(request, 'treasure.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form':form})