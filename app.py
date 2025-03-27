import asyncio
import streamlit as st
import torch
import torchaudio
from transformers import pipeline
import soundfile as sf
import os
from pydub import AudioSegment
import tempfile

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


st.set_page_config(page_title="Speech Recognition", layout="centered")

@st.cache_resource
def load_model():
    return pipeline("automatic-speech-recognition", model="openai/whisper-small")

asr_pipeline = load_model()

st.title(" Speech Recognition App")

uploaded_file = st.file_uploader("Upload an audio file (WAV, MP3, FLAC)", type=["wav", "mp3", "flac"])

def convert_to_mono(file_path):
    audio = AudioSegment.from_file(file_path)
    audio = audio.set_channels(1)  
    mono_path = file_path.replace(file_path.split(".")[-1], "wav")
    audio.export(mono_path, format="wav")
    return mono_path

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name.split('.')[-1]) as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    temp_audio_path = convert_to_mono(temp_audio_path)


    audio_data, samplerate = sf.read(temp_audio_path)

    with st.spinner("Transcribing..."):
        transcript = asr_pipeline({"array": audio_data, "sampling_rate": samplerate})["text"]

    st.subheader("Transcription Result:")
    st.write(transcript)

    os.remove(temp_audio_path)