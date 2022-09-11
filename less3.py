from collections import deque
from timeit import timeit
from random import randint

dq = deque()
lst = list()
my_lst = [i for i in range(200, 300)]

# тест 1
print('append')
print(timeit('for i in range(100): test_dq.append(i)', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst.append(i)', globals=globals(), number=10000))
print('extend')
print(timeit('for i in range(100): test_dq.extend(my_lst)', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst.append(my_lst)', globals=globals(), number=10000))
print('pop')
print(timeit('for i in range(100): test_dq.pop()', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst.pop()', globals=globals(), number=10000))

dq.clear()
lst.clear()

# тест 2
print('appendleft')
print(timeit('for i in range(100): test_dq.appendleft(i)', globals=globals(), number=1000))
print(timeit('for i in range(100): test_lst.insert(0, i)', globals=globals(), number=1000))
print('extendleft')
print(timeit('test_dq.extendleft(my_lst)', globals=globals(), number=10000))
print(timeit('my_lst + test_lst', globals=globals(), number=10000))
print('popleft')
print(timeit('for i in range(10): test_dq.pop()', globals=globals(), number=10000))
print(timeit('for i in range(10): test_lst.pop(0)', globals=globals(), number=10000))

dq.clear()
lst.clear()

# тест 3
for i in range(101):
    lst.append(i)

for i in range(101):
    dq.append(i)

print('Операция получения элемента')
print(timeit('for i in range(100): test_dq[randint(0, 100)]', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst[randint(0, 100)]', globals=globals(), number=10000))
