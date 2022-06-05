from django.contrib import admin
from .models import *

admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(Income)
admin.site.register(Source)