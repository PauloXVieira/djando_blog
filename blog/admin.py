from django.contrib import admin
from blog.models import Tag, Category, Page, Post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_display_links = ["name"]
    search_fields = ["id", "name", "slug"]
    list_per_page = 10
    ordering = ["-id"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_display_links = ["name"]
    search_fields = ["id", "name", "slug"]
    list_per_page = 10
    ordering = ["-id"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ["id", "title", "slug"]
    list_display_links = ["title"]
    search_fields = ["id", "title", "slug"]
    list_per_page = 1
    ordering = ["-id"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ["id", "title", "is_published"]
    list_display_links = ["title"]
    search_fields = ["id", "title", "slug", "excerpt", "content"]
    list_editable = ["is_published"]
    ordering = ["-id"]
    readonly_fields = ["id", "created_at", "updated_at", "created_by", "updated_by"]
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ["category", "tags"]

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        obj.save()
