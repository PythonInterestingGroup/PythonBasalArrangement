def inputSex():
    sex = raw_input("Please enter your sex(male or female):")
    if sex == 'male' or sex == 'female':
      return sex
    else:
       print("Please enter the correct sex information!male or female")
     
def inputWaist():
    waist = input("Please enter your waist(cm):")
    return waist

def inputWeight():
    weight = input("Please enter your weight(kg):")
    return weight
    
s  = inputSex()
wa = inputWaist()
we = inputWeight()
a  = wa*0.74
if s == 'male':
   b = we * 0.082 + 44.74
elif s == 'female': 
   b = we * 0.082 + 34.89 
axunge  = a - b
fatRate = round(axunge/we,4)
print("your fatRate is: %.2f%%"%(fatRate*100))
if s == 'male':
   if 0.02<=fatRate<0.05:
      print ('your can add fat properly')
   elif 0.06<=fatRate<0.13:
      print ('Great!You have athlete body')
   elif 0.14<=fatRate<0.17:
      print ('your are really healthy')
   elif 0.18<=fatRate<0.25:
      print ('not bad')
   elif 0.26<=fatRate:
      print ('your are too fat')
   else:
      print('serious warning!you must attention body health')
elif s == 'female':
   if 0.1<=fatRate<0.13:
      print ('your can add fat properly')
   elif 0.14<=fatRate<0.2:
      print ('Great!You have athlete body')
   elif 0.21<=fatRate<0.24:
      print ('your are really health')
   elif 0.25<=fatRate<0.31:
      print ('not bad')
   elif 0.32<=fatRate:
      print ('your are too fat')
   else:
      print('serious warning!you must attention body health')
   


