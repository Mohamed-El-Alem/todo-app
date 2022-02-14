
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
     
    #path('', include('todoApp.urls')),
    #path('users/', include('django.contrib.auth.urls')),
    #path('users/', include('users.urls')),
    
    
    # path('users/', include('users.urls')),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
