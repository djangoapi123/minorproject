from django.contrib import admin

# Register your models here.


from .models import product  , reconfigure , ls , lsre ,vl, vm



admin.site.register(product)

admin.site.register(reconfigure)

admin.site.register(ls)


admin.site.register(lsre)


admin.site.register(vl)



admin.site.register(vm)