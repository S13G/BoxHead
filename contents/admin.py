from django.contrib import admin

# Register your models here.
from contents.models import Content, BoxMap


class ContentAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


class BoxMapAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


admin.site.register(Content, ContentAdmin)
admin.site.register(BoxMap, BoxMapAdmin)
