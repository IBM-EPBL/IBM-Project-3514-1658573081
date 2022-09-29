temp = int(input("Enter the temperature value :"))
humidity= int(input("Enter the humidity value :"))
if( temp > 103):
    while(temp> 103):
       print("high temperature occuring")
       temp-=1
else:
 print(" Normal temperature")
