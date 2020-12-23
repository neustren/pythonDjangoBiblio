from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Produto
from .forms import ProdutoModelForm


class IndexView(ListView):
    models = Produto
    template_name = 'indexcrud.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('indexcrud')


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('indexcrud')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('indexcrud')


def purgen(request, pk):
    print(dir(request))
    print(f'Metodo: {request.method}')

    voudeletei = Produto.objects.get(id=pk)
    voudeletei.delete()

    # return render(request, 'indexcrud.html')
    # return IndexView.as_view()
    return redirect('indexcrud')