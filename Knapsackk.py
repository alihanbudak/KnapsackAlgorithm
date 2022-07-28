import time
file = open("ks_10000_0.txt", "r")
value = []
weight = []
for x in file:
  x = x.split(" ")
  value.append(int(x[0]))
  weight.append(int(x[1]))
value.reverse()
weight.reverse()
n = value.pop()
MW = weight.pop()
value.reverse()
weight.reverse()
file.close()
selected = []
starttime = time.time()
def knapSack(value,weight,n,MW):
  result=0
  greedyCap=MW
  tempArr = []
  tempWeight = []
  tempProfit = []
  for i in range(n):
    tempArr.append(i)
    tempWeight.append(weight[i])
    tempProfit.append(value[i])
    selected.append(0)
  
  for i in range(n):
    for j in range(n - i - 1):
      val1 = float(float(tempProfit[j]) / float(tempWeight[j]))
      val2 = float(float(tempProfit[j+1]) / float(tempWeight[j+1]))
      if(val1 > val2):
        temp = tempProfit[j]
        tempProfit[j] = tempProfit[j+1]
        tempProfit[j+1] = temp

        temp = tempWeight[j]
        tempWeight[j] = tempWeight[j+1]
        tempWeight[j+1] = temp

        temp = tempArr[j]
        tempArr[j] = tempArr[j+1]
        tempArr[j+1] = temp
      
  for i in range(n):
    if(tempWeight[i] <= greedyCap and greedyCap > 0):
      result += tempProfit[i]
      greedyCap -=tempWeight[i]
      selected[tempArr[i]] = 1
  return result
print(knapSack(value,weight,n,MW))
for i in range(n):
  print(selected[i],end=" ")
print("\n--- %s saniye ---"% (time.time() - starttime))