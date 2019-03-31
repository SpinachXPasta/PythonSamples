
#Hacker Rank Regression challenge
# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import numpy as np 
from sklearn import linear_model as lm

arr = sys.stdin.readlines()
x_dim = int(arr[0].split(" ")[0])
x_train_len = int(arr[0].split(" ")[1])
x_test_len = int(arr[x_train_len+1].split(" ")[0])

x_train = []
y_train = []
x_test = []
for i in arr[1:x_train_len+1]:
    extract = [float(j) for j in i.split(" ")]
    x_train.append(extract[0:x_dim])
    y_train.append(extract[x_dim:][0])
for i in arr[x_train_len+2:]:
    extract = [float(j) for j in i.split(" ")]
    x_test.append(extract)

reg = lm.LinearRegression().fit(x_train,y_train)
predict = reg.predict(x_test)
for i in predict:
    print (i)


