mar,hindi,eng,sci,math = input("Enter marks of 5 subject").split()
total = int(mar) + int(hindi) + int(eng) + int(sci) + int(math)
print(total)

avg = total*100/5
print(avg)

if avg>60:
  print("Grade D")
elif avg>70:
  print("Grade C")
elif avg>80:
  print("Grade B") 
elif avg>90:
  print("Grade A")  
else:
  print("fail")  
