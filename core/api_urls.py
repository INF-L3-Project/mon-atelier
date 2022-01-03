from rest_framework.routers import DefaultRouter
from core.api_views import (OrderViewSet, ClientViewSet, ModeleViewSet, OrderItemViewSet,
	CategoryViewSet, WorkerViewSet,AuthViewSet, MesureViewSet, ArticleViewSet, WorkshopViewSet
	)

router = DefaultRouter()
router.register('workshops', WorkshopViewSet, basename='workshops')
router.register('categories', CategoryViewSet, basename='categories')
router.register('modeles', ModeleViewSet, basename='modeles')
router.register('orders', OrderViewSet, basename='orders')
router.register('clients', ClientViewSet, basename='clients')
router.register('mesures', MesureViewSet, basename='mesures')
router.register('articles', ArticleViewSet, basename='articles')
router.register('order_items', OrderItemViewSet, basename='order_items')
router.register('workers', WorkerViewSet, basename='workers')
router.register('auth', AuthViewSet, basename='auth')


urlpatterns = []

urlpatterns += router.urls