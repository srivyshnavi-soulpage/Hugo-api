from django.db import models
from .users import User


class Project(models.Model):
    assignee=models.ForeignKey(User,on_delete=models.CASCADE)
    clientname=models.CharField(max_length=255,null=False)
    projectname=models.CharField(max_length=255,null=False)
    description=models.CharField(max_length=255,null=True)
    startdate=models.DateField(name=None,auto_now=False,auto_now_add=False)
    enddate=models.DateField(name=None,auto_now=False,auto_now_add=False)



class ProjectAssignee(models.Model):
    assignee=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)

    class Meta:

        verbose_name="ProjectAssignee"
        verbose_name="projectAssignee"
        db_table="projectAssignee"
        #unique_together=("assignee,project")
    
    def __str__(self):
        return self.employee_project