class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []

        for i in range(rowIndex + 1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)  # The first and last elements in each row are 1.
                else:
                    prevRow = i - 1
                    leftVal = triangle[prevRow][j - 1]
                    rightVal = triangle[prevRow][j]
                    row.append(leftVal + rightVal)  # Sum of the two numbers above.

            triangle.append(row)

        return triangle[rowIndex]
