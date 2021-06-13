class Sample:

    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label
        self.distance_row = [0]

    def compute_euclidean_distance(self, other):
        temp_sum = 0
        for i in range(len(self.genes)):
            temp_sum += ((self.genes[i] - other.genes[i]) ** 2)
        return temp_sum ** 0.5

    def get_dist(self, other):
        return self.distance_row[other.s_id - 1]
