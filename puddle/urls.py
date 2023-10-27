from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
    path('buy/', include('buy.urls', namespace='buy')),
    
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


