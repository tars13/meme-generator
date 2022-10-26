"""Define the class for a quote model."""


class QuoteModel:
    """Represent models for quote."""

    def __init__(self, body: str, author: str) -> None:
        """Create a new 'QuoteModel'.

        :param body: content of quote in text
        :param author: auther of quote in text
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return string representation of quote."""
        return f"<{self.body}, {self.author}>"
