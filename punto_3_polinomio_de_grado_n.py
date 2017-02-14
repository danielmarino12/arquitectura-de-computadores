#1_multiplicion_con_sumas_sucesivas

def multi(x,y):

   z=0
   
   while y>0:
   
      z=z+x
	  
      y-=1
	  
   return z
   
   
#2_potenencia_de_dos_numeros

def poten(x,y):

   z=1
   
   while y>0:
   
      z=mul(z,x)
	  
      y-=1
	  
   return z
   
#3_polinomio_de_grado_n
   
def polino(a,g,n):

   z=0
   
   while n>=0:
   
      z=z+mul(g[n],poten(a,n))
	  
      n-=1
	  
   return z
   
g=[1,4,2]

print polino(1,g,2)