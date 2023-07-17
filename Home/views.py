from django.conf.urls import url
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from manage_index.models import Product, CommentPro


def index(request):
    get_pro = Product.objects.all()

    context = {
        'get_pro': get_pro,
    }
    return render(request, "index/update/index.html", context)
    return render(request, "index/index.html", context)


def detai_product(request, slug):
    get_detail_pro = Product.objects.get(slug=slug)
    id = get_detail_pro.id
    comments = CommentPro.objects.filter(product_id=id, status='True')
    context = {
        'get_detail_pro': get_detail_pro,
        'comments': comments,
    }
    return render(request, "index/update/detail_product.html", context)
    return render(request, "index/detail_product.html", context)


def addcommentpr(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user
    id = int(id)
    if request.method == 'POST':
        rate = request.POST['rate']
        comment = request.POST['comment']
        ip = request.META.get('REMOTE_ADDR')
        CommentPro.objects.create(product_id=id, user=current_user, rate=rate, comment=comment, ip=ip)
        messages.success(request, "cám ơn bạn đã đánh giá sản phẩm.")
        return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)