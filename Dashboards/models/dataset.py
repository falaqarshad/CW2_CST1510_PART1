class Dataset:
    def __init__(self, dataset_id, name, size_mb, rows, source):
        self._id = dataset_id
        self._name = name
        self._size_mb = size_mb
        self._rows = rows
        self._source = source

    def get_source(self):
        return self._source

    def get_size(self):
        return self._size_mb

    def get_rows(self):
        return self._rows

    def __str__(self):
        return f"{self._name} ({self._size_mb} MB, {self._rows} rows, source={self._source})"
        