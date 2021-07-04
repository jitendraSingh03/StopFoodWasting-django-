from django.contrib import admin
from .models import userpost,orderBook,moneyRefund,contect,feedback,account
# Register your models here.
admin.site.register(orderBook)

admin.site.register(userpost)


admin.site.register(moneyRefund)

admin.site.register(contect)

admin.site.register(feedback)

admin.site.register(account)

