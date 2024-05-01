from django.contrib import admin
from .models import Blog, Category, Comment

# Register your models here.

class BloagAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    
    
    

#admin.site.register([Blog, Category])

admin.site.register(Blog, BloagAdmin)
admin.site.register(Category)
admin.site.register(Comment)

