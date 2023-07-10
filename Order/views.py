from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json
# Create your views here.
from django.utils.crypto import get_random_string

from Order.models import ProductCart, ProductTotalInCart, Order
from manage_index.models import Product, UserProfile


def add_to_cart(request, product_id):
    url = request.META.get('HTTP_REFERER')  # get last url
    quantity = int(request.POST.get('quantity', 1))  # Chuyển đổi quantity sang kiểu số nguyên
    print("---------")
    print(product_id)

    if 'cart' not in request.session:
        request.session['cart'] = {}  # Khởi tạo giỏ hàng nếu chưa tồn tại

    cart = request.session['cart']

    if isinstance(cart, int):  # Kiểm tra nếu giỏ hàng là một số nguyên
        cart = {}  # Khởi tạo giỏ hàng mới

    # Kiểm tra xem sản phẩm đã tồn tại trong giỏ hàng chưa
    if str(product_id) in cart:
        cart[str(product_id)] += int(quantity)  # Cộng thêm số lượng sản phẩm
    else:
        cart[str(product_id)] = int(quantity)  # Thêm sản phẩm mới vào giỏ hàng

    request.session['cart'] = cart  # Lưu giỏ hàng vào session


    # # Kiểm tra xem session có tồn tại hay không
    # if 'cart' not in request.session:
    #     request.session['cart'] = {}  # Khởi tạo giỏ hàng nếu chưa tồn tại
    #
    # cart = request.session['cart']
    # cart[str(product_id)] = cart.get(str(product_id), 0) + int(quantity)  # Thêm sản phẩm vào giỏ hàng
    #
    # request.session.modified = True  # Đánh dấu session đã thay đổi



    # # Kiểm tra xem giỏ hàng đã tồn tại trong phiên chưa
    # if 'cart' not in request.session:
    #     request.session['cart'] = []
    #
    # # Kiểm tra xem giỏ hàng đã tồn tại trong phiên chưa
    # if 'cart' not in request.session:
    #     request.session['cart'] = {}
    #
    # # Kiểm tra xem giỏ hàng đã lưu trữ dưới dạng dict chưa
    # if not isinstance(request.session['cart'], dict):
    #     request.session['cart'] = {}
    #
    # # Kiểm tra xem sản phẩm đã tồn tại trong giỏ hàng chưa
    # if product_id in request.session['cart']:
    #     # Sản phẩm đã tồn tại, cộng dồn số lượng
    #     request.session['cart'][product_id] += int(quantity)
    # else:
    #     # Sản phẩm chưa tồn tại, thêm mới
    #     request.session['cart'][product_id] = int(quantity)
    #
    # print(request.session['cart'])  # In giá trị của biến cart
    # print("----------------giỏ hàng--------------------------")
    #
    # print(product_id)
    # print(type(product_id))
    # if quantity is not None:
    #     quantity = int(quantity)
    # else:
    #     print("trường số lượng lỗi")
    # print(quantity)
    # quantity = int(quantity)
    # print(type(quantity))
    # # Xử lý khi giá trị 'quantity' không tồn tại
    # # Có thể đặt một giá trị mặc định cho quantity hoặc thông báo lỗi
    # print("------------------------------------------")
    # if 'cart' not in request.session:
    #     request.session['cart'] = {}
    #
    # cart = request.session['cart']
    # if product_id in cart:
    #     # Nếu sản phẩm đã tồn tại trong giỏ hàng, chỉ cập nhật số lượng
    #     cart[product_id] += quantity
    # else:
    #     # Nếu sản phẩm chưa tồn tại trong giỏ hàng, thêm mới
    #     # Nếu sản phẩm chưa tồn tại trong giỏ hàng, thêm mới
    #     cart[product_id] = quantity
    #
    # request.session.modified = True  # Đánh dấu session đã được thay đổi


    return HttpResponseRedirect(url)


def updateid(request):
    quantity = int(request.POST.get('new_quantity'))
    updateid = int(request.POST.get('cart_id'))
    if 'cart' in request.session:
        cart = request.session['cart']
        print(cart)
        print(quantity)
        print("----------check cart--------")
        if str(updateid) in cart:
            print("----------check product_id--------")
            # Kiểm tra số lượng mới, không cho phép giá trị âm
            if quantity > 0:
                cart[str(updateid)] = quantity
                request.session.modified = True  # Đánh dấu session đã được thay đổi
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Số lượng sản phẩm phải lớn hơn 0.'})
        else:
            return JsonResponse({'success': False, 'message': 'Sản phẩm không tồn tại trong giỏ hàng.'})
    else:
        return JsonResponse({'success': False, 'message': 'Giỏ hàng không tồn tại.'})


def cart(request):
    # cart = request.session.get('cart', {})
    # print("--------show cart----------")
    # print(cart)  # exam ({'1': 10, '2': 19})
    # print("--------1----------")
    # cart = {key: value for key, value in cart.items() if value is not None}
    # if 'null' in cart:
    #     del cart['null']
    # request.session.modified = True  # Đánh dấu session đã được thay đổi
    # ids = list(cart.keys())
    # ids_int = [int(id) for id in ids]
    # print(ids_int)  # (1,2)
    # print("--------2----------")
    # result = []  # [[1, 10], [2, 19]]
    cart = request.session.get('cart', {})
    # print("--------show cart----------")
    # print(cart)  # exam ({'1': 10, '2': 19})
    # print("--------1----------")
    if isinstance(cart, dict):
        cart = {key: value for key, value in cart.items() if value is not None}
    else:
        # Xử lý khi cart không phải là dictionary
        # Có thể gán cart thành một dictionary trống hoặc thực hiện xử lý phù hợp với trường hợp này
        cart = {}
    if 'null' in cart:
        del cart['null']
    request.session.modified = True  # Đánh dấu session đã được thay đổi
    ids = list(cart.keys())
    ids_int = [int(id) for id in ids]
    print(ids_int)  # (1,2)
    result = []  # [[1, 10], [2, 19]]

    for key, value in cart.items():
        result.append([int(key), int(value)])


    get_p = Product.objects.all().filter(id__in=list(ids_int))
    sum_price = 0
    for r in get_p:
        v_id = r.id
        filtered_list = list(filter(lambda x: x[0] == v_id, result))
        if len(filtered_list) > 0:
            r.soluong = filtered_list[0][1]
            r.tong = r.soluong * r.price
            sum_price = sum_price + r.tong
            print("Đã tìm thấy phần tử:", filtered_list[0][1])
        else:
            print("Không tìm thấy phần tử có giá trị đầu là", v_id)
        print("-------------------------------------")
        # filtered_list = list(filter(lambda x: x[0] == v_id, result)
    context = {
        'cart': cart,
        'get_p': get_p,
        'sum_price': sum_price,
    }
    return render(request, "index/cart/cart.html", context)

def remove_from_cart(request, product_id):
    print("-----===---------")
    if 'cart' in request.session:
        cart = request.session['cart']
        if str(product_id) in cart:
            del cart[str(product_id)]
            request.session.modified = True  # Đánh dấu session đã được thay đổi

    return redirect('cart')  # Chuyển hướng đến trang giỏ hàng


@login_required
def checkout(request):
    current_user = request.user
    try:
        get_pro = UserProfile.objects.get(user_id=current_user.id)
    except:
        get_pro = ""
    cart = request.session.get('cart', {})
    if isinstance(cart, dict):
        cart = {key: value for key, value in cart.items() if value is not None}
    else:
        # Xử lý khi cart không phải là dictionary
        # Có thể gán cart thành một dictionary trống hoặc thực hiện xử lý phù hợp với trường hợp này
        cart = {}
    if 'null' in cart:
        del cart['null']
    request.session.modified = True  # Đánh dấu session đã được thay đổi
    ids = list(cart.keys())
    ids_int = [int(id) for id in ids]
    result = []  # [[1, 10], [2, 19]]
    for key, value in cart.items():
        result.append([int(key), int(value)])

    get_p = Product.objects.all().filter(id__in=list(ids_int))
    sum_price = 0
    for r in get_p:
        v_id = r.id
        filtered_list = list(filter(lambda x: x[0] == v_id, result))
        if len(filtered_list) > 0:
            r.soluong = filtered_list[0][1]
            r.tong = r.soluong * r.price
            sum_price = sum_price + r.tong
    context = {
        'cart': cart,
        'get_p': get_p,
        'sum_price': sum_price,
        'get_pro': get_pro,
    }
    return render(request, "index/cart/checkout.html", context)


def orderproduct(request):
    current_user = request.user

    cart = request.session.get('cart', {})
    print(cart)  # exam ({'1': 10, '2': 19})
    if isinstance(cart, dict):
        cart = {key: value for key, value in cart.items() if value is not None}
    else:
        # Xử lý khi cart không phải là dictionary
        # Có thể gán cart thành một dictionary trống hoặc thực hiện xử lý phù hợp với trường hợp này
        cart = {}
    if 'null' in cart:
        del cart['null']
    request.session.modified = True  # Đánh dấu session đã được thay đổi
    ids = list(cart.keys())
    ids_int = [int(id) for id in ids]
    result = []  # [[1, 10], [2, 19]]
    for key, value in cart.items():
        result.append([int(key), int(value)])

    get_p = Product.objects.all().filter(id__in=list(ids_int))
    sum_price = 0
    for r in get_p:
        v_id = r.id
        filtered_list = list(filter(lambda x: x[0] == v_id, result))
        if len(filtered_list) > 0:
            r.soluong = filtered_list[0][1]
            r.tong = r.soluong * r.price
            sum_price = sum_price + r.tong
    if get_p:
        if request.method == 'POST':
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            address = request.POST['address']
            address2 = request.POST['address2']
            ordercode = get_random_string(15).upper()  # random cod
            data = Order()
            data.user = current_user
            data.Name = lastName
            data.Address = address
            data.code = ordercode
            data.total = sum_price
            data.save()
            for rs in get_p:
                v_id = rs.id
                filtered_list = list(filter(lambda x: x[0] == v_id, result))
                if len(filtered_list) > 0:
                    rs.soluong = filtered_list[0][1]
                    rs.tong = rs.soluong * rs.price
                    sum_price = sum_price + rs.tong

                    detail = ProductTotalInCart()

                    detail.order_id = data.id  # Order Id
                    detail.product_id = rs.id
                    detail.quantity = filtered_list[0][1]
                    detail.price = rs.soluong * rs.price
                    detail.save()
                    request.session['cart'] = 0
            context = {
                'ordercode': ordercode,
            }
            return render(request, "index/cart/oder_complated.html", context)

    return render(request, "index/cart/checkout.html")


def cart_item_count(request):
    cart = request.session.get('cart', {})
    item_count = len(cart)
    return JsonResponse({'count': item_count})


