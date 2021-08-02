from django.db import models
from .users import User

GENDER_CHOICES = (("MALE", "Male"), ("FEMALE", "Female"))

class Employee(models.Model):
    
   # User model as Foreign Key
   user = models.ForeignKey(User, on_delete=models.CASCADE)

   first_name = models.CharField(max_length=255, blank=True, null=True)
   lastname = models.CharField(max_length=255, blank=True,null=True)
   # Employee date of birth
   #date_of_birth = models.DateField(blank=True)

   # gender
   
   gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)

   # blood group
   blood_group = models.CharField(max_length=255, blank=True)

   # aadhar number
   aadhar_number = models.CharField(max_length=12, blank=True)

   # pan number
   pan_number = models.CharField(max_length=10, blank=True)

   # permanent address
   permanent_address = models.TextField(blank=True)

   # current address
   current_address = models.TextField(blank=True)

   # Employee avatar
#    avatar = models.FileField(
#        upload_to="hugo_users/", blank=True, default="hugo_users/default-user-icon.svg"
#    )

   # contact Info
   # alternate email/ personal email
   personal_email = models.EmailField(max_length=255, blank=True)

   # Employee contact number
   phone = models.CharField(max_length=10, unique=True, blank=True)

   # Employee alternate contact number
   alternate_phone = models.CharField(max_length=10, blank=True)

   # emergency contact person
   emergency_contact_person = models.CharField(max_length=255, blank=True)

   # emergency contact number
   emergency_contact_number = models.CharField(max_length=10, blank=True)

   # Job Info issued by HR
   # Employee ID
   emp_id = models.CharField(max_length=10, blank=True)

   # Employee date of joining in the company
   date_of_joined = models.DateField(blank=True, null=True)

   # Employee date of relieving in the company
   last_working_date = models.DateField(blank=True, null=True)

   # laptop serial number given to employee
   device_serial_number = models.CharField(max_length=255, blank=True)

   # team
#    team = models.ForeignKey(
#        "TeamInfo", on_delete=models.SET_NULL, blank=True, null=True
#    )

   # reporting supervisor
   reporting = models.CharField(max_length=255, blank=True)

   # designation
   designation = models.CharField(max_length=255, blank=True)

   # division
   division = models.CharField(max_length=255, blank=True)

   # employee status
   is_active = models.BooleanField(default=True)



class Employment(models.Model):
      employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
      company= models.CharField(max_length=255, blank=True,null=True)
      designation = models.CharField(max_length=255,blank=True, null=True)
      startdate = models.DateField(max_length=255, blank=True, null=True)
      enddate = models.DateField(max_length=255, blank=True, null=True)


class EmployDocs(models.Model):
       docs=models.FileField(upload_to='empdocs')
       employment=models.ForeignKey(Employment, on_delete=models.CASCADE)
       #employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
      

class Education(models.Model):
   name= models.CharField(max_length=255, unique=True)
   qualifications = models.CharField(max_length=255,null=True, blank=True)
   course= models.CharField(max_length=255,null=True, blank=True)
   specialization= models.CharField(max_length=255,null=True)
   institution= models.CharField(max_length=255,null=True)
   employee=models.ForeignKey(Employee, on_delete=models.CASCADE)


class EducationDocs(models.Model):
   education= models.ForeignKey(Education,on_delete=models.CASCADE)
   name= models.CharField(max_length=255,blank=True)
   docs=models.FileField(upload_to='edu_docs')
   

class Internship(models.Model):
   title=models.CharField(max_length=255, blank=True)
   intern=models.CharField(max_length=255, blank=True)
   startdate=models.DateField(name=None, auto_now=False, auto_now_add=False)
   enddate=models.DateField(name=None,auto_now=False,auto_now_add=False)