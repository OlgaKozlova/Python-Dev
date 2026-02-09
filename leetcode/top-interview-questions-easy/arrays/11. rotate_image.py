class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        last = size - 1
        layers = size // 2
        for layer in range(layers):
            layerMaxIndex = size - 1 - layer   # это last (глобальный)
            layerMaxOffset = layerMaxIndex - layer  # длина стороны-1
            for layerIndex in range(layerMaxOffset):
                firstIndex = [layer, layerIndex + layer]
                secondIndex = [layerIndex + layer, layerMaxIndex]
                thirdIndex = [layerMaxIndex, layerMaxIndex - layerIndex]
                fourthIndex = [layerMaxIndex - layerIndex, layer]
                #print(layer, firstIndex, secondIndex, thirdIndex, fourthIndex)
                
                tmp = matrix[firstIndex[0]][firstIndex[1]]
                matrix[firstIndex[0]][firstIndex[1]] = matrix[fourthIndex[0]][fourthIndex[1]]
                matrix[fourthIndex[0]][fourthIndex[1]] = matrix[thirdIndex[0]][thirdIndex[1]]
                matrix[thirdIndex[0]][thirdIndex[1]] = matrix[secondIndex[0]][secondIndex[1]]
                matrix[secondIndex[0]][secondIndex[1]] = tmp
                
                
        