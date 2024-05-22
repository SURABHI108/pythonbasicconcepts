a = [1,2,3,4]
b = int(input("enter any number"))
for i in range(len(a)):
    if b == a[i] :
        print("number found in list")
        break;
        
# two array comparision using in perator      
xyz = [0,12,4,6,242,7,9]
print([x for x in xyz if x not in a]);
