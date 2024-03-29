from django import forms
from typing import Any
from wagtail.admin.widgets import AdminPageChooser as AdminPageChooser
from wagtail.contrib.search_promotions.models import SearchPromotion as SearchPromotion
from wagtail.search.models import Query as Query

class SearchPromotionForm(forms.ModelForm):
    sort_order: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

SearchPromotionsFormSetBase: Any

class SearchPromotionsFormSet(SearchPromotionsFormSetBase):
    minimum_forms: int = ...
    minimum_forms_message: Any = ...
    def add_fields(self, form: Any, *args: Any, **kwargs: Any) -> None: ...
    def clean(self) -> None: ...
