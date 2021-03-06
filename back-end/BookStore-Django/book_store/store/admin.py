from django.contrib import admin
from store.models import BookModel, AuthorModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['__str__', 'quantity']
    list_editable = ['quantity']
    search_fields = ['name', 'author__full_name']
    list_filter = ['author']


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    pass

# admin.site.register(AuthorModel)