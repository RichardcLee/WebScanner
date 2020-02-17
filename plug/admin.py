from django.contrib import admin
from .models import PlugType, JsonPlug, ScriptPlug


# Register your models here.

class PlugAdmin(admin.ModelAdmin):
    pass


admin.site.register(PlugType, PlugAdmin)
admin.site.register(JsonPlug, PlugAdmin)
admin.site.register(ScriptPlug, PlugAdmin)
