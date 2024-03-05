from django.urls import path,include
from CarDekhoApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("showroom",views.Showroom_Viewset, basename='showroom')




urlpatterns = [
    path('list/',views.car_list_view,name='car_list'),
    path('<int:pk>/',views.car_detail_view,name='card_detail_view'),
    path('',include(router.urls)),
    # path('showroom/',views.Showroom_View.as_view(),name='showroom_view'),
    # path('showroom/<int:pk>/',views.Showroom_Details.as_view(),name='showroom_details'),
    path('review/',views.ReviewList.as_view(),name='review_list'),
    path('review/<int:pk>/',views.ReviewDetails.as_view(),name='review_details'),
    
]
