import random
def load_sample_image_data(n: int, frames: int):
    for _ in range(n, frames):
        
        sample_images = [[[(round(ch1,0), round(ch2,0), round(ch3,0)) for ch1, ch2, ch3 in zip([[random.randint(0, 255) for _ in range(n)]  for _ in range(n)]
                                                                                            , [[random.randint(0, 255) for _ in range(n)]  for _ in range(n)], [[random.randint(0, 255) for _ in range(n)]  for _ in range(n)])] for _ in range(n)] for _ in range(frames)]
    return sample_images

if __name__ == "__main__":
    n = 100
    frames = 100
    sample_image_data = load_sample_image_data(n, frames)
    with open("image_data_sample.txt", "w") as f:
        f.write(str(sample_image_data))