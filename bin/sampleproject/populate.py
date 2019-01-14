import os

def delete_everything():
	
	Residence.objects.all().delete()

def populate():
	
	print 'Populating database...'
	print '----------------------\n'
	
	#residenceFile = open("users_residence.txt", "r")
	#userAntennaFile = open("users_antenna.txt", "r")
	#contador = 0
	
	#for line in residenceFile:
	#	lineSplit = line.split(",")
		#add_residence(lineSplit[0],lineSplit[1],lineSplit[2],lineSplit[3],lineSplit[4])
		#contador+=1
		#print(lineSplit[0]+"-..-"+lineSplit[1]+"-..-"+lineSplit[2]+"-..-"+lineSplit[3]+"-..-"+lineSplit[4])
		#if (contador == 4):
		#	break
		
	#for line in userAntennaFile:
	#	lineSplit = line.split(",")
	#	add_userantenna(lineSplit[0], lineSplit[1])

		#contador+=1
		#print(lineSplit[0]+"-..-"+lineSplit[1])
		#if (contador == 8):
		#	break

	#residenceFile.close
	#userAntennaFile.close
	
	

def add_residence(user, antenna, lat, lon, city):

	r, created = Residence.objects.get_or_create(user=user, antenna=antenna, lat=lat, lon=lon, city=city)
	
	return r
	
def add_userantenna(user, antenna):
	
	u, created = UserAntenna.objects.get_or_create(antenna=antenna, user=user)

	return u

if __name__ == '__main__':

	print '\n' + ('=' * 80)+ '\n'
	import django
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sampleproject.settings')
	
	django.setup()
	from residence.models import Residence, UserAntenna
	from django.contrib.auth.models import User
	from django.db import IntegrityError
	#populate()
	delete_everything()
