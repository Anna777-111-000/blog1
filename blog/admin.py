from django.contrib import admin

# Register your models here.
from .models import Author, Category, Post, Tag, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug') 
    search_fields = ('title', 'description') 
    prepopulated_fields = {'slug': ('title',)} 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'publication_date', 'is_published')
    list_filter = ('author', 'category', 'publication_date', 'is_published')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)  
    fieldsets = ( 
        ('Основная информация', {
            'fields': ('title', 'slug', 'category', 'content')
        }),
        ('Дополнительная информация', {
            'fields': ('picture', 'publication_date', 'is_published'),
            'classes': ('collapse',) 
        }),
    )
