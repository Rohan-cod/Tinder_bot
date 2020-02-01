from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Account
from .main import TinderBot
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager




class HomePageView(CreateView):
	model = Account
	template_name = 'index.html'
	fields = {'username', 'password',}
	def submit(request):
		if request.method == 'POST':
			name=request.POST['username']
			pasw=request.POST['password']
			driver = webdriver.Chrome(ChromeDriverManager().install())
			bot=TinderBot(str(name),str(pasw))