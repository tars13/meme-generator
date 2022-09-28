"""Concrete quote ingestor class for csv files."""

from .IngestorInterface import IngestorInterface, QuoteModel
import pandas as pd

class IngestorCSV(IngestorInterface):
    """The csv file have a header and be of 2 columns, first column labelled
    'body' and second column labelled 'author'.
    """

    supported_formats = {"csv"}

    @classmethod
    def parse(cls, path: str):
        """Parse CSV file and list of quote models."""
        if not cls.can_ingest(path):
            raise Exception(f'unsupported file format: requires{cls.supported_formats}')
        quotes = []
        df = pd.read_csv(path, header=0)
        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)
        return quotes