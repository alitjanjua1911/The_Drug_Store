from django.db import models

# Create your models here.
class about(models.Model):
    heading=models.CharField(max_length=100, null=True)
    description1=models.CharField(max_length=300, null=True)
    description2=models.CharField(max_length=300, null=True)
    photo = models.ImageField(upload_to='static/assets/aboutImages', default='assets/img/about/about.jpg')
    status=models.NullBooleanField(default=True)

    def __str__(self):
        return self.heading

class aboutCreativeTeam(models.Model):
    name=models.CharField(max_length=50, null=True)
    designation=models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=400, null=True)
    status = models.NullBooleanField(default=True)
    photo=models.ImageField(upload_to='static/assets/creativeTeamImages', default='assets/img/team/team_member_1.jpg')

class aboutTestimonials(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=400, null=True)
    photo = models.ImageField(upload_to='static/assets/testimonialsImages', default='assets/img/testimonial/team-member-1.jpg')
    status = models.NullBooleanField(default=True)