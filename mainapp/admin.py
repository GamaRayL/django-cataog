from django.contrib import admin

from mainapp.models import Category, Product, Post, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'body',
                    'img_preview', 'create_date', 'is_published', 'view_count',)
    list_filter = ('title', 'create_date', 'is_published', 'view_count',)
    search_fields = ('title', 'body',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_name', 'version_number', 'is_current_version',)
    list_filter = ('version_number',)
    search_fields = ('product',)
