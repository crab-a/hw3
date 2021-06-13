class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link
        self.samples = samples
        self.clusters = []
# sgr
    def compute_silhoeutte(self):
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

    def compute_summery_silhoeutte(self):
        dict_for_point = self.compute_silhoeutte()
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
