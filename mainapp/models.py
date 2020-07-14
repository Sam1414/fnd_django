from django.db import models
from django.shortcuts import render
from django import forms
import json
import os
import time
# import nltk
# from nltk.stem import PorterStemmer
# import numpy as np
# from scipy.sparse import csr_matrix, hstack, vstack
# import tensorflow as tf
# import tensorflow_hub as hub

# Create your models here.


def mod(request, forms):
    heading = forms.cleaned_data['heading']
    content = forms.cleaned_data['content']

    # heading = preproc(heading)
    # content = preproc(content)

    # feat_svec = feature_vector(heading, content)

    d = {'heading': heading, 'content': content}

    json_data = json.dumps(d)
    i = open('Input.json', 'w')
    i.write(json_data)
    i.close()

    # While loop runs till Output.json is empty
    while(os.stat('Output.json').st_size == 0):
        time.sleep(1)
        pass

    o = open('Output.json', 'r+')
    result = json.load(o)
    d['result'] = result['result']
    d['similarity'] = result['similarity']
    d['admin_link'] = result['admin_link']
    d['admin_data'] = result['admin_data']
    d['image_url'] = result['image_url']
    o.truncate(0)
    o.close()

    return render(request, 'mainapp/new1.html', {'form_data': d})


# def preproc(text):
#     lst_stop_words = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other",
#                       "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
#     punctuations = '''!()-[\’\“\”]{—};:'"\,<>./?@#$%^&*_~'''
#     ps = PorterStemmer()
#     word_lst = text.lower().split()
#     new_word_lst = []
#     for word in word_lst:
#         mod_word = ''.join([char for char in word if char not in punctuations])
#         mod_word = ps.stem(mod_word)
#         new_word_lst.append(mod_word)
#         if mod_word in lst_stop_words:
#             new_word_lst.remove(mod_word)
#     mod_text = ' '.join(new_word_lst)

#     return mod_text


# def feature_vector(heading, content):
#     feat_vec = np.empty((1025))
#     feat_vec[:] = np.nan
#     feat_svec = csr_matrix(feat_vec)

#     # embed = tf.saved_model.load('embed')

#     # @param["https://tfhub.dev/google/universal-sentence-encoder/4", "https://tfhub.dev/google/universal-sentence-encoder-large/5"]
#     # module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
#     # embed = hub.load(module_url)

#     head_emb = embed(heading)
#     cont_emb = embed(content)
#     sim = np.inner(head_emb, cont_emb)
#     feat_svec = vstack((feat_svec, hstack((head_emb[0], sim[0], cont_emb[0]))))
#     feat_svec = feat_svec.tocsr()
#     feat_svec = feat_svec[1:]

#     return feat_svec
