import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weigth1 = np.array([w11, w12])
    weigth2 = np.array([-1, 1])

    sum_hidden = np.dot(weigth1, x)
    print('Значения сумм на нейронах скрытого поля:'+str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print('Значения на выходах нейронов скрытого слоя: '+str(out_hidden))

    sum_end = np.dot(weigth2, out_hidden)
    y = act(sum_end)
    print('Выходное значение НС: '+str(y))

    return y

house = 0
rock = 1
attr = 1

res = go(house, rock, attr)
if res == 1:
    print('Ты мне нравишься')

else:
    print('Созвонимся')