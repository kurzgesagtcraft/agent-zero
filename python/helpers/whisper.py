import base64
import warnings
import whisper
import tempfile
import time
import asyncio
from python.helpers import runtime, rfc, settings, files
from python.helpers.print_style import PrintStyle

# Suppress FutureWarning from torch.load
warnings.filterwarnings("ignore", category=FutureWarning)

_model = None
_model_name = ""
is_updating_model = False  # Tracks whether the model is currently updating

def preload(model_name:str):
    try:
        # return runtime.call_development_function(_preload, model_name)
        return _preload(model_name)
    except Exception as e:
        # if not runtime.is_development():
        raise e
        
def _preload(model_name:str):
    global _model, _model_name, is_updating_model

    while is_updating_model:
        time.sleep(0.1)

    try:
        is_updating_model = True
        if not _model or _model_name != model_name:
                PrintStyle.standard(f"Loading Whisper model: {model_name}")
                _model = whisper.load_model(name=model_name, download_root=files.get_abs_path("/tmp/models/whisper")) # type: ignore
                _model_name = model_name
    finally:
        is_updating_model = False

def is_downloading():
    # return runtime.call_development_function(_is_downloading)
    return _is_downloading()

def _is_downloading():
    return is_updating_model

def is_downloaded():
    try:
        # return runtime.call_development_function(_is_downloaded)
        return _is_downloaded()
    except Exception as e:
        # if not runtime.is_development():
        raise e
        # Fallback to direct execution if RFC fails in development
        # return _is_downloaded()

def _is_downloaded():
    return _model is not None

def transcribe(model_name:str, audio_bytes_b64: str):
    # return runtime.call_development_function(_transcribe, model_name, audio_bytes_b64)
    return _transcribe(model_name, audio_bytes_b64)


def _transcribe(model_name:str, audio_bytes_b64: str):
    _preload(model_name)
    
    # Decode audio bytes if encoded as a base64 string
    audio_bytes = base64.b64decode(audio_bytes_b64)

    # Create temp audio file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as audio_file:
        audio_file.write(audio_bytes)

    # Transcribe the audio file
    result = _model.transcribe(audio_file.name, fp16=False) # type: ignore
    return result
