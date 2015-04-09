from django.conf.urls import patterns, include, url
from articles import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ArticleListView.as_view(), name="article"),
    url(r'^articles/(?P<title>\S+)$', views.ArticleDetail.as_view(), name="article_detail"),
)