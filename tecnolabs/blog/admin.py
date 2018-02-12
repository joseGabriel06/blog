from django.contrib import admin

from .models import Post

class AdminPost(admin.ModelAdmin):
	list_display  = ['title','author', 'created_date']
	list_filter   = ['author']
	search_fields = ['author']
	class Meta:
		model = Post
		
admin.site.register(Post,AdminPost)

# Register your models here.
