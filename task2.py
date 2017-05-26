waist  = raw_input('Please enter your waist: cm\n')
weight = raw_input('Please enter your weight: kg\n')
sex    = raw_input('Please enter your sex:male or female; \n')
if sex == 'male':
   a = waist*0.74
   b = weight*0.082 + 44.74
   axunge = a-b
   fatRate = axunge/weight
   if 0.02<=fatRate<0.05:
      print ('your fatRate is: %.2f %%,your can add fat properly'%(fatRate*100))
   elif 0.06<=fatRate<0.13:
      print ('your fatRate is: %.2f %%,Great!You have athlete body'%(fatRate*100))
   elif 0.14<=fatRate<0.17:
      print ("your fatRate is: %.2f %% your are really healthy"%(fatRate*100))
   elif 0.18<=fatRate<0.25:
      print ('your fatRate is: %.2f %%,not bad'%(fatRate*100))
   elif 0.26<=fatRate:
      print ('your fatRate is: %.2f %%,your are too fat'%(fatRate*100))
   else:
      print('serious warning!you must attention body health')
elif sex == 'female':
   a = waist*0.74
   b = weight*0.082 + 34.89
   axunge = a-b
   fatRate = axunge/weight
   if 0.1<=fatRate<0.13:
      print ('your fatRate is: %.2f %%,your can add fat properly'%(fatRate*100))
   elif 0.14<=fatRate<0.2:
      print ('your fatRate is: %.2f %%,Great!You have athlete body'%(fatRate*100))
   elif 0.21<=fatRate<0.24:
      print ("your fatRate is: %.2f %% your are really healthy"%(fatRate*100))
   elif 0.25<=fatRate<0.31:
      print ('your fatRate is: %.2f %%,not bad'%(fatRate*100))
   elif 0.32<=fatRate:
      print ('your fatRate is: %.2f %%,your are too fat'%(fatRate*100))
   else:
      print('serious warning!you must attention body health')
else:
      print('make sure your enter message')