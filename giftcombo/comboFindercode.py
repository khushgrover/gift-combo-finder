import random
fp1=open('comboFinder.csv')
fp2=open('outputcombo.csv','w')
Set={}
chromosome={}
x=0
for line in fp1:
    if x==0:
        x=1
        continue
    l=line.split(',')
    a = l[0]
    b = int(l[1].strip())
    Set[a] = b
ResultList=list()
i=10
UB=int(input("Enter upper bound:"))
LB=int(input("Enter lower bound:"))
while(i>0):
    for j in range(random.sample(range(2,5),1)[0]):
            k = random.randint(1,100)
            chromosome['P' + str(k)]=Set['P'+ str(k)]
    k=sum(chromosome.values())
    m=set(chromosome.keys())
    if k >=LB and k<=UB:
       ResultList.append(m) 
    chromosome.clear()
    i=i-1
fp2.write("Combos Generated:"+str(len(ResultList)) + '\n')
for line in ResultList:
    fp2.write(str(line) + ' \n')
fp2.close()
fp1.close()
print ("\nWriting done !! \nOpen outputcombo.csv to view the content")