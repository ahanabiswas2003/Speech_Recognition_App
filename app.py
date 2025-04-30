import streamlit as st
from transformers import pipeline
import soundfile as sf
import tempfile

# Load the model
@st.cache_resource
def load_model():
    return pipeline("automatic-speech-recognition", model="openai/whisper-small")

asr_pipeline = load_model()

st.set_page_config(page_title="Speech Recognition", layout="centered")

st.title("🎙️ Speech Recognition App")

uploaded_file = st.file_uploader("Upload an audio file (WAV, MP3, FLAC)", type=["wav", "mp3", "flac"])

if uploaded_file:
    # Save uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name.split('.')[-1]) as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    # Just read audio with soundfile, no mono conversion
    try:
        audio_data, samplerate = sf.read(temp_audio_path)
    except Exception as e:
        st.error(f"Error reading audio file: {e}")
        st.stop()

    with st.spinner("Transcribing..."):
        try:
            transcript = asr_pipeline({"array": audio_data, "sampling_rate": samplerate})["text"]
            st.subheader("📝 Transcription Result:")
            st.write(transcript)
        except Exception as e:
            st.error(f"Error during transcription: {e}")
            st.stop()
