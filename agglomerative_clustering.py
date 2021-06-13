import cluster


class AgglomerativeClustering:

    def __init__(self, link, samples):
        self.link = link
        self.samples = samples
        self.clusters = [cluster.Cluster(c_id, sample) for c_id, sample in enumerate(self.samples)]

    def compute_rand_index(self):
        TP = 0
        TN = 0
        FP = 0
        FN = 0

        for i, sample1 in enumerate(self.samples):
            for j, sample2 in enumerate(self.samples):
                if i > j:
                    if sample1.label == sample2.label:
                        FP += 1
                        for current_cluster in self.clusters:
                            if sample1 in current_cluster.samples & sample2 in current_cluster.samples:
                                TP += 1
                                FP -= 1
                                break
                    else:
                        TN += 1
                        for current_cluster in self.clusters:
                            if sample1 in current_cluster.samples & sample2 in current_cluster.samples:
                                FN += 1
                                TN -= 1
                                break
        true = TP + TN
        return true / sum([TP, TN, FP, FN])
