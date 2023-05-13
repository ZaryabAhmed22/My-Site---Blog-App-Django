from django.contrib import admin
from .models import Author, Blog, Tag
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "date", "tags")
    list_display = ("title", "author", "date")


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
admin.site.register(Tag)
