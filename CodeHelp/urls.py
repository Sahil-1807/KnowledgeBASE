from django.contrib import admin
from django.urls import path
from Code import views as code_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',code_view.index,name='index'),
    path('category/<int:id>/',code_view.category,name='category'),
    path('tag/<int:id>/',code_view.tags,name='tags'),
    path('detail/<int:id>/',code_view.detail,name='detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)