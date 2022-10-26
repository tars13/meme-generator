"""Module that declares abstract base class giving interface."""

from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Abstract base class for actual Ingestor classes for different types of files.

    Each child class will actually ingest the files and return desired data.
    """

    supported_formats = {'csv', 'docx', 'pdf', 'txt'}

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine if a file path is an extension of one of the supported formats."""
        ext = path.split('.')[-1]
        return ext in cls.supported_formats

    @classmethod
    @abstractmethod
    def parse(cls, path: str):
        """Ingest the file in path and returns a list of QuoteModels of ingested Quotes."""
        pass
