from django.db import models
from django.conf import settings

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length = 50)
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Post(models.Model):
    writer = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name='제목', help_text="포스팅 제목을 입력해주세요. 최대 100자 내외") #verbose_name: 어드민 한글로 설정
    category = models.CharField(max_length=10, default = True,
        choices = (
            ('제목1', '세간'), #저장될 값 /  UI에 보여질 레이블
            ('제목2', '픽즐'),
            ('제목3', '모잇')
        )) # 길이 제한이 있는 문자열
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    #likes = models.IntegerField()

    def __str__(self):
        return self.title
