import cv2

def draw_points(image, point):
    cv2.circle(image, tuple(point), 2, (255,0,0), 5)

def print_points(path, points):
    img = cv2.imread(path)

    for point in points:
        draw_points(img, point)

    cv2.imshow(path, img)
    cv2.waitKey(0)

