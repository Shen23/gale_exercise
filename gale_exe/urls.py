from django.conf.urls import include, url
from django.contrib import admin
from articles import views
from articles.models import Article


urlpatterns = [
#url('^$', 'articles.views.home', name = 'home'),
    #url('^$', views.ArticleListView.as_view(model = Article)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^', include('articles.urls')),
]
    # Examples:
    # url(r'^$', 'gale_exe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url('^$', 'articles.views.home', name = 'home'),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^markdown/', include("django_markdown.urls")),