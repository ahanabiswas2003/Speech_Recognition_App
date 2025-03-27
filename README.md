This is a **Speech Recognition Web App** that allows users to upload or record audio and get the transcribed text. The application utilizes **Hugging Face Transformers** for speech-to-text conversion and is built using **Streamlit** for an interactive UI.

## Features
- 🎙️ Upload audio
- 📜 Convert speech to text using **Hugging Face ASR models**.
- 🖥️ User-friendly **Streamlit** interface.
- ☁️ **Deployed on Streamlit Community Cloud** for free access.

---

## Technologies Used
- **Python**: Core programming language.
- **Hugging Face Transformers**: Speech recognition model.
- **Streamlit**: UI framework.
- **Pydub**: Audio processing.
- **FFmpeg**: Required for handling audio formats.
- **Torch & Torchaudio**: Backend support for ASR models.

---

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/speech-recognition-app.git
cd speech-recognition-app
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Install FFmpeg (Required for Audio Processing)
- **Windows**:
  - Download from: https://ffmpeg.org/download.html
  - Add FFmpeg to system PATH.
- **Linux**:
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```
- **Mac**:
  ```bash
  brew install ffmpeg
  ```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

---

## Deployment on Streamlit Cloud

### **Step 1: Push to GitHub**
Ensure your project is in a **public GitHub repository**.

### **Step 2: Deploy on Streamlit**
1. Go to [Streamlit Cloud](https://share.streamlit.io/).
2. Click **New App**.
3. Select your GitHub repository.
4. Set **main script path** to `app.py`.
5. Click **Deploy**.

Your app will be live at:
```
https://your-username-your-repo-name.streamlit.app
```

---

## Usage
1. Open the app in your browser.
2. Upload or record an audio file.
3. Click **Transcribe**.
4. View and copy the transcribed text.

---

## Troubleshooting
- **ModuleNotFoundError (torchaudio, transformers, etc.)** → Run `pip install -r requirements.txt`.
- **FFmpeg Not Found Error** → Ensure FFmpeg is installed and added to PATH.
- **App Not Deploying on Streamlit** → Check logs under **Manage App** in Streamlit Cloud.

---

## Contributing
Feel free to fork the repository and submit **pull requests** for improvements!

---


