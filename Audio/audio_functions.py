from Models.model import queryModel, audioModel
import math

def audio_retrieval(query: audioModel, audio_data: list[tuple[float, float]], mapping: dict[str:list[list[float, float]]]):
    """
    Retrieves audio data from the query.
    
    Args:
        query (audioModel): The audio model containing the audio data.
    """
    
    audio_data = normalize_audio_data(audio_data)
    query_data = normalize_audio_data(query)
    
    matched_audio = semantic_search_audio(query_data, audio_data)
    
    matched_phonemes = map_to_phonemes(matched_audio, mapping)
    
    return matched_phonemes

def semantic_search_audio(query_data, audio_data):
    
    lenth = len(query_data)
    
    for i in range(len(audio_data) - lenth + 1):
        segment = audio_data[i:i + lenth]
        distance = sum(distance_metric(q, s) for q, s in zip(query_data, segment))
        
        if distance < 0.2:  # Threshold for matching
            return segment

    
def distance_metric(audio1, audio2):
    pitch1, frequency1 = audio1
    pitch2, frequency2 = audio2
    return math.hypot(pitch1 - pitch2, frequency1 - frequency2)

def normalize_audio_data(audio_data: list[tuple[float, float]]):
    
    for audio in audio_data:
        pitch, frequency = audio
        normalized_pitch = (pitch - min(pitch)) / (max(pitch) - min(pitch))
        normalized_frequency = (frequency - min(frequency)) / (max(frequency) - min(frequency))
        yield (normalized_pitch, normalized_frequency)    

def convert_to_phonemes(audio_data):
    """
    Converts audio data to phonemes.
    
    Args:
        audio_data (list[tuple[float, float]]): The audio data to convert.
        
    Returns:
        list[str]: The converted phonemes.
    """

    phonemes = []
    for pitch, frequency in audio_data:
        # Placeholder logic for converting pitch and frequency to phonemes
        phoneme = f"Phoneme({round(pitch, 2)}, {round(frequency, 2)})"
        phonemes.append(phoneme)
    return phonemes

def map_to_phonemes(lst: list[list[list[float, float]]], mapping: dict[str:list[list[float, float]]]) -> str:
    """
    Maps phonemes to their corresponding representations.
    
    Args:
        phonemes (list[str]): The list of phonemes to map.
        
    Returns:
        list[str]: The mapped phoneme representations.
    """
    
    mapped_phonemes = []
    broken_list = [lst[i:i + 3] for i in range(0, len(lst), 3)]
    
    for lst1 in broken_list:
        for key, val in mapping.items():
            if lst1 == val:
                mapped_phonemes.append(key)
                break
    return mapped_phonemes