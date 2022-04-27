from tokenize import Name
from django.contrib import admin
from .models import City
from .models import Clothers
from .models import Food
from .models import Actors
from .models import Singers
from .models import Films
from .models import Posts
from .models import Category
from .models import Registration
# Register your models here.
class PostsAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(City)

admin.site.register(Clothers)

admin.site.register(Food)

admin.site.register(Singers)

admin.site.register(Actors)

admin.site.register(Films)

admin.site.register(Posts)

admin.site.register(Category)

admin.site.register(Registration)