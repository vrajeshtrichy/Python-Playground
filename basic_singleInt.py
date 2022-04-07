a = [0,0,1,2,1]
singleInt = None
for i in a:
    occurances = [ele for ele in a if ele==i]
    print(occurances)
    if len(occurances)==1:
        singleInt = occurances[0]
print(singleInt)