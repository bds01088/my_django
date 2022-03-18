from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 어떻게 보여 줄건데?
    list_display = (
        'pk', 'title', 'content', 
        'created_at', 'updated_at'
        )
    # 참고
    list_filter = ('created_at', )
    list_display_links = ('title',)
    list_per_page = 2
    ordering = ('pk',)

# 관리자.사이트.등록(Article)
# 아싸리
admin.site.register(Article, ArticleAdmin)