from django.urls import path
from apps.base.views import index , blog_details

urlpatterns = [
    path('', index, name="index"),
    path('blog-details/', blog_details, name="blog_details")
]
