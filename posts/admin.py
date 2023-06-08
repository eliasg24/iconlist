"""Posts model."""

# Django
from django.contrib import admin

# Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'title', 'photo', "position")
    search_fields = ('title',)
    list_filter = ('created', 'modified')
