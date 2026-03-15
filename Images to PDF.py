from PIL import Image
import os

image_folder = "C:/Users/(YOUR NAME)/Documents/Trial"

output_pdf = "C:/Users/(YOUR NAME)/Documents/Trial/images_output.pdf"

images = []

for file in sorted(os.listdir(image_folder)):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(image_folder, file)
        img = Image.open(path).convert("RGB")
        images.append(img)

if images:
    images[0].save(output_pdf, save_all=True, append_images=images[1:])

print("PDF created successfully!")
