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
        self.distance_matrix = []

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
        for i in range(samples):
            for j in range(samples):
                if i < j:
                    continue
                elif i == j:
                    self.distance_matrix[i][j] = 0
                else:
                    self.distance_matrix[i][j] = compute_euclidean_distance(samples.genes[i], samples.genes[j])
                    self.distance_matrix[j][i] = self.distance_matrix[i][j]

        """
        make distance matrix here, save it in self.distance_matrix
        """

    def fix_create_distance_matrix(self, samples):  # i dunno
        length = len(samples)
        self.distance_matrix = [[0]*length]*length
        for i in range(length):
            for j in range(length):
                if i < j:
                    continue
                self.distance_matrix[i][j] = samples[i].compute_euclidean_distance(samples[j])
                self.distance_matrix[j][i] = self.distance_matrix[i][j]
