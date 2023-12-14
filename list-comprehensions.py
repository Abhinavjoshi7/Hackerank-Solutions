if __name__ == '__main__':

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #In this line, we use list comprehensions to generate a list of all possible coordinates (i, j, k) in a 3D grid. The loops iterate from 0 to the values of x, y, and z, respectively, creating combinations of (i, j, k) coordinates.
    #rember not to use x,y,z as the have fix values
    coordinates = list([i,j,k] for i in range (x + 1) for j in range (y + 1) for k in range (z + 1) )
    filtered_coordinates = [x for x in coordinates if sum(x) != n]
    print(filtered_coordinates)
    #Don't use this print as it prints each coordinate one by one, instead we need the entire list as one 
    # for i in filtered_coordinates:
    #     print(i)
