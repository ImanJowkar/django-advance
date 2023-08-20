from django.contrib import admin
from blogs.models import Post, Category


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'status', 'created_at', 'updated_at', 'published_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
