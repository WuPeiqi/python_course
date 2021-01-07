# 第一步：[ [] for i in range(1,10)]

print("\n".join([" ".join(['{}*{}'.format(i, j) for j in range(1, i + 1)]) for i in range(1, 10)]))

print("\n".join([" ".join(["{}*{}".format(i, j) for j in range(1, i + 1)]) for i in range(1, 10)]))
