from typing import Any, Optional
from wagtail.admin.rich_text.editors.draftail import DraftailRichTextArea as DraftailRichTextArea
from wagtail.admin.rich_text.editors.hallo import HalloFormatPlugin as HalloFormatPlugin, HalloHeadingPlugin as HalloHeadingPlugin, HalloListPlugin as HalloListPlugin, HalloPlugin as HalloPlugin, HalloRichTextArea as HalloRichTextArea

DEFAULT_RICH_TEXT_EDITORS: Any

def get_rich_text_editor_widget(name: str = ..., features: Optional[Any] = ...): ...
