from django.contrib import admin

# Register your models here.
from .models import Room,Menu,Food,Order,Sweet,Chat,Bevage
# Register your models here.
admin.site.register(Room)
admin.site.register(Menu)
admin.site.register(Food)
#admin.site.register(NorthIndianVeg)
#admin.site.register(South_Indian_Veg)
#admin.site.register(NorthIndianNonveg)
#admin.site.register(South_Indian_Nonveg)
admin.site.register(Order)
admin.site.register(Sweet)
admin.site.register(Chat)
admin.site.register(Bevage)