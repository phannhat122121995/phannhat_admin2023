from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.urls import reverse

from Order.models import Order, ProductTotalInCart
from manage_index.models import UserProfile, Product, video_list, couse_title
from django.contrib.auth.hashers import make_password

@login_required
def indexprofile(request):
    current_user = request.user
    try:
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {
            'profile': profile,
            'current_user': current_user,
        }
        return render(request, 'index/update/user/detail_user.html', context)
    except ObjectDoesNotExist:
        # Xử lý khi UserProfile không tồn tại
        # Ví dụ: gán profile một giá trị mặc định hoặc redirect đến trang khác
        profile = None
        context = {
            'profile': profile,
            'current_user': current_user,
        }
        return render(request, 'index/update/user/detail_user.html', context)


@login_required
def update_pr(request, id_user):
    current_user = request.user
    try:
        get_pro = UserProfile.objects.get(user_id=id_user)
    except:
        return HttpResponseRedirect(reverse('create_profile'))
    if request.method == 'POST' and request.FILES:
        first = request.POST['first_name']
        last = request.POST['last']
        mail = request.POST['mail']
        phone = request.POST['phone']
        country = request.POST['country']
        city = request.POST['city']
        address = request.POST['address']
        image = request.FILES['image']
        get_pro.phone = phone
        get_pro.country =country
        get_pro.city = city
        get_pro.address =address
        get_pro.image = image
        get_pro.save()
        current_user.first_name = first
        current_user.last_name = last
        current_user.email = mail
        current_user.save()
        messages.success(request, "Bạn đã cập nhập thành công!!!")
    if request.method == 'POST':
        first = request.POST['first_name']
        last = request.POST['last']
        mail = request.POST['mail']
        phone = request.POST['phone']
        country = request.POST['country']
        city = request.POST['city']
        address = request.POST['address']
        get_pro.phone = phone
        get_pro.country = country
        get_pro.city = city
        get_pro.address = address
        get_pro.save()
        current_user.first_name = first
        current_user.last_name = last
        current_user.email = mail
        current_user.save()
        messages.success(request, "Bạn đã cập nhập thành công!!!")

    context = {'updatepr': get_pro,
               'current_user': current_user,
               }
    return render(request, 'index/update/user/update_profile.html', context)

    # return render(request, 'index/user/update_profile.html',context)


@login_required
def user_oder(request):
    current_user = request.user
    order = Order.objects.filter(user_id=current_user.id)
    context = {'order': order,
               'current_user': current_user,
               }
    return render(request, 'index/update/user/user_oder.html', context)
    # return render(request, 'index/user/user_order.html', context)


@login_required
def detail_oder(request,id_oder):
    orderitems = ProductTotalInCart.objects.filter(order_id=id_oder)
    get_code = Order.objects.get(id=id_oder)
    total = 0
    for rs in orderitems:
        total += rs.product.price * rs.quantity
    context = {
        'orderitems':orderitems,
        'total':total,
        'get_code':get_code,
    }
    return render(request, 'index/update/user/detail_oder.html', context)
    # return render(request, 'index/user/detail_order.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        user = authenticate(username=request.user.username, password=old_password)
        a = request.user.username
        print("pass lỗi dây")
        print(user)
        print(old_password)
        if user is not None:
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)  # Giữ phiên đăng nhập của người dùng
                return redirect('indexprofile')  # Chuyển hướng sau khi thay đổi mật khẩu thành công
            else:
                print("pass lỗi")
                messages.warning(request, "Mật mới không chính xác! khuyến cáo đặt ít nhất 8 ky tự gồm viết hoa ký tự đặt biệt")
                return render(request, 'index/update/user/update_password.html')
                # return render(request, 'auth/update_password.html')
        else:
            messages.warning(request, "Mật khẩu củ không chính xác!")
            return render(request, 'index/update/user/update_password.html')
    return render(request, 'index/update/user/update_password.html')


@login_required
def logout_func(request):
    logout(request)
    return render(request, 'index/update/index.html')


def create_profile(request):
    current_user = request.user
    if request.method == 'POST' and request.FILES:
        first = request.POST['first_name']
        last = request.POST['last']
        mail = request.POST['mail']
        phone = request.POST['phone']
        country = request.POST['country']
        city = request.POST['city']
        address = request.POST['address']
        image = request.FILES['image']
        data = UserProfile()
        data.user_id = current_user.id
        data.phone = phone
        data.country = country
        data.city = city
        data.address = address
        data.image = image
        data.save()
        current_user.first_name = first
        current_user.last_name = last
        current_user.email = mail
        current_user.save()
        messages.success(request, "Bạn đã cập nhập thành công!!!")
    if request.method == 'POST':
        first = request.POST['first_name']
        last = request.POST['last']
        mail = request.POST['mail']
        phone = request.POST['phone']
        country = request.POST['country']
        city = request.POST['city']
        address = request.POST['address']
        data = UserProfile()
        data.user_id = current_user.id
        data.phone = phone
        data.country = country
        data.city = city
        data.address = address
        # data.image = image
        data.save()
        current_user.first_name = first
        current_user.last_name = last
        current_user.email = mail
        current_user.save()
        messages.success(request, "Bạn đã cập nhập thành công!!!")
        return HttpResponseRedirect(reverse('indexprofile'))

    context = {
               'current_user': current_user,
               }
    return render(request, 'index/update/user/create_profile.html', context)
    # return render(request, 'index/user/create_profile.html', context)



@login_required
def detail_pro_bought(request, id):
    current_user = request.user
    try:
        # get_status_s = Order.objects.get(status="Completed", user=current_user.id)
        get_status_s = Order.objects.filter(status="Completed", user=current_user.id).first()
    except:
        context = {
            'show_message': "Hãy chờ đơn hàng được thanh toán"
        }
        return render(request, 'index/update/user/detail_pro_bougth.html', context)

    if get_status_s.id:
        list_ = []
        a = Order.objects.filter(status="Completed", user=current_user.id)
        for rs in a:
            list_.append(rs.id)
        print(list_)
        getidd = ProductTotalInCart.objects.filter(order_id__in=list_)
        for rs in getidd:
            print(id)
            a = rs.product_id
            if id == a:
                print("có một sản phẩm đã mua", a)
                get_list_video = couse_title.objects.filter(product_id=id).order_by('ordinal_numbers')
                context = {
                    'get_list_video': get_list_video,
                }
                return render(request, 'index/update/user/detail_pro_bougth.html', context)
        context = {
            'show_message': "Hãy chờ đơn hàng được thanh toán"
        }
        return  render(request, 'index/update/user/detail_pro_bougth.html', context)


        # get_list_video = couse_title.objects.filter(product_id=id).order_by('ordinal_numbers')
        # get_oder_detail = ProductTotalInCart.objects.filter(order_id=get_status_s.id)
        # get_id = []
        # for rs in get_oder_detail:
        #     get_id.append(rs.product.id)
        # print("------------")
        # print(get_id)
        # print("------------")
        # if id in get_id:
        #     get_pro = Product.objects.get(id=id)
        #     get_videos = couse_title.objects.filter(product_id=id)
        #     get_list_video = couse_title.objects.filter(product_id=id).order_by('ordinal_numbers')
        #     context = {
        #         'get_pro': get_pro,
        #         'get_status_s': get_status_s,
        #         'get_videos': get_videos,
        #         'get_list_video': get_list_video,
        #     }
        #     return render(request, 'index/update/user/detail_pro_bougth.html', context)

    #     else:
    #         context = {
    #             'show_message': "Hãy chờ đơn hàng được thanh toán"
    #         }
    #         return render(request, 'index/update/user/detail_pro_bougth.html', context)
    # context = {
    #     'show_message': "Hãy chờ đơn hàng được thanh toán"
    # }
    # return render(request, 'index/update/user/detail_pro_bougth.html', context)
