from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def dtl(request):
    # name = 'jun'
    context = {
        'name': 'JUNASDFEWASDF',
        'age' : 20,
        'foods' : ['apple','banana','pizza'],
    }
    return render(request, 'dtl.html',context)

def greeting(request):
    context = {
        'name' : 'jin'
    }
    return render(request, 'greeting.html',context)

def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    # print(dir(request)) # dir 안에 있는 모든 메서드들을 알려주는 함수
    value = request.GET.get('search')
    # GET 방식으로 보낸 데이터에서 search라고 담긴 키를 저장
    # name = 'jin' 과 같은 맹락
    context = {
        'value' : value, # key : value
        # 'name' : name,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'catch.html', context)