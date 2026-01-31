import whisper
import os

import path_finder

def detect_language_from_mp3(mp3_path: str) -> str:
    """
    Detect spoken language in an MP3 file using Whisper.

    Args:
        mp3_path (str): Path to MP3 file

    Returns:
        str: Detected language (e.g., 'en', 'es', 'fr')
    """

    # Load model (small is a good balance of speed/accuracy)
    model = whisper.load_model("small")

    # Load and preprocess audio
    audio = whisper.load_audio(mp3_path)
    audio = whisper.pad_or_trim(audio)

    # Convert to log-Mel spectrogram
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect language
    _, probs = model.detect_language(mel)

    # Get highest probability language
    detected_lang = max(probs, key=probs.get)

    return detected_lang

def analyze_pack(pack_path: str):
    tally = {}
    # go over all the items in waze_filename_paths.json and analyze the mp3 and detect language. print the results
    print(f"Analyzing voice pack at: {pack_path}...")
    for filename, waze_path in path_finder.filenames_and_paths.items():
        
        full_path = os.path.join(pack_path, waze_path)
        if os.path.exists(full_path):
            language = detect_language_from_mp3(full_path)
            #print(f"File: {waze_path}, Detected Language: {language}")
            # add to tally
            if language in tally:
                tally[language] += 1    
            else:
                tally[language] = 1
        else:
            print(f"File: {waze_path} does not exist in the provided pack path.")

    print("\nTally of detected languages:")
    print(tally)
    

if __name__ == "__main__":
    cwd = os.path.dirname(os.path.abspath(__file__))
    # look in the test_packs/Voice/ directory for a sample voice pack
    sample_pack_path = os.path.join(cwd, "test_packs", "Voice 2")
    analyze_pack(sample_pack_path)