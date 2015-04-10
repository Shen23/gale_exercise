from django.contrib import admin

# Register your models here.
from .models import Article, Opt_images
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


admin.site.register(Opt_images)


class Opt_images_InLine(admin.StackedInline):
	model = Opt_images
	extra = 3

class ArticleAdmin(admin.ModelAdmin):

    inlines = [Opt_images_InLine]

    list_display = ['id', 'title', 'author', 'pub_date']

    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

# admin.site.register(Article, MarkdownModelAdmin)
admin.site.register(Article, ArticleAdmin)
