import streamlit as st
from transformers import pipeline
import soundfile as sf
import torchaudio
import tempfile

# Set Streamlit page config first
st.set_page_config(page_title="Speech Recognition", layout="centered")

# Load the model
@st.cache_resource
def load_model():
    return pipeline("automatic-speech-recognition", model="openai/whisper-small")

asr_pipeline = load_model()

st.title("🎙️ Speech Recognition App")

uploaded_file = st.file_uploader("Upload an audio file (WAV, MP3, FLAC)", type=["wav", "mp3", "flac"])

def convert_to_mono(file_path):
    # Load the audio file using torchaudio
    waveform, sample_rate = torchaudio.load(file_path)
    
    # Convert to mono by averaging the channels (if stereo)
    if waveform.shape[0] > 1:
        waveform = waveform.mean(dim=0, keepdim=True)  # Average the stereo channels
    
    # Save the mono audio to a temporary file
    mono_path = file_path.replace(file_path.split('.')[-1], "mono.wav")
    torchaudio.save(mono_path, waveform, sample_rate)
    return mono_path

if uploaded_file:
    # Save uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    # Convert to mono audio
    temp_audio_path = convert_to_mono(temp_audio_path)

    # Read the converted mono audio
    try:
        audio_data, samplerate = sf.read(temp_audio_path)
    except Exception as e:
        st.error(f"Error reading audio file: {e}")
        st.stop()

    with st.spinner("Transcribing..."):
        try:
            # Transcribe the audio
            transcript = asr_pipeline({"array": audio_data, "sampling_rate": samplerate})["text"]
            st.subheader("📝 Transcription Result:")
            st.write(transcript)
        except Exception as e:
            st.error(f"Error during transcription: {e}")
            st.stop()
