from django.contrib import admin

from .models import Post

#class PostAdmin(admin.ModelAdmin):
 #   list_dispaly=('title','author','status','created_on',)
  #  list_filter=('status',)
   # search_fields=['title','content']

admin.site.register(Post)
#admin.site.register(Post, PostAdmin)
# Register your models here.