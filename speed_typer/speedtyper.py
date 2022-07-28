# Download the sentences, and save to a file on the disk
def download_sentences():
    import os
    if not os.path.exists("sentences.txt"):
        import requests
        url = "https://python.techtalents.cloud/sentences"
        print("Downloading sentences....")
        downloaded = requests.get(url).text
        print("Finished downloading.")
        file = open("sentences.txt", "wt", newline="\n")
        file.write(downloaded)
        file.close()


# Read the file into a variable
def read_sentences():
    global sentences
    file = open("sentences.txt", "rt")
    contents = file.read()
    file.close()

    # Process the sentences (ie. break them up into smaller pieces)
    sentences = contents.splitlines()
    print("Read", len(sentences), "sentences.")


def pick_sentence():
    global sentence
    # Pick one sentence randomly
    import random

    while True:
        sentence = random.choice(sentences)
        if 60 < len(sentence) < 100:
            break
    print(sentence)


# Allow the user to type their attempt, measure time taken
def calculate_stuff():
    global cpm, accuracy
    import time
    start = time.time()
    attempt = input()
    end = time.time()
    time_taken = round(end - start, 2)
    # Characters per minute
    cpm = round(len(attempt) / time_taken * 60, 1)

    print("Took", time_taken, "seconds")
    print("Characters per minute:", cpm)

    # Calcuate an accuracy
    import rapidfuzz.distance.Levenshtein_py
    accuracy = rapidfuzz.distance.Levenshtein_py.normalized_similarity(sentence, attempt)
    accuracy = str(round(accuracy * 100, 1)) + "%"
    print("Accuracy:", accuracy)


def split_sentence(maximum_length):
    # Find the closest space to length that fits
    wrap = sentence.rindex(" ", 0, maximum_length)
    # Select the part of the string from the start until the space
    # Select the part of the string from the space until the end

    lines = [sentence[0 : wrap], sentence[wrap + 1: len(sentence)]]
    return lines
