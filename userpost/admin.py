from django.contrib import admin
from userpost.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","events_date_time","location", "date_posted")
admin.site.register(Post, PostAdmin)
# admin.site.register(Comment)
