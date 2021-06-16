import pandas
import sample


class Data:
    def __init__(self, path):
        """
        initial the new data object
        :param path: the path of the dictionary to work with
        """
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        """
        make list of all samples in the data
        """
        samples = []
        genes_names = [key for key in self.data]
        genes_names = genes_names[2:]

        for index, sample_id in enumerate(self.data["samples"]):
            s_id = self.data["samples"][index]
            label = self.data["type"][index]
            genes = []
            for gene in genes_names:
                genes.append(self.data[gene][index])
            new_sample = sample.Sample(s_id, genes, label)
            samples.append(new_sample)

        return samples


def create_distance_matrix(samples):
    """
    for any sample calculate the distance to any other sample and save that as a list in the sample data members.
    calculate the distance between any two samples and save that in a 2D matrix.
    so that [origin_sample.id][destination_sample.id] = distance
    :param samples: list of samples
    :return: None
    """
    for this_sample in samples:
        for other_sample in samples:
            if this_sample.s_id <= other_sample.s_id:
                continue
            this_sample.distance_row[other_sample.s_id] = this_sample.compute_euclidean_distance(other_sample)
            other_sample.distance_row[this_sample.s_id] = this_sample.distance_row[other_sample.s_id]
