# Speech_diarization
Speech Diarization for scrum automation 

### What is speaker diarization
Speaker diarization, also known as diarization, involves segregating an audio stream with human speech into consistent segments based on the individual identity of each speaker.

### How to perform Speaker diarization?
1. Convert Audio to Text using Whisper
2. Segregate the text by clustering the embeddings using AgglomerativeClustering

### Model Inputs
The model expects to inputs: 
1. Audio for speaker diarization
2. Number of speakers in the audio

### Model Output
the model generates a transcript file with speaker labels for each segment.

