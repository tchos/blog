from django.contrib import admin

# Register your models here.
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_on', 'last_update', )
    list_editable = ('published', )

admin.site.register(BlogPost, BlogPostAdmin)
