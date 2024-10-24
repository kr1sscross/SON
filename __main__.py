#Z1

def is_criticality_balanced():
   tempr = 500
   neu = 100
   if tempr > 800000 and neu < 500:
       return True
   else:
       return False


print(is_criticality_balanced())


#Z2


def reactor_efficiency(voltage, current, theoretical_max_power):


   generated_power = voltage*current
   pow_per = (generated_power/theoretical_max_power)*100
   if pow_per > 30:
       return("black")
   elif pow_per <= 30 and pow_per > 60:
       return("red")
   elif pow_per <= 60 and pow_per > 80:
       return("orange")
   else:
       return("green")


print(reactor_efficiency(230, 20, 500))


#Z3


def fail_safe(temp, neups, prog):


   if temp*neups < 0.9*prog:
       return("LOW")
   elif temp*neups > 0.1*prog:
       return("NORMAL")


print(fail_safe(200,10,300))
