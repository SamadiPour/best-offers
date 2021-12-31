from dataclasses import dataclass

from .app_details import AppDetails


@dataclass
class Item:
    """Class for keeping track of an scraped item."""
    url: str
    source_url: str
    source_name: str
    title: str
    details: AppDetails = None

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
