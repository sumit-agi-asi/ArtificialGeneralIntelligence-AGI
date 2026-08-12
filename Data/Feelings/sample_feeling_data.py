import random
def load_sample_feeling_data(n: int):
    for _ in range(n):
        ## Sound can only
        neurot1 = [random.normalvariate(1.0, 100.0) for _ in range(n)]  
        neurot2 = [random.normalvariate(1.0, 100.0) for _ in range(n)] 
        neurot3 = [random.normalvariate(1.0, 100.0) for _ in range(n)] 
        sample_feeling = [(n1,n2,n3) for n1,n2,n3 in zip(neurot1, neurot2, neurot3)]
    return sample_feeling

if __name__ == "__main__":
    n = 1000  # Number of sample feeling data points to generate
    sample_feeling_data = load_sample_feeling_data(n)
    with open("feeling_data_sample.txt", "w") as f:
        f.write(str(sample_feeling_data))