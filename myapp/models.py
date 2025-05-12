from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	message=models.TextField()

	def __str__(self):
		return self.name

class Admin(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=30)
    sec_from = models.DateField(auto_now_add=True)
    profile_pic = models.FileField(upload_to='profile',default='avtar.png')

    def __str__(self):
        return self.name
    
    
    
	
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	address=models.TextField()
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default="customer")

	def __str__(self):
		return self.fname


class Profile(models.Model):
	CHOICE1=(
			('singer','singer'),
			('musician','musician'),
			('painter','painter'),
			('dancer','dancer'),
            ('photographer','photographer'),
            ('sculptor','sculptor')
		)
	CHOICE2=(
			('Michael Jackson','Michael Jackson'),
			('Arijit Singh','Arijit Singh'),
			('Justin Bieber','Justin Bieber'),
            ('M.F.Hussain','M.F. Husain'),
			('Guru Randhava','Guru Randhava'),
			('Zakir Hussain','Zakir Hussain'),
			('Amjad Ali Khan','Amjad Ali Khan'),
			('Shilpa Gupta','Shilpa Gupta'),
			('Paresh Maity','Paresh Maity'),
			('Parbhu Deva','Parbhu Deva'),
            ('Atul Kasbekar','Atul Kasbekar')
            
            
		)
	artist_artist=models.ForeignKey(User,on_delete=models.CASCADE)
	artist_type=models.CharField(max_length=100,choices=CHOICE1)
	artist_name=models.CharField(max_length=100,choices=CHOICE2)
	artist_desc=models.TextField()
	artist_image=models.ImageField(upload_to='myapp/static/img/artist')
	artist_price=models.IntegerField()
	'''
	artist_performance_desc=models.TextField()
	artist_performance_image=models.ImageField(upload_to=myapp/static/img/artist)
	'''

	def __str__(self):
		return self.artist_artist.fname+" - "+self.artist_type+" - "+self.artist_name



class Book_artist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
	artist_type=models.CharField(max_length=100,blank=True,null=True)
	artist_name=models.CharField(max_length=100,blank=True,null=True)
	event_name=models.CharField(max_length=100,blank=True,null=True)
	event_date=models.DateField(blank=True,null=True)
	event_start_time=models.TimeField(blank=True,null=True)
	event_end_time=models.TimeField(blank=True,null=True)
	event_venue=models.TextField(blank=True,null=True)
	remarks=models.TextField(blank=True,null=True)
	booking_date=models.DateTimeField(default=timezone.now)
	status=models.CharField(max_length=100,default="pending")


	def __str__(self):
		return self.user.fname+" - "+self.profile.artist_name

class Review(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    message=models.TextField()
 
def __str__(self):
	return self.name
    
	


