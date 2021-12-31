from dataclasses import dataclass

from app_details import AppDetails


@dataclass
class Item:
    """Class for keeping track of an scraped item."""
    url: str
    source_url: str
    source_name: str
    title: str
    details: AppDetails

    def get_details(self) -> None:
        if self.is_app_store():
            # ask apple class for details
            # self.app_details = AppleAppDetails(self.url).get()
            pass
        elif self.is_google_play():
            # ask google class for details
            # self.app_details = GoogleAppDetails(self.url).get()
            pass

    def is_google_play(self) -> bool:
        return self.url is str and 'play.google.com' in self.url

    def is_app_store(self) -> bool:
        return self.url is str and 'apps.apple.com' in self.url

    # todo: complete this method
    def to_message(self) -> str:
        if self.is_google_play():
            return f'{self.title} ({self.url})'
        if self.is_app_store():
            return f'{self.title} ({self.url})'
        else:
            return f'*[{self.title}]({self.url})*\n' \
                   f'' \
                   f'' \
                   f'\n\n' \
                   f'Source: [{self.source_name}]({self.source_url})'
