from django.urls import path
from .views import RoomListView, BookingListView, RoomDetailView, CancelBookingView

app_name = 'hotel'

urlpatterns = [
    path('', RoomListView, name='RoomListView'),
    path('rooms/booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('rooms/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(),
         name='CancelBookingView')

]
