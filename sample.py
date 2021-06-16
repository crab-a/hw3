class Sample:

    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label
        self.distance_row = {s_id: 0}

    def compute_euclidean_distance(self, other):
        """
        computes the distances between self and other sample
        :param other: the other sample
        :return: the distance between them in L2 form
        """
        temp_sum = 0
        for i in range(len(self.genes)):
            temp_sum += ((self.genes[i] - other.genes[i]) ** 2)
        return temp_sum ** 0.5

    def get_dist(self, other):
        return self.distance_row[other.s_id]
