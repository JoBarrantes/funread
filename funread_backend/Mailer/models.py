from django.db import models
from Users.models import User

class Mail(models.Model):
    emailid = models.AutoField(db_column='emailId', primary_key=True)  # Field name made lowercase.
    emailto = models.CharField(db_column='emailTo', max_length=200, blank=False, null=False)  # Field name made lowercase.
    emailfrom = models.CharField(db_column='emailFrom', max_length=200, blank=False, null=False)  # Field name made lowercase.
    emailsubject = models.CharField(db_column='emailSubject', max_length=50, blank=False, null=False)  # Field name made lowercase.
    bodymessage = models.TextField(db_column='bodyMessage', max_length=500, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        
        db_table = 'mail'

class MailControl(models.Model):
    mailcontrolid = models.AutoField(db_column='mailControlId', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='date',blank=False, null=False)
    category = models.IntegerField(db_column='category', blank=False, null=False)
    status = models.CharField(max_length=5)
    idcontrol = models.ForeignKey(Mail, db_column='idControl', blank=True, null=True, on_delete=models.CASCADE, to_field='emailid')  # Field name made lowercase.
    emailfrom = models.ForeignKey(User, db_column='emailFrom', on_delete=models.CASCADE, to_field='email')  # Field name made lowercase.

    class Meta:
        
        db_table = 'mailcontrol'

#Terminar el modelo Mail y construir el model MailControl