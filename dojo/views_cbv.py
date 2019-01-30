import os
from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse

class PostListView1(TemplateView):
#CBV: 직접 문자열로 HTML 형식 응답하기

    def get(self, request):
        name = '하연'
        html = self.get_template_string().format(name = name)
        return HttpResponse(html)
 
    def get_template_string(self):
        return '''
        <h1>AskDjango</h1>
        <p><b>{name}</b>이가 제발 정신차리고 토플 공부를 했으면 좋겠다.</p>
        '''

post_list = PostListView1.as_view()

class PostListView2(TemplateView):
#CBV: 템플릿을 통해 HTML형식 응답하기

    template_name = 'dojo/post_list.html'

    def get_context_data(self): #이거 안하면 {{name}}부분 빼고 리턴
       context = super().get_context_data()
       context['name'] = '김하연'
       return context

post_list2 = PostListView2.as_view()

class PostListView3(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params = {'ensure_ascii' : False})

    def get_data(self):
        return{
            'message': '안녕, 파이썬 & 장고',
            'items' : ['파이썬', '장고', '구글', '가고', '싶다'],
        }
    

post_list3 = PostListView3.as_view()

class ExcelDownloadView(View):
    #CBV 엑셀 다운로드 응답하기
    excel_path = 'D:/__khy__/VOD_python/example.xlsx'

    def get(self, request):
        filename = os.path.basename(self.excel_path)
        with open(self.excel_path, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)  #필요한 응답헤더 세팅
            return response #마지막에 return 필수!
    
excel_download = ExcelDownloadView.as_view()
