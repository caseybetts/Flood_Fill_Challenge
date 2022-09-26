#An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
#You are also given three integers sr, sc, and newColor. This script performs a flood fill on the image starting from the pixel image[sr][sc].
#This returns the modified image after performing the flood fill.
#This script requires a row, column and color value to be specified in the prompt

# Import argv
from sys import argv
script, user_sr, user_sc, user_newColor = argv

# main fuction used to return results
def floodFill(image, sr, sc, newColor):
    sr = int(sr)
    sc = int(sc)
    newColor = int(newColor)

    # store the number of rows and columns in variables
    R,C = len(image), len(image[0])
    # store original color of cell in a variable
    originalColor = image[sr][sc]

    # exit if the new color is the same as the original color
    if image[sr][sc] == newColor:
        return image

    # recursive function to check current cell and cells above, below, left and right
    def reColor(r, c):

        # recolor the cell if the cell is the original color
        if image[r][c] == originalColor:
            image[r][c] = newColor

            # run reColor function above if the current cell is not at the top
            if r >= 1:
                reColor(r-1,c)

            # run reColor function below if the current cell is not at the bottom
            if r < R - 1:
                reColor(r+1,c)

            # run reColor function to the right if the current cell is not at the left side
            if c >= 1:
                reColor(r,c-1)

            # run reColor function to the left if the current cell is not at the right side
            if c < C - 1:
                reColor(r,c+1)

    # run reColor on the original cell
    reColor(sr, sc)

    # return the edited grid
    return image

#image must be changed here
sample_image = [[1,1,1],[1,1,0],[1,0,1]]

print(floodFill(sample_image,user_sr,user_sc,user_newColor))
