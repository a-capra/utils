#!/usr/bin/env python3
"""
Convert multiple images (JPG, PNG, TIFF, SVG, BMP, etc.) into a single PDF file.
"""

import sys
from PIL import Image


def images_to_pdf(image_paths, output_pdf):
    """
    Convert multiple images into a single PDF file.
    
    Args:
        image_paths: List of paths to image files
        output_pdf: Path to the output PDF file
    """
    try:
        # Open all images
        images = []
        for img_path in image_paths:
            img = Image.open(img_path)
            # Convert images to RGB mode if necessary (PDF requires RGB)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            images.append(img)
        
        if not images:
            print("Error: No images provided", file=sys.stderr)
            sys.exit(1)
        
        # Save the first image as PDF and append the rest with reduced quality
        if len(images) == 1:
            images[0].save(output_pdf, quality=50, optimize=True)
        else:
            images[0].save(output_pdf, save_all=True, append_images=images[1:], 
                          quality=50, optimize=True)
        
        print(f"Successfully created PDF: {output_pdf}")
        print(f"Images merged: {len(images)}")
        
    except FileNotFoundError as e:
        print(f"Error: Image file not found - {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print("Usage: python jpg2pdf.py <image1> <image2> [image3 ...] <output.pdf>")
        print("Example: python jpg2pdf.py page1.jpg page2.png page3.tiff document.pdf")
        print("\nSupported formats: JPG, PNG, TIFF, BMP, GIF, and other PIL-supported formats")
        sys.exit(1)
    
    image_paths = sys.argv[1:-1]
    output_pdf = sys.argv[-1]
    
    images_to_pdf(image_paths, output_pdf)


if __name__ == "__main__":
    main()
