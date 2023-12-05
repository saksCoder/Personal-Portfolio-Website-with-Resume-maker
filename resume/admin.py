from django.contrib import admin
from resume.models import (
    Blog,
    Contact,
    Experience,
    PersonalInfo,
    Education,
    Skills,
    Projects,
    About,
    Awards,
    resume,
)


class BlogAdmin(admin.ModelAdmin):
    class Media:  # inner class
        # what to add
        css = {"all": ("css/main.css",)}  # Dictionary

        js = ("js/blog.js",)  # Tuple


# Register your models here.
admin.site.register(Contact)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Experience)
admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Projects)
admin.site.register(About)
admin.site.register(Awards)
admin.site.register(resume)
