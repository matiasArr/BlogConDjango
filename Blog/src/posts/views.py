from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Like, PostView
from .forms import PostForm, CommentForm

# Create your views here.

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = 'login/'


    '''
    def get(self, args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('account_login')
    '''

class PostDetailView(DetailView):
    model = Post

    #crear un comentario 
    def post(self, args,**kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail-post', slug=post.slug)
    
    #envia el formulario para escribir un comentario 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm()
        }) 
        return context

    #toma el objeto del post
    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        PostView.objects.get_or_create(user=self.request.user, post=object)
        return object

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'
    
    #agregar metodo que admita solo al admin crear un post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'crear'
        })
        return context

class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Actualizar'
        })
        return context
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

# metodo para contar los likes de un usuario
def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail-post', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail-post', slug=slug)
    


