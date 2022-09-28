"""Module that encapsulate modules for ingest different types of files."""

from .IngestorInterface import IngestorInterface
from .IngestorTXT import IngestorTXT
from .IngestorDOCX import IngestorDOCX
from .IngestorCSV import IngestorCSV
from .IngestorPDF import IngestorPDF

class Ingestor(IngestorInterface):
    """Class encapsulating each file type."""

    ingestors = {IngestorCSV, IngestorDOCX, IngestorPDF, IngestorTXT}

    @classmethod
    def parse(cls, path):
        """Parse files by appropriate ingestor."""
        for ing in cls.ingestors:
            if ing.can_ingest(path):
                return ing.parse(path)