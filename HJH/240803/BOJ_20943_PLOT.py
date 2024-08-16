# 20943 문제 보기를 이해하는 표를 출력하는 코드입니다. 실행해보세요!
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-10, 10)

y1 = -0.5 * x - 1.5
plt.plot(x, y1)

y2 = -0.5 * x - 4/5
plt.plot(x, y2)

y3 = -(1/3) * x - (6/3)
plt.plot(x, y3)

y4 = -(3/9) * x - (7/9)
plt.plot(x, y4)

plt.show()