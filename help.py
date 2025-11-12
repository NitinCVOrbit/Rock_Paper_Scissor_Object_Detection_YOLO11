import os
import shutil
import random

src_images = 'Rock_Paper_Scissor_Object_Detection_Datasets/train/images'       # e.g., datasets/train/images
src_labels = 'Rock_Paper_Scissor_Object_Detection_Datasets/train/labels'       # e.g., datasets/train/labels
dst_images = 'train/images'
dst_labels = 'train/labels'

os.makedirs(dst_images, exist_ok=True)
os.makedirs(dst_labels, exist_ok=True)

image_files = [f for f in os.listdir(src_images) if f.endswith('.jpg') or f.endswith('.png')]
subset = random.sample(image_files, 3000)

for img_file in subset:
    label_file = img_file.replace('.jpg', '.txt').replace('.png', '.txt')
    shutil.copy(os.path.join(src_images, img_file), os.path.join(dst_images, img_file))
    shutil.copy(os.path.join(src_labels, label_file), os.path.join(dst_labels, label_file))
