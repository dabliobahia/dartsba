from django.contrib import admin
from django.utils.timezone import now
from dartsba.players.models import Players


class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'last', 'email', 'nickname', 'subscribed_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'nickname')
    list_filter = ('created_at',)

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'Subscribed today?'
    subscribed_today.boolean = True


admin.site.register(Players, PlayerModelAdmin)
