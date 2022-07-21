# import matplotlib.pyplot as plt
# x=([18,23,35,59,48,52])
# rt=([0,7,19,23,44,66])
# plt.bar(x,rt,color='maroon')
# plt.show()

# import numpy as np
# a= np.array(42)
# b=np.array([[1,2,3,4],1,4,5,6])
# print(a.ndim)
# print(b.ndim)

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([0,6])
# y=np.array([5,10])
# plt.plot(x,y)
# plt.show()


# import numpy as np
# import matplotlib as mb
# print(mb.__version__)


# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([10,20])
# y=np.array([5,25])
# # plt.plot(x, y,'o')
# # plt.plot(x, y,'s')
# # plt.plot(x, y,'p')
# plt.plot(x, y,'h')
# plt.plot(x,y)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6,8])
y=np.array([3,8,1,10])
plt.plot(x,y)
plt.plot(x, y, 'p')
# plt.plot(x, y,marker='p')
# plt.plot(x, y,'s:k')
# plt.plot(x, y,'s:c')
# plt.plot(x, y,'s:w')
# plt.plot(x, y,'s-b')
plt.plot(x, y,'s--r')
plt.show()