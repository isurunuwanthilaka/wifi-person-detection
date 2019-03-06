f = open("wifi_data0.csv","r")
columns=f.next().strip().split(",")
n=len(columns)
arr=[{} for _ in range(n-1)]

#counting frequencies of the data  points
for line in f:
    line=line.strip().split(",")
    for i in range(n-1):
        arr[i][line[i]]=arr[i].setdefault(line[i],0)+1

f.close()
