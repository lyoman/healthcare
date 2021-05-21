from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserModelAdmin(UserAdmin):
    list_display 	    = ["id", "username", "email",  "phone_number", "is_doctor", "is_specialist", "is_physician", "is_active", "is_staff", "is_superuser", "updated", "timestamp"]
    list_display_links  = ["updated", "username"]
    list_editable		= ["is_active"]
    list_filter			= ["is_doctor", "is_specialist", "is_physician", "is_staff", "is_superuser", "updated", "timestamp", "email", "phone_number"]
    search_fields		= ["username", "email", "phonenumber"]
    class Meta:
        model = User
  
admin.site.register(User, UserModelAdmin)


# from accounts.models import User
# import csv

# wine_csv = open('Book1.csv', 'r', encoding = "utf-8") 
# reader = csv.reader(wine_csv)
# headers = next(reader, None)[1:]

# for row in reader:  
#    wine_dict = {}
#    for h, val in zip(headers, row[1:]):
#       wine_dict[h] = val
#    wine = User.objects.create(**wine_dict)

# wine_csv.close()  