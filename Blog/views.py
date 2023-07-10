import json

from django.conf.urls import url
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from Blog.models import Category, Blog


@login_required
def home_blog(request):
    get_category = Category.objects.all()
    context = {
        'get_category': get_category,
    }

    return render(request, "blog/home_category.html",context)


@login_required
def home(request):
    if request.user.is_staff:
        get_parents = Category.objects.all()
        if request.method == 'POST' or request.FILES:
            parent = request.POST['parent']
            # parentid = Category.objects.get(id=parent)
            title = request.POST['title']
            description = request.POST['description']
            if request.FILES:
                image = request.FILES['image']
            else:
                image = "default.png"
            slug = request.POST['slug']
            status = request.POST['status']
            Category.objects.create(parent_id=parent, title=title, description=description, image=image, slug=slug, status=status)
            messages.success(request, "Bạn đã nhập danh mục thành công!!!")
        context = {
            'get_parents': get_parents,
        }
        return render(request, "blog/category.html",context)
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
def blog_update_category(request, id):
    if request.user.is_staff:
        url = request.META.get('HTTP_REFERER')  # get last url
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
            description = request.POST['description']
            image = request.FILES['image']
            slug = request.POST['slug']
            status = request.POST['status']
            update_cate.parent = parent
            update_cate.title = title
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
            description = request.POST['description']
            image = update_cate.image
            slug = request.POST['slug']
            status = request.POST['status']
            update_cate.parent = parent
            update_cate.title = title
            update_cate.description = description
            update_cate.slug = slug
            update_cate.status = status
            update_cate.image = image
            update_cate.save()
            messages.success(request, "Bạn đã sửa danh mục thành công!!!")
            # return render(request, 'manager/list_category.html')
            return HttpResponseRedirect(url)
            # return HttpResponseRedirect(reverse('blog-update-category'))
        context = {
            'get_parents': get_parents,
            'update_cate': update_cate,
        }
        return render(request, "blog/update_category.html", context)
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
def delete_category(request, id):
    if request.user.is_staff:
        delete_cate = Category.objects.filter(id=id)
        delete_cate.delete()
        return HttpResponseRedirect(reverse('home-blog-category'))
    return render(request, 'index/index.html')


@login_required
def add_blog(request):
    if request.user.is_staff:
        get_category = Category.objects.all()
        current_user = request.user  # Access User Session information
        if request.method == 'POST' and request.FILES:
            parent = request.POST['parent']
            title = request.POST['title']
            keywords = request.POST['keywords']
            image = request.FILES['image']
            slug = request.POST['slug']
            status = request.POST['status']
            description = request.POST['description']
            detail = request.POST['nhat123']
            Blog.objects.create(user=current_user, category_id=parent,  title=title, keywords=keywords, description=description,
                                   detail=detail, images=image, status=status, slug=slug)
        context = {
            'get_category': get_category,
        }
        return render(request, "blog/add_blog.html",context)
    return render(request, 'index/index.html')


@login_required
def geturlblog(request):
    if request.user.is_staff:
        slug = request.GET.get('texInputValue')
        checkurlp = Blog.objects.filter(slug=slug).exists()
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
def blog_update(request, id):
    if request.user.is_staff:
        current_user = request.user
        update_blog = Blog.objects.get(id=id)
        get_category = Category.objects.all()
        if request.method == 'POST' and request.FILES:
            parent_id = request.POST['parent']
            if parent_id:
                parent = Category.objects.get(id=parent_id)
            else:
                parent = None
            sumer = request.POST['nhat123']
            title = request.POST['title']
            keywords = request.POST['keywords']
            description = request.POST['description']
            slug = request.POST['slug']
            status = request.POST['status']
            image = request.FILES['image']
            update_blog.user_id = current_user.id
            update_blog.category = parent
            update_blog.title = title
            update_blog.keywords = keywords
            update_blog.description = description
            update_blog.slug = slug
            update_blog.status = status
            update_blog.images = image
            update_blog.detail = sumer
            update_blog.save()
            print("thanh cong")
            messages.success(request, "Bạn đã sửa danh mục thành công!!!")
        elif request.method == 'POST':
            parent_id = request.POST['parent']
            if parent_id:
                parent = Category.objects.get(id=parent_id)
            else:
                parent = None
            sumer = request.POST['nhat123']
            title = request.POST['title']
            keywords = request.POST['keywords']
            description = request.POST['description']
            slug = request.POST['slug']
            status = request.POST['status']
            update_blog.user_id = current_user.id
            update_blog.category = parent
            update_blog.title = title
            update_blog.keywords = keywords
            update_blog.description = description
            update_blog.slug = slug
            update_blog.status = status
            update_blog.detail = sumer
            update_blog.save()
            messages.success(request, "Bạn đã sửa danh mục thành công!!! không cần hình ảnh")
        context = {
            'update_blog': update_blog,
            'get_category': get_category,
        }
        return render(request, "blog/update_blog.html", context)
    return render(request, 'index/index.html')


@login_required
def geturlblogu(request):
    if request.user.is_staff:
        slug = request.GET.get('texInputValue')
        checkurl1 = Blog.objects.filter(slug=slug).exists()
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
            getid_url = Blog.objects.get(id=id_to_int)
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
def list_blog(request):
    if request.user.is_staff:
        get_Blog = Blog.objects.all()
        context = {
            'get_Blog': get_Blog,
        }
        return render(request, "blog/list_blog.html", context)
    return render(request, 'index/index.html')


@login_required
def delete_blog(request, id):
    if request.user.is_staff:
        delete_cate = Category.objects.filter(id=id)
        delete_cate.delete()
        return HttpResponseRedirect(reverse('list-blog-all'))
    return render(request, 'index/index.html')