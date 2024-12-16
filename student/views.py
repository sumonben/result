from django.shortcuts import render
from .models import Marks
from .forms import SeachResultForm
# Create your views here.

def searchResult(request):
    context={}
    if request.method=='POST':
        result=Marks.objects.filter(roll=request.POST.get('roll').strip())
        print(result)
        context['result']=result
        return render(request, 'result/show_result.html', context=context)
    form=SeachResultForm()
    context['form']=form
    return render(request, 'result/search_result.html', context=context)

