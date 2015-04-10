from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class ArticleQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish = True )

class Article(models.Model):
	title = models.CharField(max_length = 200)
	author = models.CharField(max_length = 50)
	pub_date = models.DateTimeField('date published')
	category = models.CharField(max_length = 50)
	image = models.ImageField()
	preview = models.CharField(max_length = 1000)
	text = models.TextField()
	publish = models.BooleanField(default = True)

	
	objects = ArticleQuerySet.as_manager()

	def get_absolute_url(self):
		return reverse("article_detail", kwargs = {"title": self.title})

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Article Entry"
		verbose_name_plural = "Artries"
		ordering = ["-pub_date"]
 
class Opt_images(models.Model):
	article = models.ForeignKey(Article, related_name = 'images')
	opt_images = models.ImageField()


	


