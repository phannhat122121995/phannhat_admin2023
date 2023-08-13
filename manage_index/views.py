from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

import json
# Create your views here.
from django.urls import reverse

from Blog.models import CommentBlog, Blog
from Home.models import Messagers
from Order.models import Order, ProductTotalInCart
from manage_index.models import Category, Brands, Product, ProductForm, ImagssForm, Imagss, CreateUserForm, UserProfile, \
    CommentCourse, CommentPro, video_list, couse_title, cource_video


@login_required
def index_admin(request):
    if request.user.is_staff:
        current_user = request.user
        get_profile = UserProfile.objects.count()
        count_user = User.objects.count()
        count_product = Product.objects.count()
        count_blog = Blog.objects.count()
        get_coment = CommentBlog.objects.all().order_by('create_at')[:3]
        get_image = UserProfile.objects.get(user_id=current_user.id)
        context = {
            'get_profile':get_profile,
            'count_user': count_user,
            'count_product': count_product,
            'count_blog':count_blog,
            'get_coment': get_coment,
            'get_image': get_image,
        }
        return render(request, 'manager/index.html', context)
    return render(request, 'index/index.html')


@login_required
def addcategory(request,):
    if request.user.is_staff:
        # get_parents = Category.objects.all().filter(parent__isnull=True)
        get_parents = Category.objects.all()
        # slug = request.POST.get('texInputValue')
        if request.method == 'POST' and request.FILES:
            parent = request.POST['parent']
            # parentid = Category.objects.get(id=parent)
            title = request.POST['title']
            keywords = request.POST['keywords']
            description = request.POST['description']
            image = request.FILES['image']
            slug = request.POST['slug']
            status = request.POST['status']
            print("------đã chỉnh--------")
            print(parent)
            print(type(parent))
            print("-------end-------")
            if not title and image:
                messages.warning(request, "Bạn chưa điền vào form tiêu đề danh mục hoặc trường ảnh!!!")
            else:
                Category.objects.create(parent_id=parent, title=title, keywords=keywords, description=description, image=image, slug=slug, status=status)
                messages.success(request, "Bạn đã nhập danh mục thành công!!!")
        context = {
            'get_parents': get_parents,
        }
        return render(request, 'manager/add_category.html', context)
    return render(request, 'index/index.html')


@login_required
def index_category(request):
    if request.user.is_staff:
        get_list_categorys = Category.objects.all()
        print(get_list_categorys)
        context = {
            'get_list_categorys': get_list_categorys,
        }
        return render(request, 'manager/list_category.html', context)
    return render(request, 'index/index.html')


@login_required
def update_category(request, id):
    if request.user.is_staff:
        get_parents = Category.objects.all()
        update_cate = Category.objects.get(id=id)
        if request.method == 'POST' and request.FILES:
            parent_id = request.POST['parent']
            if parent_id:
                print("in ra parent_id")
                parent = Category.objects.get(id=parent_id)
            else:
                print(" khong in ra parent_id")
                # parent = Category.objects.get(id=1)
                parent = None
            title = request.POST['title']
            keywords = request.POST['keywords']
            description = request.POST['description']
            image = request.FILES['image']
            slug = request.POST['slug']
            status = request.POST['status']
            update_cate.parent = parent
            update_cate.title = title
            update_cate.keywords = keywords
            update_cate.description = description
            update_cate.slug = slug
            update_cate.status = status
            update_cate.image = image
            update_cate.save()
            messages.success(request, "Bạn đã sửa danh mục thành công!!!")
            # return render(request, 'manager/list_category.html')
            return HttpResponseRedirect(reverse('index_category'))
        elif request.method == 'POST':
            parent_id = request.POST['parent']
            if parent_id:
                print("in ra parent_id")
                parent = Category.objects.get(id=parent_id)
            else:
                print(" khong in ra parent_id")
                parent = None
            title = request.POST['title']
            keywords = request.POST['keywords']
            description = request.POST['description']
            image = update_cate.image
            slug = request.POST['slug']
            status = request.POST['status']
            update_cate.parent = parent
            update_cate.title = title
            update_cate.keywords = keywords
            update_cate.description = description
            update_cate.slug = slug
            update_cate.status = status
            update_cate.image = image
            update_cate.save()
            messages.success(request, "Bạn đã sửa danh mục thành công!!!")
            # return render(request, 'manager/list_category.html')
            return HttpResponseRedirect(reverse('index_category'))
        context = {
            'get_parents': get_parents,
            'update_cate': update_cate,
            'get_id': update_cate,
        }
        return render(request, 'manager/update_category.html', context)
    return render(request, 'index/index.html')


@login_required
def geturl(request):
    if request.user.is_staff:
        slug = request.GET.get('texInputValue')
        checkurl1 = Category.objects.filter(slug=slug).exists()
        if not checkurl1:
            test1 = "url tốt"
            check_status = 2
            response = {
                'test1': test1,
                'check_status': check_status,
            }
            return HttpResponse(json.dumps(response, default=str), content_type="application/json")
        else:
            test1 = "url đã tồn tại xin bạn hãy sửa lại, nút thêm sẻ kích hoạt"
            check_status = 1
            response = {
                'test1': test1,
                'check_status': check_status,
            }
            return HttpResponse(json.dumps(response, default=str), content_type="application/json")
    return render(request, 'index/index.html')


@login_required
def delete_category(request, id):
    if request.user.is_staff:
        delete_cate = Category.objects.filter(id=id)
        delete_cate.delete()
        return HttpResponseRedirect(reverse('index_category'))
    return render(request, 'index/index.html')


@login_required
def geturls(request):
    if request.user.is_staff:
        slug = request.GET.get('texInputValue')
        checkurl1 = Category.objects.filter(slug=slug).exists()
        id_str = request.GET.get('id_test')
        id_to_int = int(id_str)
        if not checkurl1:
            test1 = "url tốt"
            check_status = 2
            response = {
                'test1': test1,
                'check_status': check_status,
            }
            return HttpResponse(json.dumps(response, default=str), content_type="application/json")
        else:
            getid_url = Category.objects.get(id=id_to_int)
            if getid_url.slug == slug:
                test1 = "url đã tồn tại nhưng là phiên bản củ!!!"
                check_status = 3
                response = {
                    'test1': test1,
                    'check_status': check_status,
                }
                return HttpResponse(json.dumps(response, default=str), content_type="application/json")
            else:
                test1 = "url đã tồn tại xin bạn hãy sửa lại, nút thêm sẻ kích hoạt"
                check_status = 1
                response = {
                    'test1': test1,
                    'check_status': check_status,
                }
                return HttpResponse(json.dumps(response, default=str), content_type="application/json")
    return render(request, 'index/index.html')


@login_required
def add_product(request):
    if request.user.is_staff:
        get_brands = Brands.objects.all()
        get_category = Category.objects.all()
        get_product = Product.objects.all()
        get_title = request.GET.get('textareaValue')
        detail = get_title
        print("-------get title---------")
        print(get_title)
        print(detail)
        print("----------------")
        if request.method == 'POST' and request.FILES:
            parent = request.POST['parent']
            # parentid = Category.objects.get(id=parent)
            title = request.POST['title']
            promotion = request.POST['promotion']
            keywords = request.POST['keywords']
            brands = request.POST['brands']
            image = request.FILES['image']
            slug = request.POST['slug']
            price = request.POST['price']
            amount = request.POST['amount']
            status = request.POST['status']
            description = request.POST['description']
            detail = request.POST['nhat123']
            print(price)
            if promotion is None:
                promotion = 0
            if price is None:
                price = 0
            if amount is None:
                amount = 0
            Product.objects.create(category_id=parent, brands_id=brands, title=title, keywords=keywords, description=description,
                                   detail=detail, images=image, status=status, price=price, promotion=promotion, amount=amount,
                                   slug=slug)
            messages.success(request, "Bạn đã thêm sản phẩm thành công!!!")
        context = {
            'get_brands':get_brands,
            'get_category': get_category,
            'get_product':get_product,
        }
        return render(request, 'manager/add_product.html', context)
    return render(request, 'index/index.html')


@login_required
def test(request):
    if request.user.is_staff:
        if request.user.has_perm('manage_index.add_product'):
            print("-------------------")
            print("quyen sua file")
            print("-------------------")
        else:
            print("khong sua duoc file")
            print("!!!!!!!!!!!!!!!!!!!")
            print("-------------------")
        return render(request, 'manager/test.html')
    return render(request, 'index/index.html')


@login_required
def geturlp(request):
    if request.user.is_staff:
        slug = request.GET.get('texInputValue')
        checkurlp = Product.objects.filter(slug=slug).exists()
        if not checkurlp:
            test1 = "url tốt"
            check_status = 2
            response = {
                'test1': test1,
                'check_status': check_status,
            }
            return HttpResponse(json.dumps(response, default=str), content_type="application/json")
        else:
            test1 = "url đã tồn tại xin bạn hãy sửa lại, nút thêm sẻ kích hoạt"
            check_status = 1
            response = {
                'test1': test1,
                'check_status': check_status,
            }
            return HttpResponse(json.dumps(response, default=str), content_type="application/json")
    return render(request, 'index/index.html')


@login_required
def index_product(request):
    if request.user.is_staff:
        Product_user = request.user
        if Product_user.is_superuser:
            get_data_products = Product.objects.all()
        else:
            get_data_products = Product.objects.filter(user_id=Product_user.id)

        context = {
            'get_data_products': get_data_products,
        }
        return render(request, 'manager/list_product.html', context)
    return render(request, 'index/index.html')


@login_required
def update_product(request, id):
    if request.user.is_staff:
        get_category = Category.objects.all()
        get_brand = Brands.objects.all()
        get_image = Imagss.objects.filter(product_id=id)
        images_ss = request.FILES.getlist('image_s')
        current_user = request.user
        update_prod = Product.objects.get(id=id)
        print("-------------")
        print(update_prod.user_id)
        print("-------------")

        if update_prod.user_id == current_user.id:
            if request.method == 'POST' and request.FILES:
                parent_id = request.POST['parent']
                if parent_id:
                    parent = Category.objects.get(id=parent_id)
                else:
                    parent = None
                brand_id = request.POST['brands']
                if brand_id:
                    brand = Brands.objects.get(id=brand_id)
                else:
                    brand = None
                sumer = request.POST['nhat123']
                title = request.POST['title']
                keywords = request.POST['keywords']
                description = request.POST['description']
                slug = request.POST['slug']
                status = request.POST['status']
                price = request.POST['price']
                promotion = request.POST['promotion']
                amount = request.POST['amount']

                try:
                    file_video = request.FILES['file_video']
                    update_prod.video = file_video
                except:
                    pass
                try:
                    file_pdf = request.FILES['file_pdf']
                    update_prod.pdf_file = file_pdf
                except:
                    pass
                update_prod.user_id = current_user.id
                update_prod.category = parent
                update_prod.brands = brand
                update_prod.title = title
                update_prod.keywords = keywords
                update_prod.description = description
                update_prod.slug = slug
                update_prod.status = status
                try:
                    image = request.FILES['image']
                    if image:
                        update_prod.images = image
                except:
                    print("đây không phải lỗi!!!  chưa thêm ảnh đại diện ")
                update_prod.price = price
                update_prod.promotion = promotion
                update_prod.amount = amount
                update_prod.detail = sumer
                if request.user.has_perm('manage_index.add_product'):
                    update_prod.save()
                else:
                    return render(request, 'manager/index.html')
                try:
                    image1 = request.FILES['image_s']
                    if image1:
                        for image in images_ss:
                            Imagss.objects.create(product_id=id, image_s=image)
                except:
                    print("đây không phải lỗi!!!  chưa thêm ảnh sile ")
                messages.success(request, "Bạn đã sửa danh mục thành công!!!")

            elif request.method == 'POST':
                parent_id = request.POST['parent']
                if parent_id:
                    parent = Category.objects.get(id=parent_id)
                else:
                    parent = None
                brand_id = request.POST['brands']
                if brand_id:
                    brand = Brands.objects.get(id=brand_id)
                else:
                    brand = None
                sumer = request.POST['nhat123']
                title = request.POST['title']
                keywords = request.POST['keywords']
                description = request.POST['description']
                image = update_prod.images
                slug = request.POST['slug']
                status = request.POST['status']
                price = request.POST['price']
                promotion = request.POST['promotion']
                amount = request.POST['amount']
                try:
                    file_video = request.FILES['file_video']
                    update_prod.video = file_video
                except:
                    pass
                try:
                    file_pdf = request.FILES['file_pdf']
                    update_prod.pdf_file = file_pdf
                except:
                    pass
                update_prod.user_id = current_user.id
                update_prod.category = parent
                update_prod.brands = brand
                update_prod.title = title
                update_prod.keywords = keywords
                update_prod.description = description
                update_prod.slug = slug
                update_prod.status = status
                update_prod.image = image
                update_prod.price = price
                update_prod.promotion = promotion
                update_prod.amount = amount
                update_prod.detail = sumer
                if request.user.has_perm('manage_index.add_product'):
                    update_prod.save()
                else:
                    return render(request, 'manager/index.html')
                messages.success(request, "Bạn đã sửa danh mục thành công!!!")
            context = {
                'get_category': get_category,
                'get_brand': get_brand,
                'update_prod': update_prod,
                'get_image': get_image,
            }
            return render(request, 'manager/update_product.html', context)
        elif current_user.is_superuser:
            if request.method == 'POST' and request.FILES:
                parent_id = request.POST['parent']
                if parent_id:
                    parent = Category.objects.get(id=parent_id)
                else:
                    parent = None
                brand_id = request.POST['brands']
                if brand_id:
                    brand = Brands.objects.get(id=brand_id)
                else:
                    brand = None
                sumer = request.POST['nhat123']
                title = request.POST['title']
                keywords = request.POST['keywords']
                description = request.POST['description']
                slug = request.POST['slug']
                status = request.POST['status']
                price = request.POST['price']
                promotion = request.POST['promotion']
                amount = request.POST['amount']
                update_prod.user_id = current_user.id
                update_prod.category = parent
                update_prod.brands = brand
                update_prod.title = title
                update_prod.keywords = keywords
                update_prod.description = description
                update_prod.slug = slug
                update_prod.status = status
                try:
                    print("--- trường hợp sửa sile không sửa ảnh đại diện")
                    image = request.FILES['image']
                    if image:
                        update_prod.images = image
                except:
                    print("đây không phải lỗi!!!  chưa thêm ảnh đại diện ")
                update_prod.price = price
                update_prod.promotion = promotion
                update_prod.amount = amount
                update_prod.detail = sumer
                if request.user.has_perm('manage_index.add_product'):
                    update_prod.save()
                else:
                    return render(request, 'manager/index.html')
                try:
                    image1 = request.FILES['image_s']
                    if image1:
                        for image in images_ss:
                            Imagss.objects.create(product_id=id, image_s=image)
                except:
                    print("đây không phải lỗi!!!  chưa thêm ảnh sile ")
                messages.success(request, "Bạn đã sửa danh mục thành công!!!")

            elif request.method == 'POST':
                parent_id = request.POST['parent']
                if parent_id:
                    parent = Category.objects.get(id=parent_id)
                else:
                    parent = None
                brand_id = request.POST['brands']
                if brand_id:
                    brand = Brands.objects.get(id=brand_id)
                else:
                    brand = None
                sumer = request.POST['nhat123']
                title = request.POST['title']
                keywords = request.POST['keywords']
                description = request.POST['description']
                image = update_prod.images
                slug = request.POST['slug']
                status = request.POST['status']
                price = request.POST['price']
                promotion = request.POST['promotion']
                amount = request.POST['amount']
                update_prod.user_id = current_user.id
                update_prod.category = parent
                update_prod.brands = brand
                update_prod.title = title
                update_prod.keywords = keywords
                update_prod.description = description
                update_prod.slug = slug
                update_prod.status = status
                update_prod.image = image
                update_prod.price = price
                update_prod.promotion = promotion
                update_prod.amount = amount
                update_prod.detail = sumer
                if request.user.has_perm('manage_index.add_product'):
                    update_prod.save()
                else:
                    return render(request, 'manager/index.html')
                messages.success(request, "Bạn đã sửa danh mục thành công!!!")
            context = {
                'get_category': get_category,
                'get_brand': get_brand,
                'update_prod': update_prod,
                'get_image': get_image,
            }
            return render(request, 'manager/update_product.html', context)
        else:
            return render(request, 'manager/index.html')
    return render(request, 'index/index.html')


@login_required
def geturlps(request):
    if request.user.is_staff:
        slug = request.GET.get('texInputValue')
        checkurl1 = Product.objects.filter(slug=slug).exists()
        id_str = request.GET.get('id_test')
        id_to_int = int(id_str)
        if not checkurl1:
            test1 = "url tốt !"
            check_status = 2
            response = {
                'test1': test1,
                'check_status': check_status,
            }
            return HttpResponse(json.dumps(response, default=str), content_type="application/json")
        else:
            getid_url = Product.objects.get(id=id_to_int)
            if getid_url.slug == slug:
                test1 = "url đã tồn tại nhưng là phiên bản củ!!!"
                check_status = 3
                response = {
                    'test1': test1,
                    'check_status': check_status,
                }
                return HttpResponse(json.dumps(response, default=str), content_type="application/json")
            else:
                test1 = "url đã tồn tại xin bạn hãy sửa lại, nút thêm sẻ kích hoạt"
                check_status = 1
                response = {
                    'test1': test1,
                    'check_status': check_status,
                }
                return HttpResponse(json.dumps(response, default=str), content_type="application/json")
        return None
    return render(request, 'index/index.html')


@login_required
def delete_product(request, id):
    if request.user.is_staff:
        delete_pro = Product.objects.filter(id=id)
        if request.user.has_perm('manage_index.delete_product'):
            delete_pro.delete()
        else:
            return render(request, 'manager/idex.html')
        return HttpResponseRedirect(reverse('index_product'))
    return render(request, 'index/index.html')


@login_required
def add_products(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            form2 = ImagssForm(request.POST, request.FILES)
            images_ss = request.FILES.getlist('image_s')
            current_user = request.user
            if form.is_valid() and form2.is_valid():
                data = Product()
                data.user_id = current_user.id
                data.title = form.cleaned_data['title']
                data.keywords = form.cleaned_data['keywords']
                data.description = form.cleaned_data['description']
                data.detail = form.cleaned_data['detail']
                data.images = form.cleaned_data['images']
                data.category = form.cleaned_data['category']
                data.brands = form.cleaned_data['brands']
                data.price = form.cleaned_data['price']
                data.promotion = form.cleaned_data['promotion']
                data.amount = form.cleaned_data['amount']
                data.slug = form.cleaned_data['slug']
                data.video = form.cleaned_data['video']
                data.pdf_file = form.cleaned_data['pdf_file']
                data.save()
                check_img_slide = form2.cleaned_data['image_s']
                if data and check_img_slide:
                    for image in images_ss:
                        data2 = Imagss()
                        data2.product = data
                        # data2.title_im = form2.cleaned_data['title_im']
                        data2.image_s = image
                        data2.save()
                return HttpResponseRedirect('/loginncb/add-products')

        form = ProductForm
        form2 = ImagssForm
        context={
            'form2': form2,
            'form': form,
        }
        return render(request, 'manager/add_products.html', context)
    return render(request, 'index/index.html')


@login_required
def delete_image(request, id):
    if request.user.is_staff:
        delete_image = Imagss.objects.filter(id=id)
        for rs in delete_image:
            get_id = rs.product.pk
        get_id
        delete_image.delete()
        return redirect(f'/loginncb/update-product/{get_id}')
    return render(request, 'index/index.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            gettext = form.cleaned_data.get('password1')
            get_pass = User.objects.create_user(username=form.cleaned_data.get('username'), email=form.cleaned_data.get('email'))
            get_pass.set_password(gettext)
            get_pass.save()
            # data.save()
            messages.success(request, 'Bạn đã tạo tài khoản thành công!')
            return redirect('login_user')
        messages.warning(request, 'Bạn có thể sai tên đăng nhập')
    form = CreateUserForm
    context = {
        'form':form,
    }
    return render(request, 'auth/register.html',context)


def login_user(request):
    if request.user.is_authenticated:
        return render(request, 'index/index.html')
    else:
        if request.method == 'POST':
            # Process the request if posted data are available
            username = request.POST['username']
            password = request.POST['password']
            # Check username and password combination if correct
            user = authenticate(username=username, password=password)
            if user is not None:
                # Save session as cookie to login the user
                login(request, user)

                # Success, now let's login the user.
                if request.user.is_staff:
                    return render(request, 'manager/index.html')
                else:
                    return render(request, 'index/update/index.html')
            else:
                # Incorrect credentials, let's throw an error to the screen.

                context = {
                    'error_message': 'Sai tài khoản hoặc password.'
                }
                return render(request, 'auth/login.html', context)
        else:
            # No post data availabe, let's just show the page to the user.
            return render(request, 'auth/login.html')


@login_required
def updateprofile(request):
    current_user1 = request.user
    update_User = User.objects.get(id=current_user1.id)
    a_user = User.objects.get(username=update_User)
    get_pro = UserProfile.objects.get(user_id=1)
    current_user = request.user
    if request.method == 'POST' or request.FILES:
        data = UserProfile()
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        phone = request.POST['phone']
        try:
            image = request.FILES['image']
            data.image = image
        except:
            print("---not add image to profile----")
        data.user = current_user
        data.address = address
        data.city = city
        data.phone = phone
        data.country = country
        data.save()

    if request.method == 'POST':
        a_user.first_name = request.POST['first_name']
        a_user.last_name = request.POST['last_name']
        a_user.save()
    context = {
        'update_User': update_User,
        'get_pro': get_pro,
    }
    return render(request, 'auth/updateprofile.html', context)


@login_required
def list_oder_user(request):
    if request.user.is_staff:
        getoder = Order.objects.all()
        context = {
            'getoder': getoder,
        }
        return render(request, 'manager/list_oder_user.html',context)
    return render(request, 'index/index.html')

@login_required
def update_oder_user(request, id):
    if request.user.is_staff:
        get_oder = Order.objects.get(id=id)
        orderitems = ProductTotalInCart.objects.filter(order_id=id)
        get_total = get_oder.total
        if request.method == 'POST':
            name = request.POST['name']
            phone = request.POST['phone']
            status = request.POST['status']
            address = request.POST['address']
            note = request.POST['note']
            get_oder.Name = name
            get_oder.Phone = phone
            get_oder.status = status
            get_oder.Address = address
            get_oder.note = note
            get_oder.total = get_total
            get_oder.save()
            messages.success(request, 'Bạn đã cập nhập thành công')
        context = {
            'get_oder': get_oder,
            'orderitems':orderitems,
        }
        return render(request, 'manager/update_oder_user.html', context)
    return render(request, 'index/index.html')


@login_required
def list_comment(request):
    get_coment = CommentPro.objects.all()
    if request.user.is_staff:
        context = {
            'get_coment': get_coment,
        }
        return render(request, 'manager/list_comment.html', context)
    return render(request, 'index/index.html')

@login_required
def update_list_comment(request,id):
    get_comment = CommentPro.objects.get(id=id)
    if request.user.is_staff:
        if request.method == 'POST':
            status = request.POST['status']
            get_comment.status = status
            get_comment.save()
            messages.success(request, 'Bạn đã cập nhập trạng thái thành công! bạn sẻ không sửa được trường khác!')

        context = {
            'get_comment': get_comment,
        }
        return render(request, 'manager/update_comments.html', context)
    return render(request, 'index/index.html')


@login_required
def list_comment_blog(request):
    get_coment = CommentBlog.objects.all()
    if request.user.is_staff:
        context = {
            'get_coment': get_coment,
        }
        return render(request, 'manager/list_comment_blog.html', context)
    return render(request, 'index/index.html')

@login_required
def update_list_combl(request, id):
    get_comment = CommentBlog.objects.get(id=id)
    if request.user.is_staff:
        if request.method == 'POST':
            status = request.POST['status']
            get_comment.status = status
            get_comment.save()
            messages.success(request, 'Bạn đã cập nhập trạng thái thành công! bạn sẻ không sửa được trường khác!')
        context = {
            'get_comment': get_comment,
        }
        return render(request, 'manager/update_comment_blog.html', context)
    return render(request, 'index/index.html')


@login_required
def addlistvideo(request):
    if request.user.is_staff:
        gettitle = Product.objects.all()
        if request.method == 'POST' or request.FILES:
            title_pro = request.POST['title_pro']
            title = request.POST['title']
            get_number = request.POST['get_number']
            videos = request.FILES['videos']
            allowed_extension = '.mp4'
            file_extension = '.' + videos.name.split('.')[-1].lower()

            if file_extension != allowed_extension:
                messages.warning(request, 'file không phải là mp4')
                context = {
                    'gettitle': gettitle,
                }
                return render(request, 'manager/add_list_video.html', context)

            data = video_list()
            try:
                filepdf = request.FILES['filepdf']
                data.pdffile = filepdf
            except:
                pass
            data.product_id = title_pro
            data.title = title
            data.videos = videos

            data.ordinal_numbers = get_number
            data.save()
            messages.success(request, 'Bạn đã thêm video thành công')
        else:
            messages.warning(request, 'Thêm không thành công')
        context = {
            'gettitle': gettitle,
        }
        return render(request, 'manager/add_list_video.html', context)
    return render(request, 'index/index.html')

@login_required
def listvideoall(request):
    if request.user.is_staff:
        gettitle = video_list.objects.all()
        context = {
            'gettitle':gettitle,
        }
        return render(request, 'manager/list_videos.html', context)
    return render(request, 'index/index.html')


@login_required
def update_list_video(request,id):
    if request.user.is_staff:
        gettitle = Product.objects.all()
        get_video = video_list.objects.get(id=id)
        if request.method == 'POST' or request.FILES:
            title_pro = request.POST['title_pro']
            print("-------------")
            print(title_pro)
            print("-------------")
            title = request.POST['title']
            get_number = request.POST['get_number']
            try:
                videos = request.FILES['videos']
                allowed_extension = '.mp4'
                file_extension = '.' + videos.name.split('.')[-1].lower()
                if file_extension != allowed_extension:
                    pass
                else:
                    get_video.videos = videos
            except:
                pass
            try:
                filepdf = request.FILES['filepdf']
                get_video.pdffile = filepdf
            except:
                pass
            get_video.product_id = title_pro
            get_video.title = title
            get_video.ordinal_numbers = get_number
            get_video.save()
            messages.success(request, 'Bạn đã sửa thành công')
        else:
            messages.warning(request, 'Thêm không thành công')
        context = {
            'gettitle':gettitle,
            'get_video':get_video,
        }
        return render(request, 'manager/update_videos.html', context)
    return render(request, 'index/index.html')

@login_required
def delete_videos(request, id):
    if request.user.is_staff:
        delete_pro = video_list.objects.get(id=id)
        delete_pro.delete()
        return HttpResponseRedirect(reverse('listvideoall'))
    return render(request, 'index/index.html')


@login_required
def addtitlevideo(request):
    if request.user.is_staff:
        gettitle = Product.objects.all()
        if request.method == 'POST' or request.FILES:
            title_pro = request.POST['title_pro']
            title = request.POST['title']
            get_number = request.POST['get_number']
            data = couse_title()
            data.product_id = title_pro
            data.title = title
            data.ordinal_numbers = get_number
            data.save()
            messages.success(request, 'Bạn đã thêm video thành công')
        else:
            messages.warning(request, 'Thêm không thành công')
        context = {
            'gettitle': gettitle,
        }
        return render(request, 'manager/add_title_videos.html', context)
    return render(request, 'index/index.html')


@login_required
def gettitlevides(request):
    if request.user.is_staff:
        gettitle = couse_title.objects.all()
        context = {
            'gettitle':gettitle,
        }
        return render(request, 'manager/list_title_videos.html', context)
    return render(request, 'index/index.html')


@login_required
def update_title_video(request, id):
    if request.user.is_staff:
        gettitle = Product.objects.all()
        get_video = couse_title.objects.get(id=id)
        if request.method == 'POST' or request.FILES:
            title_pro = request.POST['title_pro']
            title = request.POST['title']
            get_number = request.POST['get_number']

            get_video.product_id = title_pro
            get_video.title = title
            get_video.ordinal_numbers = get_number
            get_video.save()
            messages.success(request, 'Bạn đã sửa thành công')
        else:
            messages.warning(request, 'Thêm không thành công')
        context = {
            'gettitle': gettitle,
            'get_video': get_video,
        }
        return render(request, 'manager/update_title_videos.html', context)
    return render(request, 'index/index.html')


@login_required
def delete_title_video(request, id):
    if request.user.is_staff:
        delete_pro = couse_title.objects.get(id=id)
        delete_pro.delete()
        return HttpResponseRedirect(reverse('gettitlevides'))
    return render(request, 'index/index.html')


@login_required
def addvideopdf(request):
    if request.user.is_staff:
        gettitle = couse_title.objects.all()
        if request.method == 'POST' and request.FILES:
            title_pro = request.POST['title_pro']
            title = request.POST['title']
            get_number = request.POST['get_number']
            titlevideo = request.POST['titlevideo']
            link_video = request.POST['link_video']
            try:
                videos = request.FILES['videos']
                allowed_extension = '.mp4'
                file_extension = '.' + videos.name.split('.')[-1].lower()

                if file_extension != allowed_extension:
                    messages.warning(request, 'file không phải là mp4')
                    context = {
                        'gettitle': gettitle,
                    }
                    return render(request, 'manager/add_video_pdf.html', context)
            except:
                pass
            data = cource_video()
            try:
                filepdf = request.FILES['filepdf']
                print("--------------------")
                print(filepdf)
                print("--------------------")
                data.pdffile = filepdf
            except:
                pass
            try:
                videos = request.FILES['videos']
                data.videos = videos
            except:
                pass
            data.vimeo_link = link_video
            data.cource_id = title_pro
            data.title = title
            data.titlevideo = titlevideo
            data.ordinal_numbers = get_number
            data.save()
            messages.success(request, 'Bạn đã thêm video thành công')
        else:
            if request.method == 'POST':
                title_pro = request.POST['title_pro']
                title = request.POST['title']
                get_number = request.POST['get_number']
                titlevideo = request.POST['titlevideo']
                link_video = request.POST['link_video']
                data = cource_video()
                data.vimeo_link = link_video
                data.cource_id = title_pro
                data.title = title
                data.titlevideo = titlevideo
                data.ordinal_numbers = get_number
                data.save()
                messages.success(request, 'Bạn đã thêm video thành công, nhưng không kèm file nào cả')
            else:
                messages.warning(request, 'Thêm không thành công')
        context = {
            'gettitle': gettitle,
        }
        return render(request, 'manager/add_video_pdf.html', context)
    return render(request, 'index/index.html')


@login_required
def updatevideopdf(request, id):
    if request.user.is_staff:
        print("--------------")
        print(id)
        print("--------------")
        gettitle = couse_title.objects.all()
        get_video = cource_video.objects.get(id=id)
        if request.method == 'POST' and request.FILES:
            title_pro = request.POST['title_pro']
            title = request.POST['title']
            get_number = request.POST['get_number']
            titlevideo = request.POST['titlevideo']
            link_video = request.POST['link_video']
            try:
                videos = request.FILES['videos']
                allowed_extension = '.mp4'
                file_extension = '.' + videos.name.split('.')[-1].lower()

                if file_extension != allowed_extension:
                    messages.warning(request, 'file không phải là mp4')
                    context = {
                        'gettitle': gettitle,
                    }
                    return render(request, 'manager/add_video_pdf.html', context)
            except:
                pass
            try:
                filepdf = request.FILES['filepdf']
                print("--------------------")
                print(filepdf)
                print("--------------------")
                get_video.pdffile = filepdf
            except:
                pass
            try:
                videos = request.FILES['videos']
                get_video.videos = videos
            except:
                pass
            get_video.vimeo_link = link_video
            get_video.cource_id = title_pro
            get_video.title = title
            get_video.titlevideo = titlevideo
            get_video.ordinal_numbers = get_number
            get_video.save()
            messages.success(request, 'Bạn đã sửa thành công')
        else:
            if request.method == 'POST':
                link_video = request.POST['link_video']
                title_pro = request.POST['title_pro']
                title = request.POST['title']
                get_number = request.POST['get_number']
                titlevideo = request.POST['titlevideo']
                get_video.cource_id = title_pro
                get_video.vimeo_link = link_video
                get_video.title = title
                get_video.titlevideo = titlevideo
                get_video.ordinal_numbers = get_number
                get_video.save()
                messages.success(request, 'Bạn đã sửa thành công, nhưng không kèm file nào cả')
            else:
                messages.warning(request, 'Sửa không thành công')
        context = {
            'get_video': get_video,
            'gettitle':gettitle,
        }
        return render(request, 'manager/update_video_pdf.html', context)
    return render(request, 'index/index.html')


@login_required
def getlistvideopdf(request):
    if request.user.is_staff:
        gettitle = cource_video.objects.all()
        context = {
            'gettitle':gettitle,
        }
        return render(request, 'manager/list_video_pdf.html', context)
    return render(request, 'index/index.html')


@login_required
def delete_video_pdf(request, id):
    if request.user.is_staff:
        delete_pro = cource_video.objects.get(id=id)
        delete_pro.delete()
        return HttpResponseRedirect(reverse('getlistvideopdf'))
    return render(request, 'index/index.html')

@login_required
def list_massager(request):
    if request.user.is_staff:
        get_list_ma = Messagers.objects.all()
        context = {
            'get_list_ma': get_list_ma,
        }
        return render(request, 'manager/list_massager.html', context)
    return render(request, 'index/index.html')
