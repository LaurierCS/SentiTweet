from django.contrib import admin
from .models import Query,Result, Profile

admin.site.register(Profile)
admin.site.register(Query)
admin.site.register(Result)

