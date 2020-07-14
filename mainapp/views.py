from django.shortcuts import render
from mainapp.forms import news_form
# from mainapp.models import mod
from mainapp.models_1 import mod_1


def index(request):
    if request.method == 'POST':
        form = news_form(request.POST)
        if form.is_valid():
            # AI Model Proccessing Logic
            # pass
            # form.save(commit=True)
            return mod_1(request, form)
            # return render(request, 'mainapp/new1.html', {'form_data': form.cleaned_data})

    else:
        form = news_form()

    return render(request, 'mainapp/index_1.html', {'form': form})
