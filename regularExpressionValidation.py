#Task-9-Question-4-Validate the regular expression
import re

class RegularExpression:

    def __init__(self, data):
        self.data = data       
  
    def emailId(self):
        pattern = "^([a-z0-9._-])+(@)+([a-z0-9]+(.)+([a-z]))$"         
        if re.match(pattern, self.data):
            return True
        else:
            return False
    def bangladeshMobile(self):
        pattern ="^[0-1]{2}[0-9]{3}[0-9]{6}$"
        if re.match(pattern, self.data):
            return True
        else:
            return False
    def usaPhoneNumber(self):
        pattern = "^[(0-9)]{5}[0-9-]{4}[0-9]{4}$"
        if re.match(pattern,self.data):
            return True
        else:
            return False
    def password(self):
        pattern = "^[A-Za-z0-9!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]{16}$"
        if re.match(pattern, self.data):
            return True
        else:
            return False

print("EmailId:",RegularExpression("felix_vetharaj@hotmail.com").emailId())
print("EmailId:",RegularExpression("felix_vetharaj.com").emailId())
print("Bangladesh Monbile:",RegularExpression("01054694200").bangladeshMobile())
print("Bangladesh Monbile:",RegularExpression("01054200").bangladeshMobile())
print("USA phone number:", RegularExpression("(123)456-7890").usaPhoneNumber())
print("USA phone number:", RegularExpression("(123)4567890").usaPhoneNumber())
print("Alpha-numeric Paswword:",RegularExpression("abcdeFGhij9876&*").password())
print("Alpha-numeric Paswword:",RegularExpression("eFGhij9876&*").password())
    
