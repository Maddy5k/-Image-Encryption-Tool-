import streamlit as st
from PIL import Image
import numpy as np
import io

# Set up the secret key for encryption and decryption
KEY = 50  # You can change this value to something else for different results

# Encrypt function
def encrypt_image(img):
    img_array = np.array(img)
    encrypted_array = img_array + KEY
    encrypted_array = np.clip(encrypted_array, 0, 255)  # Clip values to be between 0 and 255
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    return encrypted_img

# Decrypt function
def decrypt_image(img):
    img_array = np.array(img)
    decrypted_array = img_array - KEY
    decrypted_array = np.clip(decrypted_array, 0, 255)  # Clip values to be between 0 and 255
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    return decrypted_img

# Function to convert PIL image to byte format
def pil_to_bytes(img, format='PNG'):
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format=format)
    return img_byte_arr.getvalue()

# Streamlit UI
st.title("Image Encryption and Decryption")

# Upload Image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Option to choose between encrypting and decrypting
    choice = st.radio("Select operation", ("Encrypt", "Decrypt"))

    if choice == "Encrypt":
        # Encrypt the image
        encrypted_img = encrypt_image(img)
        st.image(encrypted_img, caption="Encrypted Image", use_container_width=True)
        
        # Convert to bytes and create a download button
        encrypted_img_bytes = pil_to_bytes(encrypted_img)
        st.download_button("Download Encrypted Image", encrypted_img_bytes, "encrypted_image.png", "image/png")

    elif choice == "Decrypt":
        # Decrypt the image
        decrypted_img = decrypt_image(img)
        st.image(decrypted_img, caption="Decrypted Image", use_container_width=True)
        
        # Convert to bytes and create a download button
        decrypted_img_bytes = pil_to_bytes(decrypted_img)
        st.download_button("Download Decrypted Image", decrypted_img_bytes, "decrypted_image.png", "image/png")
