list = ["cat","dog","lion","elephant","tiger","crocodial"]

for item in list:
    print(item)
    
for i in range(len(list)):
  print("using range nd len",list[i])
  
# while loop
i = 0
while(i < len(list)):
    print("using while loop ",i," ",list[i])
    i= i+1
else:
  print("terminate ....")
    
# sort way 
print([list[i] for i in range(len(list))])