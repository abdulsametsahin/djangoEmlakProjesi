class HotelImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(MPTTModelAdmin):
    list_display = ['title', 'status', ]
    list_filter = ['status']
class HotelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'star', 'image_tag', 'city', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [HotelImageInline]
    prepopulated_fields = {'slug': ('title',)}
