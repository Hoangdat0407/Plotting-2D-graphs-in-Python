import numpy as np
import matplotlib.pyplot as plt

# y = 2**x
x = np.linspace(-10,10,1000)
y = 2**x

plt.plot(x,y) # Khai báo đồ thị muốn vẽ
plt.grid() # Bật lưới tọa độ (các đường kẻ ô dọc và ngang)
plt.title("Đồ thị hàm số y = 2^x")
plt.xlabel("Ox")
plt.ylabel("Oy")
plt.show() # Hiển thị đồ thị
