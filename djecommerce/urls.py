from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)



def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    if request.user.profile.account_type == "Business":
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            
            quantity = 25,
            ordered=False
        )
    else:
        order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
            
        quantity = 1,
        ordered=False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            if request.user.profile.account_type == "Business":
                order_item.quantity += 25
                order_item.save()
                messages.info(request, "This item quantity was updated.")
            else:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            order.items.add(order_item) 
            messages.info(request, "This item was added to your cart.")
            return redirect("core:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
        user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "For item was added to your cart.")
        return redirect("core:order-summary")

