from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    #fields = '__all__'
    fields = ['post_round', 'post_day', 'title', 'progress', 'thoughts', 'work_link']

    def form_valid(self, form):
        """
        Add author to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Call super-class form validation behaviour
        return super(BlogCreateView, self).form_valid(form)


class BlogUpdateView(UpdateView):
    model = Post
    fields = ['post_round', 'post_day', 'title', 'progress', 'thoughts', 'work_link']
    template_name = 'post_edit.html'

class BlogDeleteView(DeleteView):
    model=Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
