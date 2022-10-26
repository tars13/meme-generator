"""Concrete quote ingestor class for docx files."""

from xmlrpc.server import DocXMLRPCRequestHandler
from .IngestorInterface import IngestorInterface, QuoteModel
from docx import Document


class IngestorDOCX(IngestorInterface):
    """Helper module to read Docx file."""

    supported_formats = {'docx'}

    @classmethod
    def parse(cls, path: str):
        """Ingest the file in path and returns a list of QuoteModels of Ingested Quotes."""
        if not cls.can_ingest(path):
            raise Exception(f'unsupported file format: requires{cls.supported_formats}')
        quotes_docx = Document(path)
        quotes = []
        for par in quotes_docx.paragraphs:
            par_words = par.text.split(' - ')
            if len(par_words) == 2:
                quote = QuoteModel(par_words[0], par_words[1])
                quotes.append(quote)
        return quotes
