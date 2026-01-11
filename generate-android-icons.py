import os
from PIL import Image

# --- CONFIGURATION ---
# Replace this with the exact name of your icon file
SOURCE_IMAGE = "icon.png" 
# ---------------------

def create_icon_bundle(source_image_path, output_folder="custom_icon_bundle"):
    densities = {
        "mipmap-mdpi": 108,
        "mipmap-hdpi": 162,
        "mipmap-xhdpi": 216,
        "mipmap-xxhdpi": 324,
        "mipmap-xxxhdpi": 432
    }

    if not os.path.exists(source_image_path):
        print(f"Error: Could not find '{source_image_path}'. Make sure the file is in this folder.")
        return

    img = Image.open(source_image_path).convert("RGBA")

    for folder_name, size in densities.items():
        folder_path = os.path.join(output_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Foreground (Your Icon)
        foreground = img.resize((size, size), Image.Resampling.LANCZOS)
        foreground.save(os.path.join(folder_path, "morphe_adaptive_foreground_custom.png"))

        # Background (Transparent)
        background = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        background.save(os.path.join(folder_path, "morphe_adaptive_background_custom.png"))

    print(f"Success! Bundle created in: {os.path.abspath(output_folder)}")

if __name__ == "__main__":
    create_icon_bundle(SOURCE_IMAGE)