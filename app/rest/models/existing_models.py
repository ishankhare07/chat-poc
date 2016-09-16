# coding: utf-8
from sqlalchemy import BINARY, Column, DateTime, Enum, Integer, String, Table, Text, text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
metadata = Base.metadata


class AdminUser(Base):
    __tablename__ = 'admin_users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    email = Column(String(255, 'utf8_unicode_ci'), nullable=False, unique=True)
    password = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    remember_token = Column(String(100, 'utf8_unicode_ci'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class AgriEntrepreneurBusinessDevelopment(Base):
    __tablename__ = 'agri_entrepreneur_business_development'

    id = Column(Integer, primary_key=True)
    agri_entrepreneur_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer)
    area_of_specialization = Column(String(128))
    description = Column(Text)
    trade_terms = Column(String(128))
    profile_details = Column(String(128))
    image = Column(String(255), nullable=False)
    is_active = Column(Integer, nullable=False)


class AssortedProduct(Base):
    __tablename__ = 'assorted_product'

    id = Column(Integer, primary_key=True)
    parent_product_type = Column(String(255), nullable=False)
    product_type = Column(String(220), nullable=False)
    subcategory = Column(String(255), nullable=False)
    product_name = Column(String(220), nullable=False)
    quantity = Column(String(220), nullable=False)
    quality = Column(String(220), nullable=False)
    delivery_area = Column(String(220), nullable=False)
    price = Column(String(220), nullable=False)
    user_id = Column(Integer, nullable=False)
    average_lead_time = Column(String(220), nullable=False)
    payment_terms = Column(String(220), nullable=False)
    majority_packaging = Column(String(220), nullable=False)
    service_id = Column(Integer, nullable=False)
    edit_time = Column(String(255), nullable=False)


class Banner(Base):
    __tablename__ = 'banner'

    banner_id = Column(Integer, primary_key=True)
    image_name = Column(String(50), nullable=False)
    title = Column(String(20), nullable=False)
    status = Column(Integer, nullable=False)
    type = Column(String(10), nullable=False)


class ColdStorageSpace(Base):
    __tablename__ = 'cold_storage_space'

    id = Column(Integer, primary_key=True)
    cold_storage_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer)
    area_of_specialization = Column(String(128))
    location_address = Column(String(128))
    number_of_chambers = Column(String(128))
    per_chamber_capacity = Column(String(128))
    total_capacity = Column(String(128))
    space_capacity = Column(String(128))
    availability_period = Column(String(128))
    technology_used = Column(String(128))
    specific_items = Column(String(128))
    description = Column(Text)
    trade_terms = Column(String(128))
    profile_details = Column(String(128))
    image = Column(String(255), nullable=False)
    is_active = Column(Integer, nullable=False)


class Consultancy(Base):
    __tablename__ = 'consultancy'

    id = Column(Integer, primary_key=True)
    consultancy_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer, nullable=False)
    area_of_expertise = Column(String(200), nullable=False)
    differentation_factor = Column(Text, nullable=False)
    client_name = Column(String(100), nullable=False)
    year = Column(String(200), nullable=False)
    name_of_assignment = Column(String(200), nullable=False)
    location = Column(String(200), nullable=False)
    project_budget = Column(String(200), nullable=False)
    no_of_projects = Column(Integer, nullable=False)
    project_name_1 = Column(String(200), nullable=False)
    project_name_2 = Column(String(255), nullable=False)
    project_name_3 = Column(String(255), nullable=False)
    project_name_4 = Column(String(255), nullable=False)
    position_held = Column(String(200), nullable=False)
    contribution_and_impact_description = Column(Text, nullable=False)
    total_experiance_year = Column(Integer, nullable=False)
    highest_qualification = Column(String(200), nullable=False)
    language_skill = Column(String(200), nullable=False)
    employment_details = Column(String(200), nullable=False)
    professional_membership = Column(String(200), nullable=False)
    contact_person_name = Column(String(200), nullable=False)
    contact_person_phone_no = Column(Integer, nullable=False)
    commercial_terms = Column(Text, nullable=False)
    image = Column(String(255), nullable=False)
    total_experiance_month = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)


class DehydratedProduct(Base):
    __tablename__ = 'dehydrated_product'

    id = Column(Integer, primary_key=True)
    parent_product_type = Column(String(255), nullable=False)
    dehydrated_sub_category = Column(String(255), nullable=False)
    product_type = Column(String(220), nullable=False)
    subcategory = Column(String(255), nullable=False)
    product_name = Column(String(220), nullable=False)
    quality = Column(String(220), nullable=False)
    price = Column(String(220), nullable=False)
    user_id = Column(Integer, nullable=False)
    payment_terms = Column(String(220), nullable=False)
    majority_packaging = Column(String(220), nullable=False)
    edit_time = Column(Integer, nullable=False)


class DistributionAndLogisticsService(Base):
    __tablename__ = 'distribution_and_logistics_services'

    id = Column(Integer, primary_key=True)
    distribution_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer)
    area_of_expertise = Column(String(128))
    number_of_vehicles = Column(String(128))
    type_of_vehicles = Column(String(128))
    area = Column(String(128))
    cold_chain_transport_and_delivery_service = Column(String(128))
    description_and_specifications = Column(Text)
    fleet_size = Column(String(128))
    permit = Column(String(128))
    area_speciality = Column(String(128))
    product_speciality = Column(String(128))
    refrence_customer_name_1 = Column(String(128))
    refrence_customer_phone_1 = Column(String(128))
    refrence_customer_name_2 = Column(String(128))
    refrence_customer_phone_2 = Column(String(128))
    refrence_customer_name_3 = Column(String(128))
    refrence_customer_phone_3 = Column(String(128))
    refrence_customer_name_4 = Column(String(128))
    refrence_customer_phone_4 = Column(String(128))
    profile_details = Column(Text)
    image = Column(String(255), nullable=False)
    is_active = Column(Integer, nullable=False)


class Employe(Base):
    __tablename__ = 'employe'

    id = Column(Integer, primary_key=True)
    organisation_name = Column(String(255), nullable=False)
    join_date = Column(String(255), nullable=False)
    left_date = Column(String(255), nullable=False)
    position_held = Column(String(255), nullable=False)
    service_id = Column(Integer, nullable=False)


class EnquiryDatum(Base):
    __tablename__ = 'enquiry_data'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, nullable=False)
    buyer_id = Column(Integer, nullable=False)
    name = Column(String(30), nullable=False)
    last_name = Column(String(220), nullable=False)
    contact = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    product_name = Column(String(30), nullable=False)
    product_type = Column(String(30), nullable=False)
    mini_quantity = Column(Integer, nullable=False)
    unit = Column(String(10), nullable=False)
    date = Column(String(15), nullable=False)
    msg = Column(Text, nullable=False)
    file_name = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    date_time = Column(String(255), nullable=False)
    customer_type = Column(String(220), nullable=False)
    location = Column(String(220), nullable=False)
    price = Column(String(220), nullable=False)
    quality = Column(String(50), nullable=False)
    enquirer_type = Column(String(50), nullable=False)
    frequency = Column(String(50), nullable=False)
    additional_comments = Column(String(255), nullable=False)
    variety = Column(String(50), nullable=False)
    packing = Column(String(50), nullable=False)
    payment = Column(String(50), nullable=False)
    reading_status = Column(Integer, nullable=False)
    enquiry_url = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    replies = relationship("Reply", backref="enquiry_data")

class Reply(Base):
    __tablename__ = 'replies'

    id = Column(Integer, primary_key=True)
    message = Column(Text, nullable=False)
    enquiry_id = Column(Integer, ForeignKey('enquiry_data.id'))
    from_user = Column(Integer, ForeignKey('user.user_id'))
    to_user = Column(Integer, ForeignKey('user.user_id'))

    def __repr__(self):
        return '<Reply: {0}, msg: {1}>'.format(self.id, self.message)

class EnquiryReplyDatum(Base):
    __tablename__ = 'enquiry_reply_data'

    id = Column(Integer, primary_key=True)
    enquiry_data_id = Column(Integer, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    name = Column(String(30), nullable=False)
    contact = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    location = Column(String(220), nullable=False)
    product_name = Column(String(30), nullable=False)
    product_type = Column(String(30), nullable=False)
    mini_quantity = Column(Integer, nullable=False)
    unit = Column(String(10), nullable=False)
    date = Column(String(15), nullable=False)
    msg = Column(Text, nullable=False)
    file_name = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    enquiry_url = Column(Text, nullable=False)


class ExportImportFacilitator(Base):
    __tablename__ = 'export_import_facilitator'

    id = Column(Integer, primary_key=True)
    export_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer)
    area_of_specialization = Column(String(128))
    registration_with_orgination = Column(String(128))
    applied_by_country = Column(String(128))
    items_handed = Column(String(128))
    export_trading_zones = Column(String(128))
    trade_terms = Column(Text)
    profile_details = Column(Text)
    image = Column(String(255), nullable=False)
    is_active = Column(Integer, nullable=False)


class FreshcutProduct(Base):
    __tablename__ = 'freshcut_product'

    id = Column(Integer, primary_key=True)
    parent_product_type = Column(String(255), nullable=False)
    fresh_sub_category = Column(String(255), nullable=False)
    product_type = Column(String(220), nullable=False)
    subcategory = Column(String(255), nullable=False)
    product_name = Column(String(220), nullable=False)
    quality = Column(String(220), nullable=False)
    price = Column(String(220), nullable=False)
    user_id = Column(Integer, nullable=False)
    payment_terms = Column(String(220), nullable=False)
    majority_packaging = Column(String(220), nullable=False)
    edit_time = Column(Integer, nullable=False)


class HitechApplicationsTechnology(Base):
    __tablename__ = 'hitech_applications_technology'

    id = Column(Integer, primary_key=True)
    hitech_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer)
    application_type = Column(String(128))
    application_description = Column(Text)
    application_store_link = Column(String(128))
    application_type_free = Column(String(10))
    number_of_downloads = Column(String(128))
    user_rating = Column(String(128))
    profile_details = Column(String(128))
    image = Column(String(255), nullable=False)
    is_active = Column(Integer, nullable=False)


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    referance_id = Column(Integer, nullable=False)
    image = Column(String(100), nullable=False)
    type = Column(String(20), nullable=False)


class LeadsConsume(Base):
    __tablename__ = 'leads_consume'

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, nullable=False)
    enquiry_id = Column(Integer, nullable=False)
    lead_consume_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    assigned_by_name = Column(String(50), nullable=False)
    assigned_by_id = Column(Integer, nullable=False)
    comments = Column(Text, nullable=False)


class LeadsTransaction(Base):
    __tablename__ = 'leads_transactions'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, nullable=False)
    added_by_id = Column(Integer)
    added_by_name = Column(String(100), nullable=False)
    leads_count = Column(Integer, nullable=False)
    added_date = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    lead_type = Column(String(30), nullable=False)
    comments = Column(Text, nullable=False)


class LiaisonForGovtFinancialSchemesAndSubsidy(Base):
    __tablename__ = 'liaison_for_govt_financial_schemes_and_subsidies'

    id = Column(Integer, primary_key=True)
    govt_financial_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer, nullable=False)
    area_of_expertise = Column(String(200), nullable=False)
    specialist_organization = Column(String(200), nullable=False)
    service_provided = Column(String(200), nullable=False)
    description = Column(String(200), nullable=False)
    trade_terms = Column(String(200), nullable=False)
    profile_details = Column(String(200), nullable=False)
    image = Column(String(255), nullable=False)
    is_active = Column(Integer, nullable=False)


class MachineryAndEquipmentSupplier(Base):
    __tablename__ = 'machinery_and_equipment_supplier'

    id = Column(Integer, primary_key=True)
    machinery_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer)
    categories = Column(String(128))
    types_of_storage = Column(String(128))
    product_description = Column(Text)
    product_usage = Column(Text)
    description = Column(String(128))
    service_pre_after_sale_services = Column(String(128))
    delivery_area = Column(String(128))
    client_name = Column(Text)
    year = Column(Text)
    location = Column(Text)
    number_of_plants_sold = Column(String(128))
    number_of_customer_service = Column(String(128))
    important_customer_1 = Column(String(128))
    important_customer_2 = Column(String(128))
    important_customer_3 = Column(String(128))
    trade_terms = Column(Text)
    profile_details = Column(Text)
    image = Column(String(200), nullable=False)
    is_active = Column(Integer, nullable=False)


t_migrations = Table(
    'migrations', metadata,
    Column('migration', String(255, 'utf8_unicode_ci'), nullable=False),
    Column('batch', Integer, nullable=False)
)


class NewBuyerEnquiry(Base):
    __tablename__ = 'new_buyer_enquiries'

    id = Column(Integer, primary_key=True)
    script_runtime = Column(DateTime, nullable=False)
    enquiry_count = Column(Integer)


class NewSellerEnquiry(Base):
    __tablename__ = 'new_seller_enquiries'

    id = Column(Integer, primary_key=True)
    script_runtime = Column(DateTime, nullable=False)
    enquiry_count = Column(Integer, nullable=False)


class OrderSupplier(Base):
    __tablename__ = 'order_supplier'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    fob_price = Column(String(255), nullable=False)
    service_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    subtype = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    sub_category = Column(String(255), nullable=False)
    name2 = Column(String(100), nullable=False)
    varity = Column(String(100), nullable=False)
    grade = Column(String(200), nullable=False)
    size = Column(String(10), nullable=False)
    colure_in = Column(String(10), nullable=False)
    other_speciality = Column(String(30), nullable=False)
    wastes_1 = Column(String(255), nullable=False)
    wastes_2 = Column(String(256), nullable=False)
    wastes_3 = Column(String(256), nullable=False)
    wastes_4 = Column(String(256), nullable=False)
    packed_in = Column(String(100), nullable=False)
    pack_size = Column(String(50), nullable=False)
    minimum_quantity = Column(Integer, nullable=False)
    unit = Column(String(20), nullable=False)
    fresh_cut = Column(String(2), nullable=False)
    colour = Column(String(255), nullable=False)
    delivery_start_date = Column(String(25), nullable=False)
    delivery_end_date = Column(String(25), nullable=False)
    supply_ability = Column(Integer, nullable=False)
    shelf_life_day = Column(Integer, nullable=False)
    possible_destination = Column(String(100), nullable=False)
    shipping_mode = Column(String(10), nullable=False)
    payment_mode = Column(String(255), nullable=False)
    average_lead_time = Column(Integer, nullable=False)
    lead_time_unit = Column(String(256), nullable=False)
    terms_of_services = Column(Text, nullable=False)
    product_description = Column(Text, nullable=False)
    master_pack_type = Column(String(10), nullable=False)
    master_pack_quantity = Column(Integer, nullable=False)
    advance_payment = Column(Integer, nullable=False)
    image = Column(String(255), nullable=False)
    qty_per_pack = Column(String(10), nullable=False)
    label_marking = Column(String(100), nullable=False)
    moq = Column(String(100), nullable=False)
    shipping_countries = Column(String(100), nullable=False)
    bags = Column(String(50), nullable=False)
    other_bag = Column(String(100), nullable=False)
    is_active = Column(Integer, nullable=False)


class OrderSupplierOld(Base):
    __tablename__ = 'order_supplier_old'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    fob_price = Column(String(255), nullable=False)
    service_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    subtype = Column(String(255), nullable=False)
    name2 = Column(String(100), nullable=False)
    varity = Column(String(100), nullable=False)
    grade = Column(String(200), nullable=False)
    size = Column(String(10), nullable=False)
    colure_in = Column(String(10), nullable=False)
    other_speciality = Column(String(30), nullable=False)
    wastes_1 = Column(String(255), nullable=False)
    wastes_2 = Column(String(256), nullable=False)
    wastes_3 = Column(String(256), nullable=False)
    wastes_4 = Column(String(256), nullable=False)
    packed_in = Column(String(100), nullable=False)
    pack_size = Column(String(50), nullable=False)
    minimum_quantity = Column(Integer, nullable=False)
    unit = Column(String(20), nullable=False)
    fresh_cut = Column(String(2), nullable=False)
    colour = Column(String(255), nullable=False)
    delivery_start_date = Column(String(25), nullable=False)
    delivery_end_date = Column(String(25), nullable=False)
    supply_ability = Column(Integer, nullable=False)
    shelf_life_day = Column(Integer, nullable=False)
    possible_destination = Column(String(100), nullable=False)
    shipping_mode = Column(String(10), nullable=False)
    payment_mode = Column(String(255), nullable=False)
    average_lead_time = Column(String(255), nullable=False)
    terms_of_services = Column(Text, nullable=False)
    product_description = Column(Text, nullable=False)
    master_pack_type = Column(String(10), nullable=False)
    master_pack_quantity = Column(Integer, nullable=False)
    advance_payment = Column(Integer, nullable=False)
    image = Column(String(255), nullable=False)
    qty_per_pack = Column(String(10), nullable=False)
    label_marking = Column(String(100), nullable=False)
    moq = Column(String(100), nullable=False)
    shipping_countries = Column(String(100), nullable=False)
    bags = Column(String(50), nullable=False)
    other_bag = Column(String(100), nullable=False)
    is_active = Column(Integer, nullable=False)


t_package_info = Table(
    'package_info', metadata,
    Column('package_id', Enum('1', '2', '3', '4'), nullable=False, unique=True),
    Column('package_name', String(20), nullable=False)
)


class PackagedProduct(Base):
    __tablename__ = 'packaged_product'

    id = Column(Integer, primary_key=True)
    parent_product_type = Column(String(255), nullable=False)
    product_type = Column(String(220), nullable=False)
    subcategory = Column(String(255), nullable=False)
    product_name = Column(String(220), nullable=False)
    quality = Column(String(220), nullable=False)
    price = Column(String(220), nullable=False)
    user_id = Column(Integer, nullable=False)
    payment_terms = Column(String(220), nullable=False)
    majority_packaging = Column(String(220), nullable=False)
    edit_time = Column(Integer, nullable=False)


class Package(Base):
    __tablename__ = 'packages'

    id = Column(Integer, primary_key=True)
    package_id = Column(Enum('1', '2', '3', '4'), nullable=False)
    vendor_id = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    added_by = Column(Integer, nullable=False)


class PackagingOfFruitAndVegetablesProcessedProduct(Base):
    __tablename__ = 'packaging_of_fruit_and_vegetables_processed_products'

    id = Column(Integer, primary_key=True)
    packaging_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer)
    area_of_expertise = Column(String(128))
    material = Column(String(128))
    capacity = Column(String(128))
    dimension = Column(String(128))
    type = Column(String(128))
    specialization = Column(String(128))
    software_skills = Column(String(128))
    printing_service = Column(String(128))
    types_of_printing = Column(String(128))
    printing_on = Column(String(128))
    delivery_area = Column(String(128))
    supply_ability = Column(String(128))
    trade_terms = Column(String(128))
    profile_details = Column(Text)
    image = Column(String(255), nullable=False)
    others = Column(String(255), nullable=False)
    paper_board_type = Column(String(255), nullable=False)
    is_active = Column(Integer, nullable=False)


class Payment(Base):
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    request = Column(String(220), nullable=False)
    response = Column(String(220), nullable=False)
    status = Column(Integer, nullable=False)
    time = Column(Integer, nullable=False)


class ProductionOfFruitAndVegetable(Base):
    __tablename__ = 'production_of_fruit_and_vegetables'

    id = Column(Integer, primary_key=True)
    production_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer)
    area_of_expertise = Column(String(128))
    type_of_service = Column(String(128))
    description = Column(Text)
    trade_terms = Column(String(128))
    profile_details = Column(Text)
    image = Column(String(255), nullable=False)
    is_active = Column(Integer, nullable=False)


class QualityControlAndAssurance(Base):
    __tablename__ = 'quality_control_and_assurance'

    id = Column(Integer, primary_key=True)
    quality_name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    service_id = Column(Integer)
    area_of_specialization = Column(String(128))
    certifications = Column(String(128))
    differentation_factor = Column(Text)
    client = Column(String(128))
    year = Column(String(200), nullable=False)
    name_of_assignment = Column(String(128))
    location = Column(String(128))
    project_budget = Column(String(128))
    project_features_1 = Column(String(128))
    project_features_2 = Column(String(128))
    project_features_3 = Column(String(128))
    project_features_4 = Column(String(128))
    position_hold = Column(String(128))
    contribution_and_impact_description = Column(Text)
    contact_person = Column(String(128))
    contact_person_phone_no = Column(Integer)
    commercial_terms = Column(Text)
    image = Column(String(255), nullable=False)
    is_active = Column(Integer, nullable=False)


class SeedsProduct(Base):
    __tablename__ = 'seeds_product'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    product_name = Column(String(255), nullable=False)
    varity = Column(String(100), nullable=False)
    germination_per = Column(String(20), nullable=False)
    purity_per = Column(String(20), nullable=False)
    pack_size = Column(String(50), nullable=False)
    treated = Column(String(3), nullable=False)
    more_info = Column(Text, nullable=False)
    payment_mode = Column(String(255), nullable=False)
    delivery_start_date = Column(String(25), nullable=False)
    delivery_end_date = Column(String(25), nullable=False)
    packed_in = Column(String(100), nullable=False)
    possible_destination = Column(String(100), nullable=False)
    fob_price = Column(String(255), nullable=False)
    maturity_days = Column(String(255), nullable=False)
    season = Column(String(255), nullable=False)
    colour = Column(String(255), nullable=False)
    _yield = Column('yield', String(255), nullable=False)
    product_description = Column(Text, nullable=False)
    image = Column(String(255), nullable=False)
    is_active = Column(Integer, nullable=False)


class Service(Base):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    type = Column(String(200), nullable=False)
    user_id = Column(Integer, nullable=False)
    creation_date = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    service_type = Column(String(20), nullable=False)
    edit_time = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)


class ServiceProvider(Base):
    __tablename__ = 'service_provider'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    organisation_name = Column(String(100), nullable=False)
    designation = Column(String(100), nullable=False)
    service_offer = Column(String(100), nullable=False)
    refernces = Column(String(100), nullable=False)
    trade_terms = Column(Text, nullable=False)
    client_name = Column(String(100), nullable=False)
    business_type = Column(String(255), nullable=False)
    response_rate = Column(String(255), nullable=False)
    registered_since = Column(Integer, nullable=False)
    year_estabilished = Column(Integer, nullable=False)
    reviews = Column(Integer, nullable=False)
    no_of_employees = Column(Integer, nullable=False)
    main_product = Column(String(255), nullable=False)
    average_lead_time = Column(Integer, nullable=False)
    total_production_volume = Column(Integer, nullable=False)
    factory_warehouse_size = Column(Integer, nullable=False)
    factory_warehouse_location = Column(String(255), nullable=False)


class ServiceProviderProductmeta(Base):
    __tablename__ = 'service_provider_productmeta'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    service_type = Column(String(255), nullable=False)
    key_type = Column(String(255), nullable=False)
    value = Column(String(255), nullable=False)


class ShopInShop(Base):
    __tablename__ = 'shop_in_shop'

    id = Column(Integer, primary_key=True)
    parent_product_type = Column(String(255), nullable=False)
    product_type = Column(String(220), nullable=False)
    subcategory = Column(String(255), nullable=False)
    product_name = Column(String(220), nullable=False)
    quantity = Column(String(220), nullable=False)
    quality = Column(String(220), nullable=False)
    delivery_area = Column(String(220), nullable=False)
    price = Column(String(220), nullable=False)
    user_id = Column(Integer, nullable=False)
    average_lead_time = Column(String(220), nullable=False)
    payment_terms = Column(String(220), nullable=False)
    majority_packaging = Column(String(220), nullable=False)
    other_bag = Column(String(255), nullable=False)
    service_id = Column(Integer, nullable=False)
    edit_time = Column(Integer, nullable=False)


class TblMigration(Base):
    __tablename__ = 'tbl_migration'

    version = Column(String(255), primary_key=True)
    apply_time = Column(Integer)


class ThaiFruitsProduct(Base):
    __tablename__ = 'thai_fruits_product'

    id = Column(Integer, primary_key=True)
    parent_product_type = Column(String(255), nullable=False)
    product_type = Column(String(220), nullable=False)
    subcategory = Column(String(255), nullable=False)
    product_name = Column(String(220), nullable=False)
    quantity = Column(String(220), nullable=False)
    quality = Column(String(220), nullable=False)
    delivery_area = Column(String(220), nullable=False)
    price = Column(String(220), nullable=False)
    user_id = Column(Integer, nullable=False)
    average_lead_time = Column(String(220), nullable=False)
    payment_terms = Column(String(220), nullable=False)
    majority_packaging = Column(String(220), nullable=False)
    other_bag = Column(String(255), nullable=False)
    service_id = Column(Integer, nullable=False)
    edit_time = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    phone_no = Column(String(15), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    pin_no = Column(Integer, nullable=False)
    type = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Integer, nullable=False)
    role = Column(String(40), nullable=False)
    creation_date = Column(Integer, nullable=False)
    edit_date = Column(Integer, nullable=False)
    country = Column(String(255), nullable=False)
    district = Column(String(255), nullable=False)
    ip = Column(String(255), nullable=False)
    added_by = Column(Integer, nullable=False)
    is_phone_verified = Column(BINARY(1), nullable=False, server_default=text("'0'"))
    enquiries = relationship("EnquiryDatum", backref="user")


class UserOtp(Base):
    __tablename__ = 'user_otp'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    generated_otp = Column(String(100), nullable=False)
    generation_time = Column(DateTime, nullable=False)
    expiry_time = Column(DateTime, nullable=False)


class Variable(Base):
    __tablename__ = 'variable'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    value = Column(Integer, nullable=False)


class VendorLead(Base):
    __tablename__ = 'vendor_leads'

    supplier_id = Column(Integer, primary_key=True)
    total_added_leads = Column(Integer, nullable=False)
    total_consume_leads = Column(Integer, nullable=False)
    total_remaining_leads = Column(Integer, nullable=False)
