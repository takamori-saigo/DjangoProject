from django.contrib import admin
from .models import *
from django.utils.html import format_html


class skills_part_statistic(admin.TabularInline):
    model = Table_Skills
    extra = 1
    fields = ('name', 'data', 'image')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        
    image_preview.short_description = 'Preview'
    image_preview.allow_tags = True 

@admin.register(Skills_statistic)
class Skills_statistic(admin.ModelAdmin):
    list_display = ('title', 'content')
    inlines = [skills_part_statistic]

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


class demand_part_statistic(admin.TabularInline):
    model = Table_Demand
    extra = 1
    fields = ('name', 'data', 'image')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        
    image_preview.short_description = 'Preview'
    image_preview.allow_tags = True 

@admin.register(Demand_statistic)
class Demand_statistic(admin.ModelAdmin):
    list_display = ('title', 'content')
    inlines = [demand_part_statistic]


class geography_part_statistic(admin.TabularInline):
    model = Table_Geography
    extra = 1
    fields = ('name', 'data', 'image')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        
    image_preview.short_description = 'Preview'
    image_preview.allow_tags = True 

@admin.register(Geography_statistic)
class Geography_statistic(admin.ModelAdmin):
    list_display = ('title', 'content')
    inlines = [geography_part_statistic]