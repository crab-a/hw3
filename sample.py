class Sample:

    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label

    def compute_euclidean_distance(self, other):
        temp_sum = 0
        for i in range(len(self.genes)):
            temp_sum += ((self.genes[i] - other.genes[i])**2)
        return temp_sum**0.5

    def get_dist_to_other(self,other):
        self.dist_row[other.s_id-1]