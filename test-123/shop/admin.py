from django.contrib import admin
from shop.models import Category, Item, Tag

class ItemInLine(admin.TabularInline):
    model = Item
    extra = 1
    
class ItemTagInLine(admin.TabularInline):
    model = Tag.items.through
    extra = 1
    
class TagInLine(admin.TabularInline):
    model = Item.tags.through
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    ordering = ['name']
    inlines = [ItemInLine]
    
class ItemAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['price']
    list_display = ['id', 'name', 'price']
    autocomplete_fields = ['category']
    fields = ['name', 'price', 'category', 'description']
    inlines = [TagInLine]
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    ordering = ['name']
    inlines = [ItemTagInLine]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)
