from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView
app_name = BlogConfig.name


urlpatterns = [
    path("blogs/", BlogListView.as_view(), name="blogs"),
    path("blog/detail/<int:pk>/", BlogDetailView.as_view(), name="detail")

]