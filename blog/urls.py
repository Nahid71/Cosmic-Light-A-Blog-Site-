from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from post.views import (
    index, blog, post, search,
    post_create, post_update, post_delete, category
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='post-search'),
    path('create/', post_create, name='post-create'),
    path('post/<id>', post, name='post-details'),
    path('category/<cate>', category, name='category-list'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
