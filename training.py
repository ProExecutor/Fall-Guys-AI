from fastai.vision.all import *
import time
import cv2
import numpy as np
from utils.grabscreen import grab_screen

def label_func(x): return x.parent.name

def run():
    path = Path("E:/DoorDash/")
    fnames = get_image_files(path)
    print(f"Total Images:{len(fnames)}")

    dls = ImageDataLoaders.from_path_func(path, fnames, label_func,bs=40, num_workers=0)
    learn = cnn_learner(dls, resnet18, metrics=error_rate)
    print("Loaded")
    learn.fine_tune(4, base_lr=1.0e-02)

    learn.export()

    start_time = time.time()
    image = grab_screen(region=(50, 100, 799, 449))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert back to 3 channel image
    image = cv2.resize(image, (224, 224))
    image = image / 255.0  # Normalize pixel values
    image = image.astype(np.float32)  # Convert image data type to float32
    test = learn.predict(image)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(test)

if __name__ == '__main__':
    run()
