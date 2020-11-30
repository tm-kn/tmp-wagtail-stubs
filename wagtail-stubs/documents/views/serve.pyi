from typing import Any
from wagtail.core import hooks as hooks
from wagtail.core.forms import PasswordViewRestrictionForm as PasswordViewRestrictionForm
from wagtail.core.models import CollectionViewRestriction as CollectionViewRestriction
from wagtail.documents import get_document_model as get_document_model
from wagtail.documents.models import document_served as document_served
from wagtail.utils import sendfile_streaming_backend as sendfile_streaming_backend
from wagtail.utils.sendfile import sendfile as sendfile

def document_etag(request: Any, document_id: Any, document_filename: Any): ...
def serve(request: Any, document_id: Any, document_filename: Any): ...
def authenticate_with_password(request: Any, restriction_id: Any): ...
