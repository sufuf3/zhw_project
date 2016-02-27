# coding=UTF-8
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse, Http404

def home(request):
    return render(request, 'eternal/home.html')
