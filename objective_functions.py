import numpy as np


def obj_func1(x:float):
    return -x * np.exp(-x/5)


if __name__ == "__main__":
    from binary_search import binary_search
    import numpy as np
    import matplotlib.pyplot as plt

    xs = np.linspace(-5, 25, 101)
    ys = list(map(obj_func1, xs))

    plt.plot(xs, ys)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Objective Function 1')
    plt.show()

    print(binary_search(obj_func1, num_of_points=101))