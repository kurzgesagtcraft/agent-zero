import asyncio
import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10811'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10811'
from python.helpers import runtime, whisper, settings
from python.helpers.print_style import PrintStyle
from python.helpers import kokoro_tts
import models


def preload():
    try:
        set = settings.get_default_settings()

        # preload whisper model
        try:
            whisper.preload(set["stt_model_size"])
        except Exception as e:
            PrintStyle().error(f"Error in preload_whisper: {e}")

        # preload embedding model
        if set["embed_model_provider"] == models.ModelProvider.HUGGINGFACE.name:
            try:
                # Use the new LiteLLM-based model system
                emb_mod = models.get_embedding_model(
                    models.ModelProvider.HUGGINGFACE, set["embed_model_name"]
                )
                emb_mod.embed_query("test")
            except Exception as e:
                PrintStyle().error(f"Error in preload_embedding: {e}")

        # preload kokoro tts model if enabled
        if set["tts_kokoro"]:
            try:
                kokoro_tts.preload()
            except Exception as e:
                PrintStyle().error(f"Error in preload_kokoro: {e}")

        PrintStyle().print("Preload completed")
    except Exception as e:
        PrintStyle().error(f"Error in preload: {e}")


# preload transcription model
if __name__ == "__main__":
    PrintStyle().print("Running preload...")
    runtime.initialize()
    preload()
