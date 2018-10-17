###################################### BEGIN PROGRAM ####################################################################################

userInputA = input("Enter time 1: ")                                        #INPUT 1
userInputB = input("Enter time 2: ")                                        #INPUT 2


                                               #Splitting of INPUT 1
hh1, mm1, ss1 = userInputA.split(':')
                                               #Splitting of INPUT 2
hh2, mm2, ss2 = userInputB.split(':')

hh1 = int(hh1)                                                      #converting input characters
mm1 = int(mm1)                                                      #to integers for arithmetic purposes.
ss1 = int(ss1)

hh2 = int(hh2)  
mm2 = int(mm2)
ss2 = int(ss2)


ss3 = (ss1+ss2)%60                                                  #Clock Arithmetic -- adding of individual integer elements
ssOF = (ss1+ss2)//60
mm3 = (mm1+mm2+ssOF)%60                                             #as well as accounting for the 'overflow' of time.
mmOF = (mm1+mm2+ssOF)//60
hh3 = (hh1+hh2+mmOF)%24

ClockArithmeticOP = "{}:{}:{}".format(hh3, mm3, ss3)                #Optimizing the output into a single defined element

print(" {} + {} = {} ".format(userInputA, userInputB, ClockArithmeticOP))       #Final Output


######################################### END PROGRAM #####################################################################################
