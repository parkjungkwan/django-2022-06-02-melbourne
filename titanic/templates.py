from context.domains import Dataset
from context.models import Model


class TitanicTemplate(object):
    def __init__(self):
        self.dataset = Dataset()
        self.model = Model()
        
