import io
from django.http import FileResponse
from django.views.generic import View
from reportlab.pdfgen import canvas

# weasyprint
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML


class Index2View(View):

    def get(self, request, *args, **kwargs):
        texto = ['Neus teste 1', 'Neus evoluindo', 'Neus programador', 'Neus economista']

        html_string = render_to_string('relatorio.html', {'texto': texto})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/relatorio2.pdf')

        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # Faz download: attachment; Abre no navegador: inline
            response['Content-Disposition'] = 'inline; filename="relatorio2.pdf"'
        return response


# reportlab
class IndexView(View):

    def get(self, request, *args, **kwargs):
        # Cria um arquivo para receber os dados e gerar o PDF
        buffer = io.BytesIO()

        # Criar o arquivo pdf
        pdf = canvas.Canvas(buffer)

        # Insere coisas no pdf
        pdf.drawString(100, 100, "Neus rox")

        # Quando acabamos de inserir coisas no PDF
        pdf.showPage()
        pdf.save()

        # Retomando o buffer para o início do arquivo
        buffer.seek(0)

        # Faz gerar o download do arquivo em PDF
        # return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')

        # Abrir o pdf direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')
