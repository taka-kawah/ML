import numpy as np
import sys

def calcArr(arr1, arr2):
    # 配列で演算
    print("plus\n", arr1 + arr2)
    print("minus\n", arr1 - arr2)
    print("multiply\n", arr1 * arr2)
    print("devide\n", arr1 / arr2)

def calcMatrix(arr1, arr2):
    # 行列で演算
    print("multiply\n", np.dot(arr1, arr2))

def calcVector(arr1, arr2):
    print("ベクトル演算", arr1, arr2)

if __name__ == "__main__":
    arr1 = np.array([
        [2, 3]
    ])
    arr2 = np.array([
        [5, 6, 3],
        [12, 5, 3]
    ])
    
    
    match sys.argv[1]:
        case "a":
            calcArr(arr1, arr2)
        case "m":
            calcMatrix(arr1, arr2)
        case "v":
            calcVector(arr1, arr2)