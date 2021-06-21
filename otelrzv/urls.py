from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('home/', include('home.urls')),
    path('hotel/', include('hotel.urls')),
    path('user/', include('user.urls')),
    path('reserve/', include('reserve.urls')),
    path('hotel/<int:id>/<slug:slug>/', views.hotel_detail, name='hotel_detail'),

]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "HOTEL RESERVATION ADMIN"
admin.site.site_title = "HOTEL RESERVATION ADMIN"
admin.site.site_index_title = "Welcome To Hotel Reservation Admin"
