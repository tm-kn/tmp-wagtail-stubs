from typing import Any
from wagtail.contrib.search_promotions.models import SearchPromotion as SearchPromotion
from wagtail.search.models import Query as Query

register: Any

def get_search_promotions(search_query: Any): ...
