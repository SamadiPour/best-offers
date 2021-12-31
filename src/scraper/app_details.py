from dataclasses import dataclass


@dataclass
class IAP:
    name: str
    price: float

    def __lt__(self, other):
        return self.price < other.price


@dataclass
class AppDetails:
    """Class for keeping track of AppStore or GooglePlay details."""
    name: str
    developer: str
    price: float
    rate: float
    rate_count: int
    app_icon_url: str
    iap_list: list[IAP]

    def is_qualified(self):
        return self.price == 0 and self.rate > 3.5 and self.rate * self.rate_count > 200
