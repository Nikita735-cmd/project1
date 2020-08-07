from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'creater_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'views', 'is_published', 'creater_at')
    readonly_fields = ('get_photo', 'views', 'is_published', 'creater_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img scr="{obj.photo.url}" widt="75">')
        else:
            return '-'
    get_photo.short_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
        list_display = ('id', 'title')
        list_display_links = ('id', 'title')
        search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управелине новостями'
admin.site.site_header = 'Управелине новостями'
