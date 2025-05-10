from django.contrib.auth import login
from django.shortcuts import redirect, render
from userapp.forms import RegistrationForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todoapp:home')
    else:
        form = RegistrationForm()
    return render(request, 'userapp/registration.html', {'form': form})