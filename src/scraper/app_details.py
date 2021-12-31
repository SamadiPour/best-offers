from dataclasses import dataclass


@dataclass
class IAP:
    name: str
    price: float


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
        return self.rate * self.rate_count > 200 and self.price == 0
