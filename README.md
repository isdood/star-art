# star-art
A cross-platform studio for developing pixel art, with AI integration &amp; tool-kits.

## Installation Instructions

### Arch Linux
1. Clone the repository:
   ```sh
   git clone https://github.com/isdood/star-art.git
   cd star-art
   ```
2. Install the required dependencies:
   ```sh
   sudo pacman -S python python-pip
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python src/main.py
   ```

### Android
1. Clone the repository:
   ```sh
   git clone https://github.com/isdood/star-art.git
   cd star-art
   ```
2. Install the required dependencies:
   ```sh
   termux-setup-storage
   pkg install python
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python src/main.py
   ```

### Web Version
1. Clone the repository:
   ```sh
   git clone https://github.com/isdood/star-art.git
   cd star-art
   ```
2. Navigate to the `web` directory:
   ```sh
   cd web
   ```
3. Start a local web server:
   ```sh
   python -m http.server
   ```
4. Open your web browser and go to `http://localhost:8000` to run the application.

## Usage Instructions
1. Launch the application.
2. Use the pixel art tool-kits to create and edit pixel art.
3. Explore the AI integration features to enhance your artwork.
4. Customize the UI/theming elements to suit your preferences.
5. Use the animation tool to create and manage frame-by-frame animations.
6. Upload a photo using the "Upload Photo" button.
7. Reimagine the uploaded photo in a pixel art format using the "Reimagine with AI" button.

## Contributing Guidelines
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```sh
   git checkout -b feature-name
   ```
3. Make your changes and commit them with descriptive messages:
   ```sh
   git commit -m "Add feature description"
   ```
4. Push your changes to your forked repository:
   ```sh
   git push origin feature-name
   ```
5. Create a pull request to the main repository.
