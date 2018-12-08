from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string

from leaders.Badge_list import BadgeList

from xhtml2pdf import pisa
from django.conf import settings




from weasyprint import HTML, CSS
def render_to_pdf(request, template_src, time_now, time_then, troop, month=1):
	
	data = BadgeList(request, month)
	context_dict = {
	'pioneer': data.pioneer(),
	'explorer': data.explorer(),
	'adventurer': data.adventurer(),
	'other': data.other(),
	'month': month,
	'troop': troop,
	'time_now': time_now,
	'time_then': time_then,
	}

	html_string = render_to_string(template_src, context_dict)

#	template = get_template(template_src)
#	html = template.render(context_dict)
	
	#report size

	#css for report
	report_path = '/pdf/report.css'.format()



	pdf = HTML(
		string=html_string,
		base_url=request.build_absolute_uri()
		).write_pdf(
		stylesheets=[CSS(settings.STATIC_ROOT +  report_path)],
		presentational_hints=True)
	return pdf