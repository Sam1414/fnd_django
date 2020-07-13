from django.shortcuts import render
from mainapp.forms import news_form
from mainapp.models import mod


def index(request):
    if request.method == 'POST':
        form = news_form(request.POST)
        if form.is_valid():
            # AI Model Proccessing Logic
            # pass
            # form.save(commit=True)
            return mod(request, form)
            # return render(request, 'mainapp/new1.html', {'form_data': form.cleaned_data})

    else:
        form = news_form()

    return render(request, 'mainapp/index.html', {'form': form})
