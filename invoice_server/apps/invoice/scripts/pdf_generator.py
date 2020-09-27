from io import BytesIO
from django.template.loader import render_to_string
from weasyprint import HTML
from django.shortcuts import HttpResponse
import tempfile

def generate_pdf(template_src, context_dict, req):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename = "invoice.pdf"'
    response['Content-Transfer-Encoding'] = 'binary'


    html_string = render_to_string(template_src, context_dict)
    html = HTML(string=html_string, base_url=req.build_absolute_uri())
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=False) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
        output.close()

    return response