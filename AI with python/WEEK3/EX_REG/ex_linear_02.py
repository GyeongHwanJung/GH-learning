import numpy as np
from matplotlib import pyplot as plt

# array() : numpy 배열 생성 함수
data=np.array( [[100,20], [150,24], [300, 36], [400, 47], [130, 22],
                [240,32], [350,47], [200, 42], [100, 21], [110, 21],
                [190,30], [120,25], [130, 18], [270, 48], [255, 28]])

#plt.scatter(data[:,0], data[:, 1])
print(data.shape)
print('data[:, 0] =>', data[:, 0])
print('data[:, 1] =>', data[:, 1])

# 그래프 출력
plt.scatter(data[:,0], data[:, 1])
plt.title('Time & Distance')
plt.xlabel('Delivery Distance')
plt.ylabel('Time Consumed')
plt.axis([0, 420, 0, 50])
plt.show()