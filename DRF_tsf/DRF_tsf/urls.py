
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'employee', views.employeeViewSet)
router.register(r'employee', views.studentViewSet)
router.register(r'employee', views.teacherViewSet)
router.register(r'user', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', )
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
