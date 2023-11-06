import numpy as np
import cv2

data = np.load("../data/training_data_Gate.npy", allow_pickle=True)
targets = np.load("../data/target_data_Gate.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

for i, image in enumerate(data):
    print(targets[i])
    image = image.astype(np.uint8)  # Ensure the image is uint8
    cv2.imshow(f"Image {i}", image)  # Unique window name for each image

    cv2.waitKey(1)  # Small delay instead of waiting for key press

cv2.destroyAllWindows()  # destroys the window showing image
