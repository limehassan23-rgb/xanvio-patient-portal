from django.contrib import admin
from django.urls import path, include
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # CHANGE 'home' TO 'search_page' HERE:
    path('', views.search_page, name='search_page'), 
    
    path('', include('portal.urls')), 
]