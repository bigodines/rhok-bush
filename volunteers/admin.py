from django.contrib import admin

from volunteers.models import Skill, Resource


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


admin.site.register(Skill, SkillAdmin)
admin.site.register(Resource, ResourceAdmin)