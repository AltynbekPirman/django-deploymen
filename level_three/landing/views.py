from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    index_dict = {'greet':'hello world'}
    return render(request, "landing/index.html", context=index_dict)

def form_page(request):
    form = forms.registerForm()

    if request.method == "POST":
        form = forms.registerForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    return render(request, "landing/form.html", context={'registration':form})
