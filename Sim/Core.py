import numpy as np

class SNNCore:
    '''Simulate a core for TrueNorth style SNN ( Leaky Integrate and Fire Commands )'''

    def __init__(self, numNeurons, numAxons):
        self.numNeurons = numNeurons
        self.numAxons = numAxons

        # Configuration for Inference
        self.s = np.empty ((numAxons, numNeurons), dtype = np.int_ ) # Synapse Values (=0 for no connection)
        self.leak = np.empty ((numNeurons), dtype = np.int_)         # leak Values
        self.threshold = np.empty ((numNeurons), dtype = np.int_)    # Threshold Values       
        self.potential = np.empty ((numNeurons), dtype = np.int_)    # Current Potential Values

        # Configuration for Learning


    def updateParamsInfer(self):
        ''' Updates the Learned Params to Inference Params'''
        None

    def step(self, act):
        ''' Applies activation to update neuron potentials  and return spike bitvector'''
        self.potential += self.leak + np.dot(act,self.s) 
        spikesGen = (self.poential > self.threshold) # Gen Spikes
        self.potential [spikesGen] = 0.0             # Reset spike generating neurons
        self.potential [self.potential < 0.0] = 0.0  # Reset neurons with neg Potential
        return spikesGen

