from django.db import models
from datetime import date
from django.contrib.auth import get_user_model

User = get_user_model()

today = date.today()


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    # In admin dashboard for Contacts - each row is shown as contact object(1) - to change it to name field of each contact:
    def __str__(self):
        return self.name + " - " + self.email


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)  # Primary Key
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=20, default="Sakshi")
    tags = models.CharField(max_length=40, default="")
    date = models.CharField(max_length=30, default=today.strftime("%b %d, %Y"))
    content = models.TextField()
    short_desc = models.CharField(max_length=300, default="")
    slug = models.CharField(max_length=100)
    # time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="img/", default="")

    def __str__(self):  # Tunder method
        return self.title


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)
    mobile = models.PositiveIntegerField(blank=True)

    def full_name(self):
        return " ".join([self.first_name, self.last_name])


class Education(models.Model):
    DEGREE_CHOICES = (
        ("Mtech/MA/MSc/MCom/MBA", "Masters"),
        ("BE/Btech/BA/BSc/BCom", "Bachelor"),
        ("12th", "High School"),
    )
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    stream = models.CharField(max_length=100)
    passing_year = models.DateField()
    result = models.CharField(max_length=5)


class Experience(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()


class Skills(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    skill_detail = models.TextField()


class Projects(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    project_detail = models.TextField()


class About(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    about_detail = models.TextField()


class Awards(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    award_detail = models.TextField()


class resume(models.Model):
    # user1 = models.ForeignKey(
    #     User.get_username, on_delete=models.CASCADE, default="Unknown"
    # )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)
    mobile = models.PositiveIntegerField(blank=True)

    degree = models.CharField(max_length=100)
    varsity_name = models.CharField(max_length=100)
    passing_year = models.DateField()
    result = models.CharField(max_length=10, blank=True)

    title = models.CharField(max_length=100, blank=True)
    place = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    description = models.TextField(blank=True)

    skill_detail = models.TextField()
    project_detail = models.TextField(blank=True)
    about_detail = models.TextField(blank=True)
    award_detail = models.TextField(blank=True)
