from django.contrib import admin
# from django.contrib.admin.filters import ListFilter
from .models import Category, Post, Contact


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display= ("image_tag","title","discription")
    search_fields= ('title',)
    


admin.site.register(Category, CategoryAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display= ("image_tag","Post_title","add_date")
    search_fields= ('Post_title',)
    list_filter= ('cat',)
    class Media():
        js= ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js' 'https://cdn.scaleflex.it/plugins/filerobot-image-editor/3.12.17/filerobot-image-editor.min.js')


admin.site.register(Post, PostAdmin )


class ContactAdmin(admin.ModelAdmin):
     list_display= ("name","email", "timeStamp")
     filter= ('timeStamp')
     
    


admin.site.register(Contact, ContactAdmin )