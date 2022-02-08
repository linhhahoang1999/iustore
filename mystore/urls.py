from django.urls import path
from .views import index, cart, item, user,customer,payment,manage,types,product, addressAPI,warehouse,bank,shipper

app_name = 'mystore'

urlpatterns = [
    path('', index.home, name='home'),
    path('cart', cart.cart, name = 'cart'),
    path('add-to-cart', cart.addToCart, name='add-to-cart'),
    path('cart/delete/<item_id>', cart.deleteItem, name='cart/delete'),
    path('login', user.login, name='login'),
    path('logout', user.logout, name='logout'),
    path('customer/notification', customer.notification, name='notification'),
    path('customer/info', customer.info, name='info'),
    path('customer/order', customer.order, name='customer-order'),
    path('item/<item_id>', item.showItemDetail, name='item-detail'),
    path('search', item.searchItem, name='search-item'),
    path('checkout', payment.checkout, name='checkout'),
    path('handle-checkout', payment.handleCheckout, name='handle-checkout'),
    path('checkout/delivery-address/show-edit', payment.editDeliveryAddress, name='delivery-address/show-edit'),
    path('checkout/delivery-address/handle-edit', payment.handleDeliveryAddress, name='delivery-address/handle-edit'),
    path('type/category', types.getTypeByCategory, name='type-by-category'),
    path('product', product.product, name = 'product'),
    path('product/active', product.active, name = 'product-active'),
    path('bank', bank.getBanks, name='bank'),
    path('customer/address', customer.address, name='customer-address'),
    # customer
    path('order/view/<int:order_id>', customer.viewOrderDetail, name='order/view'),
    path('item/<item_id>/comment', item.showItemComment, name='item/comment'),
    path('item_review', item.handleComment, name='item-review'),
    path('item/type/<type_id>', item.item_type, name='item-type'),
    # manager
    path('saler', manage.saler, name = 'saler'),
    path('shipment', manage.shipment, name = 'shipment'),
    path('registation', user.register, name = 'register'),
    path('new-product', manage.newProduct, name = 'new-product'),
    path('new-product-detail/type/<int:type_id>', manage.newProductDetail, name='new-product-detail'),
    path('import-product', manage.importProduct, name='import-product'),
    path('warehouse', warehouse.warehouse, name='warehouse'),
    path('search-product', product.active, name = 'search-product'),
    path('product/send-warehouse/<order_id>', manage.sendWarehouse, name='send-warehouse'),
    path('warehouse/export-product/<order_id>', warehouse.exportProduct, name='export-product'),
    path('shipper', shipper.shipper, name='shipper'),
    path('shipper/shipping/<order_id>', shipper.shipping, name='shipping'),
    path('shipper/finished/<order_id>', shipper.finished, name='finished'),
    path('saler/view-order/<order_id>', manage.viewOrder, name = 'view-order'),
    path('product/get-list', product.getList, name = 'get-list'),
    path('product/up-shelf/<product_id>', product.upShelf, name = 'up-shelf'),
    path('shipper/cancel', shipper.cancel , name = 'cancel'),
    # address api
    path('city', addressAPI.getCities, name='city'),
    path('city/<int:city_id>/district', addressAPI.getDistrictsInCity, name='district-in-city'),
    path('district/<int:district_id>/ward', addressAPI.getWardsInDistrict, name='ward-in-district'),
]
