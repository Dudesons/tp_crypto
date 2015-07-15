from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import RequestContext, loader
from algo_hash import hash_algo



def home(request):
    pwd = request.POST.get("pwd")
    if pwd is None:
        pwd_crypt = ''
    else:
        r = hash_algo(pwd)
        if r[0] is True:
            pwd_crypt = r[1]
        else:
            pwd_crypt = "error hash_algo return False"
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'pwd': pwd_crypt
    })
    return HttpResponse(template.render(context))