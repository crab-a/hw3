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
        """
        this method receives two clusters and calculate the distance from each other according single link
        :param cluster: the first cluster
        :param other: the second cluster
        :return: the distance between the two closest points in different clusters (means the single link distance)
        """
        dist_list = []
        for this_sample in cluster.samples:
            for other_sample in other.samples:
                dist_list.append(this_sample.get_dist(other_sample))
        return min(dist_list)

    def name(self):
        """
        :return: string "single link"
        """
        return "single link"


class CompleteLink(Link):
    def compute(self, cluster, other):
        """
        this method receives two clusters and calculate the distance from each other according complete link
        :param cluster: the first cluster
        :param other: the second cluster
        :return: the longest distance between the two points in different clusters (means the complete link distance)
        """
        max_dist = 0
        for this_sample in cluster.samples:
            for other_sample in other.samples:
                if this_sample.get_dist(other_sample) > max_dist:
                    max_dist = this_sample.get_dist(other_sample)
        return max_dist

    def name(self):
        """
        :return: string "complete link"
        """
        return "complete link"
