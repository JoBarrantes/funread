from django.db import models

class Tags(models.Model):
    tagsid = models.AutoField(db_column='TagsId', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, unique=True)  # Field name made lowercase.
    descriptionn = models.CharField(db_column='Descriptionn', max_length=50)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tags'