from django.shortcuts import render
from .models import SEO_data
# from django.http import HttpResponse

def show_index(request):
	try:
		seo_information = SEO_data.objects.get(page="ГЛАВНАЯ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
	}
	return render(request, 'baseapp/index.html', context)

def show_dvs_page(request):

	try:
		seo_information = SEO_data.objects.get(page="ДВС")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
	}

	return render(request, 'baseapp/dvs.html', context)

def show_kpp_page(request):

	try:
		seo_information = SEO_data.objects.get(page="КПП")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
	}

	return render(request, 'baseapp/kpp.html', context)

def show_reductor_page(request):

	try:
		seo_information = SEO_data.objects.get(page="РЕДУКТОРЫ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
	}

	return render(request, 'baseapp/reductor.html', context)

def show_tnvd_page(request):

	try:
		seo_information = SEO_data.objects.get(page="ТНВД")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
	}

	return render(request, 'baseapp/tnvd.html', context)	

def show_forsunki_page(request):

	try:
		seo_information = SEO_data.objects.get(page="ФОРСУНКИ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
	}

	return render(request, 'baseapp/forsunki.html', context)	

def show_tachograph_page(request):

	try:
		seo_information = SEO_data.objects.get(page="ТАХОГРАФЫ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
	}

	return render(request, 'baseapp/tachograph.html', context)

def show_other_page(request):

	try:
		seo_information = SEO_data.objects.get(page="ПРОЧЕЕ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
	}

	return render(request, 'baseapp/other.html', context)

def show_contact_page(request):

	try:
		seo_information = SEO_data.objects.get(page="КОНТАКТЫ")
	except:
		seo_information = None

	context = {
		'seo_information': seo_information,
	}

	return render(request, 'baseapp/contact.html', context)	