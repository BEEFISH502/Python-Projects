from PIL import Image, ImageTk
import tkinter as tk
import numpy as np

# ASCII character set from darkest to lightest
ascii_characters = "@%#*+=-:. "  # Characters from darkest to lightest

def resize_image(image, new_width, new_height):
    """Resize image to specified width and height while maintaining aspect ratio."""
    aspect_ratio = image.height / image.width
    if new_height is None:
        new_height = int(new_width * aspect_ratio)  # Maintain aspect ratio if height is not specified
    else:
        # If height is specified, adjust width to maintain aspect ratio
        new_width = int(new_height * aspect_ratio)
    
    print(f"Resizing image to {new_width}x{new_height}...")
    return image.resize((new_width, new_height))

def luminance_to_ascii(luminance):
    """Map normalized luminance (0 to 1) to an ASCII character based on its intensity."""
    index = int(luminance * (len(ascii_characters) - 1))  # Scale luminance to index
    return ascii_characters[index]

def generate_ascii_art(image, width=200, height=200):
    print("Resizing image for ASCII output...")
    image = resize_image(image, width, height)

    print("Converting to grayscale...")
    grayscale_image = image.convert("L")

    # Inverting the grayscale image
    inverted_grayscale_image = Image.eval(grayscale_image, lambda x: 255 - x)

    grayscale_array = np.array(inverted_grayscale_image) / 255  # Normalize to 0-1

    ascii_art = ""
    print("Generating ASCII art...")
    for y in range(grayscale_image.height):
        for x in range(grayscale_image.width):
            luminance = grayscale_array[y, x]
            ascii_char = luminance_to_ascii(luminance)
            ascii_art += ascii_char
        ascii_art += '\n'  # New line for each row

    print("ASCII art generated.")
    return ascii_art

def show_ascii_art(ascii_art):
    print("Setting up Tkinter window...")
    root = tk.Tk()
    root.title("ASCII Art Viewer")

    # Use a fixed font size for the ASCII characters to minimize window size change
    text_widget = tk.Text(root, wrap=tk.NONE, font=("Courier", 2), bg="black", fg="white")  # Font size for ASCII
    text_widget.insert(tk.END, ascii_art)
    text_widget.config(state=tk.DISABLED)  # Make it read-only
    text_widget.pack(expand=True, fill=tk.BOTH)

    print("Starting Tkinter main loop...")
    root.mainloop()

# Main function to load the image and generate ASCII art
def main(image_path, width=300, height=300):
    print(f"Loading image from: {image_path}")
    try:
        image = Image.open(image_path).convert('RGB')  # Load the image
    except Exception as e:
        print(f"Error loading image: {e}")
        print("Image loaded successfully.")
        return

    # Generate ASCII art
    ascii_art = generate_ascii_art(image, width=width, height=height)

    # Show the ASCII art in a Tkinter window
    show_ascii_art(ascii_art)

# Specify the C:image path
image_path = 'C:/Users/Brandon/OneDrive/IMG_1143.jpg'  # Update with your image path

# Run the main function with desired ASCII width and height
if __name__ == "__main__":
    main(image_path, width=300, height=300)  # Adjust width and height as desired 