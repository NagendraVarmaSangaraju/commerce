from django.urls import path
from . import views
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    Home1View,
    OfficeView,
    # LRView,
    SearchResultsView,
    
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

    path('home1/',Home1View.as_view(),name='home1'),
    path('office/',OfficeView.as_view(),name='office'),
    # path('livingroom/',LRView.as_view(),name='livingroom'),
    path('contact-us/',views.contact_us,name='contact_us'),
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    path('locateus/',views.locateus,name='locateus'),
    path('aboutus/',views.aboutus,name='aboutus'),
]
