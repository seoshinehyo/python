import numpy as np

x = np.array([[1.83, 1.76, 1.69, 1.86, 1.77, 1.73],
              [86.0, 74.0, 59.0, 95.0, 80.0, 68.0]])

y = x[0:2, 1:3]
z = x[0:2][1:3]

print(f'x shape : {x.shape}')
print(f'y shape : {y.shape}')
print(f'z shape : {z.shape}')
print(f'z values : {z}')
print('BMI data')
print(x[1] / (x[0]**2))

print(np.arange(5))