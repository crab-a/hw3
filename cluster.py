class Cluster:
    def __init__(self, c_id, samples):
        self.id = c_id
        self.samples = samples

    def merge(self, other):
        self.samples.extend(other.samples)
        self.samples = sorted(self.samples, key=lambda sample: self.samples[sample].s_id)
        del other

    def print_details(self, silhouette):
        def print_samples_ids(samples):
            for sample in samples:
                print(sample.s_id, sep=", ", end="")
        print(f"Cluster {self.id}: [{print_samples_ids(self.samples)}] dominant label = {somthing}, silhouette = {silhouette}")  # need to find dominant label



