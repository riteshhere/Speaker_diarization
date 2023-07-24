import torch
import torchaudio
import pyannote.audio
from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding
from pyannote.audio import Audio
from pyannote.core import Segment
import contextlib
import wave
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import datetime
import subprocess


class SpeakerDiarizer:
    def __init__(self, num_speakers=2):
        self.num_speakers = num_speakers

        # NOTE: You would have to ensure that the necessary libraries are installed
        # and the models are available on the path where this class is used
        import whisper
        self.model = whisper.load_model('large')
        self.embedding_model = PretrainedSpeakerEmbedding(
            "speechbrain/spkrec-ecapa-voxceleb",
            device=torch.device("cuda"))

    def segment_embedding(self, segment, path, duration):
        start = segment["start"]
        end = min(duration, segment["end"])
        clip = Segment(start, end)
        audio = Audio()
        waveform, sample_rate = audio.crop(path, clip)
        return self.embedding_model(waveform[None])

    def diarize(self, path):
        if path[-3:] != 'wav':
            subprocess.call(['ffmpeg', '-i', path, 'audio.wav', '-y'])
            path = 'audio.wav'

        result = self.model.transcribe(path)
        segments = result["segments"]

        with contextlib.closing(wave.open(path,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)

        embeddings = np.zeros(shape=(len(segments), 192))
        for i, segment in enumerate(segments):
            embeddings[i] = self.segment_embedding(segment, path, duration)

        embeddings = np.nan_to_num(embeddings)

        clustering = AgglomerativeClustering(self.num_speakers).fit(embeddings)
        labels = clustering.labels_
        for i in range(len(segments)):
            segments[i]["speaker"] = 'SPEAKER ' + str(labels[i] + 1)

        def time(secs):
            return datetime.timedelta(seconds=round(secs))

        transcript = ""
        for (i, segment) in enumerate(segments):
            if i == 0 or segments[i - 1]["speaker"] != segment["speaker"]:
                transcript += "\n" + segment["speaker"] + ' ' + str(time(segment["start"])) + '\n'
            transcript += segment["text"][1:] + ' '

        return transcript
