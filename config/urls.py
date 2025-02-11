from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, CustomLogoutView

router = DefaultRouter()
router.register(r'api/products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # namespace 추가
    # 인증 관련 URL 패턴
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/logged-out/', auth_views.TemplateView.as_view(template_name='registration/logged_out.html'), name='logged-out'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)