import abc
class Link:
    @abc.abstractmethod
    def compute(self, cluster, other):

class SingleLink(Link):
    def compute(self, cluster, other):
        dist_list = []
        for this_sample in range(cluster):
            for other_sample in range(other):
                dist_list.append(this_sample.get_dist(other_sample))
        return min(dist_list)

class CompleteLink(Link):
    def compute(self, cluster, other):
        max_dist =0
        for this_sample in range(cluster):
            for other_sample in range(other):
                if this_sample.get_dist(other_sample) > max_dist:
                    max_dist = this_sample.get_dist(other_sample)
        return max_dist