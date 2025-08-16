from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm, PostModelForm, CommentForm
from .models import Post, Profile, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from taggit.models import Tag

# Create your views here.
class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login/')
    template_name = 'blog/register.html'

@login_required
def profile_view(request):
    # Ensure the user has a profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')  # name of the URL pattern, not the path
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'blog/profile.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostModelForm
    template_name = 'blog/post_form.html'
    login_url = 'login/'
    success_url = reverse_lazy('posts')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    form_class = PostModelForm
    template_name = 'blog/post_form.html'
    login_url = 'login/'
    success_url = reverse_lazy('posts')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def test_func(self):
        return self.get_object().author == self.request.user
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('/posts/')
    login_url = 'login/'

    def test_func(self):
        return self.get_object().author == self.request.user
    
# PostDetailView with embedded comments using ListView
class PostDetailView(ListView):
    model = Comment
    template_name = 'blog/blog_post_detail.html'
    context_object_name = 'comments'

    def get_queryset(self):
        self.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return Comment.objects.filter(post=self.post).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post
        context['form'] = CommentForm
        return context

# Create Comment (handled on a separate URL)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_post_detail', kwargs={'pk': self.kwargs['pk']})
    
# Update comment view
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return comment.user == self.request.user

    def get_success_url(self):
        return reverse('blog_post_detail', kwargs={'pk': self.object.post.pk})


# Delete comment view
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'
    login_url = 'login'

    def test_func(self):
        comment = self.get_object()
        return comment.user == self.request.user

    def get_success_url(self):
        return reverse_lazy('blog_post_detail', kwargs={'pk': self.object.post.pk})
    
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
    
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__slug=tag_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context