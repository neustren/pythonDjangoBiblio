from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib import messages

from .models import Servico, Funcionario
from .forms import ContatoForm


# class IndexView(TemplateView):
class IndexView(FormView):
    template_name = 'indexfusion.html'
    form_class = ContatoForm
    success_url = reverse_lazy('indexfusion')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Erro ao enviar e-mail")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

# class TesteView(TemplateView):
#     template_name = '500.html'
