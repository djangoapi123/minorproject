from django.db import models

# Create your models here.


from django.db import models

# Create your models here


class product(models.Model):
    p_id=models.IntegerField(primary_key=True)
    p_na=models.CharField(max_length=100)
    p_dis=models.CharField(max_length=100)
    p_loc=models.CharField(max_length=100)
    p_sn=models.CharField(max_length=100)
    p_pr=models.FloatField()
    p_ph=models.IntegerField()
    p_da=models.DateField()
    p_ex=models.CharField(max_length=100)
    
    
    def __str__ (self):
        return f"{self.p_na} ->  {self.p_da}"  

class reconfigure(models.Model):
    id=models.IntegerField(primary_key=True)
    na=models.CharField(max_length=100)
    dis=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    sn=models.CharField(max_length=100)
    pr=models.FloatField()
    ph=models.IntegerField()
    da=models.DateField()

    def __str__(self):
        return self.na



class ls(models.Model):
    id=models.IntegerField(primary_key=True)
    na=models.CharField(max_length=100)
    de=models.CharField(max_length=100)
    pr=models.IntegerField()
    da=models.DateField()
    eda=models.DateField()



class lsre(models.Model):
    id=models.IntegerField(primary_key=True)
    na=models.CharField(max_length=100)
    de=models.CharField(max_length=100)
    pr=models.IntegerField()
    da=models.DateField()
    eda=models.DateField()


class vl(models.Model):
    un=models.CharField(max_length=100,primary_key=True)
    p=models.CharField(max_length=100)



class vm(models.Model):
    un=models.CharField(max_length=100,primary_key=True)
    p=models.CharField(max_length=100)

