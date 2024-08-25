import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# Title of the app
st.title('Image Processing\nImage Gradients, Smoothing, and Thresholding')

# File uploader for image files
uploaded_file = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Read the uploaded image
    image = np.array(Image.open(uploaded_file))

    # Use st.expander to fold the original image display
    with st.expander("Show Original Image"):
        st.image(image, caption='Uploaded Image', use_column_width=True)

    # Select box for choosing the operation
    option = st.selectbox(
        'Choose an image processing operation:',
        ('Image Gradients', 'Smoothing', 'Thresholding')
    )

    processed_image = None

    if option == 'Image Gradients':
        # Display radio buttons for Image Gradients methods
        edge_method = st.radio(
            'Choose an Image Gradients method:',
            ('Laplacian', 'Sobel', 'Canny')
        )

        # Convert image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if edge_method == 'Laplacian':
            edges = cv2.Laplacian(gray_image, cv2.CV_64F)
            processed_image = np.uint8(np.absolute(edges))  # Convert to unsigned 8-bit image

        elif edge_method == 'Sobel':
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)  # X direction
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)  # Y direction
            processed_image = cv2.magnitude(sobelx, sobely)
            processed_image = np.uint8(np.absolute(processed_image))  # Convert to unsigned 8-bit image

        elif edge_method == 'Canny':
            processed_image = cv2.Canny(gray_image, 100, 200)

    elif option == 'Smoothing':
        # Display radio buttons for smoothing methods
        smoothing_method = st.radio(
            'Choose a smoothing method:',
            ('cv.blur', 'cv.GaussianBlur', 'cv.medianBlur', 'cv.bilateralFilter')
        )

        if smoothing_method == 'cv.blur':
            processed_image = cv2.blur(image, (5, 5))

        elif smoothing_method == 'cv.GaussianBlur':
            processed_image = cv2.GaussianBlur(image, (5, 5), 0)

        elif smoothing_method == 'cv.medianBlur':
            processed_image = cv2.medianBlur(image, 5)

        elif smoothing_method == 'cv.bilateralFilter':
            processed_image = cv2.bilateralFilter(image, 9, 75, 75)

    elif option == 'Thresholding':
        # Convert image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Display radio buttons for thresholding methods
        threshold_method = st.radio(
            'Choose a thresholding method:',
            ('THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV', 'THRESH_OTSU')
        )

        if threshold_method == 'THRESH_BINARY':
            _, processed_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

        elif threshold_method == 'THRESH_BINARY_INV':
            _, processed_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

        elif threshold_method == 'THRESH_TRUNC':
            _, processed_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_TRUNC)

        elif threshold_method == 'THRESH_TOZERO':
            _, processed_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_TOZERO)

        elif threshold_method == 'THRESH_TOZERO_INV':
            _, processed_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_TOZERO_INV)

        elif threshold_method == 'THRESH_OTSU':
            _, processed_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    if processed_image is not None:
        # Display the processed image
        st.write(f'{option} Processed Image:')
        st.image(processed_image, caption=f'{option} Processed Image', use_column_width=True, channels="GRAY" if option != 'Smoothing' else "RGB")

        # Convert the processed image to a format that can be downloaded
        processed_pil_image = Image.fromarray(processed_image)
        buffered = BytesIO()
        processed_pil_image.save(buffered, format="PNG")
        img_data = buffered.getvalue()

        # Download button
        st.download_button(
            label="Download Processed Image",
            data=img_data,
            file_name="processed_image.png",
            mime="image/png"
        )





