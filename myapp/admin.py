from django.contrib import admin
from .models import Contact,Admin,Profile,Book_artist,Review,User


# Register your models here.
admin.site.register(Contact)
admin.site.register(Admin)
admin.site.register(User) 
admin.site.register(Profile)
admin.site.register(Book_artist)
admin.site.register(Review)


