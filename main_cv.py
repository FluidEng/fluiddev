import spherical_objects as so
import cv_manipulation as cm

if __name__ == "__main__":
    width = 1920
    height = 1080

    path = ""
    filename = '158295988-24ab142c-f348-48c3-8c07-5752f6015aaf.jpeg'

    cartesian_points = [[10,10],[20,10],[10,20],[20,20]]

    #ca_bbox = so.CartesianBbox()
    ca_bbox = so.CartesianBbox(cartesian_points, 'xyxy')

    #cm.print_points(path + filename, ca_bbox.points)

    sp_spherical_bbox = so.bbox_to_spherical(ca_bbox)

    # verify
    ca_pts = []
    for point in sp_spherical_bbox.points3D:
        cv_points = so.convert_point(point)
        print("cv_points 2 _ verify", cv_points)
        ca_pts.append(cv_points)

    ############ polygon ##########

    # create some points
    interval = 10
    interval_x = int(width / interval)
    interval_y = int(height / interval)

    points_poly = []
    for int_x in range(int(width/interval_x)):
        for int_y in range(int(height/interval_y)):
            points_poly.append((int_x * interval_x, int_y * interval_y))
    cm.print_points(path + filename, points_poly)

    # convert to poly_bbox
    poly_bbox = so.CartesianPolygon(points_poly, "xy")
    sp_spherical_bbox = so.polygon_to_spherical(poly_bbox)

    #print("last", sp_spherical_bbox.points3D)
    #print("last 0", [i[0] for i in sp_spherical_bbox.points3D])

    ### plotting poly

    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')
    x = np.array([i[0] for i in sp_spherical_bbox.points3D])
    print("x", x)
    y = np.array([i[1] for i in sp_spherical_bbox.points3D])
    print("y", y)
    z = np.array([i[2] for i in sp_spherical_bbox.points3D])
    print("z", z)
    c = x + y
    ax.scatter(x, y, z, c=c)
    plt.axis('off')
    plt.show()

