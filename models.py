from django.db import models

# Create your models here.

class Marka(models.Model):
	marka = models.CharField(verbose_name=u'Question marka', max_length=255, help_text='This marka')	

class Modeli(models.Model):
	modeli = models.CharField(verbose_name=u'the modeli', max_length=255, help_text='modeli')
	conect = models.ForeignKey(Marka, on_delete=models.CASCADE)

class TupZap(models.Model):
	tupzap = models.CharField(verbose_name=u'tup zapchastun', max_length=255, help_text='tupzap')
	#conect = models.ForeignKey(Question, on_delete=models.CASCADE)

class Nation(models.Model):
	nation = models.CharField(verbose_name=u'country of origin', max_length=255, help_text='country of orign')

class Producer(models.Model):
	producer = models.CharField(verbose_name=u'The Producer', max_length=255, help_text='The Producer')


		
class Magazun(models.Model):
	magazun = models.CharField(verbose_name=u'The Magazun', max_length=255, help_text='The magazun')
	conect1 = models.ForeignKey(Marka, on_delete=models.CASCADE) #'''Modeli, TupZap, Nation, Producer)'''on_delete=models.CASCADE
	conect2 = models.ForeignKey(Modeli) #on_delete=models.CASCADE)
	conect3 = models.ForeignKey(TupZap) #on_delete=models.CASCADE)
	conect4 = models.ForeignKey(Nation) #on_delete=models.CASCADE)
	conect5 = models.ForeignKey(Producer) #on_delete=models.CASCADE)
	
