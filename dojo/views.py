from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os


# Create your views here.
def mysum(request, numbers):
    #request : HTTPREQUEST
    #numbers = '1/2/12/123/1232/1232/3213/1232'
    # result = sum(map(int, numbers.split('/')))
    result = sum(map(lambda s: int(s or 0), numbers.split('/')))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))

def post_list(request):
    name = '하연'
    return HttpResponse("""
    <h1>AskDjango</h1>

    <p><b>{name}</b>이가 제발 정신차리고 토플 공부를 했으면 좋겠다.</p>""".format(name=name))

def post_list2(request):
    name = '하연'
    return render(request, 'dojo/post_list.html', {'name':name})

def post_list3(request):
    return JsonResponse({
        'message': '안녕, 파이썬 & 장고',
        'items' : ['파이썬', '장고', '구글', '가고', '싶다'],
    }, json_dumps_params = {'ensure_ascii' : False} )

def excel_download(request):
    #filepath = 'D:/__khy__/VOD_python/example.xlsx'
    filepath = os.path.join(settings.BASE_DIR, 'example.xlsx')
    filename = os.path.basename(filepath) #파일 이름 인자 부분만 추출
    
    with open(filepath, 'rb') as f: #read binary file(텍스트 파일 아닌것 binary)
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel') #기본 text/html
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename) #header 적어주기
        return response