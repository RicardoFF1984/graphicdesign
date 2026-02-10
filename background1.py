from PIL import Image
import numpy as np
import os
from pathlib import Path

def create_gradient(width=1920, height=1080, color1=(255, 0, 128), color2=(0, 128, 255)):
    """Create a smooth gradient background"""
    img = np.zeros((height, width, 3), dtype=np.uint8)
    
    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        img[y, :] = [r, g, b]
    
    return Image.fromarray(img)

# ===== CUSTOMIZE THESE =====
folder_name = "MyBackgrounds"  # ← Change this to your folder name
file_name = "cool_gradient.png"  # ← Change this to your file name
# ===========================

# Get desktop path
desktop = os.path.join(Path.home(), 'Desktop')

# Create your custom folder on desktop
save_folder = os.path.join(desktop, folder_name)
os.makedirs(save_folder, exist_ok=True)

# Create full path with your file name
full_path = os.path.join(save_folder, file_name)

# Create and save
bg = create_gradient()
bg.save(full_path)

print(f"✓ Saved successfully!")
print(f"📁 Folder: {save_folder}")
print(f"📄 File: {file_name}")
