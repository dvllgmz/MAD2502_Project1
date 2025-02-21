import numpy as np

def get_barycentric_coordinates(triangle_coordinates:np.ndarray, point_coordinates: np.ndarray):
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]
    point_x, point_y = point_coordinates

    '''
    Known equations:
    Eq. 1: x1lambda1 + x2lambda2 + x3lambda3 = x
    Eq. 2: y1lambda1 + y2lambda2 + y3lambda3 = y
    Eq. 3: lambda1 + lambda2 + lambda3 = 1
    
    Eq. 3 becomes: lambda1 = 1 - lambda2 - lambda3
    
    Substitute into Eqs. 1,2:
    (1-lam2-lam3)x1 + x2lam2 + x3lam3 = x
    (1-lam2-lam3)y1 + y2lam2 + y3lam3 = y
    
    Distribute and Group:
    (x2-x1)lam2 + (x3-x1)lam3 = x - x1
    (y2-y1)lam2 + (y3-y1)lam3 = y - y1
    
    Use variables A, B, C to write system of equations in standard form:
    Axlam2 + Bxlam3 = Cx
    Aylam2 + Bylam3 = Cy
    
    Eliminate 'lam2' variable by scaling both equations by appropriate constants and then adding both equations:
    Multiplied by Ay => AxAylam2 + AyBxlam3 = AyCx
    Multiplied by -Ax => -AxAylam2 - AxBxlam3 = -AxCy
    Added => AyBxlam3 - AxBxlam3 = AyCx - AxCy
    
    Simplify, solve for lam3:
    lam3(AyBx - AxBx) = AyCx - AxCy
    lam3 = (AyCx - AxCy) / (AyBx - AxBy)
    
    Follow similar steps to solve for lam1, lam2:
    lam2 = (ByCx - BxCy) / (AxBy - AyBx)
    lam1 = 1 - ((ByCx - BxCy) / (AxBy - AyBx)) - ((AyCx - AxCy) / (AyBx - AxBx))
    '''
    # Variables representing coefficients of x, y equations when written in standard form (Ax + By = C)
    # x variable equations
    Ax = x2 - x1
    Bx = x3 - x1
    Cx = point_x - x1
    # y variable equations
    Ay = y2 - y1
    By = y3 - y1
    Cy = point_y - y1

    # Solving for lam3, lam2 according to reduced equation explained above
    lam3 = (Ay*Cx - Ax*Cy) / (Ay*Bx - Ax*By)
    lam2 = (By*Cx - Bx*Cy) / (Ax*By - Ay*Bx)
    # Solving for lam1 according to Eq. 'lam1 = 1 - lam2 - lam3'
    lam1 = 1 - lam2 - lam3

    bary_coords = np.array([lam1, lam2, lam3])
    return bary_coords

def get_cartesian_coordinates(triangle_coordinates, barycentric_coordinates):
    """
    Known equations:
    r1 * x1 + r2 * x2 + r3 * x3 = x_goal
    r1 * y1 + r2 * y2 + r3 * y3 = y_goal
    r1 + r2 + r3 = 1, but we know r1,r2,r3 (barycentric_coordinates) and everything that isn't x_goal and y_goal. (triangle coordinates)
    :param triangle_coordinates:
    :param barycentric_coordinates:
    :return:
    """
    # Initialize variables according to parameters
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]
    r1, r2, r3 = barycentric_coordinates[0]

    # Check r1, r2, r3 validity.
    if ((r1 + r2 + r3)) != 1:
        return "Invalid barycentric coordinates."

    # Compute using equations above
    x_goal = r1 * x1 + r2 * x2 + r3 * x3
    y_goal = r1 * y1 + r2 * y2 + r3 * y3
    result = np.array([x_goal, y_goal])

    # Call get_barycentric_coordinates() using calculated result to verify
    verify = get_barycentric_coordinates(triangle_coordinates, result)
    verify = np.round(verify, 3)

    if (verify[0], verify[1], verify[2]) != (r1,r2,r3):
        return "Something went wrong, cartesian"
    return result

def is_inside_triangle(triangle_coordinates, point_coordinates):
    bary_coord = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    return np.all(bary_coord >= 0)