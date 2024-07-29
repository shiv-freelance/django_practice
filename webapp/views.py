from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm

# Create your views here.
def home_page(request):
    # return HttpResponse('Hello World!!!')
    return render(request, 'webapp/index.html')


# - Register
def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            # return redirect('webapp/login.html')
    
    context = {"form": form}

    return render(request, 'webapp/register.html', context=context)

