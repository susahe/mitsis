from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(requst):
        context = RequestContext(requst)
        category_list = "dashboard " 
        context_dict= {'dashboard':category_list }
        
        return render_to_response('dashboard/dashboard.html',context_dict,context)