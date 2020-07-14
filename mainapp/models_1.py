from django.db import models
from django.shortcuts import render
from django import forms
import json
import os
import time


def mod_1(request, forms):
    user_link = forms.cleaned_data['link']

    d = {'user_link': user_link}

    json_data = json.dumps(d)
    i = open('Input.json', 'w')
    i.write(json_data)
    i.close()

    # While loop runs if Output.json file is empty
    while(os.stat('Output.json').st_size == 0):
        time.sleep(1)
        pass

    o = open('Output.json', 'r+')
    result = json.load(o)
    d['result'] = result['result']
    d['similarity'] = result['similarity']
    d['user_data'] = result['user_data']
    d['admin_data'] = result['admin_data']
    o.truncate(0)
    o.close()

    # Form Data Keys
    # user_link, result, similarity, user_data, admin_data

    return render(request, 'mainapp/new2.html', {'form_data': d})
