
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'employee', views.employeeViewSet)
router.register(r'student', views.studentViewSet)
router.register(r'teacher', views.teacherViewSet)
router.register(r'user', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),#api url
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
