from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import SearchForms
from .models import CategoryModel, ProductsModel


# def home_page(request):
#
#     categories = CategoryModel.objects.all()
#     products = ProductsModel.objects.all()
#     context = {'categories': categories, 'products': products}
#
#
#     return render(request, template_name='index.html', context=context)

class HomePage(ListView):
    template_name = 'index.html'
    model = ProductsModel
    context_object_name = 'products'
    form_class = SearchForms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        return context

def search(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            exact_product = ProductsModel.objects.get(title__icontains=get_product)
            return redirect(f'/products/{exact_product.id}')
        except:
            return redirect('/')

def product_page(request, id):
    product = ProductsModel.objects.get(id=id)
    context = {'product': product}
    return render(request, template_name='single_products.html',
                  context=context)