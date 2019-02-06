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
    list_display = ['id', 'title', 'content', 'content_size']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '내용 글자수'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'job']