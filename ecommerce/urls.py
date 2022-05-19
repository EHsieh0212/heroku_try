"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin, auth       #auth協助使用者登入登出
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from eco import views as eco_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    #Home
    path('', eco_views.home, name='home'),
    

    #Calendar
    path('<str:user>/<int:year>/<str:month>', eco_views.a_calendar, name='calendar'),  #path:whole url / slug:hyphen-and_underscores_stuff / UUID: universally unique identifier

    #Auth
    #path('members/', include('django.contrib.auth.urls')),  #使用django urls system
    path('members/', include('members.urls')),
    re_path(r'^saml/', include('django_saml.urls')),
    


    #searchresult
    path('search/', eco_views.search_order, name = 'search_order'),
    path('second_page/<order_id>', eco_views.list_order, name = 'list_order'),

]

#urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


#Configure Admin Titles
admin.site.site_header = 'Ecommerce Admin'
admin.site.site_title = 'Ecommerce Title'