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
        samples_ids = []
        for sample in self.samples:
            samples_ids.append(sample.s_id)

        print(f"Cluster {self.id}: ", end="")
        print(samples_ids, sep=', ', end=", ")
        print(f'dominant label = {self.get_dominant()}, silhouette = {round(silhouette, 3)}')

    def get_dominant(self):
        labels_dict = {}
        dominant = ""
        for sample in self.samples:
            if sample.label in labels_dict:
                labels_dict[sample.label] += 1
            else:
                labels_dict[sample.label] = 1
        maximum = 0
        for label, value in labels_dict.items():
            if value > maximum:
                maximum = value
                dominant = label
            elif value == maximum:
                if label > dominant:
                    dominant = label
        return dominant
