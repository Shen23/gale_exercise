from django.conf.urls import include, url
from articles import views


urlpatterns = [
	url(r'^$', views.ArticleListView.as_view(), name="article"),


    url(r'^articles/(?P<pk>\d+)$', views.ArticleDetail.as_view(), name="article_detail"),
    ]

