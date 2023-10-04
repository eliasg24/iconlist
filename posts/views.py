"""Posts views."""

# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.images import ImageFile
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, TemplateView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post

class PostsFeedView(ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('position',)
    paginate_by = 30
    context_object_name = 'posts'


class PostDetailView(DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(TemplateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

    def post(self, request):
        r = request.POST
        title = r.get("title", None)
        photo = request.FILES["photo"]
        position = r.get("position", None)

        posts = Post.objects.filter(position__gte=position)
        for post in posts:
            post.position += 1
            post.save()

        print("photo")
        print(r)
        print(photo)

        Post.objects.create(title=title,
                            photo=photo,
                            position=position)
        
        return HttpResponseRedirect(reverse_lazy('posts:feed'))


