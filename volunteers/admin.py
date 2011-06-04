from django.contrib import admin

from volunteers.models import Profile, Call, Skill, Resource


class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CallAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Call, CallAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Resource, ResourceAdmin)