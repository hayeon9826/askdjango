from django.db import models
from django.conf import settings
import re
from django.forms import ValidationError
from django.utils import timezone


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value): #[+-]?는 없거나 있거나
        raise ValidationError("Invalid LngLat Type")

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length = 50)
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

class Post(models.Model):

    writer = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name='제목', help_text="포스팅 제목을 입력해주세요. 최대 100자 내외") #verbose_name: 어드민 한글로 설정
    category = models.CharField(max_length=10, default = True,
        choices = (
            ('제목1', '세간'), #저장될 값 /  UI에 보여질 레이블
            ('제목2', '픽즐'),
            ('제목3', '모잇')
        )) # 길이 제한이 있는 문자열
    content = models.TextField(help_text='Markdown 문법을 써주세요.')
    tags = models.CharField(max_length = 100, blank = True) #옵션필드 (blank = true)
    lnglat = models.CharField(max_length=50, blank = True, #옵션필드 (blank = True)
        validators = [lnglat_validator],
        help_text = '경도, 위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices = STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    test_field = models.IntegerField(default=10)
    #likes = models.IntegerField()

    def __str__(self):
        return self.title
