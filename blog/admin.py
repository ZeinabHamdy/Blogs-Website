from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User
from django.utils.timezone import now


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'updated_at',]
    readonly_fields = ['created_at', 'updated_at', 'published_at',]
    ordering = ['updated_at', 'published_at',]
    list_filter = ['author', 'status', 'created_at', 'updated_at',]
    search_fields = ['title', 'content',]
    raw_id_fields = ['author',]

    # handle published_at , status logic 
    def save_model(self, request, obj, form, change):
        if obj.status == 'published':
            if obj.published_at is None:  
                obj.published_at = now()
        elif change and 'status' in form.changed_data and obj.status == 'draft':
            # Prevent changing back to draft after publishing
            old_obj = Post.objects.get(pk=obj.pk)
            if old_obj.status == 'published':
                raise ValueError("You cannot change status back to draft once published.")
        
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
