from django.db import models
import datetime

# Create your models here.

class Available(models.Model):
    roomNo=models.IntegerField(default=None)
    startTime=models.TimeField(default=datetime.time(0,0,0))
    endTime=models.TimeField(default=datetime.time(0,0,0))

    def __str__(self):
        return "%s - %s"%(str(self.startTime),str(self.endTime))

class Guest(models.Model):
    Name=models.CharField(max_length=50,null=True)
    roomNo=models.IntegerField(default=None)
    Date=models.DateField(default=datetime.date.today,blank=True)
    Time=models.ForeignKey(Available,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return "%s - %s"%(self.Name,str(self.roomAllotted))
   



