from django.contrib import admin
from .models import Post, Author
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Post)
admin.site.unregister(Post)
admin.site.register(Author)
admin.site.unregister(Author)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = ['make_published']

    list_display = ['id', 'title', 'content',
                    'category', 'content_size', 'status']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '내용 글자수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status = 'p')
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Publisehd 상태로 변경'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'job']