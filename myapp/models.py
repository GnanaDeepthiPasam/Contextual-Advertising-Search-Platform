from django.db import models

# Create your models here.

# Model 1

class Tag(models.Model):

    def __str__(self):

        return self.tagname

    tagname=models.CharField(max_length=100)

# Model 2

class Advert(models.Model):

    def __str__(self):

        return self.name

    name=models.CharField(max_length=200, default=' ')
    tags=models.ManyToManyField(Tag) # We are using 'ManyToMany' Field because many advertisements could have many tags
                                     # 'Tag' is the model which we defined in 'Model 1'
    image=models.ImageField(upload_to='image/', default=' ')
    ad_url=models.CharField(max_length=500,default=' ')
    
    # Final thing we need to add here is that 'URL'where the user would be redirected to when the user clicks on this particular ad img
    