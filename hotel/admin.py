class HotelImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(MPTTModelAdmin):
    list_display = ['title', 'status', ]
    list_filter = ['status']
