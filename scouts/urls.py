"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from scouts.views import Login_Error_redirect
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

main_urls = [
path('account/', include('accounts.urls', namespace='accounts'))
    
]


urlpatterns = [
#    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('leaders/scout_info/', admin.site.urls),
    path('leaders/', include('leaders.urls', namespace='leaders')),

    path('account/', Login_Error_redirect.as_view(), name="accounts_redirect"),
    path('', include('home.urls', namespace='home_page')),
    path('login/',  include('login.urls', namespace='login')),
    path('record_book/', include('record_book.urls', namespace='record_book')),
    path('<slug:slug>/', include(main_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()