#!/usr/bin/env python3

# remove white rectangle from bottom of scanned images

import os
from PIL import Image

input_folder = "040-scan-pages"
output_folder = "045-crop-scan-area"

def remove_white_bottom(input_path, output_path):
    img = Image.open(input_path).convert("RGB")
    width, height = img.size
    pixels = img.load()

    # Scan upward from bottom
    crop_line = height
    for y in range(height - 1, -1, -1):
        row_all_white = True
        for x in range(width):
            if pixels[x, y] != (255, 255, 255):  # not pure white
                row_all_white = False
                break
        if not row_all_white:
            crop_line = y + 1
            break

    # Crop if needed
    if crop_line < height:
        img_cropped = img.crop((0, 0, width, crop_line))
    else:
        img_cropped = img.copy()

    img_cropped.save(output_path)

def batch_process_tiffs(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in sorted(os.listdir(input_folder)):
        if filename.lower().endswith((".tif", ".tiff")):
            in_path = os.path.join(input_folder, filename)
            out_path = os.path.join(output_folder, filename)
            if os.path.exists(out_path):
                # print(f"Keeping {out_path}")
                continue

            print(f"Writing {out_path}")
            remove_white_bottom(in_path, out_path)

if __name__ == "__main__":
    batch_process_tiffs(input_folder, output_folder)
