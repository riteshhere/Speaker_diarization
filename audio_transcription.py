from speaker_diarization import SpeakerDiarizer
from find_names import assign_speaker_name, transcript_to_dictionary

print("Initializing SpeakerDiarizer...")
diarizer = SpeakerDiarizer(num_speakers=2)

print("Running diarization...")
transcript = diarizer.diarize('audio_files\Meeting1.mp3')

print("Finished diarization. Transcript:")
print(transcript)

print("Assigning Names:")
fin_transcript = assign_speaker_name(transcript)
print(fin_transcript)

transcript_dictionary = transcript_to_dictionary(fin_transcript)
