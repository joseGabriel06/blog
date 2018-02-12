from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.views.generic import(CreateView, DeleteView)
from .models import Post
from .forms import PostForm

class ClassHomeView(ListView):
	model = Post
	def get_queryset(self, *args, **kwargs):
		qs = super(ClassHomeView,self).get_queryset(*args,**kwargs)
		return qs
class ClassPostDetailView(DetailView):
	model = Post
	
class ClassPostCreateView(CreateView):
	form_class = PostForm

	def form_valid(self, form):
		formpost = form.save(commit=False)
		formpost.author = self.request.user
		formpost.save()
		self.object = formpost
		return redirect('home')
	