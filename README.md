# Speech_diarization
ipynb file will be present in research_files folder
The model requires GPU to generate output, please install CUDA and pytorch version compatible with your system

### What is speaker diarization
Speaker diarization, also known as diarization, involves segregating an audio stream with human speech into consistent segments based on the individual identity of each speaker.

### How to perform Speaker diarization?
1. Convert Audio to Text using Whisper
2. Segregate the text by clustering the embeddings using AgglomerativeClustering
3. Perform NER to recognize names of participants

### Model Inputs
The model expects to inputs: 
1. Audio for speaker diarization
2. Number of speakers in the audio

### Model Output
1. Model will generate a complete transcript of the audio
2. Dictionary of diarization with participant's name.

