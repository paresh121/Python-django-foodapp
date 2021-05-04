from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
def index(req):
    # tem= loader.get_template('food/index.html')
    item_list=Item.objects.all()
    context={
        'item_list':Item.objects.all(),
    }
    # return HttpResponse(tem.render(context, req))
    return render(req,'food/index.html', context)
# same as index
class IndexClassView(ListView):
    model=Item
    template_name='food/index.html'
    context_object_name='item_list'
#
def item(req):
    return HttpResponse('lISTED ITEMS')
def detail(req,item_id):
    get_item=Item.objects.get(id=item_id)
    context={
        "item":get_item,
    }
    return render(req, 'food/detail.html', context)
#
class FoodDetail(DetailView):
    model=Item
    template_name='food/detail.html'
    context_object_name='item'


#
def create_item(req):
    form = ItemForm(req.POST or None)
    if(form.is_valid()):
        form.save()
        return redirect ('food:index')
    context={
        'form': form,
    }
    return render(req, 'food/create_item_form.html',context)
def update_item(req,id):
    item= Item.objects.get(id=id)
    form = ItemForm(req.POST or None, instance= item)
    if(form.is_valid()):
        form.save()
        return redirect ('food:index')
    context={
        'form': form,
        'item': item
    }
    return render(req, 'food/create_item_form.html',context)   
def delete_item(req,id):
    item=Item.objects.get(id=id)
    if req.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(req,'food/delete_form.html',{'item': item,})