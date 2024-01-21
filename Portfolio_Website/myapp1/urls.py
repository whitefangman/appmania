from django.conf import settings
from django.urls import path, re_path
from . import views  # Import the views module

urlpatterns = [
    path('land/', views.land_view, name='land_view'),
    path('home/', views.home_view, name='home_view'),

]

# Include static and media URL patterns for debug mode
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
