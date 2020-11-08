from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class HomepageView(View):
	def get(self, request):
		return render(request, 'homepage.html')

	def post(self, request):
		return render(request, 'homepage.html')