from django.contrib import admin
from .models import ToDo
from .models import ToMeet
from .models import ToHabits

admin.site.register(ToDo)

admin.site.register(ToMeet)

admin.site.register(ToHabits)
