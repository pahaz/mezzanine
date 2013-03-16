"""
Default settings for the ``mezzanine.forms`` app. Each of these can be
overridden in your project's settings module, just like regular
Django settings. The ``editable`` argument for each controls whether
the setting is editable via Django's admin.

Thought should be given to how a setting is actually used before
making it editable, as it may be inappropriate - for example settings
that are only read during startup shouldn't be editable, since changing
them would require an application reload.
"""

from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting


register_setting(
    name="FORMS_DISABLE_SEND_FROM_EMAIL_FIELD",
    description=_("If ``True``, emails sent to extra recipients for form "
        "submissions won't be sent from an address taken from one of the "
        "form's email fields."),
    editable=False,
    default=False,
)

register_setting(
    name="FORMS_FIELD_MAX_LENGTH",
    description=_("Max length allowed for field values in the forms app."),
    editable=False,
    default=2000,
)

register_setting(
    name="FORMS_LABEL_MAX_LENGTH",
    description=_("Max length allowed for field labels in the forms app."),
    editable=False,
    default=200,
)

register_setting(
    name="FORMS_CSV_DELIMITER",
    description=_("Char to use as a field delimiter when exporting form "
        "responses as CSV."),
    editable=False,
    default=",",
)

register_setting(
    name="FORMS_UPLOAD_ROOT",
    description=_("Absolute path for storing file uploads for the forms app."),
    editable=False,
    default="",
)

register_setting(
    name="FORMS_EXTRA_FIELDS",
    description=_("Extra field types for the forms app. Should contain a "
        "sequence of three-item sequences, each containing the ID, dotted "
        "import path for the field class, and field name, for each custom "
        "field type. The ID is simply a numeric constant for the field, "
        "but cannot be a value already used, so choose a high number such "
        "as 100 or greater to avoid conflicts."),
    editable=False,
    default=(),
)

register_setting(
    name="FORMS_VISIBLE_USER_COLOMN",
    description=_("Display users column in admin view entries list"),
    editable=False,
    default=False
)