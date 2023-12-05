from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("bloc.urls")),
    path('', include("things.urls")),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('users.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

