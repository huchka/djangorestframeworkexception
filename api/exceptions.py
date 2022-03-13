import logging

from rest_framework.exceptions import ValidationError

# logging
logger = logging.getLogger(__file__)


class CustomValidationError(ValidationError):
    def __init__(self, detail=None, code=None):
        logger.error(f"{detail=}")
        self.detail = [{"error_field_name": k, "error_validation_message": v} for k, v in detail.items()]
