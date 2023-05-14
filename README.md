# image-viewer
Python UI program that acts as a photos app to every image stored in the folder `artof`, and in all directories recursively within `artof`

## Dependencies

- Python 3.9 or later
- Pillow (`pip install pillow`)

## How to use

1. Clone / download this repository anywhere in a new folder.
2. Create a new folder named `artof` in the same directory as where you extracted everything.
3. Stuff all your images in `artof`. If you have folders of images, you can drag the entire folder because this program walks through all files recursively given it is in `artof`. This program only considers images files of the most common file extensions (PNG, JPG, WEBM, JFIF, ...)
4. To run the program, you need python installed. Most of the time, you would type `python main.py` to run it. Or maybe not `python` - it really depends on how you installed python.

Use the arrow keys / WASD / NM to scroll through images, and use Z or X to shrink / grow the window by a factor of 2 respectively. This only works if the window is focused.

Consider using a batch file to make running the py script faster.
