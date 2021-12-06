from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from .models import Item, OrderItem, Order
from django.utils import timezone
from django.views.generic import ListView,DetailView

def products(request):
    context={
        'items':Item.objects.all()
    }
    return render(request,"products.html",context)

def checkout(request):
    return render(request,"checkout.html")



class HomeView(ListView):
    model=Item
    template_name="home.html"

class ItemDetailView(DetailView):
    model=Item
    template_name="products.html"

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(
        item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            #messages.info(request, "This item quantity was updated.")
           # return redirect("core:order-summary")
        else:
            ordered_date = timezone.now()
            order=Order.objects.create(user=request.user,ordered_date=ordered_date)
            order.items.add(order_item)
           # messages.info(request, "This item was added to your cart.")
            #return redirect("core:order-summary")
            return redirect("core:products",slug=slug)

  #  else:
       # ordered_date = timezone.now()
       # order = Order.objects.create(
           # user=request.user, ordered_date=ordered_date)
        #order.items.add(order_item)
       # messages.info(request, "This item was added to your cart.")
        #return redirect("core:order-summary")