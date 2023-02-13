from django.contrib import admin
from.models import *

admin.site.site_header = "farmersCon Admindashboard"
# Register your models here.
admin.site.register(Speakers)
admin.site.register(Sponsers)
admin.site.register(Faqs)
