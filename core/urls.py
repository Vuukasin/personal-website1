from django.urls import path

from .views import blog_view, home_view, resume_view

urlpatterns = [

    path('', home_view, name="home"),
    path('blog/', blog_view, name="blog"),
    path('resume/', resume_view, name="resume"),

]