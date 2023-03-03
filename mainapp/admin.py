from django.contrib import admin
from.models import *

admin.site.site_header = "farmersCon Admindashboard"
# Register your models here.
admin.site.register(Speakers)
admin.site.register(Sponsers)
admin.site.register(Faqs)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Blog_post)
admin.site.register(Questions)
admin.site.register(Registration)
