import cv2
import numpy as np

# import sys
# sys.path.append("D:/UWaterloo/academics/programs/langchain/ice_breaker")


def detect_blur_fft(img_path: str):
    '''Detect if an image is blurry or sharp via Fast Fourier Transform'''
    idx1 = img_path.find("'")
    idx2 = img_path.find("'", idx1 + 1)
    img = cv2.imread(img_path[idx1 + 1: idx2], cv2.IMREAD_GRAYSCALE)
    print("Image loaded successfully.")
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    # magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

    rows, cols = img.shape
    crow, ccol = rows // 2 , cols // 2
    radius = 20

    # Mask out the low frequencies in the center
    mask = np.ones((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), radius, 0, -1)
    high_freq_energy = np.sum(np.abs(fshift) * mask)
    
    # print(f"High Frequency Energy: {high_freq_energy}")
    if high_freq_energy < 1e9:
        # print("Likely blurry")
        res = "This image is likely blurry rather than sharp"
    else:
        # print("Likely sharp")
        res = "This image is likely sharp rather than blurry"
    return res

def detect_blur_lap(img_path, threshold=300):
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    variance = laplacian.var()

    if variance < threshold:
        print("Image is blurry")

if __name__ == '__main__':
    detect_blur_fft("axolotl_1_blur.jpg")
    detect_blur_fft("axolotl_1.jpg")
    # detect_blur_lap('blurred.jpg')
    # detect_blur_lap('dog.PNG')