from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'blogger.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='/blog/', permanent=True),
        name='home'),
    url(r'^blog/', include('blog.urls',
                           namespace='blog',
                           app_name='blog')),
    url(r'accounts/login/$', views.LoginView.as_view(),
        name='login'),
    url(r'accounts/logout/$', views.LogoutView.as_view(permanent=False),
        name='logout'),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

