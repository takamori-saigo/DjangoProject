from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(MainPageContent)
class PageContentAdmin(admin.ModelAdmin):

    list_display = ('titlePage', 'preview_content')
    search_fields = ('titlePage',)

    readonly_fields = ('preview_content',)

    def preview_content(self, obj): return format_html(obj.contentPage)
    
    preview_content.allow_tags = True

class part_statistic(admin.TabularInline):

    model = tableStatistic

    extra = 1

    fields = ('name', 'data', 'image')

    def image_preview(self, obj):
        if obj.image:

            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        
    image_preview.short_description = 'Preview'

    image_preview.allow_tags = True 

@admin.register(Statistic)
class GeneralStatisticsAdmin(admin.ModelAdmin):

    list_display = ('title', 'content')

    inlines = [part_statistic]