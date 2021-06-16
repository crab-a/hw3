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
        create a list of all samples in data.
        :return list of samples
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
