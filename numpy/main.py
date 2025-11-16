import numpy as np

def main():
    x_1 = np.array([1, 2, 3])
    x_2 = np.array([
        [10, 24, 23],
        [3, 4, 9]
    ])
    x_3 = np.array([
        [
            [4, 5, 5],
            [5, 6, 9]
        ],
        [
            [3, 4, 4],
            [5, 6, 7],
        ],
        [
            [3, 4, 4],
            [5, 6, 7],
        ]
    ])
    
    print(x_1.ndim, x_1.shape)
    print(x_2.ndim, x_2.shape)
    print(x_3.ndim, x_3.shape)

if __name__ == "__main__":
    main()