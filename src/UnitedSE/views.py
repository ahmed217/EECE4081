from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
               'page': {'title': 'United Social Engine', 
                        'content': 'doing something'},
               }
    return render(request,'UnitedSE/index.html',context)
