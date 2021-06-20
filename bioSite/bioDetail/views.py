from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, FingerForm
from .models import UserFingerprint, UserData
from django.contrib import messages
from .model_load import *
import cv2
import numpy as np


def homepage(request):
	return render(request, 'bioDetail/home.html')

def register(request):
	if request.method == "POST":
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			user = UserData()
			user.name = form.cleaned_data.get('name')
			user.email = form.cleaned_data.get('email')
			user.phone = form.cleaned_data.get('phone')
			user.gender = form.cleaned_data.get('gender')
			user.address = form.cleaned_data.get('address')
			user.occupation = form.cleaned_data.get('occupation')
			user.organisation = form.cleaned_data.get('organisation')
			user.photo = form.cleaned_data.get('photo')
			user.save()
			request.session['token'] = UserData.objects.latest('date_pub').pk
			print(request.session['token'])
			return redirect('bioDetail:finger')
		else:
			for msg in form.error_messages:
				messages.error(form.error_messages[msg])

	form = UserForm()
	return render(request, 'bioDetail/register.html', {'form': form})
	

def finger(request):
	if request.method == "POST":
		form = FingerForm(request.POST, request.FILES)
		if form.is_valid():
			img_path = form.cleaned_data.get('f_img').read()
			img = img_ready(img_path)
			feat = get_feature(img)
			user_d = UserData.objects.get(pk=request.session.get('token'))
			user_finger = UserFingerprint(user_data=user_d, finger_feature=feat.tolist())
			user_finger.save()
			return redirect('bioDetail:homepage')
		else:
			for msg in form.error_messages:
				messages.error(form.error_messages[msg])

	form = FingerForm()
	return render(request, 'bioDetail/finger_image.html', {'form': form})
			

def authentic(request):
	if request.method == "POST":
		form = FingerForm(request.POST, request.FILES)
		if form.is_valid():
			img_path = form.cleaned_data.get('f_img').read()
			img = img_ready(img_path)
			feat = get_feature(img)
			feat = feat.reshape(1, -1)
			user_d = UserFingerprint.objects.all()
			if user_d.exists():
				feat_d = dict()
				for u in user_d:
					feat_d[u.user_data] = np.array(u.finger_feature)
			else:
				return redirect('bioDetail:no_user')
				
			m_user = calc_dist(feat_d, feat)
			if m_user == None:
				return redirect('bioDetail:no_user')
			else:
				return render(request, 'bioDetail/users.html', {'user': m_user})
		else:
			for msg in form.error_messages:
				messages.error(form.error_messages[msg])

	form = FingerForm()
	return render(request, 'bioDetail/finger_image.html', {'form': form})


def no_user(request):
	return render(request, 'bioDetail/no_user.html')
