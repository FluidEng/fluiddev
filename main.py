import spherical_objects as so

if __name__ == "__main__":
    ca_points = so.CartesianBbox([[10,10],[20,10],[10,20],[20,20]], 'xyxy')

    sp_pts = []
    for point in ca_points.points:
        cv_points = so.convert_point(point)
        print("cv_points 1", cv_points)
        sp_pts.append(cv_points)

    sp_points = so.SphericalBbox(sp_pts, 'xyz')

    ca_pts = []
    for point in sp_points.points3D:
        cv_points = so.convert_point(point)
        print("cv_points 2", cv_points)
        ca_pts.append(cv_points)