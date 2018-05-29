"""Exceptions for Entrez integration."""


class BadParameter(ValueError):
    """Caller passed an unusable parameter."""


class ParseError(ValueError):
    """Could not parse XML response."""


class RequestFailed(ConnectionError):
    """Request to NCBI failed."""


class BadResponse(ValueError):
    """Response from NCBI was bad."""
