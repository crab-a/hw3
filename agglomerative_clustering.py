class AgglomerativeClustering:

    def __init__(self, link, samples):
        self.link=link
        self.samples=samples

    def compute_rand_index(self):
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        for sample in samples:
            do