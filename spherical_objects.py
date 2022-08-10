import math
from typing import List

# Lens constants assuming a 1080p image
f = 714.285714
center = [960, 540]
D = 1.082984  # For image-1, switch to 0.871413 for image-2
D = 0.871413  #im2


def cartesian2sphere(pt):
    x = (pt[0] - center[0]) / f
    y = (pt[1] - center[1]) / f

    r = math.sqrt(x*x + y*y)
    if r != 0:
        x /= r
        y /= r
    r *= D
    sin_theta = math.sin(r)
    x *= sin_theta
    y *= sin_theta
    z = math.cos(r)

    return [x, y, z]


def sphere2cartesian(pt):
    r = math.acos(pt[2])
    r /= D
    if pt[2] != 1:
        r /= math.sqrt(1 - pt[2] * pt[2])
    x = r * pt[0] * f + center[0]
    y = r * pt[1] * f + center[1]
    return [x, y]


def convert_point(point: List[int]) -> List[int]:
    """Convert single points between Cartesian and spherical coordinate systems"""
    if len(point) == 2:
        return cartesian2sphere(point)
    elif len(point) == 3:
        return sphere2cartesian(point)
    else:
        raise ValueError(f'Expected point to be 2 or 3D, got {len(point)} dimensions')


class CartesianBbox:

    def __init__(self, points: List[int], fmt: str):
        assert fmt in ['xyxy', 'xywh', 'cxcywh'], 'Invalid bbox format'
        assert len(points) == 4, 'Cartesian bbox must have 4 values'
        self.points = points
        self.fmt = fmt


class SphericalBbox:

    def __init__(self, points3D: List[int], fmt: str):
        # Question 1
        assert fmt in ['xyz'], 'Invalid bbox format'
        assert len(points3D) == 4, 'Spherical bbox must have 4 values'
        self.points3D = points3D


def bbox_to_spherical(cartesian: CartesianBbox) -> SphericalBbox:
    # Question 2
    sp_pts = []
    for point in cartesian.points:
        cv_points = convert_point(point)
        print("cv_points 1", cv_points)
        sp_pts.append(cv_points)
    return SphericalBbox(sp_pts, 'xyz')


class CartesianPolygon:
    def __init__(self, points: List[int], fmt: str):
        pass  # Question 3
        assert fmt in ['xy'], 'Invalid bbox format'
        assert len(points) < 1000, 'Cartesian bbox must have maximum 1000 values'
        self.points = points

class SphericalPolygon:
    def __init__(self, points3D: List[int]):
        # Question 4
        self.points3D = points3D


def polygon_to_spherical(cartesian: CartesianPolygon) -> SphericalPolygon:
    # Question 4
    poly3d = []
    for cart_pt in cartesian.points:
        cv_points = convert_point(cart_pt)
        print("cv_points 1", cv_points)
        poly3d.append(cv_points)
    return SphericalPolygon(poly3d)
