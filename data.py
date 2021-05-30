import pandas


class Data:

    def __init__(self, path):
        """
        initial the new data object
        :param path: the path of the dictionary to work with
        """
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def get_all_districts(self):
        """
        this method return a list of the regions in the data object
        :return: list of the regions in the dataset
        """
        regions_set = set()
        for region in self.data["denominazione_region"]:
            regions_set.add(region)
        return list(regions_set)

    def set_districts_data(self, districts):
        """
        this method receives a list of districts and change the data object keeping only the values for
        the regions which are in that list
        :param districts: a list of regions
        :return: void
        """
        new_data = {}
        for key in self.data.keys():
            new_col = []
            data_entry = {}
            for index, value in enumerate(self.data[key]):
                if self.data['denominazione_region'][index] in districts:
                    new_col.append(value)
            data_entry[key] = new_col
            new_data.update(data_entry)
        self.data = new_data
