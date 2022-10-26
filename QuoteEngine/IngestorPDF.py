"""Concrete quote ingestor class for pdf files."""

import subprocess
import random
import os
from .IngestorInterface import IngestorInterface, QuoteModel
from .IngestorTXT import IngestorTXT


class IngestorPDF(IngestorInterface):
    """Helper module to read PDF file.

    Use a subprocess to call pdftotext to convert the pdf to a random temp
    text file. Then call the pre-written IngestorTXT to ingest the resulting
    txt file.
    """

    supported_formats = {"pdf"}

    @classmethod
    def parse(cls, path: str):
        """Ingest the file in path and returns a list of QuoteModels of ingested Quotes."""
        if not cls.can_ingest(path):
            raise Exception(f"unsupported file format: requires{cls.supported_formats}")

        tmp = f"{random.randint(0,1000000)}.txt"
        subprocess.run(['pdftotext', path, tmp], shell=True, check=True)

        quotes = IngestorTXT.parse(tmp)

        os.remove(tmp)
        return quotes
