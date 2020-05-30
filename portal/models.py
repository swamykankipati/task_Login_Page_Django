from django.db import models
# Create your models here.
class Register(models.Model):
	
	firstName = models.CharField(max_length=50)
	
	emailId = models.EmailField(null = True,unique=True)
	
	password = models.CharField(max_length=10,null=True)	

	
		
	def __str__(self):
		return self.firstName+' '+self.emailId
		