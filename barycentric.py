import numpy as np




def get_barycentric_coordinates(triangle_coordinates, point_coordinates):
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]
    x, y = point_coordinates
    ''' I solved for lambda using the determinant/matrix idea you can get from the equations but I'm not sure if this is the right way
        [x1, x2, x3]  [lambda1]    =   x
        [y1, y2, y3]  [lambda2]    =   y
        [1,  1,   1]  [lambda3]    =   1

        det = x1(y2 - y3) + x2(y1 - y3) + x3(y1 - y2)

    '''
    det = x1 * (y2 - y3) + x2 * (y1 - y3) + x3 * (y1 - y2)

    lambda_1 = ((x - x2) * (y3 - y2) - (y - y2) * (x3 - x2)) / det
    lambda_2 = ((x - x3) * (y1 - y3) - (y - y3) * (x1 - x3)) / det
    lambda_3 = 1 - lambda_1 - lambda_2

    return np.array([lambda_1, lambda_2, lambda_3])







def get_cartesian_coordinates(triangle_coordinates, barycentric_coordinates):
    """
    Okay, so now we have:
    r1 * x1 + r2 * x2 + r3 * x3 = x_goal
    r1 * y1 + r2 * y2 + r3 * y3 = y_goal
    r1 + r2 + r3 = 1, but we know r1,r2,r3 (barycentric_coordinates) and everything that isn't x_goal and y_goal. (triangle coordinates)
    :param triangle_coordinates:
    :param barycentric_coordinates:
    :return:
    """
    # this is just multiplication? Lets set up our variables first
    x1 = triangle_coordinates[0,0]
    y1 = triangle_coordinates[1,0]
    x2 = triangle_coordinates[0,1]
    y2 = triangle_coordinates[1,1]
    x3 = triangle_coordinates[0,2]
    y3 = triangle_coordinates[1,2]
    r1 = barycentric_coordinates[0]
    r2 = barycentric_coordinates[1]
    r3 = barycentric_coordinates[2]
    # first, lets make sure r1, r2, r3 are valid.
    if ((r1 + r2 + r3)) != 1:
        return "invalid barycentric coordinates"
    # compute like equations above
    x_goal = r1 * x1 + r2 * x2 + r3 * x3
    y_goal = r1 * y1 + r2 * y2 + r3 * y3
    possible_result = np.array([x_goal, y_goal])
    # another check to make sure we're not failing is to put it into the get_barycentric_coordinates, since they're sort of inverses of eachother.
    checker = get_barycentric_coordinates(triangle_coordinates, possible_result)

    if (checker[0], checker[1], checker[2]) != (r1,r2,r3):
        return "something went wrong, cartesian"
    return possible_result







def is_inside_triangle(triangle_coordinates, point_coordinates):
    """* The function `is_inside_triangle` takes the same input arguments as `get_barycentric_coordinates` but it returns a `bool` as to whether the point lies inside of the triangle or not.
The relevant property of barycentric coordinates is that a point is inside of the the triangle if all coordinates are non-negative.
    So we just check if any of the provided array is less than 1, i think? Unless theres a misunderstanding. If anything, get the 3-figure array, check if they're negative. if they are, return false. if not, return true.

    if ((barycentric_coordinates[0] < 0) or (barycentric_coordinates[1] < 0) or  (barycentric_coordinates[2] < 0)):
        return False
    return True
    """

    barycentric_coord = get_barycentric_coordinates(triangle_coordinates, point_coordinates)

    return np.all(barycentric_coord >= 0)








'''def get_barycentric_coordinates(triangle_coordinates, point_coordinates):

    #setting up triangle and "goal" coordinates.
    x1 = triangle_coordinates[0,0]
    y1 = triangle_coordinates[1,0]
    x2 = triangle_coordinates[0,1]
    y2 = triangle_coordinates[1,1]
    x3 = triangle_coordinates[0,2]
    y3 = triangle_coordinates[1,2]
    x_goal = point_coordinates[0]
    y_goal = point_coordinates[1]

    #our equations begin looking like this
    #r1*x1+r2*x2+r3*x3 == x_goal
    #r1*y1+r2*y2+r3*y3 == y_goal
    #r1+r2+r3 = 1
    """
    goal:
    - eliminate variables until we have 1 left that we can solve for.
    - then, plug in the rest until everything is complete"""
    #get rid of one variable via subsitution (r1 = 1- r2 -r3). Remeber this for when we solve for r1 after we solve for r2 and r3.
    #so now it looks like
    #(1-r2-r3)*x1+r2*x2+r3*x3 == x_goal
    #(1-r2-r3)*y1+r2*y2+r3*y3 == y_goal
    #distribute
    #x1 -  r2*x1 - r3*x1 + r2*x2 +r3*x3 == x_goal
    #y1 - r2*y1 - r3*y1 + r2*y2 +  r3*y3 == y_goal
    #group for readability
    #(x2-x1)*r2+(x3-x1)*r3 == x_goal - x1
    #(y2 - y1) * r2 + (y3 - y1) * r3 == y_goal - y1
    #for better readability, lets have x2-x1 be a1, x3-x1 be b1, and x_goal - x1 be c1.
    #same with the y variables, with a2,b2, and c2. (save these equations after we solve for this first variable)
    a1 = x2 - x1
    b1 = x3 - x1
    c1 = x_goal - x1
    a2 = y2 - y1
    b2 = y3 - y1
    c2 = y_goal - y1
    #a1 * r2 + b1 * r3 = c1
    #a2 * r2 + b2 * r3 = c2
    #we can eliminate a second unknown by either:
    #multiplying the first equation by a2 and the second equation by a1
    #or multiplying the first equation by b2 and the second equation by b1
    #that way, we have an (a1* a2 * r2) or (b1 * b2 * r2) term on both equations.
    #then, we can subtract the two equations to get a result for one variable. Lets stick with teh first option.
    # so, multiply the first equation by a2....
    #(a2+a1) * r2 + (a2+b1) * r3 = c1*a2
    # and multiply the second equation by a1...
    #(a1+a2) * r2 + (a1 + b2) * r3 = c2*a1
    # now we subtract the top by the bottom...
    #(a2+a1-(a1+a2)) * r2 + (a2*b1 - (a1*b2)) * r3= c1*a2 - c2*a1
    # ^^^^^^^^^^^^^ this term is 0 now, so now we can solve for r3.
    # r3 = (c1*a2-c2*a1)/((a2+b1-(a1+b2)))
    #
    r3_num = c1*a2 - c2*a1
    r3_dem = a2*b1 - (a1*b2)
    r3 = r3_num/r3_dem
    # now we can plug in r3 into the equations we saved earlier. here are they for reference again.

    #a1 * r2 + b1 * r3 = c1
    #a2 * r2 + b2 * r3 = c2

    # some algebra later, we get....
    # r2 = (c1-(b1*r3))/a1
    # and
    # r2 = (c2 - (b2*r3))/a2.
    # make sure they equal eachother (with all the variables, if not then raise an error)
    r2_num_1 = c1-(b1*r3)
    r2_num_2 = c2-(b2*r3)

    r2_value_1 = np.round(r2_num_1/a1, decimals=3)
    r2_value_2 = np.round(r2_num_2/a2, decimals=3)
    #we use np.round() because floating point stuff is funny. you know with the 2.00000001 and all of that. theres probably a better way to do this?
    # since we know r2 and r3 now, we can go back all the way to here:
    #r1 = 1- r2 -r3
    if r2_value_1 == r2_value_2:
        r2 = r2_value_1
        r1 = 1 - r2 - r3
    else:
        print("something went wrong")
        return "error"

    # and then we should be good?
    return np.array([r1, r2, r3])

'''