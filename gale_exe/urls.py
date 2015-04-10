from django.conf.urls import patterns, include, url
from django.contrib import admin
from articles import views
from articles.models import Article
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns(
#url('^$', 'articles.views.home', name = 'home'),
    #url('^$', views.ArticleListView.as_view(model = Article)),
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^', include('articles.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Examples:
    # url(r'^$', 'gale_exe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url('^$', 'articles.views.home', name = 'home'),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^markdown/', include("django_markdown.urls")),