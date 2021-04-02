from django.shortcuts import render

def home(request):
	print("here")
	return render(request, 'base/index.html')