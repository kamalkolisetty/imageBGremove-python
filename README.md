 
# Image Background Remover

This project removes the background from an image using the `rembg` library in Python and saves the output as a PNG image with transparency.

## 📄 Project Overview

The Image Background Remover takes an input image file, processes it to remove the background, and outputs a new image file with transparent areas where the background was removed. This can be useful for creating product images, profile photos, and more.

## 📦 Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/kamalkolisetty/imageBGremove-python.git
     
    ```

2. **Install Dependencies**

   Ensure you have Python 3 installed, then install the required libraries:
    ```bash
    pip install rembg pillow
    ```

> Note: If you encounter issues with `rembg`, check for specific versions of dependencies, as `pooch` or other libraries may need downgrading for compatibility.

## 🛠 Usage

1. Place the image you want to process in the project directory.

2. Edit `background_remover.py` to set your file paths:
   ```python
   input_path = r"your_image_path.jpg"  # Path to your input image
   output_path = "output.png"           # Path for the saved output image
   ```

3. Run the script:
    ```bash
    python background_remover.py
    ```

4. The output image (`output.png`) with a transparent background will be saved in the same directory.

## 📜 Example Code

Here’s the Python code used in this project:

```python
from rembg import remove
from PIL import Image
import io

# Define input and output paths
input_path = r"your_image_path.jpg"
output_path = "output.png"

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
```

## ✅ Requirements

- Python 3.6+
- `rembg` (background removal library)
- `Pillow` (Python Imaging Library)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## 🐛 Troubleshooting

If you encounter `TypeError: retrieve() got an unexpected keyword argument 'progressbar'`:
1. Downgrade `pooch`:
   ```bash
   pip install pooch==1.6.0
   ```

2. Alternatively, remove `progressbar=True` from `rembg`'s `u2net.py` file in your Python environment:
   - Go to `<your Python path>/lib/site-packages/rembg/sessions/u2net.py`
   - Remove `progressbar=True` from `pooch.retrieve(...)` in the file.

 
## 🙌 Acknowledgments

- The `rembg` library by [danielgatis](https://github.com/danielgatis/rembg) for the powerful background removal tool.
- `Pillow` for Python image handling.

---

## 🎬 Demonstration

Here’s a demonstration of how the code works with an example image:

1. **Original Image**:
   ![Original Image](inp1.jpg)

2. **Output Image with Transparent Background**:
   ![Output Image](final2.png)
 

