import os
import random
from tkinter import *
from PIL import ImageTk, Image


def get_files_recursive(directory: str):
    file_list = []
    for rootdir, directories, tfiles in os.walk(directory):
        for filename in tfiles:
            full_file_path = os.path.join(rootdir, filename)
            file_list.append(full_file_path)
    return file_list


exts = [".jpg", ".png", ".jfif", ".webp", ".jpeg"]
with open("bpath.txt", encoding="UTF-8", mode="r") as f:
    base_path = f.read().strip()
files = get_files_recursive(base_path)
big_list = [f for f in files if any(f.endswith(x) for x in exts)]

current_index = 0
random.shuffle(big_list)
list_len = len(big_list)


def choose_next() -> str:
    """Relative to base path choose a random file from it."""
    global current_index
    current_index = (current_index + 1) % list_len
    return big_list[current_index]


def choose_previous() -> str:
    global current_index
    current_index = (current_index - 1) % list_len
    return big_list[current_index]

def choose_current() -> str:
    global current_index
    return big_list[current_index]


def wrap_bracket(text: str) -> str:
    return '"' + text + '"'


def resize_image(img, root):
    # Keep the aspect ratio by resizing the image to fit within a bounding box
    # with the specified size while maintaining the aspect ratio
    img.thumbnail((root.winfo_screenwidth(), root.winfo_screenheight()))

    # Resize the image to the size of the tkinter window
    img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    return img


def resize_image_2(image, scale):
    # Get the size of the original image
    width, height = image.size

    # Calculate the new size
    new_width = int(width * scale)
    new_height = int(height * scale)

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Return the resized image
    return resized_image


scale_factor = 0.5


if __name__ == '__main__':
    root = Tk()
    root.title("Image randomizer")
    cur_img_stringvar = StringVar()


    def cbreload(*args):
        randimg = choose_current()
        # print(f"Displaying {randimg}")]
        im = Image.open(randimg)
        im = resize_image_2(im, scale_factor)
        img2 = ImageTk.PhotoImage(im)
        panel.configure(image=img2)
        panel.image = img2
        curr_image = os.path.basename(randimg)
        cur_img_stringvar.set(curr_image)
        
    def cbfn(*args):
        randimg = choose_previous()
        # print(f"Displaying {randimg}")]
        im = Image.open(randimg)
        im = resize_image_2(im, scale_factor)
        img2 = ImageTk.PhotoImage(im)
        panel.configure(image=img2)
        panel.image = img2
        curr_image = os.path.basename(randimg)
        cur_img_stringvar.set(curr_image)

    def cbrn(*args):
        randimg = choose_next()
        # print(f"Displaying {randimg}")]
        im = Image.open(randimg)
        im = resize_image_2(im, scale_factor)
        img2 = ImageTk.PhotoImage(im)
        panel.configure(image=img2)
        panel.image = img2
        curr_image = os.path.basename(randimg)
        cur_img_stringvar.set(curr_image)


    l_key = ['Left', 'Down', 'a', 's', 'n', 'b']
    r_key = ['Right', 'Up', 'w', 'd', 'm']

    def on_arrow_key_press(event):
        global scale_factor
        if event.keysym in l_key:
            cbrn()
        elif event.keysym in r_key:
            cbfn()
        elif event.keysym == 'z':
            scale_factor *= 0.5
            cbreload()
        elif event.keysym == 'x':
            scale_factor *= 2
            cbreload()
            


    root.bind('<z>', on_arrow_key_press)
    root.bind('<x>', on_arrow_key_press)
    root.bind('<m>', on_arrow_key_press)
    root.bind('<n>', on_arrow_key_press)
    root.bind('<b>', on_arrow_key_press)
    root.bind('<w>', on_arrow_key_press)
    root.bind('<a>', on_arrow_key_press)
    root.bind('<s>', on_arrow_key_press)
    root.bind('<d>', on_arrow_key_press)
    root.bind('<Left>', on_arrow_key_press)
    root.bind('<Right>', on_arrow_key_press)
    root.bind('<Up>', on_arrow_key_press)
    root.bind('<Down>', on_arrow_key_press)
    button = Button(root, text="Previous", command=cbrn)
    button.place(x=10)
    button = Button(root, text="Next", command=cbfn)
    button.place(x=70)

    panel = Label(root, textvariable=cur_img_stringvar)
    panel.pack()
    img = ImageTk.PhotoImage(Image.open(choose_next()))
    panel = Label(root, image=img)
    panel.pack()
    root.mainloop()
