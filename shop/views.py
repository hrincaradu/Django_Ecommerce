from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Slider, ProductReview
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def prod_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
    
    paginator = Paginator(products,6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products =  paginator.page(paginator.num_pages)
    
    slider = Slider.objects.all()


            
            
    
    return render(request, 'shop/category.html',{'category':category, 'prods':products, 'slider':slider}) 


def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product , category_id=category_id, id=product_id)
#reviews
    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        title = request.POST.get('title', '')
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')
        if rating:
            reviews= ProductReview.objects.filter(user=request.user, product = product)
            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.title = title
                review.content = content
                review.save()
                messages.success(request, 'Your review has been updated.')
            else:
                review = ProductReview.objects.create(
                product = product,
                title=title,
                rating = rating,
                content = content,
                user = request.user)
                messages.success(request, 'Your review has been posted.')

                
            return redirect(url)
    return render(request, 'shop/product.html', {'product':product})


#reviews

