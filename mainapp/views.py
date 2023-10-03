from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from mainapp.forms import ProductForm, VersionForm
from mainapp.models import Product, Post, Version


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Каталог товаров'
    }


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('mainapp:products')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('mainapp:products')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('mainapp:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        formset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = formset(instance=self.object)

        return context_data


class PostListView(ListView):
    model = Post
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)

        return queryset


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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'body',)
    success_url = reverse_lazy('mainapp:posts')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'body',)

    def get_success_url(self):
        return reverse('mainapp:post', args=[self.object.pk])


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('mainapp:posts')
