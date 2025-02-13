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
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name', 'bio')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author_name', 'publication_date', 'is_approved')
    list_filter = ('publication_date', 'is_approved')
    search_fields = ('author_name', 'author_email', 'content')
