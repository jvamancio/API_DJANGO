from django.db import models

class ETP(models.Model):

   etp_id = models.CharField(primary_key=True, max_length=100) 
   etp = models.CharField(max_length=10, null=False, blank=False) 
   tipo_entrega = models.CharField(max_length=15, null=False, blank=False) 
   tipo_etp = models.CharField(max_length=30, null=False, blank=False) 
   elaborador = models.CharField(max_length=100, null=False, blank=False) 
   demanda = models.CharField(max_length=100, null=False, blank=False) 
   vendor = models.CharField(max_length=30, null=False, blank=False) 
   motivador = models.CharField(max_length=50, null=False, blank=False) 
   des_macro_project = models.CharField(max_length=200, null=False, blank=False) 
   obj_project = models.CharField(max_length=200, null=False, blank=False) 
   titulo = models.CharField(max_length=150, null=False, blank=False)
   info_complementar_atributos = models.TextField(null=False, blank=False)

   def __str__(self):
      return self.etp   
    
class OE(models.Model):
   
   etp = models.ForeignKey(ETP, on_delete=models.CASCADE)
   oe_id = models.AutoField(primary_key=True)
   id = models.CharField(max_length=50)
   TipoElemento = models.CharField(max_length=20)
   numOE = models.CharField(max_length=15)
   TipoOE = models.CharField(max_length=20)
   Status = models.CharField(max_length=20)
   
   def __str__(self):
      return self.numOE
