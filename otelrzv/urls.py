from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('references/', views.references, name='references'),
    path('contact/', views.contact, name='contact'),
    path('home/', include('home.urls')),
    path('hotel/', include('hotel.urls')),
    path('user/', include('user.urls')),
    path('reserve/', include('reserve.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_hotels, name='category_hotels'),
    path('hotel/<int:id>/<slug:slug>/', views.hotel_detail, name='hotel_detail'),
    path('search/', views.hotel_search, name='hotel_search'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('faq/', views.faq, name='faq'),

]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "HOTEL RESERVATION ADMIN"
admin.site.site_title = "HOTEL RESERVATION ADMIN"
admin.site.site_index_title = "Welcome To Hotel Reservation Admin"
