import numpy as np

def get_barycentric_coordinates(triangle_coordinates, point_coordinates):
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]
    x, y = point_coordinates
    ''' solving the matrix for lambda
        [x1, x2, x3]  [lambda1]    =   x
        [y1, y2, y3]  [lambda2]    =   y
        [1,  1,   1]  [lambda3]    =   1
        
        det = x1(y2 - y3) + x2(y1 - y3) + x3(y1 - y2)
    
    '''
    det = x1*(y2 - y3) + x2*(y1 - y3) + x3*(y1 - y2)

    lambda_1 = ((x - x2)*(y3 - y2) - (y - y2)*(x3 - x2)) / det
    lambda_2 = ((x - x3)*(y1 - y3) - (y - y3)*(x1 - x3)) / det
    lambda_3 = 1 - lambda_1 - lambda_2

    return np.array([lambda_1, lambda_2, lambda_3])

#def get_cartesian_coordinates():



#def is_inside_triangle():