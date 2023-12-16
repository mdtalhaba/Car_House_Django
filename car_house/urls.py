from django.contrib import admin
from django.urls import path, include
from . views import home, DetailsCarView, buy_car
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_validation.urls')),
    path('brand/<slug:brand_slug>', home, name='brand_slug'),
    path('', home, name='home'),
    path('car_details/<int:id>', DetailsCarView.as_view(), name='car_details'),
    path('car_details/buy/<int:car_id>', buy_car, name='buy_car'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
