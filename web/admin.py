from django.contrib import admin
from .models import Post, Comment, PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "category", "date_created")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("date_created", "comment")


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
