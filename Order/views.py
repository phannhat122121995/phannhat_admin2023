from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from Order.models import ProductCart


def cart(request):
    return render(request, "index/cart/cart.html")


def addtocart(request):

    if 'cart' not in request.session:
        request.session['cart'] = []
    if request.user.is_authenticated:
        cart = (request.session['cart'])
        if request.method == "POST":
                data = json.loads(request.body)
                if data==0:
                    return HttpResponse(len(cart))
                else:
                    cart.append(int(data))
                    request.session['cart']=cart
                #catalog is the name of the main pagedata

        return HttpResponse(len(cart))
    else:

        return HttpResponse('0')


    # url = request.META.get('HTTP_REFERER')  # get last url
    # idproduct = request.POST['idproduct']
    # current_user = request.user  # Access User Session information
    # checkproduct = ProductCart.objects.filter(product_id=idproduct, user_id=current_user.id)
    # if checkproduct:
    #     control = 1  # The product is in the cart
    #     print("sản phẩm này đã có")
    # else:
    #     print("sản phẩm chưa có trong giỏ hàng")
    #     control = 0  # The product is not in the cart"""
    # if control == 0 and request.method == 'POST' and 'btnform2' in request.POST:
    #     data = ProductCart()
    #     idproduct = request.POST['idproduct']
    #     # something
    #     data.save()
    #     return HttpResponseRedirect(url)
    # else:
    #     checkproduct = ProductCart.objects.filter(product_id=idproduct).first()
    #     update_cart = ProductCart.objects.get(id=checkproduct.id)
    #     if checkproduct:
    #         control = 1  # The product is in the cart
    #         print("sản phẩm này đã có")
    #     else:
    #         print("sản phẩm chưa có trong giỏ hàng")
    #         control = 0  # The product is not in the cart"""
    #     if control == 0 and request.method == 'POST' and 'btnform2' in request.POST:
    #         data = ProductCart()
    #         idproduct = request.POST['idproduct']
    #         quantity = request.POST['quantity']
    #         data.user = current_user
    #         data.product_id = idproduct
    #         data.quantity = quantity
    #         data.save()
    #         return HttpResponseRedirect(url)
    #     else:
    #         checkproduct = ProductCart.objects.filter(product_id=idproduct).first()
    #         update_cart = ProductCart.objects.get(id=checkproduct.id)
    #         quantity = request.POST['quantity']
    #         quantity = int(quantity)
    #         totalql = quantity + update_cart.quantity
    #         update_cart.quantity = totalql
    #         update_cart.save()
    #         return HttpResponseRedirect(url)
    #     update_cart.save()
    #     return HttpResponseRedirect(url)