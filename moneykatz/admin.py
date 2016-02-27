from django.contrib import admin
from moneykatz.models import Category, File


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'document')


class CategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}
        list_display = ('name', 'slug', 'views')

admin.site.register(Category, CategoryAdmin)
admin.site.register(File, FileAdmin)
