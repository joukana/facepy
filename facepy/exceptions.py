class FacepyError(Exception):
    """Base class for exceptions raised by Facepy."""
    pass

class APIError(FacepyError): pass