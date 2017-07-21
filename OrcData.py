from urllib.request import urlopen

"""ord_data_collect module: contains the OrcData class. """

class OrcData:
    """OrcData Class"""
    url = "https://directory.orc.network/"

    def __init__(self):
        # Get the data
        orc_data = urlopen(self.url)

        # Convert bytes to string type
        self.orc_str = orc_data.read().decode('utf-8')

    @property
    def calc_num_nodes(self) -> int:
        search_string = 'capacity":'
        num_nodes = 0
        index = 0
        while (index != -1) or (len(self.orc_str) <= num_nodes):
            index = self.orc_str.find(search_string, index+1)
            num_nodes = num_nodes + 1
        return num_nodes

    @property
    def calc_data_vol(self) -> int:
        data_stored = 0
        start1 = 0
        start2 = 0
        alloc_storage = '0'
        avail_storage = '0'
        search_string1 = '"allocated":'
        search_string2 = ',"available":'
        alloc_offset = len(search_string1)
        search_string3 = '"available":'
        avail_offset = len(search_string3)
        search_string4 = '},"timestamp"'
        while self.orc_str.find(search_string1, start1) != -1:
            data_stored = data_stored + (int(alloc_storage) - int(avail_storage))
            """" retrieves the allocated storage value from the JSON string """
            start1 = self.orc_str.find(search_string1, start1) + alloc_offset
            end1 = self.orc_str.find(search_string2, start1)
            alloc_storage = self.orc_str[start1:end1]
            """ retrieves the available storage value from the JSON string """
            start2 = self.orc_str.find(search_string3, start2) + avail_offset
            end2 = self.orc_str.find(search_string4, start2)
            avail_storage = self.orc_str[start2:end2]
        return data_stored


"""Test"""
print('Number of Nodes: ', OrcData().calc_num_nodes)
print('Volume of Data Stored: ', OrcData().calc_data_vol)

