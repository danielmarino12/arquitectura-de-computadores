#1_multiplicion_con_sumas_sucesivas

def multi(x,y):

   z=0
  
   while y>0:
   
      z=z+x
	  
      y-=1
	  
   return z
   
#4_factorial_ 

def factor(x):

  z=1
  
  while x>0:
  
     z=mul(z,x)
	 
     x-=1
	 
  return z
  
print factor(8)