import spacy

def assign_speaker_name(dialogue):
    # Load the Spacy model
    nlp = spacy.load('en_core_web_sm')

    # Split into lines
    lines = dialogue.strip().split("\n")

    # Initialize speaker names dictionary
    speaker_dict = {}

    for i in range(0, len(lines), 2):
        speaker_line = lines[i]
        dialogue_line = lines[i+1]

        # Get speaker number from the speaker line
        speaker_number = speaker_line.split()[1]

        # Perform NER on the dialogue line
        doc = nlp(dialogue_line)
        names = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']

        # If there are names in the dialogue line, use the last one as the speaker's name
        if names:
            speaker_dict[speaker_number] = names[-1]

        # Get speaker's name from the dictionary, or use the speaker number if the name is not known
        speaker_name = speaker_dict.get(speaker_number, f"SPEAKER {speaker_number}")

        # Print the dialogue line with the speaker's name
        print(f"{speaker_name} {speaker_number} {speaker_line.split()[2]}")
        print(dialogue_line)


def transcript_to_dictionary(dialogue):
    # Split the output into lines
    lines = dialogue.splitlines()

    # Initialize the dictionary
    dictionary = {}

    # Iterate through the lines and construct the dictionary
    for i in range(0, len(lines), 2):
        name_line = lines[i]
        text_line = lines[i + 1]

        # Extract name and text
        name = name_line.split()[0]
        text = text_line

        # Add to the dictionary
        dictionary[name] = text

    return dictionary