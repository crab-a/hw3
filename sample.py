class Sample:

    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label
        self.distance_row = {s_id: 0}

    def compute_euclidean_distance(self, other):
        """
        computes the distances between self and the other sample
        :param other: the other sample
        :return: the distance between them in L2 form
        """
        temp_sum = 0
        for i in range(len(self.genes)):
            temp_sum += ((self.genes[i] - other.genes[i]) ** 2)
        return temp_sum ** 0.5

    def get_dist(self, other):
        return self.distance_row[other.s_id]


def create_distance_matrix(samples):
    """
    for every sample in the list calculate the distance to any other sample and save all distances in a dict with the
    s_id as key
    :param samples: list of samples
    :return: None
    """
    for this_sample in samples:
        for other_sample in samples:
            if this_sample.s_id <= other_sample.s_id:
                continue
            this_sample.distance_row[other_sample.s_id] = this_sample.compute_euclidean_distance(other_sample)
            other_sample.distance_row[this_sample.s_id] = this_sample.distance_row[other_sample.s_id]
