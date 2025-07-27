from python.helpers.api import ApiHandler, Request, Response

from python.helpers import runtime, settings, whisper

class Transcribe(ApiHandler):
    def process(self, input: dict, request: Request) -> dict | Response:
        audio = input.get("audio")
        ctxid = input.get("ctxid", "")

        context = self.get_context(ctxid)
        if not whisper.is_downloaded():
            context.log.log(type="info", content="Whisper STT model is currently being initialized, please wait...")

        set = settings.get_settings()
        result = whisper.transcribe(set["stt_model_size"], audio) # type: ignore
        return result
