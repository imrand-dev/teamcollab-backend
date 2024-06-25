from django.contrib import admin

from core.models import Project, Member


@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "description"]


@admin.register(Member)
class ProjectMemberModelAdmin(admin.ModelAdmin):
    list_display = ["uid", "role"]
