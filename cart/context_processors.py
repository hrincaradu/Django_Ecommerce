from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    item_count = 0 
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            item_count=len(cart_items)
            # for cart_item in cart_items:
            #     print("- "+str(cart_item.quantity))
            #     item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0 
    return {'item_count':item_count}
