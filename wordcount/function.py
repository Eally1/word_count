#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def count(request):
    content = request.GET['text']
    total_count = len(content)
    dict = {}
    for i in content:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i]+=1
    sort_dict = sorted(dict.items(),key=lambda a:a[1],reverse=True)

    return  render(request,'count.html', {'count':total_count,'text':content,'count_dict':dict,'sort_dict':sort_dict})
