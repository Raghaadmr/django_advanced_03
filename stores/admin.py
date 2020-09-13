from django.contrib import admin
from .models import Store



class StoreAdmin(admin.ModelAdmin):
	Display = ('id','name','description')
	Search = ['name','description']
	Add_filter = ['added']
	Clickable =( 'id','name')
	Editable=['description']
admin.site.register(Store,StoreAdmin)
