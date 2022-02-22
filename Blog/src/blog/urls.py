from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    search,
    LoginUser
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('login/', LoginUser.as_view(), name='account_login'),
    path('logout/',include('allauth.urls'), name='account_logout'),
    path('signup/',include('allauth.urls'), name='account_signup'),
    path('', PostListView.as_view(), name='list'),
    path('search/', search, name='search'),
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('<slug>/', PostDetailView.as_view(), name='detail-post'),
    path('<slug>/update', PostUpdateView.as_view(), name='update-post'),
    path('<slug>/delete', PostDeleteView.as_view(), name='delete-post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)