import numpy as np

class MatrixMixin:
    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(np.array2string(self.data))

    def __str__(self):
        return np.array2string(self.data)

    @property
    def shape(self):
        return self.data.shape

    @shape.setter
    def shape(self, new_shape):
        self.data = self.data.reshape(new_shape)
