from django.shortcuts import render, HttpResponse
from residence.models import Residence, UserAntenna

# Create your views here.
def home(request):
	return render(request,'mainWindow.html')

def search(request, antennas):

	#antennasSplit = antennas.split(",")
	userPerAntenna = UserAntenna.objects.filter(antenna=antennas)
	cities = []

	for user in userPerAntenna:
		
		userSplit = user.split(",")
		userResidence = Residence.objects.filter(user=userSplit[1])
		userResidenceSplit = userResidence[0].split(",")
		cities.append(userResidenceSplit[4])


	#for antenna in antennasSplit:
	#	userPerAntenna = UserAntenna.objects.filter(antenna=antenna)
	#	userPerAntennaSplit = userPerAntenna.split(",")
	#	userResidence
