from django.contrib import admin

# Register your models here.
from reserve.models import Reserve


class ReserveAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'room', 'checkin', 'checkout', 'status', 'create_at', 'user']
    list_filter = ['status']
    readonly_fields = ('checkin', 'checkout', 'user', 'hotel', 'room', 'id')


admin.site.register(Reserve, ReserveAdmin)
