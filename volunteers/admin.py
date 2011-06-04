from django.contrib import admin

from volunteers.models import Profile, Call, Skill, Resource


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(Profile)
admin.site.register(Call)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Resource, ResourceAdmin)