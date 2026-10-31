#!/usr/bin/env python3
"""
Image Knot Weaver - Digital Image Manipulation
Spinning image transformations and artistic effects...
"""

from PIL import Image, ImageFilter, ImageEnhance, ImageChops
import numpy as np
import math

def load_image(path):
    """Load an image from file"""
    return Image.open(path).convert('RGB')

def apply_filter(image, filter_type='blur'):
    """Apply various filters to the image"""
    if filter_type == 'blur':
        return image.filter(ImageFilter.BLUR)
    elif filter_type == 'edge':
        return image.filter(ImageFilter.FIND_EDGES)
    elif filter_type == 'contours':
        return image.filter(ImageFilter.CONTOUR)
    elif filter_type == 'smooth':
        return image.filter(ImageFilter.SMOOTH)
    elif filter_type == 'dodge':
        return image.filter(ImageFilter.DODGE)
    elif filter_type == 'burn':
        return image.filter(ImageFilter.BURN)
    else:
        return image

def adjust_brightness(image, factor):
    """Adjust brightness by a factor (positive = brighter)"""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    """Adjust contrast by a factor (positive = higher contrast)"""
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def rotate_image(image, angle=45):
    """Rotate image by specified angle"""
    w, h = image.size
    rot_matrix = [(-math.radians(angle)), 0, 0, math.radians(angle), 0, 1]
    
    # Using PIL rotate instead (simpler)
    return image.rotate(angle, expand=True)

def sepia_tone(image):
    """Apply sepia tone filter"""
    width, height = image.size
    pixels = image.load()
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            
            # Apply sepia transformation
            sepia_r = int(0.393 * r + 0.581 * g + 0.163 * b)
            sepia_g = int(0.274 * r + 0.537 * g + 0.130 * b)
            sepia_b = int(0.189 * r + 0.464 * g + 0.051 * b)
            
            pixels[x, y] = (sepia_r, sepia_g, sepia_b)
    
    return image

def create_dithered_image(image):
    """Apply simple color quantization posterization effect"""
    width, height = image.size
    
    # Convert to RGB and then apply simple color reduction/quantization
    rgb_image = image.convert('RGB')
    pixels = rgb_image.load()
    
    # Simple color quantization - reduce to 16 levels per channel (posterization)
    factor = 256 // 16  # 16
    
    new_pixels = []
    
    for x in range(width):
        row = []
        for y in range(height):
            r, g, b = pixels[x, y]
            
            # Quantize colors to 16 levels (creates posterized effect)
            q_r = int((r // factor) * factor)
            q_g = int((g // factor) * factor)
            q_b = int((b // factor) * factor)
            
            row.append((q_r, q_g, q_b))
        new_pixels.extend(row)
    
    # Create new image with quantized colors
    dithered_image = Image.new('RGB', (width, height), color=(0, 0, 0))
    dithered_image.putdata(new_pixels)
    
    return dithered_image

def main():
    """Demonstrate image manipulation capabilities"""
    
    print("Image Knot Weaver - Digital Image Manipulation Suite")
    print("=" * 50)
    
    # Create a test pattern programmatically if no input
    import os
    
    # First, let's create a sample canvas to demonstrate the tools
    canvas_size = (600, 400)
    
    # Create gradient background
    img_array = np.zeros((canvas_size[1], canvas_size[0], 3), dtype=np.uint8)
    
    # Add some color variation
    for i in range(canvas_size[1]):
        for j in range(canvas_size[0]):
            img_array[i, j, 0] = (j % 256 * 2) // 2  # Red gradient
            img_array[i, j, 1] = (i % 256 * 3) // 3  # Green gradient  
            img_array[i, j, 2] = ((i + j) % 256) / 4  # Blue diagonal
    
    test_image = Image.fromarray(img_array)
    
    # Apply various transformations
    print("\nApplying image filters...")
    
    blur_result = apply_filter(test_image, 'blur')
    edge_result = apply_filter(test_image, 'edge')
    contours_result = apply_filter(test_image, 'contours')
    
    print("Applying artistic effects...")
    
    sepia_result = sepia_tone(blur_result)
    rotated_result = rotate_image(sepia_result, 30)
    
    brightened = adjust_brightness(rotated_result, 1.2)
    contrast_boost = adjust_contrast(brightened, 1.5)
    
    print("Applying color posterization...")
    
    # Simple dithering/pseudo-color reduction
    posterized = create_dithered_image(contrast_boost)
    
    print("Applying contour filter...")
    contours2 = apply_filter(test_image, 'contours')
    
    # Save demonstration results
    output_base = 'projects/image_knots/results'
    
    os.makedirs(output_base, exist_ok=True)
    
    test_image.save(os.path.join(output_base, 'gradient_canvas.png'))
    blur_result.save(os.path.join(output_base, 'blur_effect.png'))
    edge_result.save(os.path.join(output_base, 'edge_detection.png'))
    contours_result.save(os.path.join(output_base, 'contours.png'))
    sepia_result.save(os.path.join(output_base, 'sepia_tone.png'))
    rotated_result.save(os.path.join(output_base, 'rotated_30deg.png'))
    posterized.save(os.path.join(output_base, 'posterized_image.png'))
    
    print(f"\nImage knot weavings saved to {output_base}/")
    print("Available operations:")
    print("  - Filters: blur, edge, contours, smooth, dodge, burn")
    print("  - Adjustments: brightness, contrast")
    print("  - Transformations: rotate, sepia tone, posterization")

if __name__ == '__main__':
    import math
    main()
