import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from resume.models import Contact, Blog
from django.shortcuts import redirect, render

# Create your views here.

from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf  # created in step 4


from django.contrib.sites.requests import RequestSite
from django.contrib.auth import get_user_model
from .models import (
    PersonalInfo,
    Education,
    Experience,
    Skills,
    About,
    Awards,
    Projects,
    resume,
)
from .forms import (
    PersonalInfoForm,
    EducationForm,
    ExperienceForm,
    SkillsForm,
    AwardsForm,
    AboutForm,
    ProjectsForm,
)

User = get_user_model()


# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    context = {"success": False}
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        context = {"success": True}
        print("Tha data has been written to the DB")
    return render(request, "contact.html", context)


def blog(request):
    blogs = Blog.objects.all()
    context = {"blogs": blogs}
    # for blog in blogs:

    # image = Image.open(blog.image.url)
    # image.thumbnail((650, 400))
    # image.save()
    # print(image.size)
    return render(request, "blog.html", context)


def blog_post(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {"blog": blog}
    return render(request, "blog-post.html", context)


def portfolio(request):
    return render(request, "portfolio.html")


# def cv1(request):
#     return render(request, "cv1.html")


# def cv2(request):
#     return render(request, "cv2.html")


def resume_form(request):
    return render(request, "resume_form.html")


def resumeFill(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        address = request.POST["address"]
        email = request.POST["email"]
        github = request.POST["github"]
        linkedin = request.POST["linkedin"]
        website = request.POST["website"]
        mobile = request.POST["mobile"]

        degree = request.POST["degree"]
        varsity_name = request.POST["varsity_name"]
        passing_year = request.POST["passing_year"]
        result = request.POST["result"]

        title = request.POST["title"]
        place = request.POST["place"]
        start_date = request.POST["start_date"]
        end_date = request.POST["end_date"]
        description = request.POST["description"]

        skill_detail = request.POST["skill_detail"]
        project_detail = request.POST["project_detail"]
        about_detail = request.POST["about_detail"]
        award_detail = request.POST["award_detail"]

        my_resume = resume.objects.create(
            first_name=first_name,
            last_name=last_name,
            address=address,
            email=email,
            github=github,
            linkedin=linkedin,
            website=website,
            mobile=mobile,
            degree=degree,
            varsity_name=varsity_name,
            passing_year=passing_year,
            result=result,
            title=title,
            place=place,
            start_date=start_date,
            end_date=end_date,
            description=description,
            skill_detail=skill_detail,
            project_detail=project_detail,
            about_detail=about_detail,
            award_detail=award_detail,
        )

        my_resume.save()
        return redirect("home")
    return render(request, "input_file.html")


def make_cv1(request):
    last_entry = resume.objects.all().last()
    first_name = last_entry.first_name
    last_name = last_entry.last_name
    address = last_entry.address
    email = last_entry.email
    github = last_entry.github
    linkedin = last_entry.linkedin
    website = last_entry.website
    mobile = last_entry.mobile

    degree = last_entry.degree
    varsity_name = last_entry.varsity_name
    passing_year = last_entry.passing_year
    result = last_entry.result

    title = last_entry.title
    place = last_entry.place
    start_date = last_entry.start_date
    end_date = last_entry.end_date
    description = last_entry.description

    skill_detail = last_entry.skill_detail
    project_detail = last_entry.project_detail
    about_detail = last_entry.about_detail
    award_detail = last_entry.award_detail

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "email": email,
        "github": github,
        "linkedin": linkedin,
        "website": website,
        "mobile": mobile,
        "degree": degree,
        "varsity_name": varsity_name,
        "passing_year": passing_year,
        "result": result,
        "title": title,
        "place": place,
        "start_date": start_date,
        "end_date": end_date,
        "description": description,
        "skill_detail": skill_detail,
        "project_detail": project_detail,
        "about_detail": about_detail,
        "award_detail": award_detail,
    }
    if request.method == "GET":
        return render(
            request, "cv1.html", context
        )  # , context_instance=RequestContext(request))

    return render(request, "cv1.html")


def make_cv2(request):
    last_entry = resume.objects.all().last()
    first_name = last_entry.first_name
    last_name = last_entry.last_name
    address = last_entry.address
    email = last_entry.email
    github = last_entry.github
    linkedin = last_entry.linkedin
    website = last_entry.website
    mobile = last_entry.mobile

    degree = last_entry.degree
    varsity_name = last_entry.varsity_name
    passing_year = last_entry.passing_year
    result = last_entry.result

    title = last_entry.title
    place = last_entry.place
    start_date = last_entry.start_date
    end_date = last_entry.end_date
    description = last_entry.description

    skill_detail = last_entry.skill_detail
    project_detail = last_entry.project_detail
    about_detail = last_entry.about_detail
    award_detail = last_entry.award_detail

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "email": email,
        "github": github,
        "linkedin": linkedin,
        "website": website,
        "mobile": mobile,
        "degree": degree,
        "varsity_name": varsity_name,
        "passing_year": passing_year,
        "result": result,
        "title": title,
        "place": place,
        "start_date": start_date,
        "end_date": end_date,
        "description": description,
        "skill_detail": skill_detail,
        "project_detail": project_detail,
        "about_detail": about_detail,
        "award_detail": award_detail,
    }
    if request.method == "GET":
        return render(
            request, "cv2.html", context
        )  # , context_instance=RequestContext(request))

    return render(request, "cv2.html")


def resume_2(request):
    last_entry = resume.objects.all().last()
    first_name = last_entry.first_name
    last_name = last_entry.last_name
    address = last_entry.address
    email = last_entry.email
    github = last_entry.github
    linkedin = last_entry.linkedin
    website = last_entry.website
    mobile = last_entry.mobile

    degree = last_entry.degree
    varsity_name = last_entry.varsity_name
    passing_year = last_entry.passing_year
    result = last_entry.result

    title = last_entry.title
    place = last_entry.place
    start_date = last_entry.start_date
    end_date = last_entry.end_date
    description = last_entry.description

    skill_detail = last_entry.skill_detail
    project_detail = last_entry.project_detail
    about_detail = last_entry.about_detail
    award_detail = last_entry.award_detail

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "email": email,
        "github": github,
        "linkedin": linkedin,
        "website": website,
        "mobile": mobile,
        "degree": degree,
        "varsity_name": varsity_name,
        "passing_year": passing_year,
        "result": result,
        "title": title,
        "place": place,
        "start_date": start_date,
        "end_date": end_date,
        "description": description,
        "skill_detail": skill_detail,
        "project_detail": project_detail,
        "about_detail": about_detail,
        "award_detail": award_detail,
    }
    if request.method == "GET":
        return render(
            request, "resume2.html", context
        )  # , context_instance=RequestContext(request))

    return render(request, "resume2.html")


def resumeView(request):
    last_entry = resume.objects.all().last()
    first_name = last_entry.first_name
    last_name = last_entry.last_name
    address = last_entry.address
    email = last_entry.email
    github = last_entry.github
    linkedin = last_entry.linkedin
    website = last_entry.website
    mobile = last_entry.mobile

    degree = last_entry.degree
    varsity_name = last_entry.varsity_name
    passing_year = last_entry.passing_year
    result = last_entry.result

    title = last_entry.title
    place = last_entry.place
    start_date = last_entry.start_date
    end_date = last_entry.end_date
    description = last_entry.description

    skill_detail = last_entry.skill_detail
    project_detail = last_entry.project_detail
    about_detail = last_entry.about_detail
    award_detail = last_entry.award_detail

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "email": email,
        "github": github,
        "linkedin": linkedin,
        "website": website,
        "mobile": mobile,
        "degree": degree,
        "varsity_name": varsity_name,
        "passing_year": passing_year,
        "result": result,
        "title": title,
        "place": place,
        "start_date": start_date,
        "end_date": end_date,
        "description": description,
        "skill_detail": skill_detail,
        "project_detail": project_detail,
        "about_detail": about_detail,
        "award_detail": award_detail,
    }
    if request.method == "GET":
        return render(
            request, "resume.html", context
        )  # , context_instance=RequestContext(request))

    return render(request, "resume.html")


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template("resume2.html")
        last_entry = resume.objects.all().last()
        first_name = last_entry.first_name
        last_name = last_entry.last_name
        address = last_entry.address
        email = last_entry.email
        github = last_entry.github
        linkedin = last_entry.linkedin
        website = last_entry.website
        mobile = last_entry.mobile

        degree = last_entry.degree
        varsity_name = last_entry.varsity_name
        passing_year = last_entry.passing_year
        result = last_entry.result

        title = last_entry.title
        place = last_entry.place
        start_date = last_entry.start_date
        end_date = last_entry.end_date
        description = last_entry.description

        skill_detail = last_entry.skill_detail
        project_detail = last_entry.project_detail
        about_detail = last_entry.about_detail
        award_detail = last_entry.award_detail

        context = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "email": email,
            "github": github,
            "linkedin": linkedin,
            "website": website,
            "mobile": mobile,
            "degree": degree,
            "varsity_name": varsity_name,
            "passing_year": passing_year,
            "result": result,
            "title": title,
            "place": place,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
            "skill_detail": skill_detail,
            "project_detail": project_detail,
            "about_detail": about_detail,
            "award_detail": award_detail,
        }
        html = template.render(context)
        pdf = render_to_pdf("resume2.html", context)
        if pdf:
            response = HttpResponse(pdf, content_type="/pdf")
            filename = "Resume_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response["Content-Disposition"] = content
            return response
        return HttpResponse("Not found")


"""
          Procfile - heroku
web: waitress-serve --port=8000 portfolio.wsgi:application
web: waitress-serve --port=$PORT portfolio.wsgi:application
"""
