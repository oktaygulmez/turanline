from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenBlacklistView

from products.views import (ProductCategoriesViewSet, ProductSubTypesViewSet,
                            ProductsViewSet, ProductTypesViewSet,
                            ManufacturerCountryViewSet)
from users.views import (CartProductsViewSet, ReviewsViewSet,
                         TokenObtainPairViewDoc, TokenRefreshViewDoc,
                         TokenVerifyViewDoc, UserViewSet, ProviderViewSet,
                         CustomerViewSet, SuperAdminNewsViewSet)

router = DefaultRouter()

router.register(r'catalog', ProductsViewSet)

router.register(r'categories', ProductCategoriesViewSet)
router.register(r'types', ProductTypesViewSet)
router.register(r'subtypes', ProductSubTypesViewSet)


router.register(r'reviews', ReviewsViewSet)
router.register(r'cart', CartProductsViewSet)
router.register(r'users', UserViewSet)

router.register(r'country', ManufacturerCountryViewSet)
router.register(r'provider', ProviderViewSet)
router.register(r'customer', CustomerViewSet)

router.register(
    r'superusernews',
    SuperAdminNewsViewSet
)

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'api/',
        include(router.urls)
    ),
    path(
        '__debug__/',
        include('debug_toolbar.urls')
    ),
    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    path(
        'api/token/',
        TokenObtainPairViewDoc.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'api/token/refresh/',
        TokenRefreshViewDoc.as_view(),
        name='token_refresh',
    ),
    path(
        'api/token/verify/',
        TokenVerifyViewDoc.as_view(),
        name='token_verify',
    ),
    path(
        'api/token/logout/',
        TokenBlacklistView.as_view(),
        name='token_blacklist',
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
