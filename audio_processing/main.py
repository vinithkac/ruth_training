import torch

from utils import _models

OUTPUT_DIR = "transcripts"


class Transcribe:
    def __init__(self, model: str = "large", language: str = "en"):
        self.model = model
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.language = language

    def transcribe(self):
        pass


t = Transcribe()
