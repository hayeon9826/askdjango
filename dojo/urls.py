from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns=[
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    url(r'^post$', views.post_list, name="post"),
    url(r'^post2$', views.post_list2, name='post2'),
    url(r'^post3$', views.post_list3, name='post3'),
    url(r'^excel$', views.excel_download, name='excel'),

    url(r'^cbv/post$', views_cbv.post_list, name="post"),
    url(r'^cbv/post2$', views_cbv.post_list2, name='post2'),
    url(r'^cbv/post3$', views_cbv.post_list3, name='post3'),
    url(r'^cbv/excel$', views_cbv.excel_download, name='excel')
]

