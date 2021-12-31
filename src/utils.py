import re


def extract_urls(text) -> list[str]:
    """
    Extracts URLs from a string.
    """
    urls = re.findall(r'\b(?:https?://)?(?:(?i:[a-z]+\.)+)[^\s,]+\b', text, flags=re.IGNORECASE)
    return urls


def format_markdown_v2(text) -> str:
    """
    Formats a string to be used in Markdown v2.
    https://core.telegram.org/bots/api#markdownv2-style

    In all other places characters
    '_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!'
    must be escaped with the preceding character '\'.
    """
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!])', r'\\\1', text)
