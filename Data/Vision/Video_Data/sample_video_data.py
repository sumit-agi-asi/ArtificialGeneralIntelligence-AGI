import random
def load_sample_video_data(n: int, fps: int, time: int):
    for _ in range(n, fps, time):
        
        sample_video = [[[[(round(ch1,0), round(ch2,0), round(ch3,0)) for ch1, ch2, ch3 in zip([[random.randint(0, 255) for _ in range(n)]  for _ in range(n)]
                                                                                            , [[random.randint(0, 255) for _ in range(n)]  for _ in range(n)], [[random.randint(0, 255) for _ in range(n)]  for _ in range(n)])] for _ in range(n)] for _ in range(fps)] for _ in range(time)]
    return sample_video

if __name__ == "__main__":
    n = 100
    fps = 30
    time = 50
    sample_video_data = load_sample_video_data(n, fps, time)
    with open("video_data_sample.txt", "w") as f:
        f.write(str(sample_video_data))