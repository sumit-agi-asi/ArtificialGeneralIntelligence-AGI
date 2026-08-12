import random
def load_sample_thinking_data(n: int, t: int):
    for _ in range(n, t):
        '''
        It generates the (r, theta, phi, insentity [of synapse]) for n time step.
        It assumes brain to be a spherical ball of unit radius.
        Thought is collective synapses of brain's all neurons.
        Its affect is felt throughout the spherical positions of brain.
        It is represneted by the intensity at few points in the spherical coordinates of brain.
        r is the distance from the center of brain to the point in the brain. 
        theta is the angle from the z-axis to the point in the brain.
        phi is the angle from the x-axis to the point in the brain.
        '''
        
        r = [[random.normalvariate(0, 1.0) for _ in range(n)]  for _ in range(t)]
        theta = [[random.normalvariate(0.0, 360.0) for _ in range(n)]  for _ in range(t)]
        phi = [[random.normalvariate(0.0, 180.0) for _ in range(n)]  for _ in range(t)]
        intensity = [[random.normalvariate(0.0, 100.0) for _ in range(n)]  for _ in range(t)]
        
        
        sample_thinking = [(p, t1, p1, i1) for p, t1, p1, i1 in zip(r, theta, phi, intensity)]
    return sample_thinking

if __name__ == "__main__":
    n = 100  
    t = 5 
    sample_thinking_data = load_sample_thinking_data(n, t)
    with open("thinking_data_sample.txt", "w") as f:
        f.write(str(sample_thinking_data))