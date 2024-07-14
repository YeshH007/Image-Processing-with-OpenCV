import cv2

def load_image(file_path):
    return cv2.imread(file_path)

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_blur(image, kernel_size=(5, 5)):
    return cv2.GaussianBlur(image, kernel_size, 0)

def detect_edges(image, threshold1, threshold2):
    return cv2.Canny(image, threshold1, threshold2)

def save_image(file_path, image):
    cv2.imwrite(file_path, image)

def display_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

file_path = 'input_image.jpg'
image = load_image(file_path)
gray_image = convert_to_grayscale(image)
blurred_image = apply_blur(gray_image)
edges_image = detect_edges(blurred_image, 50, 150)
save_image('edges_image.jpg', edges_image)
display_image('Edges', edges_image)
