from django.urls import path
from . import views

urlpatterns = [
    path("candlepost/", views.CandlePostListCreate.as_view(), name="candlepost-view-create"),
    path("candlepost/<int:pk>/", views.CandlePostRetriveUpdateDestroy.as_view(), name="update")
]