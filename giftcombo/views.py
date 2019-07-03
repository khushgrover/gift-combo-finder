from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import ComboForm
from .models import Combo
#from giftcombo.comboFindercode import *

def upload_file(request):
	if request.method == 'POST':
		form = ComboForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect(file_download)
	else:
	    form = ComboForm()
	return render(request, 'upload_file.html', {
		'form': form
		})

def file_download(request):
	combos = Combo.objects.all()
	return render(request, 'file_download.html', {
		'combos' : combos
		})