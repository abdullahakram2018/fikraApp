from django.contrib import admin
from accountapp.models import *
# Register your models here.

admin.site.register(TypeDoc)
admin.site.register(Currency)
admin.site.register(FinancialCenter)
admin.site.register(Account)
admin.site.register(Unit)
admin.site.register(Item)
admin.site.register(Store)
admin.site.register(Entry)
admin.site.register(AccountEntry)
admin.site.register(EntryDetails)