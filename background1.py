from PIL import Image
import numpy as np
import os
from pathlib import Path

def create_gradient(width=1920, height=1080, color1=(255, 0, 128), color2=(0, 128, 255)):
    """Create a smooth gradient background"""
    
    # Create a blank image array with dimensions: height x width x 3 color channels (RGB)
    # dtype=np.uint8 means each color value is 0-255
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Loop through each horizontal row of pixels (from top to bottom)
    for y in range(height):
        # Calculate blend ratio: 0.0 at top, 1.0 at bottom
        ratio = y / height
        
        # Blend the red channel: more color1 at top, more color2 at bottom
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        # Blend the green channel
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        # Blend the blue channel
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        
        # Set all pixels in this row (y) to the calculated RGB color
        img[y, :] = [r, g, b]
    
    # Convert NumPy array to PIL Image object and return it
    return Image.fromarray(img)

# Get folder name from user
print("=== Gradient Background Creator ===\n")
folder_name = input("Enter folder name (e.g., MyBackgrounds): ")

# Get file name from user
file_name = input("Enter file name (e.g., gradient.png): ")

# Make sure the file has .png extension
if not file_name.endswith('.png'):
    file_name += '.png'

# Get first color (top of gradient) from user
print("\nEnter the TOP color (RGB values 0-255):")
r1 = int(input("  Red (0-255): "))
g1 = int(input("  Green (0-255): "))
b1 = int(input("  Blue (0-255): "))
color1 = (r1, g1, b1)

# Get second color (bottom of gradient) from user
print("\nEnter the BOTTOM color (RGB values 0-255):")
r2 = int(input("  Red (0-255): "))
g2 = int(input("  Green (0-255): "))
b2 = int(input("  Blue (0-255): "))
color2 = (r2, g2, b2)

# Get the path to the user's Desktop folder
desktop = os.path.join(Path.home(), 'Desktop')

# Create the full path to your custom folder on the desktop
save_folder = os.path.join(desktop, folder_name)

# Create the folder if it doesn't exist (exist_ok=True prevents errors if it already exists)
os.makedirs(save_folder, exist_ok=True)

# Create the complete file path (folder + filename)
full_path = os.path.join(save_folder, file_name)

# Create the gradient image with user's custom colors
bg = create_gradient(color1=color1, color2=color2)

# Save the image to the specified path as a PNG file
bg.save(full_path)

# Print success messages showing where the file was saved
print(f"\n✓ Saved successfully!")
print(f"📁 Folder: {save_folder}")
print(f"📄 File: {file_name}")
print(f"🎨 Colors: {color1} → {color2}")
