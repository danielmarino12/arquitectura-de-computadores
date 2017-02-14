#1_multiplicion_con_sumas_sucesivas

def multi(x,y):

   z=0
   
   while y>0:
   
      z=z+x
	  
      y-=1
	  
   return z

print multi(8,9)