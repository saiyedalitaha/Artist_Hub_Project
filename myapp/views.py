from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Contact,User,Profile,Book_artist
from django.conf import settings

from .models import *

# Create your views here.
def indexpage(request):
    return render(request,'indexpage.html')



def admin_page(request):
    return render(request,'admin_page.html')


def feedback(request):
    return render(request,'feedback.html')



def about(request):
    profiles=Profile.objects.all()
    return render(request,'about.html',{'profiles':profiles})


def customer_review(request):
    if request.method=="POST":
        Review.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            message=request.POST['message'],
        )
        msg= "Customer Review saved Successfully"
        return render(request,'customer_review.html',{'msg':msg})
    else:
        return render(request,'customer_review.html')

    return render(request,'customer_review.html')


def artist_review(request):
    if request.method=="POST":
        Review.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            message=request.POST['message'],
        )
        msg= "Artist Review saved Successfully"
        return render(request,'artist_review.html',{'msg':msg})
    else:
        return render(request,'artist_review.html')

    return render(request,'artist_review.html')


def reviews(request):
    return render(request,'reviews.html')



def artist_header(request):
    return render(request,'artist_header.html')

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            message=request.POST['message'],
        )
        msg= "Contact saved Successfully"
        return render(request,'contact.html',{'msg':msg})
    else:
        return render(request,'contact.html')



def artist_delete_profile(request,pk):
    profile=Profile.objects.get(pk=pk)
    profile.delete()
    return redirect('artist_view_profile')


def artist(request):
    profiles=Profile.objects.all()
    all=len(profiles)
    singer=len(Profile.objects.filter(artist_type="singer"))
    musician=len(Profile.objects.filter(artist_type="musician"))
    painter=len(Profile.objects.filter(artist_type="painter"))
    dancer=len(Profile.objects.filter(artist_type="dancer"))
    photographer=len(Profile.objects.filter(artist_type="photographer"))
    sculptor=len(Profile.objects.filter(artist_type="sculptor"))
    return render(request,'artist.html',{'all':all,'profiles':profiles,'singer':singer,'musician':musician,'painter':painter,'dancer':dancer,'photographer':photographer,'sculptor':sculptor})
    
	

def track(request):
    return render(request,'track.html')


def blog_page(request):
    return render(request,'blog_page.html')



def contact(request):
    if request.method=="POST":
        Contact.objects.create(
		name=request.POST['name'],
		email=request.POST['email'],
		mobile=request.POST['mobile'],
		message=request.POST['message'],)
        msg="Contact Saved Succesfully"
        return render(request,'contact.html',{'msg':msg})
    else:
     return render(request,'contact.html')
    

def signup(request):
    if request.method=="POST":
        try:
            User.object.get(email=request.POST['email'])
            msg="Email Already Registered"
            return render(request,'signup.html',{'msg':msg})
		
        except: 
            if request.POST['password'] == request.POST['cpassword']:
	            User.objects.create(
					usertype=request.POST['usertype'],
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					password=request.POST['password'],)
            msg='User signup Successfully'
            return render(request,'login.html',{'msg':msg})
        else:
            msg ="password and confirm password are not match"	
            return render(request,'signup.html',{'msg':msg})
    else:
            return render(request,'signup.html')	
        
def login(request):
    try:
        user = User.objects.get(email=request.session['email'])
        return render(request,'indexpage.html',{'user':user})
    except:
        if request.method == 'POST':
            try:
                user = User.objects.get(email=request.POST['email'])
                if request.POST['password'] == user.password:
                    request.session['email'] = user.email
                    request.session['fname'] = user.fname

                    return render(request,'indexpage.html',{'user':user})
                return render(request,'login.html',{'msg':'Incorrect Password'})
            except:
                return render(request,'signup.html',{'msg':'Account does not exist please sign up first!!'})
        return render(request,'login.html')

def profile(request):
    user=User.objects.get(email=request.session['email'])
    if user.usertype=="customer":
        if request.method=="POST":
            user.usertype=request.POST['usertype']
            user.fname=request.POST['fname']
            user.lname=request.POST['lname']
            user.email=request.POST['email']
            user.mobile=request.POST['mobile']
            user.address=request.POST['address']
        
            user.save()
            msg="User update successfully"
            return render(request,'profile.html',{'msg':msg,'user':user,})
        else:
            return render(request,'profile.html',{'user':user})
    else:
        if request.method=="POST":
            user.usertype=request.POST['usertype']
            user.fname=request.POST['fname']
            user.lname=request.POST['lname']
            user.email=request.POST['email']
            user.mobile=request.POST['mobile']
            user.address=request.POST['address']
            user.save()
            msg="User update successfully"
            return render(request,'artist_profile.html',{'msg':msg,'user':user})
        else:
            return render(request,'artist_profile.html',{'user':user})
            
            




def bookings(request):
	user=User.objects.get(email=request.session['email'])
	profile=Profile.objects.filter(artist_artist=user)
	print("Profile : ",profile[0].artist_artist)
	booking=Book_artist.objects.all()
	book_artist=[]
	for i in booking:
		if i.profile.artist_artist==profile[0].artist_artist:
			book_artist.append(i)
	
	return render(request,'bookings.html',{'booking':book_artist})




def view_booking(request):
    user=User.objects.get(email=request.session['email'])
    booking=Book_artist.objects.filter(user=user)
    return render(request,'view_booking.html',{'booking':booking})







def reject_booking(request,pk):
    booking=Book_artist.objects.get(pk=pk)
    booking.status="rejected"
    booking.save()
    user=User.objects.get(email=request.session['email'])
    profile=Profile.objects.filter(artist_artist=user)
    booking=Book_artist.objects.filter(status="rejected")
    book_artist=[]
    for i in booking:
        if i.profile.artist_artist==profile[0].artist_artist:
            book_artist.append(i)
    return render(request,'rejected_booking.html',{'booking':book_artist})
        
      
def accepted_booking(request):
	user=User.objects.get(email=request.session['email'])
	profile=Profile.objects.filter(artist_artist=user)
	booking=Book_artist.objects.filter(status="accepted")
	book_artist=[]
	for i in booking:
		if i.profile.artist_artist==profile[0].artist_artist:
			book_artist.append(i)
	return render(request,'accepted_booking.html',{'booking':book_artist})      
 
def accept_booking(request,pk):
	booking=Book_artist.objects.get(pk=pk)
	booking.status="accepted"
	booking.save()
	user=User.objects.get(email=request.session['email'])
	profile=Profile.objects.filter(artist_artist=user)
	booking=Book_artist.objects.filter(status="accepted")
	book_artist=[]
	for i in booking:
		if i.profile.artist_artist==profile[0].artist_artist:
			book_artist.append(i)
	return render(request,'accepted_booking.html',{'booking':book_artist})
 
 
 
  
        

def rejected_booking(request):
    user=User.objects.get(email=request.session['email'])
    profile=Profile.objects.filter(artist_artist=user)
    booking=Book_artist.objects.filter(status="rejected")
    book_artist=[]
    for i in booking:
        if i.profile.artist_artist==profile[0].artist_artist:
            book_artist.append(i)
    return render(request,'rejected_booking.html',{'booking':book_artist})


def confirmed_booking(request):
    user=User.objects.get(email=request.session['email'])
    profile=Profile.objects.filter(artist_artist=user)
    booking=Book_artist.objects.filter(status="paid")
    book_artist=[]
    for i in booking:
        if i.profile.artist_artist==profile[0].artist_artist:
            book_artist.append(i)
    return render(request,'confirmed_booking.html',{'booking':book_artist})


def pending_booking(request):
    user=User.objects.get(email=request.session['email'])
    profile=Profile.objects.filter(artist_artist=user)
    booking=Book_artist.objects.filter(status="pending")
    book_artist=[]
    for i in booking:
        if i.profile.artist_artist==profile[0].artist_artist:
            book_artist.append(i)
    return render(request,'pending_booking.html',{'booking':book_artist})
    

    
def customer_confirmed_booking(request):
    user=User.objects.get(email=request.session['email'])
    booking=Book_artist.objects.filter(user=user)
    return render(request,'customer_confirmed_booking.html',{'booking':booking})

def customer_pending_booking(request):
    user=User.objects.get(email=request.session['email'])
    booking=Book_artist.objects.filter(user=user)
    return render(request,'customer_pending_booking.html',{'booking':booking})

def customer_accepted_booking(request):
    net_price=0
    user=User.objects.get(email=request.session['email'])
    booking=Book_artist.objects.filter(user=user,status="accepted")
    for i in booking:
        net_price=net_price+i.profile.artist_price
    return render(request,'customer_accepted_booking.html',{'booking':booking,'net_price':net_price})
    
    
def customer_canceled_booking(request):
    user=User.objects.get(email=request.session['email'])
    booking=Book_artist.objects.filter(user=user)
    return render(request,'customer_canceled_booking.html',{'booking':booking})


def all_bookings(request):
	user=User.objects.get(email=request.session['email'])
	profile=Profile.objects.filter(artist_artist=user)
	print("Profile : ",profile[0].artist_artist)
	booking=Book_artist.objects.all()
	book_artist=[]
	for i in booking:
		if i.profile.artist_artist==profile[0].artist_artist:			book_artist.append(i)
	
	return render(request,'bookings.html',{'booking':book_artist})		



def change_password(request):
    user=User.objects.get(email=request.session['email'])
    if user.usertype=="customer":
        if request.method=="POST":
            if user.password==request.POST['old_password']:
                if request.POST['new_password']==request.POST['cnew_password']:
                    user.password=request.POST['new_password']
                    user.save()
                    return redirect('logout')
                else:
                    msg="New password and confirm new password does not marched"
                    return render(request,'change_password.html',{'msg':msg})
            else:
                    msg="Old password is incorrect"
                    return render(request,'change_password.html',{'msg':msg})
        else:
                return render(request,'change_password.html')
    else:
        if request.method=="POST":
            if user.password==request.POST['old_password']:
                if request.POST['new_password']==request.POST['cnew_password']:
                    user.password=request.POST['new_password']
                    user.save()
                    return redirect('logout')
                else:
                    msg="New password and confirm New password does not match"
                    return render(request,'artist_change_password.html',{'msg':msg})
            else:
                msg="Old passowrd is incorrect"
                return render(request,'artist_change_password.html',{'msg': msg})
        else:
            return render(request,'artist_change_password.html')
                    

def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    except:
        return render(request,'login.html')
        
            
def artist_index(request):
      return render(request,'artist_index.html')
  

def artist_add_profile(request):
    if request.method=="POST":
        artist_artist=User.objects.get(email=request.session['email'])
        Profile.objects.create(
            artist_artist=artist_artist,
            artist_type=request.POST['artist_type'],
            artist_name=request.POST['artist_name'],
            artist_desc=request.POST['artist_desc'],
            artist_price=request.POST['artist_price'],
            artist_image=request.FILES['artist_image'],
            )
        msg = "Artist added successfully"
        return render(request,'artist_add_profile.html',{'msg':msg})
    else:
        return render(request,'artist_add_profile.html')
    
def artist_view_profile(request):
	artist_artist=User.objects.get(email=request.session['email'])
	profiles=Profile.objects.filter(artist_artist=artist_artist)
	return render(request,'artist_view_profile.html',{'profiles' :profiles})


def artist_edit_profile(request,pk):
	profile=Profile.objects.get(pk=pk)
	if request.method=="POST":
		profile.artist_type=request.POST['artist_type']
		profile.artist_name=request.POST['artist_name']
		profile.artist_desc=request.POST['artist_desc']
		profile.artist_price=request.POST['artist_price']
		try:
			profile.artist_image=request.FILES['artist_image']
		except:
			pass
		profile.save()	
		return render(request,'artist_edit_profile.html',{'profile' :profile})	
	else:
		return render(request,'artist_edit_profile.html',{'profile' :profile})



    
       

def artist_detail(request,pk):
    profile=Profile.object.get(pk=pk)
    return render(request,'artist_detail.html',{'profile':profile})


def artist_delete_profile(request,pk):
	profile=Profile.objects.get(pk=pk)
	profile.delete()
	return redirect('artist_view_profile')

def book_artist(request,pk):
    profile=Profile.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        Book_artist.objects.create(
            user=user,
            profile=profile,
            artist_type=request.POST['artist_type'],
            artist_name=request.POST['artist_name'],
            event_name=request.POST['event_name'],
            event_date=request.POST['event_date'],
            event_start_time=request.POST['event_start_time'],
            event_end_time=request.POST['event_end_time'],
            event_venue=request.POST['event_venue'],
            remarks=request.POST['remarks']
        )
        msg = "Booking request sent Successfully"
        booking=Book_artist.objects.filter(user=user)
        print(booking)
        return render(request,'customer_pending_booking.html',{'booking':booking})
    else:
        return render(request,'book_artist.html',{'profile':profile})


         
def profile(request):
    user=User.objects.get(email=request.session['email'])
    if user.usertype=="customer":
        if request.method=="POST":
            
            user.usertype=request.POST['usertype']
            user.fname=request.POST['fname']
            user.lname=request.POST['lname']
            user.email=request.POST['email']
            user.mobile=request.POST['mobile']
            user.address=request.POST['address']
            user.save()
            msg="User update successfully"
            return render(request,'profile.html',{'msg':msg,'user':user})
        else:
            return render(request,'profile.html',{'user':user})
    else:
        if request.method=="POST":
            user.usertype=request.POST['usertype']
            user.fname=request.POST['fname']
            user.lname=request.POST['lname']
            user.email=request.POST['email']
            user.mobile=request.POST['mobile']
            user.address=request.POST['address']
            user.save()
            msg="User update successfully"
            return render(request,'artist_profile.html',{'msg':msg,'user':user})
        else:
            return render(request,'artist_profile.html',{'user':user})
			

def search(request):
    artist_artist=User.objects.get(email=request.session['email'])
    profiles=Profile.objects.filter(artist_artist=artist_artist,artist_name__contains=request.POST['search'])
    return render(request,'search.html',{'profiles':profiles})

def artist_singer(request):
    profiles=Profile.objects.all()
    all=len(profiles)
    singer=len(Profile.objects.filter(artist_type="singer"))
    musician=len(Profile.objects.filter(artist_type="musician"))
    painter=len(Profile.objects.filter(artist_type="painter"))
    dancer=len(Profile.objects.filter(artist_type="dancer"))
    photographer=len(Profile.objects.filter(artist_type="photographer"))
    sculptor=len(Profile.objects.filter(artist_type="sculptor"))
    return render(request,'artist.html',{'all':all,'profiles':profiles,'singer':singer,'musician':musician,'painter':painter,'dancer':dancer,'photographer':photographer,'sculptor':sculptor})

def artist_musician(request):
    profiles=Profile.objects.all()
    all=len(profiles)
    singer=len(Profile.objects.filter(artist_type="singer"))
    musician=len(Profile.objects.filter(artist_type="musician"))
    painter=len(Profile.objects.filter(artist_type="painter"))
    dancer=len(Profile.objects.filter(artist_type="dancer"))
    photographer=len(Profile.objects.filter(artist_type="photographer"))
    sculptor=len(Profile.objects.filter(artist_type="sculptor"))
    return render(request,'artist.html',{'all':all,'profiles':profiles,'singer':singer,'musician':musician,'painter':painter,'dancer':dancer,'photographer':photographer,'sculptor':sculptor})



def artist_painter(request):
    profiles=Profile.objects.all()
    all=len(profiles)
    singer=len(Profile.objects.filter(artist_type="singer"))
    musician=len(Profile.objects.filter(artist_type="musician"))
    painter=len(Profile.objects.filter(artist_type="painter"))
    dancer=len(Profile.objects.filter(artist_type="dancer"))
    photographer=len(Profile.objects.filter(artist_type="photographer"))
    sculptor=len(Profile.objects.filter(artist_type="sculptor"))
    return render(request,'artist.html',{'all':all,'profiles':profiles,'singer':singer,'musician':musician,'painter':painter,'dancer':dancer,'photographer':photographer,'sculptor':sculptor})
   
   
   
def artist_dancer(request):
    profiles=Profile.objects.all()
    all=len(profiles)
    singer=len(Profile.objects.filter(artist_type="singer"))
    musician=len(Profile.objects.filter(artist_type="musician"))
    painter=len(Profile.objects.filter(artist_type="painter"))
    dancer=len(Profile.objects.filter(artist_type="dancer"))
    photographer=len(Profile.objects.filter(artist_type="photographer"))
    sculptor=len(Profile.objects.filter(artist_type="sculptor"))
    return render(request,'artist.html',{'all':all,'profiles':profiles,'singer':singer,'musician':musician,'painter':painter,'dancer':dancer,'photographer':photographer,'sculptor':sculptor})
   
   
def artist_photographer(request):
    profiles=Profile.objects.all()
    all=len(profiles)
    singer=len(Profile.objects.filter(artist_type="singer"))
    musician=len(Profile.objects.filter(artist_type="musician"))
    painter=len(Profile.objects.filter(artist_type="painter"))
    dancer=len(Profile.objects.filter(artist_type="dancer"))
    photographer=len(Profile.objects.filter(artist_type="photographer"))
    sculptor=len(Profile.objects.filter(artist_type="sculptor"))
    return render(request,'artist.html',{'all':all,'profiles':profiles,'singer':singer,'musician':musician,'painter':painter,'dancer':dancer,'photographer':photographer,'sculptor':sculptor})



def artist_sculptor(request):
    profiles=Profile.objects.all()
    all=len(profiles)
    singer=len(Profile.objects.filter(artist_type="singer"))
    musician=len(Profile.objects.filter(artist_type="musician"))
    painter=len(Profile.objects.filter(artist_type="painter"))
    dancer=len(Profile.objects.filter(artist_type="dancer"))
    photographer=len(Profile.objects.filter(artist_type="photographer"))
    sculptor=len(Profile.objects.filter(artist_type="sculptor"))
    return render(request,'artist.html',{'all':all,'profiles':profiles,'singer':singer,'musician':musician,'painter':painter,'dancer':dancer,'photographer':photographer,'sculptor':sculptor})

    
    
    
    
    
        
        
        
        
        
        
        
        
	
		
    