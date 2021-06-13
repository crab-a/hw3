import cluster


class AgglomerativeClustering:

    def __init__(self, link, samples):
        self.link = link
        self.samples = samples
        self.clusters = [cluster.Cluster(c_id, sample) for c_id, sample in enumerate(self.samples)]

    def compute_silhouette(self):
        dict = {}
        min_dist_to_cluster_list = []
        for cluster in self.clusters:
            for sample in cluster.samples:
                if len(cluster.samples) == 1:
                    dict[sample.s_id] = 0
                else:
                    in_cluster = 0
                    for other in cluster.samples:
                        in_cluster += sample.get_dist(other)
                    in_cluster = in_cluster / (len(cluster.samples) - 1)
                    for other_cluster in self.clusters:
                        if cluster == other_cluster:
                            continue
                        out = 0
                        for other in other_cluster.samples:
                            out += (sample.get_dist(other))
                        min_dist_to_cluster_list.append(out / len(other_cluster.samples))
                    out_cluster = min(min_dist_to_cluster_list)
                    dict[sample.s_id] = (out_cluster - in_cluster) / max(out_cluster, in_cluster)
        return dict

    def compute_summery_silhouette(self):
        dict_for_point = self.compute_silhouette()
        silhoeutte_dict = {}
        silhoeutte_all = 0
        for cluster in self.clusters:
            cluster_rate = 0
            for sample in cluster.samples:
                cluster_rate += dict_for_point[sample.s_id]
            silhoeutte_dict[cluster.id] = cluster_rate / len(cluster.samples)
        for sample in self.samples:
            silhoeutte_all += dict_for_point[sample.s_id]
        silhoeutte_dict[0] = silhoeutte_all / len(self.samples)
        return silhoeutte_dict

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

    def run(self, max_clusters):
        pass
