from django.contrib import admin

# Register your models here.
from usuarios.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')  # meteu um underline
    exclude = ['autor', ]

    def _autor(self, instance):  # instancia é o "Post" lá do metodo com todas suas variáveis
        return f'{instance.autor.get_full_name()}'

    # mostrar só os posts do proprio autor; Pega a original e trás com um .filter
    def get_queryset(self, request):
        gs = super(PostAdmin, self).get_queryset(request)  # a original
        return gs.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        super().save_model(request, obj, form, change)
