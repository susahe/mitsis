from django.shortcuts import render,render_to_response
from django.template import RequestContext

def index(requst):
        context = RequestContext(requst)
     #   category_list = Category.objects.order_by('-view')[:6]
        context_dict= {'courses':"Hi how are you" }
     #   for category in category_list:
    #        category.url = category.name.replace(' ', '_')
            
        return render_to_response('courses/index.html',context_dict,context)