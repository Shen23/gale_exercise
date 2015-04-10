from django.conf.urls import patterns, include, url
from articles import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns(
	'',
	url(r'^$', views.ArticleListView.as_view(), name="article"),


    url(r'^articles/(?P<pk>\d+)$', views.ArticleDetail.as_view(), name="article_detail"),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

