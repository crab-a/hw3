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
        for index, sample_id in enumerate(self.data["samples"]):
            s_id = self.data["s_id"][index]
            genes = self.data["genes"][index]
            label = self.data["type"][index]
            new_sample = sample(s_id, genes, label)



    def create_distance_matrix(self, samples):
        self.distance_matrix[len(samples)][len(samples)] = 0
        """
        make distance matrix here, save it in self.distance_matrix
        """
