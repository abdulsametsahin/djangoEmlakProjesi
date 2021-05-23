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

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'hotel', 'image_tag']
    readonly_fields = ('image_tag',)
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_hotels_count', 'related_hotels_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Hotel,
            'category',
            'hotels_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                                                Hotel,
                                                'category',
                                                'hotels_count',
                                                cumulative=False)
        return qs

    def related_hotels_count(self, instance):
        return instance.hotels_count

    related_hotels_count.short_description = 'Related hotels (for this specific category)'

    def related_hotels_cumulative_count(self, instance):
        return instance.hotels_cumulative_count

    related_hotels_cumulative_count.short_description = 'Related hotels (in tree)'
