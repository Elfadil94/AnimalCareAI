PRAGMA foreign_keys = ON;

-- =====================================================
-- AnimalCare AI Database
-- Version 1.0
-- =====================================================

-- =====================================================
-- OWNERS
-- =====================================================

CREATE TABLE IF NOT EXISTS owners (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    first_name TEXT NOT NULL,

    last_name TEXT NOT NULL,

    email TEXT UNIQUE,

    phone TEXT,

    password_hash TEXT,

    country TEXT,

    city TEXT,

    address TEXT,

    language TEXT DEFAULT 'en',

    timezone TEXT DEFAULT 'UTC',

    profile_photo TEXT,

    is_active INTEGER DEFAULT 1,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

CREATE INDEX idx_owner_email
ON owners(email);

CREATE INDEX idx_owner_uuid
ON owners(uuid);

-- =====================================================
-- SPECIES
-- =====================================================

CREATE TABLE IF NOT EXISTS species (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    scientific_name TEXT,

    average_lifespan INTEGER,

    description TEXT

);

-- =====================================================
-- BREEDS
-- =====================================================

CREATE TABLE IF NOT EXISTS breeds (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    species_id INTEGER NOT NULL,

    name TEXT NOT NULL,

    origin_country TEXT,

    average_weight REAL,

    average_height REAL,

    description TEXT,

    FOREIGN KEY(species_id)
        REFERENCES species(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_breed_species
ON breeds(species_id);

-- =====================================================
-- PETS
-- =====================================================

CREATE TABLE IF NOT EXISTS pets (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    owner_id INTEGER NOT NULL,

    species_id INTEGER NOT NULL,

    breed_id INTEGER,

    animalcare_id TEXT UNIQUE,

    microchip_number TEXT UNIQUE,

    passport_number TEXT,

    insurance_number TEXT,

    name TEXT NOT NULL,

    gender TEXT CHECK(gender IN ('Male','Female','Unknown')),

    neutered INTEGER DEFAULT 0,

    hybrid INTEGER DEFAULT 0,

    blood_type TEXT,

    color TEXT,

    birth_date DATE,

    age REAL,

    weight REAL,

    height REAL,

    body_condition_score INTEGER,

    profile_photo TEXT,

    qr_code TEXT,

    notes TEXT,

    is_active INTEGER DEFAULT 1,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(owner_id)
        REFERENCES owners(id)
        ON DELETE CASCADE,

    FOREIGN KEY(species_id)
        REFERENCES species(id),

    FOREIGN KEY(breed_id)
        REFERENCES breeds(id)

);

CREATE INDEX idx_pet_owner
ON pets(owner_id);

CREATE INDEX idx_pet_species
ON pets(species_id);

CREATE INDEX idx_pet_breed
ON pets(breed_id);

CREATE INDEX idx_pet_uuid
ON pets(uuid);

CREATE INDEX idx_pet_microchip
ON pets(microchip_number);-- =====================================================
-- PET IMAGES
-- =====================================================

CREATE TABLE IF NOT EXISTS pet_images (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    image_type TEXT,

    image_path TEXT NOT NULL,

    ai_processed INTEGER DEFAULT 0,

    ai_summary TEXT,

    uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_pet_images_pet
ON pet_images(pet_id);

-- =====================================================
-- WEIGHT HISTORY
-- =====================================================

CREATE TABLE IF NOT EXISTS weight_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    weight REAL NOT NULL,

    body_condition_score INTEGER,

    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    notes TEXT,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_weight_pet
ON weight_history(pet_id);

-- =====================================================
-- BEHAVIOR TYPES
-- =====================================================

CREATE TABLE IF NOT EXISTS behavior_types (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT UNIQUE NOT NULL,

    description TEXT

);

-- =====================================================
-- BEHAVIOR LOGS
-- =====================================================

CREATE TABLE IF NOT EXISTS behavior_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    behavior_type_id INTEGER,

    mood TEXT,

    appetite TEXT,

    activity_level TEXT,

    sleep_quality TEXT,

    notes TEXT,

    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE,

    FOREIGN KEY(behavior_type_id)
        REFERENCES behavior_types(id)

);

CREATE INDEX idx_behavior_pet
ON behavior_logs(pet_id);

-- =====================================================
-- FOOD BRANDS
-- =====================================================

CREATE TABLE IF NOT EXISTS food_brands (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    manufacturer TEXT,

    website TEXT

);

-- =====================================================
-- FOOD TYPES
-- =====================================================

CREATE TABLE IF NOT EXISTS food_types (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE

);

-- =====================================================
-- NUTRITION LOGS
-- =====================================================

CREATE TABLE IF NOT EXISTS nutrition_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    food_brand_id INTEGER,

    food_type_id INTEGER,

    meal_name TEXT,

    quantity REAL,

    quantity_unit TEXT,

    meals_per_day INTEGER,

    water_intake_ml REAL,

    supplements TEXT,

    appetite TEXT,

    notes TEXT,

    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE,

    FOREIGN KEY(food_brand_id)
        REFERENCES food_brands(id),

    FOREIGN KEY(food_type_id)
        REFERENCES food_types(id)

);

CREATE INDEX idx_nutrition_pet
ON nutrition_logs(pet_id);-- =====================================================
-- MEDICAL HISTORY
-- =====================================================

CREATE TABLE IF NOT EXISTS medical_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    diagnosis_date DATE,

    condition_name TEXT NOT NULL,

    condition_type TEXT,

    severity TEXT,

    status TEXT,

    veterinarian TEXT,

    clinic TEXT,

    treatment TEXT,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_medical_pet
ON medical_history(pet_id);

-- =====================================================
-- ALLERGIES
-- =====================================================

CREATE TABLE IF NOT EXISTS allergies (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    allergen TEXT NOT NULL,

    allergy_type TEXT,

    severity TEXT,

    symptoms TEXT,

    treatment TEXT,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_allergy_pet
ON allergies(pet_id);

-- =====================================================
-- SURGERIES
-- =====================================================

CREATE TABLE IF NOT EXISTS surgeries (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    surgery_name TEXT NOT NULL,

    surgery_date DATE,

    veterinarian TEXT,

    clinic TEXT,

    anesthesia_type TEXT,

    outcome TEXT,

    recovery_days INTEGER,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_surgery_pet
ON surgeries(pet_id);

-- =====================================================
-- CHRONIC DISEASES
-- =====================================================

CREATE TABLE IF NOT EXISTS chronic_diseases (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    disease_name TEXT NOT NULL,

    diagnosed_date DATE,

    status TEXT,

    monitoring_frequency TEXT,

    medications TEXT,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_chronic_pet
ON chronic_diseases(pet_id);

-- =====================================================
-- MEDICAL VISITS
-- =====================================================

CREATE TABLE IF NOT EXISTS medical_visits (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    visit_date DATE,

    veterinarian TEXT,

    clinic TEXT,

    visit_reason TEXT,

    diagnosis TEXT,

    treatment TEXT,

    follow_up_date DATE,

    visit_cost REAL,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_visit_pet
ON medical_visits(pet_id);-- =====================================================
-- VACCINATIONS
-- =====================================================

CREATE TABLE IF NOT EXISTS vaccinations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    vaccine_name TEXT NOT NULL,

    manufacturer TEXT,

    batch_number TEXT,

    dose_number INTEGER,

    vaccination_date DATE,

    next_due_date DATE,

    veterinarian TEXT,

    clinic TEXT,

    certificate_path TEXT,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_vaccination_pet
ON vaccinations(pet_id);

CREATE INDEX idx_vaccination_due
ON vaccinations(next_due_date);

-- =====================================================
-- MEDICATIONS
-- =====================================================

CREATE TABLE IF NOT EXISTS medications (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    medication_name TEXT NOT NULL,

    dosage TEXT,

    frequency TEXT,

    route TEXT,

    start_date DATE,

    end_date DATE,

    prescribed_by TEXT,

    purpose TEXT,

    side_effects TEXT,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_medication_pet
ON medications(pet_id);

-- =====================================================
-- PRESCRIPTIONS
-- =====================================================

CREATE TABLE IF NOT EXISTS prescriptions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    prescription_date DATE,

    veterinarian TEXT,

    clinic TEXT,

    diagnosis TEXT,

    instructions TEXT,

    pdf_path TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_prescription_pet
ON prescriptions(pet_id);

-- =====================================================
-- PRESCRIPTION ITEMS
-- =====================================================

CREATE TABLE IF NOT EXISTS prescription_items (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    prescription_id INTEGER NOT NULL,

    medication_name TEXT NOT NULL,

    dosage TEXT,

    frequency TEXT,

    duration_days INTEGER,

    notes TEXT,

    FOREIGN KEY(prescription_id)
        REFERENCES prescriptions(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_prescription_items
ON prescription_items(prescription_id);

-- =====================================================
-- MEDICATION REMINDERS
-- =====================================================

CREATE TABLE IF NOT EXISTS medication_reminders (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    medication_id INTEGER NOT NULL,

    reminder_time DATETIME,

    repeat_pattern TEXT,

    enabled INTEGER DEFAULT 1,

    last_sent DATETIME,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE,

    FOREIGN KEY(medication_id)
        REFERENCES medications(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_medication_reminders_pet
ON medication_reminders(pet_id);

CREATE INDEX idx_medication_reminders_med
ON medication_reminders(medication_id);-- =====================================================
-- INSURANCE
-- =====================================================

CREATE TABLE IF NOT EXISTS insurance (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    provider_name TEXT NOT NULL,

    policy_number TEXT UNIQUE,

    plan_name TEXT,

    coverage_details TEXT,

    start_date DATE,

    expiry_date DATE,

    emergency_contact TEXT,

    claim_email TEXT,

    website TEXT,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_insurance_pet
ON insurance(pet_id);

CREATE INDEX idx_insurance_policy
ON insurance(policy_number);

-- =====================================================
-- MICROCHIPS
-- =====================================================

CREATE TABLE IF NOT EXISTS microchips (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    chip_number TEXT UNIQUE NOT NULL,

    manufacturer TEXT,

    implant_date DATE,

    implant_location TEXT,

    registration_country TEXT,

    registry_name TEXT,

    registry_url TEXT,

    status TEXT,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_microchip_pet
ON microchips(pet_id);

CREATE INDEX idx_microchip_number
ON microchips(chip_number);

-- =====================================================
-- PET PASSPORTS
-- =====================================================

CREATE TABLE IF NOT EXISTS pet_passports (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    passport_number TEXT UNIQUE,

    issuing_country TEXT,

    issue_date DATE,

    expiry_date DATE,

    issuing_authority TEXT,

    qr_code TEXT,

    pdf_path TEXT,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_passport_pet
ON pet_passports(pet_id);

-- =====================================================
-- DOCUMENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS documents (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    document_type TEXT,

    title TEXT,

    file_path TEXT,

    file_size INTEGER,

    mime_type TEXT,

    uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    notes TEXT,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_documents_pet
ON documents(pet_id);

-- =====================================================
-- EMERGENCY CONTACTS
-- =====================================================

CREATE TABLE IF NOT EXISTS emergency_contacts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    owner_id INTEGER NOT NULL,

    full_name TEXT NOT NULL,

    relationship TEXT,

    phone TEXT,

    email TEXT,

    address TEXT,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(owner_id)
        REFERENCES owners(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_emergency_owner
ON emergency_contacts(owner_id);-- =====================================================
-- CLINICS
-- =====================================================

CREATE TABLE IF NOT EXISTS clinics (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    clinic_name TEXT NOT NULL,

    license_number TEXT,

    email TEXT,

    phone TEXT,

    website TEXT,

    country TEXT,

    city TEXT,

    address TEXT,

    latitude REAL,

    longitude REAL,

    logo TEXT,

    is_active INTEGER DEFAULT 1,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

CREATE INDEX idx_clinic_uuid
ON clinics(uuid);

-- =====================================================
-- VETERINARIANS
-- =====================================================

CREATE TABLE IF NOT EXISTS veterinarians (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    clinic_id INTEGER,

    first_name TEXT NOT NULL,

    last_name TEXT NOT NULL,

    license_number TEXT,

    specialization TEXT,

    email TEXT,

    phone TEXT,

    profile_photo TEXT,

    biography TEXT,

    years_experience INTEGER,

    is_active INTEGER DEFAULT 1,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(clinic_id)
        REFERENCES clinics(id)
        ON DELETE SET NULL

);

CREATE INDEX idx_vet_clinic
ON veterinarians(clinic_id);

CREATE INDEX idx_vet_uuid
ON veterinarians(uuid);

-- =====================================================
-- APPOINTMENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS appointments (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    pet_id INTEGER NOT NULL,

    owner_id INTEGER NOT NULL,

    veterinarian_id INTEGER,

    clinic_id INTEGER,

    appointment_datetime DATETIME NOT NULL,

    appointment_type TEXT,

    status TEXT,

    reason TEXT,

    diagnosis TEXT,

    treatment TEXT,

    follow_up_required INTEGER DEFAULT 0,

    follow_up_date DATE,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE,

    FOREIGN KEY(owner_id)
        REFERENCES owners(id)
        ON DELETE CASCADE,

    FOREIGN KEY(veterinarian_id)
        REFERENCES veterinarians(id)
        ON DELETE SET NULL,

    FOREIGN KEY(clinic_id)
        REFERENCES clinics(id)
        ON DELETE SET NULL

);

CREATE INDEX idx_appointment_pet
ON appointments(pet_id);

CREATE INDEX idx_appointment_owner
ON appointments(owner_id);

CREATE INDEX idx_appointment_vet
ON appointments(veterinarian_id);

CREATE INDEX idx_appointment_date
ON appointments(appointment_datetime);

-- =====================================================
-- INVOICES
-- =====================================================

CREATE TABLE IF NOT EXISTS invoices (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    appointment_id INTEGER,

    invoice_number TEXT UNIQUE,

    subtotal REAL DEFAULT 0,

    tax REAL DEFAULT 0,

    discount REAL DEFAULT 0,

    total REAL DEFAULT 0,

    currency TEXT DEFAULT 'USD',

    payment_status TEXT,

    issued_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(appointment_id)
        REFERENCES appointments(id)
        ON DELETE SET NULL

);

CREATE INDEX idx_invoice_appointment
ON invoices(appointment_id);

-- =====================================================
-- PAYMENTS
-- =====================================================

CREATE TABLE IF NOT EXISTS payments (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    invoice_id INTEGER NOT NULL,

    payment_method TEXT,

    transaction_reference TEXT,

    amount REAL,

    currency TEXT DEFAULT 'USD',

    payment_date DATETIME,

    status TEXT,

    notes TEXT,

    FOREIGN KEY(invoice_id)
        REFERENCES invoices(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_payment_invoice
ON payments(invoice_id);-- =====================================================
-- LABORATORIES
-- =====================================================

CREATE TABLE IF NOT EXISTS laboratories (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    name TEXT NOT NULL,

    email TEXT,

    phone TEXT,

    website TEXT,

    country TEXT,

    city TEXT,

    address TEXT,

    accreditation TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

CREATE INDEX idx_lab_uuid
ON laboratories(uuid);

-- =====================================================
-- LAB TESTS
-- =====================================================

CREATE TABLE IF NOT EXISTS lab_tests (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    laboratory_id INTEGER,

    veterinarian_id INTEGER,

    test_name TEXT NOT NULL,

    sample_type TEXT,

    ordered_date DATE,

    collected_date DATE,

    completed_date DATE,

    status TEXT,

    notes TEXT,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE,

    FOREIGN KEY(laboratory_id)
        REFERENCES laboratories(id)
        ON DELETE SET NULL,

    FOREIGN KEY(veterinarian_id)
        REFERENCES veterinarians(id)
        ON DELETE SET NULL

);

CREATE INDEX idx_labtest_pet
ON lab_tests(pet_id);

-- =====================================================
-- LAB RESULTS
-- =====================================================

CREATE TABLE IF NOT EXISTS lab_results (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    lab_test_id INTEGER NOT NULL,

    parameter_name TEXT,

    result_value TEXT,

    unit TEXT,

    reference_range TEXT,

    interpretation TEXT,

    abnormal INTEGER DEFAULT 0,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(lab_test_id)
        REFERENCES lab_tests(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_labresults_test
ON lab_results(lab_test_id);

-- =====================================================
-- VITAL SIGNS
-- =====================================================

CREATE TABLE IF NOT EXISTS vital_signs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    body_temperature REAL,

    heart_rate INTEGER,

    respiratory_rate INTEGER,

    blood_pressure TEXT,

    oxygen_saturation REAL,

    blood_glucose REAL,

    pain_score INTEGER,

    hydration_status TEXT,

    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    notes TEXT,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_vitals_pet
ON vital_signs(pet_id);

-- =====================================================
-- DNA PROFILES
-- =====================================================

CREATE TABLE IF NOT EXISTS dna_profiles (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    laboratory_id INTEGER,

    test_provider TEXT,

    breed_composition TEXT,

    inherited_conditions TEXT,

    report_file TEXT,

    report_date DATE,

    notes TEXT,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE,

    FOREIGN KEY(laboratory_id)
        REFERENCES laboratories(id)
        ON DELETE SET NULL

);

CREATE INDEX idx_dna_pet
ON dna_profiles(pet_id);

-- =====================================================
-- AI REPORTS
-- =====================================================

CREATE TABLE IF NOT EXISTS ai_reports (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    pet_id INTEGER NOT NULL,

    report_type TEXT,

    ai_provider TEXT,

    ai_model TEXT,

    symptoms TEXT,

    prompt TEXT,

    response_json TEXT,

    health_score INTEGER,

    risk_level TEXT,

    emergency INTEGER DEFAULT 0,

    confidence_score REAL,

    generated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_ai_pet
ON ai_reports(pet_id);

CREATE INDEX idx_ai_uuid
ON ai_reports(uuid);

-- =====================================================
-- IMAGE ANALYSIS
-- =====================================================

CREATE TABLE IF NOT EXISTS image_analysis (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    image_id INTEGER NOT NULL,

    ai_report_id INTEGER,

    findings TEXT,

    detected_conditions TEXT,

    confidence REAL,

    analyzed_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(image_id)
        REFERENCES pet_images(id)
        ON DELETE CASCADE,

    FOREIGN KEY(ai_report_id)
        REFERENCES ai_reports(id)
        ON DELETE SET NULL

);

CREATE INDEX idx_image_analysis_image
ON image_analysis(image_id);

-- =====================================================
-- HEALTH SCORES
-- =====================================================

CREATE TABLE IF NOT EXISTS health_scores (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    overall_score INTEGER,

    nutrition_score INTEGER,

    activity_score INTEGER,

    weight_score INTEGER,

    vaccination_score INTEGER,

    medical_score INTEGER,

    ai_score INTEGER,

    calculated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    notes TEXT,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_healthscore_pet
ON health_scores(pet_id);-- =====================================================
-- ORGANIZATIONS (Multi-Tenant)
-- =====================================================

CREATE TABLE IF NOT EXISTS organizations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    name TEXT NOT NULL,

    organization_type TEXT,

    email TEXT,

    phone TEXT,

    website TEXT,

    country TEXT,

    city TEXT,

    address TEXT,

    logo TEXT,

    subscription_plan TEXT,

    is_active INTEGER DEFAULT 1,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

CREATE INDEX idx_org_uuid
ON organizations(uuid);

-- =====================================================
-- USERS
-- =====================================================

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    organization_id INTEGER,

    owner_id INTEGER,

    veterinarian_id INTEGER,

    email TEXT UNIQUE NOT NULL,

    password_hash TEXT NOT NULL,

    full_name TEXT NOT NULL,

    phone TEXT,

    avatar TEXT,

    last_login DATETIME,

    is_active INTEGER DEFAULT 1,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(organization_id)
        REFERENCES organizations(id)
        ON DELETE SET NULL,

    FOREIGN KEY(owner_id)
        REFERENCES owners(id)
        ON DELETE SET NULL,

    FOREIGN KEY(veterinarian_id)
        REFERENCES veterinarians(id)
        ON DELETE SET NULL

);

CREATE INDEX idx_users_email
ON users(email);

CREATE INDEX idx_users_org
ON users(organization_id);

-- =====================================================
-- ROLES
-- =====================================================

CREATE TABLE IF NOT EXISTS roles (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT UNIQUE NOT NULL,

    description TEXT

);

-- =====================================================
-- USER ROLES
-- =====================================================

CREATE TABLE IF NOT EXISTS user_roles (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    role_id INTEGER NOT NULL,

    assigned_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE CASCADE,

    FOREIGN KEY(role_id)
        REFERENCES roles(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_user_roles_user
ON user_roles(user_id);

-- =====================================================
-- PERMISSIONS
-- =====================================================

CREATE TABLE IF NOT EXISTS permissions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    permission_key TEXT UNIQUE,

    description TEXT

);

-- =====================================================
-- ROLE PERMISSIONS
-- =====================================================

CREATE TABLE IF NOT EXISTS role_permissions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    role_id INTEGER NOT NULL,

    permission_id INTEGER NOT NULL,

    FOREIGN KEY(role_id)
        REFERENCES roles(id)
        ON DELETE CASCADE,

    FOREIGN KEY(permission_id)
        REFERENCES permissions(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_role_permissions_role
ON role_permissions(role_id);

-- =====================================================
-- API KEYS
-- =====================================================

CREATE TABLE IF NOT EXISTS api_keys (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    organization_id INTEGER,

    api_key TEXT UNIQUE,

    api_secret TEXT,

    status TEXT,

    expires_at DATETIME,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(organization_id)
        REFERENCES organizations(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_api_keys_org
ON api_keys(organization_id);-- =====================================================
-- NOTIFICATIONS
-- =====================================================

CREATE TABLE IF NOT EXISTS notifications (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    user_id INTEGER NOT NULL,

    title TEXT NOT NULL,

    message TEXT NOT NULL,

    notification_type TEXT,

    priority TEXT DEFAULT 'normal',

    is_read INTEGER DEFAULT 0,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    read_at DATETIME,

    FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_notifications_user
ON notifications(user_id);

-- =====================================================
-- REMINDERS
-- =====================================================

CREATE TABLE IF NOT EXISTS reminders (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    pet_id INTEGER NOT NULL,

    reminder_type TEXT NOT NULL,

    title TEXT NOT NULL,

    description TEXT,

    due_date DATETIME NOT NULL,

    repeat_rule TEXT,

    status TEXT DEFAULT 'pending',

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    completed_at DATETIME,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_reminders_pet
ON reminders(pet_id);

CREATE INDEX idx_reminders_due
ON reminders(due_date);

-- =====================================================
-- EMAIL QUEUE
-- =====================================================

CREATE TABLE IF NOT EXISTS email_queue (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    recipient TEXT NOT NULL,

    subject TEXT NOT NULL,

    body TEXT NOT NULL,

    status TEXT DEFAULT 'pending',

    attempts INTEGER DEFAULT 0,

    last_attempt DATETIME,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

-- =====================================================
-- SMS QUEUE
-- =====================================================

CREATE TABLE IF NOT EXISTS sms_queue (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    phone TEXT NOT NULL,

    message TEXT NOT NULL,

    status TEXT DEFAULT 'pending',

    attempts INTEGER DEFAULT 0,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

-- =====================================================
-- PUSH DEVICES
-- =====================================================

CREATE TABLE IF NOT EXISTS push_devices (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    device_name TEXT,

    platform TEXT,

    push_token TEXT UNIQUE,

    last_seen DATETIME,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_push_user
ON push_devices(user_id);

-- =====================================================
-- PUSH QUEUE
-- =====================================================

CREATE TABLE IF NOT EXISTS push_queue (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    device_id INTEGER NOT NULL,

    title TEXT,

    body TEXT,

    status TEXT DEFAULT 'pending',

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    sent_at DATETIME,

    FOREIGN KEY(device_id)
        REFERENCES push_devices(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_push_queue_device
ON push_queue(device_id);-- =====================================================
-- AI CONVERSATIONS
-- =====================================================

CREATE TABLE IF NOT EXISTS ai_conversations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    uuid TEXT UNIQUE NOT NULL,

    pet_id INTEGER NOT NULL,

    user_id INTEGER NOT NULL,

    title TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE,

    FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_ai_conversation_pet
ON ai_conversations(pet_id);

CREATE INDEX idx_ai_conversation_user
ON ai_conversations(user_id);

-- =====================================================
-- AI MESSAGES
-- =====================================================

CREATE TABLE IF NOT EXISTS ai_messages (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    conversation_id INTEGER NOT NULL,

    role TEXT NOT NULL,

    message TEXT NOT NULL,

    token_count INTEGER,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(conversation_id)
        REFERENCES ai_conversations(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_ai_messages_conversation
ON ai_messages(conversation_id);

-- =====================================================
-- AI MEMORY
-- =====================================================

CREATE TABLE IF NOT EXISTS ai_memory (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    memory_key TEXT NOT NULL,

    memory_value TEXT,

    confidence REAL,

    source TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_ai_memory_pet
ON ai_memory(pet_id);

-- =====================================================
-- AI FEEDBACK
-- =====================================================

CREATE TABLE IF NOT EXISTS ai_feedback (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    report_id INTEGER NOT NULL,

    user_id INTEGER,

    rating INTEGER,

    feedback TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(report_id)
        REFERENCES ai_reports(id)
        ON DELETE CASCADE,

    FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE SET NULL

);

CREATE INDEX idx_ai_feedback_report
ON ai_feedback(report_id);

-- =====================================================
-- GPS DEVICES
-- =====================================================

CREATE TABLE IF NOT EXISTS gps_devices (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pet_id INTEGER NOT NULL,

    device_name TEXT,

    serial_number TEXT UNIQUE,

    manufacturer TEXT,

    firmware_version TEXT,

    battery_level INTEGER,

    last_seen DATETIME,

    status TEXT,

    FOREIGN KEY(pet_id)
        REFERENCES pets(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_gps_pet
ON gps_devices(pet_id);

-- =====================================================
-- GPS LOCATIONS
-- =====================================================

CREATE TABLE IF NOT EXISTS gps_locations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    device_id INTEGER NOT NULL,

    latitude REAL,

    longitude REAL,

    altitude REAL,

    speed REAL,

    accuracy REAL,

    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(device_id)
        REFERENCES gps_devices(id)
        ON DELETE CASCADE

);

CREATE INDEX idx_gps_location_device
ON gps_locations(device_id);

CREATE INDEX idx_gps_recorded
ON gps_locations(recorded_at);

-- =====================================================
-- AUDIT LOGS
-- =====================================================

CREATE TABLE IF NOT EXISTS audit_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    entity_name TEXT,

    entity_id INTEGER,

    action TEXT,

    old_value TEXT,

    new_value TEXT,

    ip_address TEXT,

    user_agent TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE SET NULL

);

CREATE INDEX idx_audit_user
ON audit_logs(user_id);

CREATE INDEX idx_audit_entity
ON audit_logs(entity_name, entity_id);

-- =====================================================
-- SYSTEM SETTINGS
-- =====================================================

CREATE TABLE IF NOT EXISTS system_settings (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    setting_key TEXT UNIQUE,

    setting_value TEXT,

    description TEXT,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP

);