{% set platform = platform_target if platform_target and platform_target.strip() != "" else "Generic" %}
# ==============================================================================
# ENTERPRISE MARKETING ASSET FRAMEWORK: CORE CONTENT & METADATA MASTER SCHEMA
# Version: 1.0.0 | Engine: CoreAssetGenerator-v1
# Architecture: Single-Source Product Truth (SSPT) Matrix
# ==============================================================================

# GLOBAL CONFIGURATION ENVIRONMENT VARIABLES
# ------------------------------------------------------------------------------
# These template injection placeholders map 1:1 with automated pipeline variables.
PROJECT_IDENTITY_HANDLE: "{{ project_name }}"
PROJECT_CORE_DESCRIPTION: "{{ project_description }}"
UNIQUE_DOCUMENT_TRACKING_ID: "ASSET-{{ doc_id }}"
SYSTEM_GENERATION_TIMESTAMP: "{{ current_timestamp }}"
CHOSEN_MARKETING_CHANNELS: "{{ platform }}"


# ZONE 1: BRAND ARCHETYPE & VOICE CONTROLS (SEO BRAND EQUITY REGULATION)
# ------------------------------------------------------------------------------
# Directs the AI Copywriter Engine on language restrictions, tone, and positioning.

BRAND_POSITIONING_STATEMENT:
  "An elite, highly scalable enterprise technology infrastructure engineered for high-availability operational efficiency, zero-trust cryptographic data protection, and seamless automation orchestration."

TONE_AND_VOICE_ATTRIBUTES:
  - "Authoritative & Domain Expert: Uses dense technical terminology but translates it clearly into real-world business advantages."
  - "Data-Driven & Empirical: Focuses exclusively on measurable performance indicators, architectures, and hard evidence."
  - "Action-Oriented & High-Urgency: Drives immediate user progression using structured value hooks and explicit next steps."

SEO_SEMANTIC_KEYWORD_TAXONOMY:
  - "Enterprise microservices management system"
  - "High-availability system infrastructure"
  - "PostgreSQL read replica optimization"
  - "Zero-trust corporate database encryption"
  - "Real-time automated data validation"

ABSOLUTE_PROHIBITED_WORDS_ARRAY:
  - "100% guaranteed"
  - "perfect solution"
  - "magic bullet"
  - "completely cheap"
  - "best in the absolute world"


# ZONE 2: CORE TECHNICAL FACTS MATRIX (ZERO-HALLUCINATION TRUTH ANCHOR)
# ------------------------------------------------------------------------------
# These factual constraints are strictly enforced to eliminate inaccurate AI generation.

PRODUCT_FACT_REGISTRY:
  - FACT_ID: "FACT-SYS-001"
    FEATURE_SCOPE: "Architecture Topology"
    TECHNICAL_SPECIFICATION: "Decoupled Microservices Ecosystem"
    BUSINESS_VALUE_TRANSLATION: "Handles 10,000 concurrent continuous user connection requests smoothly with sub-200ms API server latency thresholds."

  - FACT_ID: "FACT-SYS-002"
    FEATURE_SCOPE: "Database Performance & Caching"
    TECHNICAL_SPECIFICATION: "Enterprise PostgreSQL RDBMS cluster with specialized read replicas implemented"
    BUSINESS_VALUE_TRANSLATION: "Offloads all complex analytical reporting and telemetry compute workloads from the primary transactional instance."

  - FACT_ID: "FACT-SYS-003"
    FEATURE_SCOPE: "Infrastructure Availability Control"
    TECHNICAL_SPECIFICATION: "Google Kubernetes Engine (GKE) multi-zone node clusters backed by automated health probes and failover"
    BUSINESS_VALUE_TRANSLATION: "Delivers an ironclad 99.9% structural operational availability SLA guarantee."

  - FACT_ID: "FACT-SYS-004"
    FEATURE_SCOPE: "Data Cryptography Regulations"
    TECHNICAL_SPECIFICATION: "TLS 1.3 cryptographic transport routing for data-in-transit, AES-256 block cipher engine volume state for data-at-rest"
    BUSINESS_VALUE_TRANSLATION: "Eliminates man-in-the-middle exploits and secures all enterprise database storage states."

  - FACT_ID: "FACT-SYS-005"
    FEATURE_SCOPE: "Security Compliance Logs"
    TECHNICAL_SPECIFICATION: "Immutable data modification ledger tracking with a strict 1-year data persistence ceiling"
    BUSINESS_VALUE_TRANSLATION: "Achieves full compliance mapping with active global data residency laws including GDPR, CCPA, and ISO-27001."


# ZONE 3: ENGAGEMENT COMPONENT BLUEPRINT (CONVERSION RATE OPTIMIZATION)
# ------------------------------------------------------------------------------
# Structured conversion patterns required for ready-to-publish social deployment.

HIGH_CONVERSION_HOOK_TEMPLATES:
  - STRUCTURED_HOOK_1:
      PATTERN: "System Panic Avoidance Framework"
      METRIC_FOCUS: "System operational uptime under massive load peaks"
      TEMPLATE_BODY: "Scale your organization to {{ project_name }} without experiencing systemic database locks. Discover how a high-availability microservices architecture guarantees your critical operations stay online."
  - STRUCTURED_HOOK_2:
      PATTERN: "Regulatory Cost Mitigation Framework"
      METRIC_FOCUS: "Data residency penalty avoidance and security transparency"
      TEMPLATE_BODY: "Legacy data storage systems expose your organization to massive compliance litigation risk. Protect your corporate workflows with TLS 1.3 transmission layers and automated logging."

CALL_TO_ACTION_VARIANT_REGISTRY:
  - PLATFORM_SCOPE: "linkedin"
    CTA_TEXT_BODY: "Request a secure technical proof-of-concept deployment. Contact our cloud infrastructure team today at https://{{ project_name }}.io/enterprise-demo"
  - PLATFORM_SCOPE: "telegram_or_zalo"
    CTA_TEXT_BODY: "Join our core developer ecosystem now for real-time engineering integration updates: https://t.me/{{ project_name }}_core_updates"


# ZONE 4: SEARCH ENGINE METADATA OPTIMIZATION (SEO ENGINE MAPPING)
# ------------------------------------------------------------------------------
# Defines programmatic schemas used for landing pages and indexing configurations.

SEO_META_SCHEMA_TAGS:
  META_TITLE_STRUCTURE: "Enterprise {{ project_name }} | High-Availability Cloud Automation Engine"
  META_DESCRIPTION_MAX_LIMIT: "Deploy {{ project_name }}, a modern microservices system configured for PostgreSQL data scaling, zero-trust encryption, and strict global compliance enforcement."
  OPEN_GRAPH_LOCALE_DEFAULT: "en_US"
  STRUCTURED_SCHEMA_MARKUP_TYPE: "SoftwareApplication"
