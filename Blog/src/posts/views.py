from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Post, Like, PostView
from .forms import PostForm, CommentForm, LoginForm
from django.contrib.auth import admin as ad
# Create your views here.


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = '/'

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = 'login/'



class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    login_url = 'login/'

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

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    login_url = '/login'
    success_url = '/'
    permission_denied_message = 'usted no esta registrado'

    #agregar metodo que admita solo al admin crear un post
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'crear'
        })
        return context

#debe requerir login 
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
#debe requerir login y una template    
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
    


