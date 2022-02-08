from django.shortcuts import redirect, render
from django.template import Context, context
from ..models import *
from ..views import cart

def warehouse(request):
    orders = Order.objects.filter(statusNow='Đợi kho')
    context = {}
    context['orders'] = []
    for order in orders:
        cart_items = CartItem.objects.filter( cart =order.cart)
        order_item = str(cart_items[0].qty) + ' ' + cart_items[0].item.name
        if len(cart_items)-1 > 0:
            order_item += ' và ' +  str(len(cart_items)-1)+' các sản phẩm khác'
        
        context['orders'].append((order,order_item))

    return render(request, 'manager/warehouse.html',context)

def exportProduct(request,order_id):
    order = Order.objects.get(id = order_id)
    order.statusNow = 'Đợi giao'
    print(order)
    order.save()
    print(order.statusNow)

    member = Member.objects.get(id = request.session.get('member'))
    updateStatus = OrderHistory()
    updateStatus.member = member
    updateStatus.order = order
    updateStatus.status = order.statusNow
    updateStatus.save()

    cart_items = CartItem.objects.filter( cart =order.cart)
    staff = WarehouseStaff.objects.get(member = member) 
    exportNote = ExportNote(warehouseStaff = staff)
    exportNote.save()
    
    for citem in cart_items :
        product=Product.objects.get(id=citem.item.product.id)
        exportP = ExportProduct( exportNote=exportNote,product = product, qty = citem.qty)
        exportP.save()
        product.qty_in_stock-= citem.qty
        product.save()
    

    return redirect('mystore:warehouse')