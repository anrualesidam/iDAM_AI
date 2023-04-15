from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_app.urls')),
    path('SignIn/', include('django.contrib.auth.urls')),   #Django auth systemm
    path('Welcome/',include('users_app.urls'), name = 'users') #Page to be redirected when logged in
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
