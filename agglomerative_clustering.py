import cluster as c
from collections import OrderedDict


class AgglomerativeClustering:

    def __init__(self, link, samples):
        self.link = link
        self.samples = samples
        self.clusters = [c.Cluster(sample.s_id, [sample]) for c_id, sample in enumerate(self.samples)]
        self.dict_clusters = OrderedDict()
        for cluster in self.clusters:
            self.dict_clusters[cluster.id] = cluster

    def run(self, max_clusters):
        """
        merges the clusters until having only max_clusters clusters
        :param max_clusters: the num of clusters to have in the end of the run method
        :return: print results
        """
        length = len(self.clusters)
        while length > max_clusters:
            for i, current_cluster in enumerate(self.dict_clusters.values()):
                for j, other_cluster in enumerate(self.dict_clusters.values()):
                    if i >= j:
                        continue
                    if i == 0 and j == 1:
                        best_cluster1 = current_cluster
                        best_cluster2 = other_cluster
                        min_dist = self.link.compute(current_cluster, other_cluster)
                    else:
                        temp_dist = self.link.compute(current_cluster, other_cluster)
                        if temp_dist < min_dist:
                            min_dist = temp_dist
                            best_cluster1 = current_cluster
                            best_cluster2 = other_cluster
            best_cluster1.merge(self.dict_clusters[best_cluster2.id])
            self.dict_clusters.pop(best_cluster2.id)
            length -= 1
        self.clusters = []
        for cluster in self.dict_clusters.values():
            self.clusters.append(cluster)
        silhouette_dict = self.compute_summery_silhouette()
        print(f'{self.link.name()}:')
        for c in self.clusters:
            c.print_details(silhouette_dict[c.id])
        print(f"Whole data: silhouette = {round(silhouette_dict[0], 3)}, RI = {round(self.compute_rand_index(), 3)}")

    def compute_silhouette(self):
        dict = {}
        for cluster in self.clusters:
            for sample in cluster.samples:
                min_dist_to_cluster_list = []
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
        """compute rand index as was described in the task description"""
        TP = 0
        TN = 0
        FP = 0
        FN = 0

        for i, sample1 in enumerate(self.samples):
            for j, sample2 in enumerate(self.samples):
                if i <= j:
                    continue
                if sample1.label == sample2.label:
                    FP += 1
                    for current_cluster in self.clusters:
                        if sample1 in current_cluster.samples and sample2 in current_cluster.samples:
                            TP += 1
                            FP -= 1
                            break
                else:
                    TN += 1
                    for current_cluster in self.clusters:
                        if sample1 in current_cluster.samples and sample2 in current_cluster.samples:
                            FN += 1
                            TN -= 1
                            break
        true = TP + TN
        return true / (TP + TN + FP + FN)
