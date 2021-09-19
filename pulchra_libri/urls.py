from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler400 = 'home.views.bad_request'
handler403 = 'home.views.permission_denied'
handler404 = 'home.views.page_not_found'
handler500 = 'home.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
