from django.contrib import admin
from django.urls import path, include
import resume.views as resume_views
import user_auth.views as user_auth_views
from .views import GeneratePDF

urlpatterns = [
    path("", resume_views.index, name="index"),
    path("about/", resume_views.about, name="about"),
    path("contact/", resume_views.contact, name="contact"),
    path("blog/", resume_views.blog, name="blog"),
    path("blog_post/<str:slug>", resume_views.blog_post, name="blog_post"),
    path("portfolio/", resume_views.portfolio, name="portfolio"),
    path("resume/", resume_views.resume, name="resume"),
    path("resume_2/", resume_views.resume_2, name="resume_2"),
    path("home/", user_auth_views.home, name="home"),
    path("make_cv1/", resume_views.make_cv1, name="make_cv1"),
    path("make_cv2/", resume_views.make_cv2, name="make_cv2"),
    path("resumefill/", resume_views.resumeFill, name="resume_fill"),
    path("resumeview/", resume_views.resumeView, name="resume_view"),
    # path("resume_form/", views.resume_form, name="resume_form"),
]
