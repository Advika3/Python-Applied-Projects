# Images to PDF Converter 

A simple Python script that converts multiple images into a single PDF document.
Uses file handling and image processing.
It helped me to convert screenshots to PDF for college assignments :))

## Features

* Converts multiple images into one PDF file
* Supports common image formats:

  * `.jpg`
  * `.jpeg`
  * `.png`
  * 
* Images are added to the PDF in alphabetical order
* Uses Python libraries for image handling

## Tools Used

* Python
* Pillow (Python Imaging Library)
* OS module for file handling

## How It Works

1. The script reads all image files from a specified folder.
2. Each image is opened and converted to RGB format.
3. The images are combined into a single PDF file.
4. `Images to PDF.py` converts images to PDF as is, while `(A4) Images to PDF.py` centers
   the images on a white A4 and converts to PDF.
6. The final PDF is saved in the same folder.

## Example Folder Structure

```
Trial/
 ├── image1.jpg
 ├── image2.png
 ├── image3.jpg
```

After running the script:

```
Trial/
 ├── image1.jpg
 ├── image2.png
 ├── image3.jpg
 └── images_output.pdf
```

## Current Configuration

The script currently reads images from a folder named:

```
Documents/Trial
```

You can modify the folder path inside the script if your images are stored elsewhere.

---

* Python file handling
* Basic automation scripts
* Image processing with Pillow
* Working with directories and file formats
