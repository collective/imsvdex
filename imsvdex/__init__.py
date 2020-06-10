import sys


def safe_text(value, encoding="utf-8"):
    """Converts a value to text, even it is already a text string.
    Copied from Products.CMFPlone.utils.safe_text

        >>> from imsvdex import safe_text
        >>> test_bytes = u'\u01b5'.encode('utf-8')
        >>> safe_text('spam') == u'spam'
        True
        >>> safe_text(b'spam') == u'spam'
        True
        >>> safe_text(u'spam') == u'spam'
        True
        >>> safe_text(u'spam'.encode('utf-8')) == u'spam'
        True
        >>> safe_text(test_bytes) == u'\u01b5'
        True
        >>> safe_text(u'\xc6\xb5'.encode('iso-8859-1')) == u'\u01b5'
        True
        >>> safe_text(test_bytes, encoding='ascii') == u'\u01b5'
        True
        >>> safe_text(1) == 1
        True
        >>> print(safe_text(None))
        None
    """

    if sys.version_info < (3,):
        if isinstance(value, unicode):
            return value
        elif isinstance(value, basestring):
            try:
                value = unicode(value, encoding)
            except (UnicodeDecodeError):
                value = value.decode("utf-8", "replace")
        return value

    if isinstance(value, str):
        return value
    elif isinstance(value, bytes):
        try:
            value = str(value, encoding)
        except (UnicodeDecodeError):
            value = value.decode("utf-8", "replace")
    return value
