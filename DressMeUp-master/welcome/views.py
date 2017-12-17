from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import View

# Create your views here.

def index(request):
	template = loader.get_template('welcome/index.html')
	return render(request,'welcome/index.html')

def cart(request):
	template = loader.get_template('welcome/cart.html')
	return render(request,'welcome/cart.html')


def checkoutStep1(request):
	template = loader.get_template('welcome/step1.html')
	return render(request,'welcome/step1.html')

def checkoutStep2(request):
	template = loader.get_template('welcome/step2.html')
	return render(request,'welcome/step2.html')

def checkoutStep3(request):
	template = loader.get_template('welcome/step3.html')
	return render(request,'welcome/step3.html')