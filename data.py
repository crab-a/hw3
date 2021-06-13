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



    def create_distance_matrix(self, samples):
        length = len(samples)
        self.distance_matrix = [[0]*length]*length
        for i in range(length):
            for j in range(length):
                if i <= j:
                    continue
                self.distance_matrix[i][j] = samples[i].compute_euclidean_distance(samples[j])
                self.distance_matrix[j][i] = self.distance_matrix[i][j]
        for i, samp in enumerate(samples):
            samp.distance_row = self.distance_matrix[i]

