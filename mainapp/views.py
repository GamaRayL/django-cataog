from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, never_cache
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mainapp.forms import ProductForm, VersionForm, ShortProductForm
from mainapp.models import Product, Post, Version, Category
from mainapp.services import get_cached_categories
from django.contrib.contenttypes.models import ContentType


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Каталог товаров'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        moderator = self.request.user.groups.filter(name='moderator').exists()
        user = self.request.user

        if user.is_superuser or moderator:
            return queryset
        else:
            return queryset.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    # permission_required = 'mainapp.add_product'
    success_url = reverse_lazy('mainapp:products')

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('mainapp:products')

    def get_form_class(self):
        if self.request.user == self.object.user or self.request.user.is_superuser:
            return ProductForm
        else:
            return ShortProductForm

    def test_func(self):
        return (
            self.request.user == self.get_object().user or
            self.request.user.is_superuser or
            self.request.user.groups.filter(name='moderator').exists()
        )


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    permission_required = 'mainapp.delete_product'
    success_url = reverse_lazy('mainapp:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = formset(instance=self.object)

        return context_data

    def test_func(self):
        return self.request.user.is_superuser


class PostListView(ListView):
    model = Post
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)

        return queryset


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'body',)
    success_url = reverse_lazy('mainapp:posts')

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'body',)

    def get_success_url(self):
        return reverse('mainapp:post', args=[self.object.pk])


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('mainapp:posts')


class PostDetailView(DetailView):
    model = Post

    def get(self, request, *args, **kwargs):
        post = self.get_object()

        if post.view_count == 100:
            subject = 'Пост достиг 100 просмотров'
            message = f'Пост "{post.title}" достиг 100 просмотров.'
            from_email = 'bantarion@yandex.ru'
            recipient_list = ['gamaizingg@gmail.com']
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        post.view_count += 1
        post.save()

        return super().get(request, *args, **kwargs)


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = 'Категории товаров'
        context_data['category_list'] = get_cached_categories()

        return context_data
