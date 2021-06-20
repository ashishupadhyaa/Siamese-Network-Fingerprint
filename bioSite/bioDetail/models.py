from django.db import models
from django.utils import timezone
from PIL import Image


class UserData(models.Model):
	choice = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
	name = models.CharField(max_length=70)
	email = models.EmailField()
	gender = models.CharField(max_length=5, choices=choice, default='M')
	phone = models.IntegerField()
	address = models.TextField()
	occupation = models.CharField(max_length=100, null=True)
	organisation = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='uploads/')
	date_pub = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

	def save(self):
		super().save()  # saving image first

		img = Image.open(self.photo.path) # Open image using self

		if img.height > 200 or img.width > 200:
			new_img = (200, 200)
			img.thumbnail(new_img)
			img.save(self.photo.path)


class UserFingerprint(models.Model):
	user_data = models.OneToOneField(UserData, verbose_name='Users', on_delete=models.CASCADE, primary_key=True)
	finger_feature = models.JSONField()

