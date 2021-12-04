from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from frontend.views import IndexView
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api import views

router = routers.DefaultRouter()
router.register(r'Users', views.UserViewSet)
router.register(r'Groups', views.GroupViewSet)
router.register(r'Person', views.PersonViewSet)
router.register(r'Direction', views.DirectionViewSet)
router.register(r'Medic', views.MedicViewSet)
router.register(r'Cite', views.CiteViewSet)
router.register(r'Diagnosis', views.DiagnosisViewSet)
router.register(r'Diet', views.DietViewSet)
router.register(r'Allergy', views.AllergyViewSet)
router.register(r'Record', views.RecordViewSet)
router.register(r'Laboratory', views.LaboratoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
