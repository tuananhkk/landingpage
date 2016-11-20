from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactModelAdmin(admin.ModelAdmin):
	list_display = [Contact, "email", "phone", "timestamp"]
	list_filter = ["timestamp"]
	search_fields = ["name", "email", "phone","content"]

	class Meta:
		model = Contact

admin.site.register(Contact, ContactModelAdmin)