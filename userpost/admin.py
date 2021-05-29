from django.contrib import admin
from userpost.models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","events_date_time","location","created_at")
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
