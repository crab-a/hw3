import abc


class Link:
    @abc.abstractmethod
    def compute(self, cluster, other):
        """this is abstract"""
        return

    @abc.abstractmethod
    def name(self):
        """this is abstract"""
        return


class SingleLink(Link):
    def compute(self, cluster, other):
        dist_list = []
        for this_sample in cluster.samples:
            for other_sample in other.samples:
                dist_list.append(this_sample.get_dist(other_sample))
        return min(dist_list)

    def name(self):
        return "single link"


class CompleteLink(Link):
    def compute(self, cluster, other):
        max_dist = 0
        for this_sample in cluster.samples:
            for other_sample in other.samples:
                if this_sample.get_dist(other_sample) > max_dist:
                    max_dist = this_sample.get_dist(other_sample)
        return max_dist

    def name(self):
        return "complete link"
