def output_to_dictionary(output):
    # Split the output into lines
    lines = output.splitlines()

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

# Example usage:
output = """Ritesh 1 0:00:00
Hi, I am Ritesh. I have completed speech diarization module. I am working on name assignation module and it will take me 5 days to complete it. I have faced some challenges to integrate Python code.
Krishna 2 0:00:12
Hi, I am Krishna. I have completed the model evaluation module. I will be working on the presentation now."""

result = output_to_dictionary(output)
print(result)
