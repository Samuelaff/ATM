import random 
def generateOTP() : 
	digits = "0123456789"
	OTP = "" 
	for i in range(4) : 
		OTP +=str(random.randint(0,9))
	return OTP 

