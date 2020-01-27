# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OMPManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(setting_name=kwargs.get("setting_name")).filter(
            locale=kwargs.get("locale"))


class AccessKeys(models.Model):
    access_key_id = models.BigIntegerField(primary_key=True)
    context = models.CharField(max_length=40)
    key_hash = models.CharField(max_length=40)
    user_id = models.BigIntegerField()
    assoc_id = models.BigIntegerField(blank=True, null=True)
    expiry_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'access_keys'


class AnnouncementSettings(models.Model):
    announcement_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'announcement_settings'
        unique_together = (('announcement_id', 'locale', 'setting_name'),)


class AnnouncementTypeSettings(models.Model):
    type_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'announcement_type_settings'
        unique_together = (('type_id', 'locale', 'setting_name'),)


class AnnouncementTypes(models.Model):
    type_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.SmallIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'announcement_types'


class Announcements(models.Model):
    announcement_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.SmallIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField()
    type_id = models.BigIntegerField(blank=True, null=True)
    date_expire = models.DateTimeField(blank=True, null=True)
    date_posted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'announcements'


class AuthSources(models.Model):
    auth_id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    plugin = models.CharField(max_length=32)
    auth_default = models.IntegerField()
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_sources'

class AuthorSettings(models.Model):
    author_id = models.BigIntegerField(primary_key=True)
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'author_settings'
        unique_together = (('author_id', 'locale', 'setting_name'),)


class Authors(models.Model):
    author_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    primary_contact = models.IntegerField()
    seq = models.FloatField()
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=90)
    suffix = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=90, blank=True, null=True)
    email = models.CharField(max_length=90)
    url = models.CharField(max_length=2047, blank=True, null=True)
    user_group_id = models.BigIntegerField(blank=True, null=True)
    include_in_browse = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'authors'


class CataloguingMetadataFieldSettings(models.Model):
    field_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'cataloguing_metadata_field_settings'
        unique_together = (('field_id', 'locale', 'setting_name'),)


class CataloguingMetadataFields(models.Model):
    field_id = models.BigIntegerField(primary_key=True)
    press_id = models.BigIntegerField()
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cataloguing_metadata_fields'


class Categories(models.Model):
    category_id = models.BigIntegerField(primary_key=True)
    press_id = models.BigIntegerField()
    parent_id = models.BigIntegerField()
    path = models.CharField(max_length=255)
    image = models.TextField(blank=True, null=True)
    seq = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'
        unique_together = (('press_id', 'path'),)


class CategorySettings(models.Model):
    category_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'category_settings'
        unique_together = (('category_id', 'locale', 'setting_name'),)


class CitationSettings(models.Model):
    citation_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'citation_settings'
        unique_together = (('citation_id', 'locale', 'setting_name'),)


class Citations(models.Model):
    citation_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    citation_state = models.BigIntegerField()
    raw_citation = models.TextField(blank=True, null=True)
    seq = models.BigIntegerField()
    lock_id = models.CharField(max_length=23, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citations'
        unique_together = (('assoc_type', 'assoc_id', 'seq'),)


class CompletedPayments(models.Model):
    completed_payment_id = models.BigIntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    payment_type = models.BigIntegerField()
    press_id = models.BigIntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.CharField(max_length=16, blank=True, null=True)
    amount = models.FloatField()
    currency_code_alpha = models.CharField(max_length=3, blank=True, null=True)
    payment_method_plugin_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'completed_payments'


class ControlledVocabEntries(models.Model):
    controlled_vocab_entry_id = models.BigIntegerField(primary_key=True)
    controlled_vocab_id = models.BigIntegerField()
    seq = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'controlled_vocab_entries'


class ControlledVocabEntrySettings(models.Model):
    controlled_vocab_entry_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'controlled_vocab_entry_settings'
        unique_together = (('controlled_vocab_entry_id', 'locale', 'setting_name'),)


class ControlledVocabs(models.Model):
    controlled_vocab_id = models.BigIntegerField(primary_key=True)
    symbolic = models.CharField(max_length=64)
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'controlled_vocabs'
        unique_together = (('symbolic', 'assoc_type', 'assoc_id'),)


class DataObjectTombstoneOaiSetObjects(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    tombstone_id = models.BigIntegerField()
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'data_object_tombstone_oai_set_objects'


class DataObjectTombstoneSettings(models.Model):
    tombstone_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'data_object_tombstone_settings'
        unique_together = (('tombstone_id', 'locale', 'setting_name'),)


class DataObjectTombstones(models.Model):
    tombstone_id = models.BigIntegerField(primary_key=True)
    data_object_id = models.BigIntegerField()
    date_deleted = models.DateTimeField()
    set_spec = models.CharField(max_length=255)
    set_name = models.CharField(max_length=255)
    oai_identifier = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'data_object_tombstones'


class EditDecisions(models.Model):
    edit_decision_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    review_round_id = models.BigIntegerField()
    stage_id = models.BigIntegerField(blank=True, null=True)
    round = models.IntegerField()
    editor_id = models.BigIntegerField()
    decision = models.IntegerField()
    date_decided = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'edit_decisions'


class EmailLog(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    sender_id = models.BigIntegerField()
    date_sent = models.DateTimeField()
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    event_type = models.BigIntegerField(blank=True, null=True)
    from_address = models.CharField(max_length=255, blank=True, null=True)
    recipients = models.TextField(blank=True, null=True)
    cc_recipients = models.TextField(blank=True, null=True)
    bcc_recipients = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_log'


class EmailLogUsers(models.Model):
    email_log_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'email_log_users'
        unique_together = (('email_log_id', 'user_id'),)


class EmailTemplates(models.Model):
    email_id = models.BigIntegerField(primary_key=True)
    email_key = models.CharField(max_length=64)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'email_templates'
        unique_together = (('email_key', 'assoc_type', 'assoc_id'),)


class EmailTemplatesData(models.Model):
    email_key = models.CharField(max_length=64)
    locale = models.CharField(max_length=5)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    subject = models.CharField(max_length=120)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_templates_data'
        unique_together = (('email_key', 'locale', 'assoc_type', 'assoc_id'),)


class EmailTemplatesDefault(models.Model):
    email_id = models.BigIntegerField(primary_key=True)
    email_key = models.CharField(max_length=64)
    can_disable = models.IntegerField()
    can_edit = models.IntegerField()
    from_role_id = models.BigIntegerField(blank=True, null=True)
    to_role_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_templates_default'


class EmailTemplatesDefaultData(models.Model):
    email_key = models.CharField(max_length=64)
    locale = models.CharField(max_length=5)
    subject = models.CharField(max_length=120)
    body = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_templates_default_data'
        unique_together = (('email_key', 'locale'),)


class EventLog(models.Model):
    log_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    date_logged = models.DateTimeField()
    ip_address = models.CharField(max_length=39)
    event_type = models.BigIntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    is_translated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_log'


class EventLogSettings(models.Model):
    log_id = models.BigIntegerField()
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'event_log_settings'
        unique_together = (('log_id', 'setting_name'),)


class Features(models.Model):
    submission_id = models.BigIntegerField()
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    seq = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'features'
        unique_together = (('assoc_type', 'assoc_id', 'submission_id'),)


class FilterGroups(models.Model):
    filter_group_id = models.BigIntegerField(primary_key=True)
    symbolic = models.CharField(unique=True, max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    input_type = models.CharField(max_length=255, blank=True, null=True)
    output_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filter_groups'


class FilterSettings(models.Model):
    filter_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'filter_settings'
        unique_together = (('filter_id', 'locale', 'setting_name'),)


class Filters(models.Model):
    filter_id = models.BigIntegerField(primary_key=True)
    filter_group_id = models.BigIntegerField()
    context_id = models.BigIntegerField()
    display_name = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    is_template = models.IntegerField()
    parent_filter_id = models.BigIntegerField()
    seq = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'filters'


class FooterCategories(models.Model):
    footer_category_id = models.BigIntegerField(primary_key=True)
    context_id = models.BigIntegerField()
    path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'footer_categories'
        unique_together = (('context_id', 'path'),)


class FooterCategorySettings(models.Model):
    footer_category_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'footer_category_settings'
        unique_together = (('footer_category_id', 'locale', 'setting_name'),)


class FooterlinkSettings(models.Model):
    footerlink_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'footerlink_settings'
        unique_together = (('footerlink_id', 'locale', 'setting_name'),)


class Footerlinks(models.Model):
    footerlink_id = models.BigIntegerField(primary_key=True)
    context_id = models.BigIntegerField()
    footer_category_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'footerlinks'


class GenreSettings(models.Model):
    genre_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'genre_settings'
        unique_together = (('genre_id', 'locale', 'setting_name'),)


class Genres(models.Model):
    genre_id = models.BigIntegerField(primary_key=True)
    context_id = models.BigIntegerField()
    seq = models.BigIntegerField(blank=True, null=True)
    sortable = models.IntegerField()
    enabled = models.IntegerField()
    category = models.BigIntegerField()
    dependent = models.IntegerField()
    entry_key = models.CharField(max_length=30, blank=True, null=True)
    supplementary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class IdentificationCodes(models.Model):
    identification_code_id = models.BigIntegerField(primary_key=True)
    publication_format_id = models.BigIntegerField()
    code = models.CharField(max_length=40)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'identification_codes'


class ItemViews(models.Model):
    assoc_type = models.BigIntegerField()
    assoc_id = models.CharField(max_length=32)
    user_id = models.BigIntegerField(blank=True, null=True)
    date_last_viewed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_views'
        unique_together = (('assoc_type', 'assoc_id', 'user_id'),)


class LibraryFileSettings(models.Model):
    file_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'library_file_settings'
        unique_together = (('file_id', 'locale', 'setting_name'),)


class LibraryFiles(models.Model):
    file_id = models.BigIntegerField(primary_key=True)
    context_id = models.BigIntegerField()
    file_name = models.CharField(max_length=255)
    original_file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    type = models.IntegerField()
    date_uploaded = models.DateTimeField()
    date_modified = models.DateTimeField()
    submission_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'library_files'


class Markets(models.Model):
    market_id = models.BigIntegerField(primary_key=True)
    publication_format_id = models.BigIntegerField()
    countries_included = models.TextField(blank=True, null=True)
    countries_excluded = models.TextField(blank=True, null=True)
    regions_included = models.TextField(blank=True, null=True)
    regions_excluded = models.TextField(blank=True, null=True)
    market_date_role = models.CharField(max_length=40)
    market_date_format = models.CharField(max_length=40)
    market_date = models.CharField(max_length=255)
    price = models.CharField(max_length=255, blank=True, null=True)
    discount = models.CharField(max_length=255, blank=True, null=True)
    price_type_code = models.CharField(max_length=255, blank=True, null=True)
    currency_code = models.CharField(max_length=255, blank=True, null=True)
    tax_rate_code = models.CharField(max_length=255, blank=True, null=True)
    tax_type_code = models.CharField(max_length=255, blank=True, null=True)
    agent_id = models.BigIntegerField(blank=True, null=True)
    supplier_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'markets'


class MetadataDescriptionSettings(models.Model):
    metadata_description_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'metadata_description_settings'
        unique_together = (('metadata_description_id', 'locale', 'setting_name'),)


class MetadataDescriptions(models.Model):
    metadata_description_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    schema_namespace = models.CharField(max_length=255)
    schema_name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    seq = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'metadata_descriptions'


class Metrics(models.Model):
    load_id = models.CharField(max_length=255)
    context_id = models.BigIntegerField()
    pkp_section_id = models.BigIntegerField(blank=True, null=True)
    assoc_object_type = models.BigIntegerField(blank=True, null=True)
    assoc_object_id = models.BigIntegerField(blank=True, null=True)
    submission_id = models.BigIntegerField(blank=True, null=True)
    representation_id = models.BigIntegerField(blank=True, null=True)
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    day = models.CharField(max_length=8, blank=True, null=True)
    month = models.CharField(max_length=6, blank=True, null=True)
    file_type = models.IntegerField(blank=True, null=True)
    country_id = models.CharField(max_length=2, blank=True, null=True)
    region = models.CharField(max_length=2, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    metric_type = models.CharField(max_length=255)
    metric = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'metrics'


class Mutex(models.Model):
    i = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'mutex'


class NewReleases(models.Model):
    submission_id = models.BigIntegerField()
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'new_releases'
        unique_together = (('assoc_type', 'assoc_id', 'submission_id'),)


class Notes(models.Model):
    note_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    contents = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes'


class NotificationMailList(models.Model):
    notification_mail_list_id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=90)
    confirmed = models.IntegerField()
    token = models.CharField(max_length=40)
    context = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'notification_mail_list'
        unique_together = (('email', 'context'),)


class NotificationSettings(models.Model):
    notification_id = models.BigIntegerField()
    locale = models.CharField(max_length=5, blank=True, null=True)
    setting_name = models.CharField(max_length=64)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'notification_settings'
        unique_together = (('notification_id', 'locale', 'setting_name'),)


class NotificationStatus(models.Model):
    press_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'notification_status'
        unique_together = (('press_id', 'user_id'),)


class NotificationSubscriptionSettings(models.Model):
    setting_id = models.BigIntegerField(primary_key=True)
    setting_name = models.CharField(max_length=64)
    setting_value = models.TextField(blank=True, null=True)
    user_id = models.BigIntegerField()
    context = models.BigIntegerField()
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'notification_subscription_settings'


class Notifications(models.Model):
    notification_id = models.BigIntegerField(primary_key=True)
    context_id = models.BigIntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    level = models.BigIntegerField()
    type = models.BigIntegerField()
    date_created = models.DateTimeField()
    date_read = models.DateTimeField(blank=True, null=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class OaiResumptionTokens(models.Model):
    token = models.CharField(unique=True, max_length=32)
    expire = models.BigIntegerField()
    record_offset = models.IntegerField()
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oai_resumption_tokens'


class PaypalTransactions(models.Model):
    txn_id = models.CharField(primary_key=True, max_length=17)
    txn_type = models.CharField(max_length=20, blank=True, null=True)
    payer_email = models.CharField(max_length=127, blank=True, null=True)
    receiver_email = models.CharField(max_length=127, blank=True, null=True)
    item_number = models.CharField(max_length=127, blank=True, null=True)
    payment_date = models.CharField(max_length=127, blank=True, null=True)
    payer_id = models.CharField(max_length=13, blank=True, null=True)
    receiver_id = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_transactions'


class PluginSettings(models.Model):
    plugin_name = models.CharField(max_length=80)
    context_id = models.BigIntegerField()
    setting_name = models.CharField(max_length=80)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'plugin_settings'
        unique_together = (('plugin_name', 'context_id', 'setting_name'),)


class PressSettings(models.Model):
    press_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'press_settings'
        unique_together = (('press_id', 'locale', 'setting_name'),)


class Presses(models.Model):
    press_id = models.BigIntegerField(primary_key=True)
    path = models.CharField(unique=True, max_length=32)
    seq = models.FloatField()
    primary_locale = models.CharField(max_length=5)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'presses'


class Processes(models.Model):
    process_id = models.CharField(unique=True, max_length=23)
    process_type = models.IntegerField()
    time_started = models.BigIntegerField()
    additional_data = models.TextField(blank=True, null=True)
    obliterated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'processes'


class PublicationDates(models.Model):
    publication_date_id = models.BigIntegerField(primary_key=True)
    publication_format_id = models.BigIntegerField()
    role = models.CharField(max_length=40)
    date_format = models.CharField(max_length=40)
    date = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'publication_dates'


class PublicationFormatSettings(models.Model):
    publication_format_id = models.BigIntegerField()
    locale = models.CharField(max_length=5, )
    setting_name = models.CharField(max_length=255, )
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'publication_format_settings'
        unique_together = (('publication_format_id', 'locale', 'setting_name'),)


class PublicationFormats(models.Model):
    publication_format_id = models.BigIntegerField()
    submission_id = models.BigIntegerField()
    physical_format = models.IntegerField(blank=True, null=True)
    entry_key = models.CharField(max_length=64, blank=True, null=True)
    seq = models.FloatField()
    file_size = models.CharField(max_length=255, blank=True, null=True)
    front_matter = models.CharField(max_length=255, blank=True, null=True)
    back_matter = models.CharField(max_length=255, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    height_unit_code = models.CharField(max_length=255, blank=True, null=True)
    width = models.CharField(max_length=255, blank=True, null=True)
    width_unit_code = models.CharField(max_length=255, blank=True, null=True)
    thickness = models.CharField(max_length=255, blank=True, null=True)
    thickness_unit_code = models.CharField(max_length=255, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    weight_unit_code = models.CharField(max_length=255, blank=True, null=True)
    product_composition_code = models.CharField(max_length=255, blank=True, null=True)
    product_form_detail_code = models.CharField(max_length=255, blank=True, null=True)
    country_manufacture_code = models.CharField(max_length=255, blank=True, null=True)
    imprint = models.CharField(max_length=255, blank=True, null=True)
    product_availability_code = models.CharField(max_length=255, blank=True, null=True)
    technical_protection_code = models.CharField(max_length=255, blank=True, null=True)
    returnable_indicator_code = models.CharField(max_length=255, blank=True, null=True)
    is_approved = models.IntegerField()
    is_available = models.IntegerField()
    remote_url = models.CharField(max_length=2047, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publication_formats'


class PublishedSubmissions(models.Model):
    pub_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField(unique=True)
    date_published = models.DateTimeField(blank=True, null=True)
    audience = models.CharField(max_length=255, blank=True, null=True)
    audience_range_qualifier = models.CharField(max_length=255, blank=True, null=True)
    audience_range_from = models.CharField(max_length=255, blank=True, null=True)
    audience_range_to = models.CharField(max_length=255, blank=True, null=True)
    audience_range_exact = models.CharField(max_length=255, blank=True, null=True)
    cover_image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'published_submissions'


class Queries(models.Model):
    query_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    stage_id = models.IntegerField()
    seq = models.FloatField()
    date_posted = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    closed = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'queries'


class QueryParticipants(models.Model):
    query_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'query_participants'
        unique_together = (('query_id', 'user_id'),)


class QueuedPayments(models.Model):
    queued_payment_id = models.BigIntegerField(primary_key=True)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    expiry_date = models.DateField(blank=True, null=True)
    payment_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queued_payments'


class Representatives(models.Model):
    representative_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    role = models.CharField(max_length=40)
    representative_id_type = models.CharField(max_length=255, blank=True, null=True)
    representative_id_value = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=2047, blank=True, null=True)
    is_supplier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'representatives'


class ReviewAssignments(models.Model):
    review_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    reviewer_id = models.BigIntegerField()
    competing_interests = models.TextField(blank=True, null=True)
    recommendation = models.IntegerField(blank=True, null=True)
    date_assigned = models.DateTimeField(blank=True, null=True)
    date_notified = models.DateTimeField(blank=True, null=True)
    date_confirmed = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    date_acknowledged = models.DateTimeField(blank=True, null=True)
    date_due = models.DateTimeField(blank=True, null=True)
    date_response_due = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    reminder_was_automatic = models.IntegerField()
    declined = models.IntegerField()
    replaced = models.IntegerField()
    cancelled = models.IntegerField()
    reviewer_file_id = models.BigIntegerField(blank=True, null=True)
    date_rated = models.DateTimeField(blank=True, null=True)
    date_reminded = models.DateTimeField(blank=True, null=True)
    quality = models.IntegerField(blank=True, null=True)
    review_round_id = models.BigIntegerField(blank=True, null=True)
    stage_id = models.IntegerField()
    review_method = models.IntegerField()
    round = models.IntegerField()
    step = models.IntegerField()
    review_form_id = models.BigIntegerField(blank=True, null=True)
    unconsidered = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_assignments'


class ReviewFiles(models.Model):
    review_id = models.BigIntegerField()
    file_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'review_files'
        unique_together = (('review_id', 'file_id'),)


class ReviewFormElementSettings(models.Model):
    review_form_element_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'review_form_element_settings'
        unique_together = (('review_form_element_id', 'locale', 'setting_name'),)


class ReviewFormElements(models.Model):
    review_form_element_id = models.BigIntegerField(primary_key=True)
    review_form_id = models.BigIntegerField()
    seq = models.FloatField(blank=True, null=True)
    element_type = models.BigIntegerField(blank=True, null=True)
    required = models.IntegerField(blank=True, null=True)
    included = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_form_elements'


class ReviewFormResponses(models.Model):
    review_form_element_id = models.BigIntegerField()
    review_id = models.BigIntegerField()
    response_type = models.CharField(max_length=6, blank=True, null=True)
    response_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_form_responses'


class ReviewFormSettings(models.Model):
    review_form_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'review_form_settings'
        unique_together = (('review_form_id', 'locale', 'setting_name'),)


class ReviewForms(models.Model):
    review_form_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    seq = models.FloatField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_forms'


class ReviewRoundFiles(models.Model):
    submission_id = models.BigIntegerField()
    review_round_id = models.BigIntegerField()
    stage_id = models.IntegerField()
    file_id = models.BigIntegerField()
    revision = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'review_round_files'
        unique_together = (('submission_id', 'review_round_id', 'file_id', 'revision'),)


class ReviewRounds(models.Model):
    review_round_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    stage_id = models.BigIntegerField(blank=True, null=True)
    round = models.IntegerField()
    review_revision = models.BigIntegerField(blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_rounds'
        unique_together = (('submission_id', 'stage_id', 'round'),)


class SalesRights(models.Model):
    sales_rights_id = models.BigIntegerField(primary_key=True)
    publication_format_id = models.BigIntegerField()
    type = models.CharField(max_length=40)
    row_setting = models.IntegerField()
    countries_included = models.TextField(blank=True, null=True)
    countries_excluded = models.TextField(blank=True, null=True)
    regions_included = models.TextField(blank=True, null=True)
    regions_excluded = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_rights'


class ScheduledTasks(models.Model):
    class_name = models.CharField(unique=True, max_length=255)
    last_run = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scheduled_tasks'


class SectionEditors(models.Model):
    context_id = models.BigIntegerField()
    section_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'section_editors'
        unique_together = (('context_id', 'section_id', 'user_id'),)


class Series(models.Model):
    series_id = models.BigIntegerField(primary_key=True)
    press_id = models.BigIntegerField()
    seq = models.FloatField(blank=True, null=True)
    featured = models.IntegerField()
    editor_restricted = models.IntegerField()
    path = models.CharField(max_length=255)
    image = models.TextField(blank=True, null=True)
    review_form_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'series'
        unique_together = (('press_id', 'path'),)


class SeriesCategories(models.Model):
    series_id = models.BigIntegerField()
    category_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'series_categories'
        unique_together = (('series_id', 'category_id'),)


class SeriesEditors(models.Model):
    press_id = models.BigIntegerField()
    series_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    can_edit = models.IntegerField()
    can_review = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'series_editors'
        unique_together = (('press_id', 'series_id', 'user_id'),)


class SeriesSettings(models.Model):
    series_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'series_settings'
        unique_together = (('series_id', 'locale', 'setting_name'),)


class Sessions(models.Model):
    session_id = models.CharField(unique=True, max_length=128)
    user_id = models.BigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=39)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    created = models.BigIntegerField()
    last_used = models.BigIntegerField()
    remember = models.IntegerField()
    data = models.TextField(blank=True, null=True)
    domain = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class Site(models.Model):
    redirect = models.BigIntegerField()
    primary_locale = models.CharField(max_length=5)
    min_password_length = models.IntegerField()
    installed_locales = models.CharField(max_length=255)
    supported_locales = models.CharField(max_length=255, blank=True, null=True)
    original_style_file_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site'


class SiteSettings(models.Model):
    setting_name = models.CharField(max_length=255)
    locale = models.CharField(max_length=5)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'site_settings'
        unique_together = (('setting_name', 'locale'),)


class SocialMedia(models.Model):
    social_media_id = models.BigIntegerField(primary_key=True)
    context_id = models.BigIntegerField()
    code = models.TextField(blank=True, null=True)
    include_in_catalog = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_media'


class SocialMediaSettings(models.Model):
    social_media_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'social_media_settings'
        unique_together = (('social_media_id', 'locale', 'setting_name'),)


class SpotlightSettings(models.Model):
    spotlight_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'spotlight_settings'
        unique_together = (('spotlight_id', 'locale', 'setting_name'),)


class Spotlights(models.Model):
    spotlight_id = models.BigIntegerField(primary_key=True)
    assoc_type = models.SmallIntegerField()
    assoc_id = models.SmallIntegerField()
    press_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'spotlights'


class StageAssignments(models.Model):
    stage_assignment_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    user_group_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    date_assigned = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stage_assignments'
        unique_together = (('submission_id', 'user_group_id', 'user_id'),)


class StaticPageSettings(models.Model):
    static_page_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'static_page_settings'
        unique_together = (('static_page_id', 'locale', 'setting_name'),)


class StaticPages(models.Model):
    static_page_id = models.BigIntegerField(primary_key=True)
    path = models.CharField(max_length=255)
    context_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'static_pages'


class SubmissionArtworkFiles(models.Model):
    file_id = models.BigIntegerField(primary_key=True)
    revision = models.BigIntegerField()
    caption = models.TextField(blank=True, null=True)
    credit = models.CharField(max_length=255, blank=True, null=True)
    copyright_owner = models.CharField(max_length=255, blank=True, null=True)
    copyright_owner_contact = models.TextField(blank=True, null=True)
    permission_terms = models.TextField(blank=True, null=True)
    permission_file_id = models.BigIntegerField(blank=True, null=True)
    chapter_id = models.BigIntegerField(blank=True, null=True)
    contact_author = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'submission_artwork_files'
        unique_together = (('file_id', 'revision'),)


class SubmissionCategories(models.Model):
    submission_id = models.BigIntegerField()
    category_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'submission_categories'
        unique_together = (('submission_id', 'category_id'),)


class SubmissionChapterAuthors(models.Model):
    author_id = models.BigIntegerField(primary_key=True)
    chapter_id = models.BigIntegerField()
    submission_id = models.BigIntegerField()
    primary_contact = models.IntegerField()
    seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'submission_chapter_authors'
        unique_together = (('author_id', 'chapter_id'),)


class SubmissionChapterSettings(models.Model):
    chapter_id = models.BigIntegerField(primary_key=True)
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'submission_chapter_settings'
        unique_together = (('chapter_id', 'locale', 'setting_name'),)


class SubmissionChapters(models.Model):
    chapter_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    chapter_seq = models.FloatField()

    class Meta:
        managed = False
        db_table = 'submission_chapters'


class SubmissionComments(models.Model):
    comment_id = models.BigIntegerField(primary_key=True)
    comment_type = models.BigIntegerField(blank=True, null=True)
    role_id = models.BigIntegerField()
    submission_id = models.BigIntegerField()
    assoc_id = models.BigIntegerField()
    author_id = models.BigIntegerField()
    comment_title = models.CharField(max_length=90)
    comments = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    viewable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'submission_comments'


class SubmissionFiles(models.Model):
    file_id = models.BigIntegerField()
    revision = models.BigIntegerField()
    source_file_id = models.BigIntegerField(blank=True, null=True)
    source_revision = models.BigIntegerField(blank=True, null=True)
    submission_id = models.BigIntegerField()
    file_type = models.CharField(max_length=255)
    genre_id = models.BigIntegerField(blank=True, null=True)
    file_size = models.BigIntegerField()
    original_file_name = models.CharField(max_length=127, blank=True, null=True)
    file_stage = models.BigIntegerField()
    direct_sales_price = models.CharField(max_length=255, blank=True, null=True)
    sales_type = models.CharField(max_length=255, blank=True, null=True)
    viewable = models.IntegerField(blank=True, null=True)
    date_uploaded = models.DateTimeField()
    date_modified = models.DateTimeField()
    #user_group_id = models.BigIntegerField(blank=True, null=True)
    uploader_user_id = models.BigIntegerField(blank=True, null=True)
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'submission_files'
        unique_together = (('file_id', 'revision'))


class SubmissionFileSettings(models.Model):
    file_id = models.BigIntegerField()
    #file_id = models.ForeignKey(SubmissionFiles, on_delete=False, related_name='file_id+', )
    locale = models.CharField(max_length=5, )
    setting_name = models.CharField(max_length=255, )
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'submission_file_settings'
        unique_together = (('file_id', 'locale', 'setting_name'))


class SubmissionSearchKeywordList(models.Model):
    keyword_id = models.BigIntegerField(primary_key=True)
    keyword_text = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'submission_search_keyword_list'


class SubmissionSearchObjectKeywords(models.Model):
    object_id = models.BigIntegerField()
    keyword_id = models.BigIntegerField()
    pos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'submission_search_object_keywords'
        unique_together = (('object_id', 'pos'),)


class SubmissionSearchObjects(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    submission_id = models.BigIntegerField()
    type = models.IntegerField()
    assoc_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'submission_search_objects'


class SubmissionSupplementaryFiles(models.Model):
    file_id = models.BigIntegerField(primary_key=True)
    revision = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'submission_supplementary_files'
        unique_together = (('file_id', 'revision'),)


class Submissions(models.Model):
    submission_id = models.BigIntegerField(primary_key=True)
    locale = models.CharField(max_length=5, blank=True, null=True)
    context_id = models.BigIntegerField()
    series_id = models.BigIntegerField(blank=True, null=True)
    series_position = models.CharField(max_length=255, blank=True, null=True)
    edited_volume = models.IntegerField()
    language = models.CharField(max_length=10, blank=True, null=True)
    ##comments_to_ed = models.TextField(blank=True, null=True)
    date_submitted = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    date_status_modified = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    submission_progress = models.IntegerField()
    pages = models.CharField(max_length=255, blank=True, null=True)
    fast_tracked = models.IntegerField()
    hide_author = models.IntegerField()
    stage_id = models.BigIntegerField()
    citations = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'submissions'


class SubmissionSettings(models.Model):
    submission_id = models.BigIntegerField()
    locale = models.CharField(max_length=5, )
    setting_name = models.CharField(max_length=255, )
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    objects = models.Manager()
    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'submission_settings'
        unique_together = (('submission_id', 'locale', 'setting_name'),)


class TGeoipCountry(models.Model):
    ip_begin = models.CharField(unique=True, max_length=15)
    ip_end = models.CharField(max_length=15)
    ip_decimal_begin = models.IntegerField()
    ip_decimal_end = models.IntegerField()
    country_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 't_geoip_country'


class TKnvMetadata(models.Model):
    submission_id = models.IntegerField(blank=True, null=True)
    isbn = models.IntegerField()
    buchtitel = models.CharField(max_length=512, blank=True, null=True)
    anz_teile = models.IntegerField(blank=True, null=True)
    verlagsname = models.CharField(max_length=512, blank=True, null=True)
    gln = models.IntegerField(blank=True, null=True)
    bindeart = models.CharField(max_length=512, blank=True, null=True)
    anz_rillungen = models.IntegerField(blank=True, null=True)
    kapitalband = models.CharField(max_length=512, blank=True, null=True)
    rueckenart = models.CharField(max_length=512, blank=True, null=True)
    ansichtsexemplar = models.CharField(max_length=512, blank=True, null=True)
    laendercode = models.CharField(max_length=512, blank=True, null=True)
    adresszeile2 = models.CharField(max_length=512, blank=True, null=True)
    adresszeile3 = models.CharField(max_length=512, blank=True, null=True)
    ort = models.CharField(max_length=512, blank=True, null=True)
    plz = models.IntegerField(blank=True, null=True)
    strasse_und_nr = models.CharField(max_length=512, blank=True, null=True)
    postfach = models.CharField(max_length=512, blank=True, null=True)
    speicherung = models.CharField(max_length=512, blank=True, null=True)
    dateiname_pdf_cover = models.CharField(max_length=512, blank=True, null=True)
    teilnummer = models.IntegerField(blank=True, null=True)
    anzahl_seiten = models.IntegerField(blank=True, null=True)
    druckfarbe = models.CharField(max_length=512, blank=True, null=True)
    pruefung_trimbox = models.CharField(max_length=512, blank=True, null=True)
    prueftoleranz = models.CharField(max_length=512, blank=True, null=True)
    papiertyp = models.CharField(max_length=512, blank=True, null=True)
    laminierungsart = models.CharField(max_length=512, blank=True, null=True)
    barcode_position = models.CharField(max_length=512, blank=True, null=True)
    dateiname_pdf_innerwork_field = models.CharField(db_column='dateiname_pdf_innerwork_', max_length=512, blank=True,
                                                     null=True)  # Field renamed because it ended with '_'.
    farbraum = models.CharField(max_length=512, blank=True, null=True)
    anzahl_farbseiten = models.IntegerField(blank=True, null=True)
    breite_der_trimbox = models.IntegerField(blank=True, null=True)
    hoehe_der_trimbox = models.IntegerField(blank=True, null=True)
    f_papiertyp = models.CharField(max_length=512, blank=True, null=True)
    letzte_seite = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_knv_metadata'


class TLicenseSettings(models.Model):
    license_id = models.IntegerField(primary_key=True)
    locale = models.CharField(max_length=6)
    setting_name = models.CharField(max_length=48)
    setting_value = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_license_settings'
        unique_together = (('license_id', 'locale', 'setting_name'),)


class TOnixAdditionals(models.Model):
    submission_id = models.IntegerField(blank=True, null=True)
    f_sent_date = models.DateField(blank=True, null=True)
    f_pages_roman = models.CharField(max_length=512)
    f_pages_arabic = models.IntegerField()
    f_b191 = models.IntegerField()
    f_b068 = models.CharField(max_length=512)
    f_b069 = models.CharField(max_length=512)
    f_b070 = models.CharField(max_length=512)
    f_b069_wg = models.CharField(max_length=512)
    f_b070_wg = models.TextField()
    f114_file_type_code = models.CharField(max_length=512)
    f115_file_format_code = models.CharField(max_length=512)
    f116_file_link_type = models.CharField(max_length=512)
    f117_cover_image = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 't_onix_additionals'


class TUsageStatistics(models.Model):
    time_stamp = models.DateTimeField(blank=True, null=True)
    client_ip = models.CharField(max_length=512, blank=True, null=True)
    request_controller = models.CharField(max_length=512, blank=True, null=True)
    request_function = models.CharField(max_length=512, blank=True, null=True)
    request_extension = models.CharField(max_length=512, blank=True, null=True)
    request_ajax = models.CharField(max_length=512, blank=True, null=True)
    request_args = models.CharField(max_length=512, blank=True, null=True)
    request_vars = models.CharField(max_length=512, blank=True, null=True)
    request_view = models.CharField(max_length=512, blank=True, null=True)
    request_http_user_agent = models.CharField(max_length=512, blank=True, null=True)
    request_language = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_usage_statistics'


class TemporaryFiles(models.Model):
    file_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    file_name = models.CharField(max_length=90)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.BigIntegerField()
    original_file_name = models.CharField(max_length=127, blank=True, null=True)
    date_uploaded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'temporary_files'


class UsageStatsTemporaryRecords(models.Model):
    assoc_id = models.BigIntegerField()
    assoc_type = models.BigIntegerField()
    day = models.BigIntegerField()
    entry_time = models.BigIntegerField()
    metric = models.BigIntegerField()
    country_id = models.CharField(max_length=2, blank=True, null=True)
    region = models.CharField(max_length=2, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    load_id = models.CharField(max_length=255)
    file_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usage_stats_temporary_records'


class UserGroupSettings(models.Model):
    user_group_id = models.BigIntegerField()
    locale = models.CharField(max_length=5)
    setting_name = models.CharField(max_length=255)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'user_group_settings'
        unique_together = (('user_group_id', 'locale', 'setting_name'),)


class UserGroupStage(models.Model):
    context_id = models.BigIntegerField()
    user_group_id = models.BigIntegerField()
    stage_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_group_stage'
        unique_together = (('context_id', 'user_group_id', 'stage_id'),)


class UserGroups(models.Model):
    user_group_id = models.BigIntegerField(primary_key=True)
    context_id = models.BigIntegerField()
    role_id = models.BigIntegerField()
    is_default = models.IntegerField()
    show_title = models.IntegerField()
    permit_self_registration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_groups'


class UserInterests(models.Model):
    user_id = models.BigIntegerField()
    controlled_vocab_entry_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_interests'
        unique_together = (('user_id', 'controlled_vocab_entry_id'),)


class UserSettings(models.Model):
    user_id = models.BigIntegerField()
    locale = models.CharField(max_length=5, )
    setting_name = models.CharField(max_length=255, )
    assoc_type = models.BigIntegerField(blank=True, null=True)
    assoc_id = models.BigIntegerField(blank=True, null=True)
    setting_value = models.TextField(blank=True, null=True)
    setting_type = models.CharField(max_length=6)

    setting_by_name = OMPManager()

    class Meta:
        managed = False
        db_table = 'user_settings'
        unique_together = (('user_id', 'locale', 'setting_name'))


class UserUserGroups(models.Model):
    user_group_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'user_user_groups'
        unique_together = (('user_group_id', 'user_id'),)


class Users(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=32)
    password = models.CharField(max_length=255)
    salutation = models.CharField(max_length=40, blank=True, null=True)
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=90)
    suffix = models.CharField(max_length=40, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    initials = models.CharField(max_length=5, blank=True, null=True)
    email = models.CharField(unique=True, max_length=90)
    url = models.CharField(max_length=2047, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    mailing_address = models.CharField(max_length=255, blank=True, null=True)
    billing_address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=90, blank=True, null=True)
    locales = models.CharField(max_length=255, blank=True, null=True)
    date_last_email = models.DateTimeField(blank=True, null=True)
    date_registered = models.DateTimeField()
    date_validated = models.DateTimeField(blank=True, null=True)
    date_last_login = models.DateTimeField()
    must_change_password = models.IntegerField(blank=True, null=True)
    auth_id = models.BigIntegerField(blank=True, null=True)
    auth_str = models.CharField(max_length=255, blank=True, null=True)
    disabled = models.IntegerField()
    disabled_reason = models.TextField(blank=True, null=True)
    inline_help = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Versions(models.Model):
    major = models.IntegerField()
    minor = models.IntegerField()
    revision = models.IntegerField()
    build = models.IntegerField()
    date_installed = models.DateTimeField()
    current = models.IntegerField()
    product_type = models.CharField(max_length=30, blank=True, null=True)
    product = models.CharField(max_length=30, blank=True, null=True)
    product_class_name = models.CharField(max_length=80, blank=True, null=True)
    lazy_load = models.IntegerField()
    sitewide = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'versions'
        unique_together = (('product_type', 'product', 'major', 'minor', 'revision', 'build'),)
