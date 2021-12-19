
from django.contrib import admin
from .models import Vids


# Register your models here.


class VidsAdmin(admin.ModelAdmin):
    list_display = ('title', 'Embedded_link', 'Date_taken', 'iclass')
    list_filter = ('title', 'Date_taken')
    fieldsets = (
        


        ('Vids Admin', {

            'fields': ('Date_taken', 'title' , 'Embedded_link', 'iclass' 
                       )
        }),
    )


admin.site.register(Vids, VidsAdmin)