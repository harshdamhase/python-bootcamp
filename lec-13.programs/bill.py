rate,quantity = input("Enter rate and quantity").split()
bill = int(rate)*(int)(quantity)
if bill>500:
  print("Acutual bill",bill)
  print("####50%#####")
  discount = (bill/100)*20
  print("paybable amount",bill-discount)
else:
  print("Actual bill",bill)
  print("####5%#####")
  discount = (bill/100)*50 
  print("payable amount",bill-discount) 


#   Enter rate and quantity10 5
# Actual bill 50
# ####5%#####
# payable amount 25.0
