🔐 Steganography Project

A simple image steganography application built with Python and Streamlit. This project allows users to hide secret text messages inside images and extract them later.

✨ Features

- Hide Text: Embed secret text messages into images.
- Reveal Text: Extract hidden messages from images.
- User-Friendly Interface: Interact with the application through a simple Streamlit interface.
- Image Support: Upload PNG and JPG images for hiding text.
- PNG Output: Save the resulting image as a PNG file.

🛠️ Technologies Used

- Python
- Streamlit
- Pillow (PIL)
- Stegano

📦 Installation

1. Clone the Repository

git clone https://github.com/MahdiMahdi1387/Steganography_Project.git
cd Steganography_Project

2. Create a Virtual Environment (Optional)

python -m venv .venv

Activate it on Linux:

source .venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

▶️ Usage

Run the application using Streamlit:

streamlit run app.py

Open the local URL displayed in your terminal to access the application.

Hide Text

1. Select Hide Text from the sidebar.
2. Upload an image.
3. Enter the secret text you want to hide.
4. Click HIDE.
5. The application generates an image containing the hidden message.

Reveal Text

1. Select Reveal Text from the sidebar.
2. Upload an image containing a hidden message.
3. Click REVEAL.
4. The application extracts and displays the hidden text, if successful.

📁 Project Structure

Steganography_Project/
├── app.py
├── requirements.txt
└── README.md

🔍 How It Works

The application uses the Stegano library to perform image steganography.

Steganography is a technique for concealing information inside another medium, such as an image. In this project, secret text is hidden inside an image and can later be extracted using the corresponding reveal functionality.

⚠️ Limitations

- The application currently focuses on hiding and extracting text messages.
- The output image is saved in PNG format.
- Successful extraction requires an image containing a compatible hidden message.
- This project is intended for learning and experimentation and should not be considered a complete security or encryption solution.

👨‍💻 Author

Mahdi

📄 License

No license has been specified yet.
