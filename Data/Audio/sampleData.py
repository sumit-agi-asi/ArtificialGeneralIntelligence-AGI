import random
def load_sample_audio_data(n: int):
    for _ in range(n):
        ## Sound can only
        pitch = [random.normalvariate(10.0, 500.0) for _ in range(n)]  
        frequency = [random.uniform(-1.0, 1.0) for _ in range(n)]  
        sample_audio = [(p, f) for p, f in zip(pitch, frequency)]
    return sample_audio

if __name__ == "__main__":
    n = 10  # Number of sample audio data points to generate
    sample_audio_data = load_sample_audio_data(n)
    with open("audio_data_sample.txt", "w") as f:
        f.write(str(sample_audio_data))