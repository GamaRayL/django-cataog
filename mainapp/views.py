from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from mainapp.models import Product, Post


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Каталог товаров'
    }


class ProductDetailView(DetailView):
    model = Product


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
            from_email = 'your_email@yandex.ru'
            recipient_list = ['email@gmail.com']
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        post.view_count += 1
        post.save()

        return super().get(request, *args, **kwargs)


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body',)
    success_url = reverse_lazy('mainapp:posts')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body',)

    def get_success_url(self):
        return reverse('mainapp:post', args=[self.object.pk])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('mainapp:posts')
