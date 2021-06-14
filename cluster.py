class Cluster:
    def __init__(self, c_id, samples):
        self.id = c_id
        self.samples = samples

    def merge(self, other):
        self.id = self.id if self.id <= other.id else other.id
        self.samples.extend(other.samples)
        self.samples.sort(key=lambda sample: sample.s_id)
        del other

    def print_details(self, silhouette):
        def print_samples_ids(samples):
            for sample in samples:
                print(sample.s_id, sep=", ", end="")

        print(
            f"Cluster {self.id}: [{print_samples_ids(self.samples)}] dominant label = {self.get_dominant()}, silhouette = {silhouette}")  # need to find dominant label

    def get_dominant(self):
        labels_dict = {}

        for sample in self.samples:
            if sample in labels_dict:
                labels_dict[sample.label] += 1
            else:
                labels_dict[sample.label] = 0
        return max(labels_dict)
