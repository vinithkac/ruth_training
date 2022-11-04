import torch

from utils import _models, load_model

OUTPUT_DIR = "transcripts"


class Transcribe:
    def __init__(self, model_name: str = "large", language: str = "en"):

        if model_name not in _models():
            raise RuntimeError(f"Model {model_name} not found; available models = {_models()}")
        self.model = load_model(model_name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.language = language

    def transcribe(self):
        pass


t = Transcribe()
