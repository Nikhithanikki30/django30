from django.contrib import admin

from home.models import Roomservice
from home.models import Contact
from home.models import RoomBooking
from home.models import Feedback


# Register your models here.
admin.site.register(Contact)
admin.site.register(Roomservice)
admin.site.register(RoomBooking)
admin.site.register(Feedback)




