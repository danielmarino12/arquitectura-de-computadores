#5_division_con_restas_sucesivas

def division(x,y):
 
   z=0
   
   while x>=y:
   
      x=x-y
	  
      z+=1
	  
   return z
   
   
print division(4,2)