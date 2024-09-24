from django.urls import path

from trading_patterns.trading.views import index, get_crypto_data, plot_graph

urlpatterns = [
    path('', index, name='index'),
    path('api/crypto/<str:crypto_id>/', get_crypto_data, name='get_crypto_data'),
    path('graph/', plot_graph, name='plot_graph')
]