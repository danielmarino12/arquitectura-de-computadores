#1_multiplicion_con_sumas_sucesivas

def multi(x,y):

   z=0
   
   while y>0:
   
      z=z+x
	  
      y-=1
	  
   return z
   
   
#2_Potencia_de_dos_numeros

def poten(x,y):

   z=1
   
   while y>0:
   
      z=mul(z,x)
	  
      y-=1
	  
   return z
 
print poten(6,8)