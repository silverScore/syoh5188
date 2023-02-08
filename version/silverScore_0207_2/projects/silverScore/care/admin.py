from django.contrib import admin

# Register your models here.

from .models import CareRank, AddressInfo

admin.site.register(AddressInfo)  # care_addressinfo 만든 걸 admin에서 관리하기 위함
admin.site.register(CareRank)  # care_carerank 만든 걸 admin에서 관리하기 위함
