from PIL import Image
import os

def alpha_blend(background, overlay, position):
    bg_width, bg_height = background.size
    overlay = overlay.convert("RGBA")
    overlay_width, overlay_height = overlay.size
    new_image = background.copy()
    for x in range(overlay_width):
        for y in range(overlay_height):
            bg_x = position[0] + x
            bg_y = position[1] + y
            if 0 <= bg_x < bg_width and 0 <= bg_y < bg_height:
                bg_pixel = background.getpixel((bg_x, bg_y))
                overlay_pixel = overlay.getpixel((x, y))
                new_pixel = (
                    int((1 - overlay_pixel[3] / 255.0) * bg_pixel[0] + overlay_pixel[3] / 255.0 * overlay_pixel[0]),
                    int((1 - overlay_pixel[3] / 255.0) * bg_pixel[1] + overlay_pixel[3] / 255.0 * overlay_pixel[1]),
                    int((1 - overlay_pixel[3] / 255.0) * bg_pixel[2] + overlay_pixel[3] / 255.0 * overlay_pixel[2]),
                )
                new_image.putpixel((bg_x, bg_y), new_pixel)

    return new_image

overlay_folder = "Datasets/cartoonset10k"
# Open the background image
background_image = Image.open("Images/VOTERID.png")
# Define the position for placing the overlay image
position = (17, 50)
# Iterate through the overlay image files in the folder
for i,filename in enumerate(os.listdir(overlay_folder)):
    if i==60:
        break
    if filename.endswith(".png"):
        overlay_path = os.path.join(overlay_folder, filename)
        overlay_image = Image.open(overlay_path)
        resized_overlay = overlay_image.resize((180, 180))
        result_image = alpha_blend(background_image.copy(), resized_overlay, position)
        result_image.save(f"FACES_ON_VOTERID/RESULT_{filename}")
