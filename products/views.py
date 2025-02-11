from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect


from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Product CRUD operations
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductListView(LoginRequiredMixin, ListView):
    """
    Display a list of all products
    """
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new product
    """
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'category', 'cost_price', 'selling_price', 
              'manufacturer', 'stock_quantity', 'commission_rate']
    success_url = reverse_lazy('products:list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing product
    """
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'category', 'cost_price', 'selling_price', 
              'manufacturer', 'stock_quantity', 'commission_rate']
    success_url = reverse_lazy('products:list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a product
    """
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:list')


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'
    
    def dispatch(self, request, *args, **kwargs):
        # 세션 완전 삭제
        auth_logout(request)
        request.session.flush()
        request.session.clear_expired()
        
        # 모든 쿠키 삭제
        response = HttpResponseRedirect(self.get_success_url())
        for cookie in request.COOKIES:
            response.delete_cookie(cookie)
            
        return response

    def get_success_url(self):
        return reverse_lazy('logged-out')  # 로그아웃 완료 페이지
