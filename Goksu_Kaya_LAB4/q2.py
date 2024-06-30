import numpy as np

r_vals=np.random.rand(10)
print(r_vals)

r_vals=np.random.randint(1,50,10)
print(r_vals)

arr=[1,3,6,8,9,7]
arr=arr*3
print(arr)

r_vals=r_vals*3
print(r_vals)

arr1=r_vals[r_vals>50]
print(arr1)

print(np.where(r_vals<60))