#from django.http import HttpResponse
from django.views import generic
from django.views.generic.list import ListView
from articles import models
from django.shortcuts import render

# def home(request):
#     context          = {}
#     template = "home.html"
#     return render(request, template, context)

class ArticleListView(generic.ListView):
	queryset = models.Article.objects.published()
	template = "home.html"
	paginate_by = 3

class ArticleDetail(generic.DetailView):
    model = models.Article
    template_name = "article.html"