# coding: utf-8

# flake8: noqa

"""
    StarRez API

    This is a way to connect with the StarRez API. We are not the developers of the StarRez API, we are just an organization that uses it and wanted a better way to connect to it.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: resdev@calpoly.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from starrez_client.api.default_api import DefaultApi

# import ApiClient
from starrez_client.api_client import ApiClient
from starrez_client.configuration import Configuration
# import models into sdk package
from starrez_client.models.address_type_item import AddressTypeItem
from starrez_client.models.application_status_item import ApplicationStatusItem
from starrez_client.models.auto_allocate_run_item import AutoAllocateRunItem
from starrez_client.models.booking_agreement_item import BookingAgreementItem
from starrez_client.models.booking_custom_field_item import BookingCustomFieldItem
from starrez_client.models.booking_item import BookingItem
from starrez_client.models.booking_linked_item import BookingLinkedItem
from starrez_client.models.booking_occupant_item import BookingOccupantItem
from starrez_client.models.booking_reason_item import BookingReasonItem
from starrez_client.models.booking_tag_item import BookingTagItem
from starrez_client.models.booking_type_item import BookingTypeItem
from starrez_client.models.calendar_item import CalendarItem
from starrez_client.models.category_custom_field_item import CategoryCustomFieldItem
from starrez_client.models.category_item import CategoryItem
from starrez_client.models.category_level_item import CategoryLevelItem
from starrez_client.models.category_permission_item import CategoryPermissionItem
from starrez_client.models.category_schedule_transaction_item import CategoryScheduleTransactionItem
from starrez_client.models.catering_item import CateringItem
from starrez_client.models.catering_item_item import CateringItemItem
from starrez_client.models.catering_type_item import CateringTypeItem
from starrez_client.models.charge_group_item import ChargeGroupItem
from starrez_client.models.charge_item_item import ChargeItemItem
from starrez_client.models.classification_item import ClassificationItem
from starrez_client.models.concern_custom_field_item import ConcernCustomFieldItem
from starrez_client.models.concern_entry_item import ConcernEntryItem
from starrez_client.models.concern_item import ConcernItem
from starrez_client.models.concern_note_item import ConcernNoteItem
from starrez_client.models.concern_sub_type_item import ConcernSubTypeItem
from starrez_client.models.concern_type_item import ConcernTypeItem
from starrez_client.models.contact_custom_field_item import ContactCustomFieldItem
from starrez_client.models.contact_item import ContactItem
from starrez_client.models.contact_note_item import ContactNoteItem
from starrez_client.models.contact_status_item import ContactStatusItem
from starrez_client.models.contribution_custom_field_item import ContributionCustomFieldItem
from starrez_client.models.contribution_entry_item import ContributionEntryItem
from starrez_client.models.contribution_item import ContributionItem
from starrez_client.models.contribution_note_item import ContributionNoteItem
from starrez_client.models.contribution_sub_type_item import ContributionSubTypeItem
from starrez_client.models.contribution_type_item import ContributionTypeItem
from starrez_client.models.correspondence_source_item import CorrespondenceSourceItem
from starrez_client.models.country_item import CountryItem
from starrez_client.models.course_item import CourseItem
from starrez_client.models.currency_conversion_item import CurrencyConversionItem
from starrez_client.models.custom_field_definition_item import CustomFieldDefinitionItem
from starrez_client.models.custom_method_tag_item import CustomMethodTagItem
from starrez_client.models.dashboard_item import DashboardItem
from starrez_client.models.dashboard_panel_item import DashboardPanelItem
from starrez_client.models.dashboard_panel_setting_item import DashboardPanelSettingItem
from starrez_client.models.dashboard_sharing_item import DashboardSharingItem
from starrez_client.models.deleted_transaction_item import DeletedTransactionItem
from starrez_client.models.document_item import DocumentItem
from starrez_client.models.dynamic_list_item import DynamicListItem
from starrez_client.models.dynamic_list_permission_item import DynamicListPermissionItem
from starrez_client.models.electronic_identity_type_item import ElectronicIdentityTypeItem
from starrez_client.models.email_from_address_item import EmailFromAddressItem
from starrez_client.models.email_from_address_permission_item import EmailFromAddressPermissionItem
from starrez_client.models.email_outbox_item import EmailOutboxItem
from starrez_client.models.end_of_session_charge_group_item import EndOfSessionChargeGroupItem
from starrez_client.models.end_of_session_item import EndOfSessionItem
from starrez_client.models.entry_address_item import EntryAddressItem
from starrez_client.models.entry_alumni_item import EntryAlumniItem
from starrez_client.models.entry_alumni_status_item import EntryAlumniStatusItem
from starrez_client.models.entry_application_custom_field_item import EntryApplicationCustomFieldItem
from starrez_client.models.entry_application_item import EntryApplicationItem
from starrez_client.models.entry_application_note_item import EntryApplicationNoteItem
from starrez_client.models.entry_application_portal_section_item import EntryApplicationPortalSectionItem
from starrez_client.models.entry_application_preference_item import EntryApplicationPreferenceItem
from starrez_client.models.entry_application_proxy_item import EntryApplicationProxyItem
from starrez_client.models.entry_application_room_mate_item import EntryApplicationRoomMateItem
from starrez_client.models.entry_application_room_preference_item import EntryApplicationRoomPreferenceItem
from starrez_client.models.entry_correspondence_item import EntryCorrespondenceItem
from starrez_client.models.entry_custom_field_item import EntryCustomFieldItem
from starrez_client.models.entry_detail_item import EntryDetailItem
from starrez_client.models.entry_electronic_identity_item import EntryElectronicIdentityItem
from starrez_client.models.entry_enrollment_item import EntryEnrollmentItem
from starrez_client.models.entry_event_item import EntryEventItem
from starrez_client.models.entry_family_item import EntryFamilyItem
from starrez_client.models.entry_group_item import EntryGroupItem
from starrez_client.models.entry_invitation_item import EntryInvitationItem
from starrez_client.models.entry_item import EntryItem
from starrez_client.models.entry_meal_item import EntryMealItem
from starrez_client.models.entry_meal_plan_detail_item import EntryMealPlanDetailItem
from starrez_client.models.entry_meal_tag_item import EntryMealTagItem
from starrez_client.models.entry_membership_item import EntryMembershipItem
from starrez_client.models.entry_note_item import EntryNoteItem
from starrez_client.models.entry_parcel_item import EntryParcelItem
from starrez_client.models.entry_portal_activity_item import EntryPortalActivityItem
from starrez_client.models.entry_position_item import EntryPositionItem
from starrez_client.models.entry_profile_item import EntryProfileItem
from starrez_client.models.entry_result_item import EntryResultItem
from starrez_client.models.entry_sdas_item import EntrySDASItem
from starrez_client.models.entry_schedule_transaction_item import EntryScheduleTransactionItem
from starrez_client.models.entry_scholarship_item import EntryScholarshipItem
from starrez_client.models.entry_school_item import EntrySchoolItem
from starrez_client.models.entry_visitor_item import EntryVisitorItem
from starrez_client.models.event_charge_item import EventChargeItem
from starrez_client.models.event_contact_entry_item import EventContactEntryItem
from starrez_client.models.event_custom_field_item import EventCustomFieldItem
from starrez_client.models.event_item import EventItem
from starrez_client.models.event_meal_plan_item import EventMealPlanItem
from starrez_client.models.event_note_item import EventNoteItem
from starrez_client.models.event_quote_item import EventQuoteItem
from starrez_client.models.event_registration_fee_item import EventRegistrationFeeItem
from starrez_client.models.event_type_item import EventTypeItem
from starrez_client.models.extension_item import ExtensionItem
from starrez_client.models.field_default_item import FieldDefaultItem
from starrez_client.models.financial_support_item import FinancialSupportItem
from starrez_client.models.function_booking_attendee_item import FunctionBookingAttendeeItem
from starrez_client.models.function_booking_catering_item import FunctionBookingCateringItem
from starrez_client.models.function_booking_catering_item_item import FunctionBookingCateringItemItem
from starrez_client.models.function_booking_charge_item import FunctionBookingChargeItem
from starrez_client.models.function_booking_item import FunctionBookingItem
from starrez_client.models.function_resource_booking_item import FunctionResourceBookingItem
from starrez_client.models.function_resource_item import FunctionResourceItem
from starrez_client.models.function_resource_type_item import FunctionResourceTypeItem
from starrez_client.models.function_room_booking_item import FunctionRoomBookingItem
from starrez_client.models.function_room_closed_item import FunctionRoomClosedItem
from starrez_client.models.function_room_item import FunctionRoomItem
from starrez_client.models.function_room_location_item import FunctionRoomLocationItem
from starrez_client.models.function_room_rate_item import FunctionRoomRateItem
from starrez_client.models.function_room_setup_item import FunctionRoomSetupItem
from starrez_client.models.function_room_type_item import FunctionRoomTypeItem
from starrez_client.models.function_type_item import FunctionTypeItem
from starrez_client.models.gl_posting_item import GLPostingItem
from starrez_client.models.generic_table_data_field_item import GenericTableDataFieldItem
from starrez_client.models.generic_table_data_item import GenericTableDataItem
from starrez_client.models.generic_table_definition_field_item import GenericTableDefinitionFieldItem
from starrez_client.models.generic_table_definition_item import GenericTableDefinitionItem
from starrez_client.models.group_contact_entry_item import GroupContactEntryItem
from starrez_client.models.group_custom_field_item import GroupCustomFieldItem
from starrez_client.models.group_item import GroupItem
from starrez_client.models.group_meal_plan_item import GroupMealPlanItem
from starrez_client.models.group_room_space_item import GroupRoomSpaceItem
from starrez_client.models.group_room_type_and_rates_item import GroupRoomTypeAndRatesItem
from starrez_client.models.housekeeping_item import HousekeepingItem
from starrez_client.models.housekeeping_schedule_item import HousekeepingScheduleItem
from starrez_client.models.housekeeping_schedule_skip_item import HousekeepingScheduleSkipItem
from starrez_client.models.incident_action_entry_item import IncidentActionEntryItem
from starrez_client.models.incident_action_item import IncidentActionItem
from starrez_client.models.incident_action_type_item import IncidentActionTypeItem
from starrez_client.models.incident_appeal_decision_item import IncidentAppealDecisionItem
from starrez_client.models.incident_appeal_type_item import IncidentAppealTypeItem
from starrez_client.models.incident_clery_geography_item import IncidentCleryGeographyItem
from starrez_client.models.incident_custom_field_item import IncidentCustomFieldItem
from starrez_client.models.incident_entry_appeal_item import IncidentEntryAppealItem
from starrez_client.models.incident_entry_correspondence_item import IncidentEntryCorrespondenceItem
from starrez_client.models.incident_entry_item import IncidentEntryItem
from starrez_client.models.incident_entry_note_item import IncidentEntryNoteItem
from starrez_client.models.incident_entry_sanction_item import IncidentEntrySanctionItem
from starrez_client.models.incident_entry_violation_item import IncidentEntryViolationItem
from starrez_client.models.incident_finding_item import IncidentFindingItem
from starrez_client.models.incident_involvement_item import IncidentInvolvementItem
from starrez_client.models.incident_item import IncidentItem
from starrez_client.models.incident_note_item import IncidentNoteItem
from starrez_client.models.incident_plea_item import IncidentPleaItem
from starrez_client.models.incident_sanction_sub_type_item import IncidentSanctionSubTypeItem
from starrez_client.models.incident_sanction_type_item import IncidentSanctionTypeItem
from starrez_client.models.incident_severity_item import IncidentSeverityItem
from starrez_client.models.incident_status_item import IncidentStatusItem
from starrez_client.models.incident_sub_type_item import IncidentSubTypeItem
from starrez_client.models.incident_type_item import IncidentTypeItem
from starrez_client.models.incident_violation_item import IncidentViolationItem
from starrez_client.models.inspection_run_template_item import InspectionRunTemplateItem
from starrez_client.models.interface_application_item import InterfaceApplicationItem
from starrez_client.models.interface_item import InterfaceItem
from starrez_client.models.interface_subscribe_item import InterfaceSubscribeItem
from starrez_client.models.invoice_item import InvoiceItem
from starrez_client.models.log_activity_item import LogActivityItem
from starrez_client.models.log_add_in_item import LogAddInItem
from starrez_client.models.log_interface_item import LogInterfaceItem
from starrez_client.models.log_metric_item import LogMetricItem
from starrez_client.models.lookup_item import LookupItem
from starrez_client.models.lookup_text_item import LookupTextItem
from starrez_client.models.mail_merge_item import MailMergeItem
from starrez_client.models.meal_plan_detail_item import MealPlanDetailItem
from starrez_client.models.meal_plan_dining_hall_item import MealPlanDiningHallItem
from starrez_client.models.meal_plan_free_item import MealPlanFreeItem
from starrez_client.models.meal_plan_item import MealPlanItem
from starrez_client.models.meal_plan_session_item import MealPlanSessionItem
from starrez_client.models.meal_pricing_item import MealPricingItem
from starrez_client.models.membership_type_item import MembershipTypeItem
from starrez_client.models.message_action_item import MessageActionItem
from starrez_client.models.message_item import MessageItem
from starrez_client.models.message_subscriber_item import MessageSubscriberItem
from starrez_client.models.message_subscription_item import MessageSubscriptionItem
from starrez_client.models.message_subscription_settings_item import MessageSubscriptionSettingsItem
from starrez_client.models.nationality_item import NationalityItem
from starrez_client.models.note_type_item import NoteTypeItem
from starrez_client.models.parcel_type_item import ParcelTypeItem
from starrez_client.models.payment_item import PaymentItem
from starrez_client.models.payment_type_item import PaymentTypeItem
from starrez_client.models.phone_charge_type_call_type_item import PhoneChargeTypeCallTypeItem
from starrez_client.models.phone_charge_type_item import PhoneChargeTypeItem
from starrez_client.models.portal_action_item import PortalActionItem
from starrez_client.models.portal_activity_item import PortalActivityItem
from starrez_client.models.portal_choice_item import PortalChoiceItem
from starrez_client.models.portal_page_action_item import PortalPageActionItem
from starrez_client.models.portal_page_item import PortalPageItem
from starrez_client.models.portal_page_widget_item import PortalPageWidgetItem
from starrez_client.models.portal_process_item import PortalProcessItem
from starrez_client.models.portal_rule_item import PortalRuleItem
from starrez_client.models.portal_rule_link_item import PortalRuleLinkItem
from starrez_client.models.portal_setting_item import PortalSettingItem
from starrez_client.models.portal_site_item import PortalSiteItem
from starrez_client.models.portal_step_item import PortalStepItem
from starrez_client.models.portal_step_link_item import PortalStepLinkItem
from starrez_client.models.portal_theme_item import PortalThemeItem
from starrez_client.models.portal_user_hold_item import PortalUserHoldItem
from starrez_client.models.portal_user_signature_item import PortalUserSignatureItem
from starrez_client.models.portal_user_token_item import PortalUserTokenItem
from starrez_client.models.preference_item import PreferenceItem
from starrez_client.models.priority_item import PriorityItem
from starrez_client.models.process_item import ProcessItem
from starrez_client.models.profile_item_item import ProfileItemItem
from starrez_client.models.profile_type_item import ProfileTypeItem
from starrez_client.models.program_custom_field_item import ProgramCustomFieldItem
from starrez_client.models.program_entry_item import ProgramEntryItem
from starrez_client.models.program_evaluation_type_item import ProgramEvaluationTypeItem
from starrez_client.models.program_item import ProgramItem
from starrez_client.models.program_note_item import ProgramNoteItem
from starrez_client.models.program_sub_type_item import ProgramSubTypeItem
from starrez_client.models.program_type_item import ProgramTypeItem
from starrez_client.models.promo_code_item import PromoCodeItem
from starrez_client.models.promo_code_record_item import PromoCodeRecordItem
from starrez_client.models.promo_code_usage_item import PromoCodeUsageItem
from starrez_client.models.record_attachment_item import RecordAttachmentItem
from starrez_client.models.refund_request_batch_configuration_item import RefundRequestBatchConfigurationItem
from starrez_client.models.refund_request_batch_configuration_item_item import RefundRequestBatchConfigurationItemItem
from starrez_client.models.refund_request_break_up_item import RefundRequestBreakUpItem
from starrez_client.models.refund_request_configuration_break_up_item import RefundRequestConfigurationBreakUpItem
from starrez_client.models.refund_request_configuration_item import RefundRequestConfigurationItem
from starrez_client.models.refund_request_item import RefundRequestItem
from starrez_client.models.region_of_birth_item import RegionOfBirthItem
from starrez_client.models.report_detail_item import ReportDetailItem
from starrez_client.models.report_item import ReportItem
from starrez_client.models.report_permission_item import ReportPermissionItem
from starrez_client.models.report_schedule_item import ReportScheduleItem
from starrez_client.models.report_setting_item import ReportSettingItem
from starrez_client.models.resource_booking_item import ResourceBookingItem
from starrez_client.models.resource_item import ResourceItem
from starrez_client.models.resource_type_item import ResourceTypeItem
from starrez_client.models.response_status_item import ResponseStatusItem
from starrez_client.models.room_attribute_item import RoomAttributeItem
from starrez_client.models.room_base_gender_item import RoomBaseGenderItem
from starrez_client.models.room_base_item import RoomBaseItem
from starrez_client.models.room_classification_item import RoomClassificationItem
from starrez_client.models.room_configuration_attribute_item import RoomConfigurationAttributeItem
from starrez_client.models.room_configuration_classification_item import RoomConfigurationClassificationItem
from starrez_client.models.room_configuration_item import RoomConfigurationItem
from starrez_client.models.room_configuration_profile_item import RoomConfigurationProfileItem
from starrez_client.models.room_configuration_room_sort_item import RoomConfigurationRoomSortItem
from starrez_client.models.room_configuration_term_type_item import RoomConfigurationTermTypeItem
from starrez_client.models.room_item import RoomItem
from starrez_client.models.room_location_area_item import RoomLocationAreaItem
from starrez_client.models.room_location_classification_item import RoomLocationClassificationItem
from starrez_client.models.room_location_floor_suite_item import RoomLocationFloorSuiteItem
from starrez_client.models.room_location_item import RoomLocationItem
from starrez_client.models.room_location_section_item import RoomLocationSectionItem
from starrez_client.models.room_manager_item import RoomManagerItem
from starrez_client.models.room_preference_item import RoomPreferenceItem
from starrez_client.models.room_profile_item import RoomProfileItem
from starrez_client.models.room_rate_charge_item import RoomRateChargeItem
from starrez_client.models.room_rate_item import RoomRateItem
from starrez_client.models.room_rate_room_type_location_item import RoomRateRoomTypeLocationItem
from starrez_client.models.room_rate_session_item import RoomRateSessionItem
from starrez_client.models.room_sort_configuration_item import RoomSortConfigurationItem
from starrez_client.models.room_sort_profile_item import RoomSortProfileItem
from starrez_client.models.room_sort_profile_item_item import RoomSortProfileItemItem
from starrez_client.models.room_space_closed_item import RoomSpaceClosedItem
from starrez_client.models.room_space_detail_item import RoomSpaceDetailItem
from starrez_client.models.room_space_inventory_condition_item import RoomSpaceInventoryConditionItem
from starrez_client.models.room_space_inventory_inspection_item import RoomSpaceInventoryInspectionItem
from starrez_client.models.room_space_inventory_inspection_item_item import RoomSpaceInventoryInspectionItemItem
from starrez_client.models.room_space_inventory_inspection_run_item import RoomSpaceInventoryInspectionRunItem
from starrez_client.models.room_space_inventory_item import RoomSpaceInventoryItem
from starrez_client.models.room_space_inventory_status_item import RoomSpaceInventoryStatusItem
from starrez_client.models.room_space_inventory_type_item import RoomSpaceInventoryTypeItem
from starrez_client.models.room_space_item import RoomSpaceItem
from starrez_client.models.room_space_key_booking_item import RoomSpaceKeyBookingItem
from starrez_client.models.room_space_key_item import RoomSpaceKeyItem
from starrez_client.models.room_space_key_type_item import RoomSpaceKeyTypeItem
from starrez_client.models.room_space_maintenance_category_item import RoomSpaceMaintenanceCategoryItem
from starrez_client.models.room_space_maintenance_item import RoomSpaceMaintenanceItem
from starrez_client.models.room_space_maintenance_item_item import RoomSpaceMaintenanceItemItem
from starrez_client.models.room_space_maintenance_job_action_item import RoomSpaceMaintenanceJobActionItem
from starrez_client.models.room_space_maintenance_materials_item import RoomSpaceMaintenanceMaterialsItem
from starrez_client.models.room_space_swap_item import RoomSpaceSwapItem
from starrez_client.models.room_space_swap_preference_item import RoomSpaceSwapPreferenceItem
from starrez_client.models.room_term_type_item import RoomTermTypeItem
from starrez_client.models.room_type_capacity_item import RoomTypeCapacityItem
from starrez_client.models.room_type_item import RoomTypeItem
from starrez_client.models.roommate_group_item import RoommateGroupItem
from starrez_client.models.roommate_group_mandatory_profile_item import RoommateGroupMandatoryProfileItem
from starrez_client.models.roommate_group_request_item import RoommateGroupRequestItem
from starrez_client.models.sdas_charge_rate_item import SDASChargeRateItem
from starrez_client.models.sdas_data_item import SDASDataItem
from starrez_client.models.saved_list_item import SavedListItem
from starrez_client.models.saved_list_item_item import SavedListItemItem
from starrez_client.models.school_item import SchoolItem
from starrez_client.models.setting_item import SettingItem
from starrez_client.models.shipping_type_item import ShippingTypeItem
from starrez_client.models.shopping_cart_item_hold_item import ShoppingCartItemHoldItem
from starrez_client.models.shopping_cart_item_item import ShoppingCartItemItem
from starrez_client.models.staff_item import StaffItem
from starrez_client.models.survey_item import SurveyItem
from starrez_client.models.survey_question_item import SurveyQuestionItem
from starrez_client.models.survey_question_response_item import SurveyQuestionResponseItem
from starrez_client.models.survey_response_item import SurveyResponseItem
from starrez_client.models.survey_type_item import SurveyTypeItem
from starrez_client.models.system_activity_item import SystemActivityItem
from starrez_client.models.table_item import TableItem
from starrez_client.models.task_item import TaskItem
from starrez_client.models.task_runner_history_item import TaskRunnerHistoryItem
from starrez_client.models.task_status_item import TaskStatusItem
from starrez_client.models.task_template_item import TaskTemplateItem
from starrez_client.models.task_template_item_item import TaskTemplateItemItem
from starrez_client.models.task_type_item import TaskTypeItem
from starrez_client.models.template_item import TemplateItem
from starrez_client.models.template_permission_item import TemplatePermissionItem
from starrez_client.models.term_item import TermItem
from starrez_client.models.term_rule_item import TermRuleItem
from starrez_client.models.term_session_free_item import TermSessionFreeItem
from starrez_client.models.term_session_item import TermSessionItem
from starrez_client.models.term_type_item import TermTypeItem
from starrez_client.models.time_slot_item import TimeSlotItem
from starrez_client.models.title_item import TitleItem
from starrez_client.models.total_item import TotalItem
from starrez_client.models.transaction_dispute_custom_field_item import TransactionDisputeCustomFieldItem
from starrez_client.models.transaction_dispute_item import TransactionDisputeItem
from starrez_client.models.transaction_dispute_item_item import TransactionDisputeItemItem
from starrez_client.models.transaction_item import TransactionItem
from starrez_client.models.transaction_link_item import TransactionLinkItem
from starrez_client.models.transaction_link_item_item import TransactionLinkItemItem
from starrez_client.models.transaction_tag_item import TransactionTagItem
from starrez_client.models.transaction_template_item import TransactionTemplateItem
from starrez_client.models.transaction_template_item_item import TransactionTemplateItemItem
from starrez_client.models.vm_data_item import VMDataItem
from starrez_client.models.vm_group_extension_item import VMGroupExtensionItem
from starrez_client.models.vm_group_item import VMGroupItem
from starrez_client.models.vm_group_mail_box_item import VMGroupMailBoxItem
from starrez_client.models.vm_group_message_item import VMGroupMessageItem
from starrez_client.models.vm_line_usage_item import VMLineUsageItem
from starrez_client.models.vmmci_item import VMMCIItem
from starrez_client.models.vm_mail_box_item import VMMailBoxItem
from starrez_client.models.vm_mail_box_type_item import VMMailBoxTypeItem
from starrez_client.models.vm_message_item import VMMessageItem
from starrez_client.models.vm_message_lamp_item import VMMessageLampItem
from starrez_client.models.visitor_item import VisitorItem
from starrez_client.models.visitor_type_item import VisitorTypeItem
from starrez_client.models.wait_list_classification_item import WaitListClassificationItem
from starrez_client.models.wait_list_entry_application_item import WaitListEntryApplicationItem
from starrez_client.models.wait_list_item import WaitListItem
from starrez_client.models.wait_list_profile_item import WaitListProfileItem
from starrez_client.models.wait_list_room_space_item import WaitListRoomSpaceItem
from starrez_client.models.web_block_item import WebBlockItem
from starrez_client.models.web_control_item import WebControlItem
from starrez_client.models.web_email_text_item import WebEmailTextItem
from starrez_client.models.web_field_item import WebFieldItem
from starrez_client.models.web_log_item import WebLogItem
from starrez_client.models.web_menu_classification_item import WebMenuClassificationItem
from starrez_client.models.web_menu_item import WebMenuItem
from starrez_client.models.web_module_item import WebModuleItem
from starrez_client.models.web_payment_item import WebPaymentItem
from starrez_client.models.web_rule_item import WebRuleItem
from starrez_client.models.web_rule_link_item import WebRuleLinkItem
from starrez_client.models.web_section_item import WebSectionItem
from starrez_client.models.web_section_text_block_item import WebSectionTextBlockItem
from starrez_client.models.web_setting_item import WebSettingItem
from starrez_client.models.web_site_item import WebSiteItem
from starrez_client.models.web_transaction_item import WebTransactionItem
from starrez_client.models.workflow_history_item import WorkflowHistoryItem
from starrez_client.models.workflow_item import WorkflowItem
from starrez_client.models.workflow_permission_item import WorkflowPermissionItem
from starrez_client.models.workflow_step_item import WorkflowStepItem
from starrez_client.models.workflow_step_permission_item import WorkflowStepPermissionItem
from starrez_client.models.zip_post_code_item import ZipPostCodeItem