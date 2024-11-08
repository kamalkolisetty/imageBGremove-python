from rembg import remove
from PIL import Image
import io

# Define input and output paths
input_path = r"C:\Users\kamal\OneDrive\Desktop\pythOOONNN\inp1.jpg"
output_path = "final2.png"

# Open the input image in binary mode
with open(input_path, "rb") as input_file:
    input_data = input_file.read()
    
    # Remove the background
    output_data = remove(input_data)
    
    # Convert the output to an image format and save it
    output_image = Image.open(io.BytesIO(output_data))
    output_image.save(output_path)

# Display the output image
output_image.show()
