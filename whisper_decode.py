# whisper_decode.py — real-time voice decode on DGX Spark
import whisper
from io import BytesIO

model = whisper.load_model("base.en")  # runs on GPU automatically

def decode_audio(audio_bytes):
    audio = BytesIO(audio_bytes)
    result = model.transcribe(audio, fp16=True)
    return result["text"].strip()  # e.g., "Log dose 1.4 mg/kg patient 123"
