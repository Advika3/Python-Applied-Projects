from PIL import Image
import os

# NOTE:
# This script currently reads images from a folder named "Trial"
# located inside the Documents directory.
# Change the path below if your images are stored elsewhere.

image_folder = "C:/Users/*YOUR NAME*/Documents/Trial"
output_pdf = "C:/Users/*YOUR NAME*/Documents/Trial/new_output.pdf"

A4_SIZE = (2480, 3508)  # A4 at 300 DPI

pages = []

for file in sorted(os.listdir(image_folder)):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(image_folder, file)

        img = Image.open(path).convert("RGB")

        # Resize image while maintaining aspect ratio
        img.thumbnail(A4_SIZE)

        # Create white A4 background
        page = Image.new("RGB", A4_SIZE, "white")

        # Center the image
        x = (A4_SIZE[0] - img.width) // 2
        y = (A4_SIZE[1] - img.height) // 2

        page.paste(img, (x, y))

        pages.append(page)

# Save PDF
if pages:
    pages[0].save(output_pdf, save_all=True, append_images=pages[1:])

print("A4 PDF created!")
