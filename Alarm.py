temp,hum = map(int,input().split(" "))
while(temp>100.4):
    print("alarm")
    temp-=1
