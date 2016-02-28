from django.contrib import admin
from moneykatz.models import Category, File, UserProfile


class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'document')


class CategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}
        list_display = ('name', 'slug', 'views')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('picture', 'spirit_animal_picture')


admin.site.register(Category, CategoryAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(UserProfile)
