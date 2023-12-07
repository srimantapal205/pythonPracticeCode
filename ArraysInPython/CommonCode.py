from numpy import *
arr1 = array([9,8,7,6,5])
arr2= arr1 + 1
print(arr2)

arr3 = array([10,20,30.5,-40])
arr4 = array([1,2,3,4])
arr5 = arr3-arr4
print(arr5)

arr2D = array([
    [1,2,3],
    [4,5,6]
])

print(arr2D)

arr3D = array([
    [
        [1,2,3],[4,5,6]
    ],
    [
        [9,8,7],[6,5,4]
    ]
])

print(arr3D)

#The ndim attribute
print('\n The Dimensions of the array')
print(arr1.ndim)
print(arr2D.ndim)
print(arr3D.ndim)

#the shape attribute
print('\n The shape of the array')
print(arr1.shape)
print(arr2D.shape)
print(arr3D.shape)

arr2D.shape =(3,2)
print(arr2D)

print("\n The size of attributs")
print(arr1.size)
print(arr2D.size)
print(arr3D.size)

print("\n The itemsize of attributs")
print(arr1.itemsize)
print(arr2D.itemsize)
print(arr3D.itemsize)

print("\n The dtype of attributs")
print(arr1.dtype)
print(arr2D.dtype)
print(arr3D.dtype)

print("\n The nbytes of attributs")
print(arr1.nbytes)
print(arr2D.nbytes)
print(arr3D.nbytes)

# the reeshape function

lngArr = arange(20)
print(lngArr)

arr2dReshape = lngArr.reshape(2,10)
print(arr2dReshape)
arr3dReshape = lngArr.reshape(10,2)
print(arr3dReshape)

#The flatten() method
flatten2DArr = arr2D.flatten()
print(flatten2DArr)

flatten3DArr = arr3D.flatten()
print(flatten3DArr)
