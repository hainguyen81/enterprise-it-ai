# 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

#### 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
  - You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
  - Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
  - You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
  - Do NOT emit relative paths that assume a sub-module directory is the root:
    * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`). Skip entirely if project is Frontend-only.
    * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
    * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
    * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
    * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
  - Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

#### 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
  - For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of {{ num_phases }} phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of {{ max_days_per_phase }} days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

#### 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
  - Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`) inherited from the requirements. 
  - You are STRICTLY BANNED from bundling tags together (e.g., NO `[REQ-001-005]`). Every single tag must be written out individually and separated by commas. Leaving any task or field without its trace tracking identifier inline is a critical framework violation.

#### 🚨 SUB-AGENT BOUNDARY & RESPONSIBILITY ISOLATION MATRIX
  You MUST strictly isolate the architectural responsibilities of all Sub-Agents listed below. They are separate functional pillars and must NEVER bleed into each other's domain:
  - 💻 **Coder Agent Role**:
    * Core Duty: Pure Application Source Code Implementation.
    * Allowed Actions: Write, refactor, and implement structural logic in application files.
    * Strict Boundary: Forbidden from writing test suites or enterprise architectural documentation.
  - 🧪 **Tester Agent Role**:
    * Core Duty: Test Suite Engineering and Validation.
    * Allowed Actions: Write unit tests, integration tests, and automation scripts. 
    * Strict Boundary: Must strictly use the target-test semi-colon pair syntax for `target_component` (`target_test_file;source_code_file`). Forbidden from writing production application code.
  - 🔍 **Reviewer Agent Role**:
    * Core Duty: Code Review, Issue/Bug Analysis and Fix Strategy.
    * Allowed Actions: Inspect code quality, enforce programming standards, detect optimization bottlenecks, analyze structural issues/bugs, and design explicit fix implementations.
  - 📝 **Doc Agent Role**:
    * Core Duty: Enterprise Technical Document Writer.
    * Allowed Actions: Author high-quality Markdown technical specifications, architecture blueprints, API references, and system compliance documents.
  - 🐳 **Docker Agent Role**:
    * Core Duty: Containerization and Package Registry Pushing.
    * Allowed Actions: Build multi-stage Dockerfiles and push container images to target registries.
  - ☁️ **GCP Agent Role**:
    * Core Duty: Baseline Google Cloud Platform Infrastructure Provisioning.
    * Allowed Actions: Build, push configurations, manage core cloud services (VPC, IAM, Storage), and orchestrate general cloud pipeline deployments.
  - ☸️ **GKE Agent Role**:
    * Core Duty: Google Kubernetes Engine Workload Orchestration.
    * Allowed Actions: Build, push configuration files, design Kubernetes deployment manifests, and manage container scaling and release strategies inside GKE clusters.

#### 🔢 EQUAL REQUIREMENT DISTRIBUTION & ZERO-FILLER DAY-CAP PROTOCOL
  - **Phase Boundary Count**: The total number of architectural phases MUST be exactly "{{ num_phases }}".
  - **Requirement Distribution Mandate**: You MUST distribute 100% of all provided project requirements into exactly "{{ num_phases }}" phases. No requirement can be left unassigned, omitted, or bundled lazily. Every phase from Phase 1 to Phase "{{ num_phases }}" must receive a balanced subset of requirements.
  - **Strict Day-Cap & Anti-Filler Rail**:
    * The maximum number of days within ANY single phase is strictly capped at: "{{ max_days_per_phase }}".
    * The actual number of days per phase can be LESS than or EQUAL to "{{ max_days_per_phase }}" (e.g., `actual_days <= max_days_per_phase`).
    * 🚨 **STRICT FORBIDDEN DIRECTIVE**: You are ABSOLUTELY FORBIDDEN from creating "filler days", redundant testing sessions, unnecessary sync setups, or placeholder tasks just to padding the day count up to the maximum limit. If a phase only requires 2 high-density days to fully implement its assigned requirements, you MUST stop at Day 2. Do not hallucinate Day 3 or Day 4.
    * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.

#### 🚨 CRITICAL FULL TRANSLATION MANDATE
  - The target generation language for all human-readable outputs is permanently bound to: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}". Everything MUST be translated into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}, except for the explicit Technical English core tokens protected by system mandates.
  - You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language.

#### 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
  - Target Output Language Context: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"
  - You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
  - 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
    * All Section and Sub-section Headers MUST be translated contextually into the Target Output Language.
    * All Table Headers MUST be translated contextually into the Target Output Language.
    * All list Prefixes and Phase Titles MUST be translated contextually into the Target Output Language.
  - 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
    * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
    * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
    * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
    * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
  - 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
    * All markdown syntax layout operators (`#`, `##`, `###`, `|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
    * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `## 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `## 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
    * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
    * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`).
    * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
    * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
    * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`). These must remain in their original raw character format to prevent backend processing errors.
    * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
    * 🚨 **STRICT CODE BLOCK FORMATTING LAW**: You are ABSOLUTELY FORBIDDEN from nesting or combining markdown code block ticks. When outputting a JSON payload, you MUST start exactly with a single line of triple backticks followed immediately by 'json' (i.e., ```json). Do NOT prepend or wrap it with ```text or any other outer text syntax. The block must open clean and close clean.
    * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
    * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.
  - **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %} while completely freezing all technical paths, tags, and block codes.


{# ─── START:RULES FOR CHUNK OPERATION ─── #}
#### MANDATORY SEGMENT INSTRUCTION:  
  - You MUST fully translate them following the rules in `CRITICAL FULL TRANSLATION MANDATE`
{% set phases_and_tasks_section = "`4.1 MASTER ARCHITECTURAL PRODUCT BACKLOG`" if force_full_export else "`--- BACKLOG TASKS ---`" %}
{% if force_full_export %}
  - You MUST include every single section below without exception to satisfy enterprise compliance requirements

{% else %}
  - **ABSOLUTE RAW EMISSION LAW (ZERO CODE-BLOCK WRAPPERS):** You are STRICTLY BANNED from wrapping your entire multi-line output response inside triple backticks markdown envelopes (i.e., ```markdown ... ```). You MUST emit your architectural structure directly into the token stream as pure, un-enveloped lines of standard vertical markdown layout text. You ARE CRITICALLY REQUIRED to retain all structural newline carriage returns, literal newline characters or line break between headers, lists, and table rows to ensure proper document rendering. Any dynamic leakage of wrapping backticks triggers an immediate infrastructure system crash.
{% endif %}
{# ─── END:RULES FOR CHUNK OPERATION ─── #}


{# ======================================================= #}
{# ─── MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT) ─── #}
{# ======================================================= #}
### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):

{# ─── START:RULES FOR CHUNK OPERATION ─── #}
{% if force_full_export %}
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE`

{% else %}
<RULE>
- **ZERO REPLICATE MANDATE (ANTI-ECHO LAW):** You are STRICTLY BANNED from replicating, copying, or printing any raw lines, paragraphs, or blocks of text from `<SYSTEM_DATA_INJECTION_POOL>`, `<PROJECT_BACKLOG_TASKS_DATA>` or `<PROJECT_SOURCE_GROUNDING_DATA>` into your output response. Those pools are strictly for internal processing, NOT targets for emission.
- **GLOBAL AUTOMATIC TERMINATION BOUNDARY:** Your very first emitted token MUST be the first visible markdown header line rendered in this active User Message. The exact microsecond you finish printing the last visible data row or string before the active segment's closing HTML framework tag (e.g., `<!--END_...-->`, example: `<!--END_{{ target_segment }}-->`), you MUST trigger an immediate hard stop and terminate the response stream instantly.
- **ABSOLUTE RAW EMISSION LAW (ZERO CODE-BLOCK WRAPPERS):** You are STRICTLY BANNED from wrapping your entire multi-line output response inside triple backticks markdown envelopes (i.e., ```markdown ... ```). You MUST emit your architectural structure directly into the token stream as pure, un-enveloped flat text. Any dynamic leakage of wrapping backticks triggers an immediate infrastructure system crash.
- **DYNAMIC TARGET ISOLATION LAW (HTML WRAPPER ANCHOR):** Identify the very first active hidden HTML framework comment block (formatted exactly as `<!--START_{{ target_segment }}-->`) rendered visible inside this active User Message. You MUST completely bypass all instruction blocks, metadata matrices, or reference data pools. Your very first emitted token MUST match the exact text of the Markdown header line (starting with `#`, `##`, or `###`) located immediately following that opening HTML tag. Zero preceding words, spaces, or configuration summaries are allowed before it.
- **STRICT HALT BOUNDARY (ZERO-TAG EXECUTION):** You are strictly commanded to ONLY generate content that exists structurally inside the active HTML framework comment pair currently triggered by the system filter. You ARE ABSOLUTELY AND CRITICALLY BANNED from replicating, echoing, or copying any raw structural chunks from the reference database pool or the `--- RAW REQUIREMENTS ---` section. The exact microsecond you finish printing the final data row or string located immediately before the closing HTML framework comment tag (`<!--END_{{ target_segment }}-->`), you MUST trigger an absolute system hard stop and terminate the response stream instantly.
- You MUST fully translate them following the rules in `CRITICAL FULL TRANSLATION MANDATE`
</RULE>
{% endif %}
{# ─── END:RULES FOR CHUNK OPERATION ─── #}

{% if not force_full_export %}
<!--START_{{ target_segment }}-->
{% endif %}

{# ======================================================= #}
{# ─── START:CHUNK:PART_1_INITIAL ─── #}
{% if force_full_export or (target_segment and target_segment.strip() == "PART_1_INITIAL") %}
# GLOBAL PROJECT CONTEXT: {{ project_name }}

## 📊 Document Control

| Item | Details |
| :--- | :--- |
| **Blueprint ID** | ARCH-{{ doc_id }} |
| **Project Name** | {{ project_name }} |
| **Version** | 1.0 (Baseline) |
| **Date.Time** | {{ current_timestamp }} |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | Pending Technical Governance Review |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### ⚙️ 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
</RULE>

### 🌊 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- You MUST render 100% of your newly generated sentences in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
</RULE>

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
<RULE>
- You MUST dynamically generate the Enterprise Compliance Standards based on the specific core items listed below.
- Each item MUST be rendered as a highly structured, high-density markdown bulleted checklist (`- ` symbols). 
- Every bullet point must be a short, punchy technical baseline statement delivering raw architectural metrics in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
</RULE>

### 🔑 3.1. Security & Compliance Baseline
<RULE>
- Dynamically extract and generate a highly structured, high-density markdown bulleted checklist (`- ` symbols) specifying the security protocols, encryption standards (e.g., JWT, AES), and RBAC boundaries mentioned in the requirements.
- Every bullet point must be a short, punchy technical statement delivering raw architectural metrics in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
- If no explicit security requirements are found in the text, you MUST derive a logical technical security baseline tailored to the project's tech stack.
</RULE>

### 🌐 3.2. Infrastructure & Performance Guardrails
<RULE>
- Dynamically extract and generate a highly structured, high-density markdown bulleted checklist (`- ` symbols) specifying the infrastructure limitations, database pooling (e.g., HikariCP), caching eviction policies (e.g., Redis), and async messaging constraints from the requirements.
- Every bullet point must be a short, punchy technical statement delivering raw architectural metrics in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
- If no explicit performance guardrails are found, you MUST derive a production-grade infrastructure baseline tailored to the project's architecture.
</RULE>

### 🥞 3.3. ARCHITECTURAL STACK MATRIX
<RULE>
- You MUST analyze the `--- RAW REQUIREMENTS ---` section to identify the actual technology stack used in the project.
- Based on your analysis, dynamically set the value of each key below to `true` or `false`.
- CRITICAL FORMAT RULE: Output ONLY the raw key-value pairs formatted exactly as `KEY=value`. Do NOT translate the keys. Do NOT add markdown formatting, quotes, or brackets inside the code block.
</RULE>

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=auto_evaluate
BACKEND_LAYER_REQUIRED=auto_evaluate
FRONTEND_LAYER_REQUIRED=auto_evaluate
MOBILE_LAYER_REQUIRED=auto_evaluate
DEVOPS_LAYER_REQUIRED=auto_evaluate
```

{% endif %}
{# ─── END:CHUNK:PART_1_INITIAL ─── #}

{# ======================================================= #}
{# ─── START:CHUNK:PART_1_BACKLOG_4_1 ─── #}
{% if force_full_export or (target_segment and target_segment.strip() == "PART_1_BACKLOG_4_1") %}
## 🏁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 📦 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
<RULE>
- You MUST analyze the `--- RAW REQUIREMENTS ---` section (raw SRS) to identify and break down the implementation tasks for the unified Master Product Tasks Backlog table directly under this section (inside the hidden HTML tags from `<!--START_BACKLOG_SYNOPSIS_GRID-->` to `<!--END_BACKLOG_SYNOPSIS_GRID-->`). Organize the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project requirements from the `--- RAW REQUIREMENTS ---` section (raw SRS).
- STEP 1 (HIGH-DENSITY DESCRIPTION): You MUST first write a comprehensive, high-density technical description paragraph directly, above the Master Product Tasks Backlog table under this section. This description paragraph must analyze the system architecture, component dependencies, and integration workflow. You MUST render 100% of this description paragraph in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
- STEP 2 (FULL REQUIREMENT BREAKDOWN TABLE): Directly below the description paragraph, you MUST dynamically generate the complete Master Product Tasks Backlog Table (inside the hidden HTML tags from `<!--START_BACKLOG_SYNOPSIS_GRID-->` to `<!--END_BACKLOG_SYNOPSIS_GRID-->`).
- MANDATORY TRANSLATION ENGINE: You MUST translate 100% of the table header text and task descriptions into the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
- TECHNICAL PRESERVATION MATRIX: You MUST NOT translate technical keys, IDs, system configurations, paths, or variables. Specifically, preserve raw English/technical formats for: Task IDs (e.g., TASK-001), Component Paths (e.g., `sources/backend/auth/`), and Targeted Tag IDs (e.g., `[ARC-001]`).
- TRACEABILITY MANDATE: You MUST ensure 100% full coverage of ALL Tag IDs (including every single `[ARC-XXX]`, `[NFR-XXX]`, etc.) extracted from the `--- RAW REQUIREMENTS ---` section. Do NOT skip, omit, or truncate any Tag ID.
- LOCALIZED TABLE SCHEMA: The markdown table structure MUST match this layout exactly, with the bracketed header text translated into the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
- The Master Product Tasks Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below (inside the hidden HTML tags from `<!--START_BACKLOG_SYNOPSIS_GRID-->` to `<!--END_BACKLOG_SYNOPSIS_GRID-->`).
- **MANDATORY ROW ANCHOR INJECTION:** Every single generated task row inside this table MUST contain the literal hidden HTML comment tag `<!--REGISTERED_BACKLOG_TASK_ROW-->`. You MUST explicitly place this tag inside the final cell (the TagID column, the 5th column), positioning it immediately after the tracking tags and right before the closing vertical pipe character `|` of that row (exact syntax pattern format: ` | ... [Tag IDs] <!--REGISTERED_BACKLOG_TASK_ROW--> |`). Any generated row that drops or filters out this structural comment anchor will cause a fatal deployment pipeline failure.
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This Master Product Tasks Backlog Table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly verified by the Type column (the 4th column):
  1. *Application Code:* Functional endpoint creations, database models, and service layer code blocks.
  2. *Enterprise Documentation:* Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. *DevOps Infrastructure:* Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **TASK ATOMICITY LAW:** You are STRICTLY BANNED from summarizing, grouping, or clustering multiple operational requirement bullets into a single generic task row to save token space.
- **1:1 TRACEABILITY RATIO & EXCLUSION LAW:** Every unique functional Tag ID identified in the raw SRS matching the `[REQ-XXX]` pattern MUST yield exactly one (1) dedicated, standalone row in this table. You are STRICTLY BANNED from summarizing or grouping multiple `[REQ]` bullets into a single row to save space. However, you MUST completely exempt all `[DAT]`, `[ARC]`, and `[EXC]` tags from this 1:1 expansion law; these system metadata domains MUST be handled exclusively via the dynamic consolidation rules specified below.
- **AUTONOMOUS MANDATORY COMPLIANCE INJECTION RAIL:** To satisfy the strict requirements of enterprise compliance, even if the raw business requirements section lacks explicit narrative text specifications for cross-cutting infrastructure, DevOps pipelines, or universal system documentation, you MUST autonomously inject dedicated, standalone framework task rows into the table matching these parameters:
  1. *Database & Token Verification Core:* You MUST ensure the generation of exactly one (1) unified database infrastructure initialization row capturing all `[DAT-XXX]` patterns (condensed as `[DAT-ALL (1 to X)]`), exactly one (1) row capturing global RBAC security `[ARC-001 to ARC-005]` patterns, and exactly one (1) row capturing system integration contracts `[ARC-006 to ARC-009]`.
  2. *Enterprise DevOps Infrastructure Injection:* You MUST dynamically inject a dedicated standalone task row for DevOps Infrastructure (handling multi-stage Dockerfiles, cloud environment setups via Terraform, and orchestration cluster manifests inside GKE). You MUST explicitly map ALL matching `[NFR-XXX]` security, performance, and cross-cutting compliance tokens directly into its TagID cell to guarantee full vertical traceability.
  3. *System Documentation Architecture Injection:* You MUST dynamically inject a dedicated standalone task row for Enterprise Documentation (handling blueprints, system topologies, localized operational manuals, and API contracts under `./sources/docs/`).
- **STRICT TASK ATOMICITY RAIL:** You MUST generate an independent, standalone row for every single functional requirement (`[REQ-XXX]`) and system capability discovered inside the `--- RAW REQUIREMENTS ---` section. You ARE ABSOLUTELY BANNED from grouping, clustering, or condensing multiple functional requirements into a single task row.
- **METADATA CONSOLIDATION & INFRASTRUCTURE ROWS:** You MUST consolidate system metadata patterns into standalone architecture enablement rows at the bottom of the table to prevent token redundancy:
  1. *Database Layer Infrastructure:* You MUST dynamically fetch the evaluated integer value of the variable `Source_DAT`. You ARE ABSOLUTELY BANNED from explicitly listing individual data columns or fields inside the cells. You MUST strictly print the TagID cell layout exactly formatted as this dynamic string pattern: `[DAT-ALL (1 to Source_DAT)]` (where you MUST substitute the text `Source_DAT` with the actual calculated integer value of the `Source_DAT` variable). In your internal mathematical evaluation layer, this consolidated token MUST hold a weight equal to exactly that calculated integer value.
  2. *Security Layer:* Harvest all architectural tokens matching `[ARC-XXX]` (Let the total unique count be variable `A`). You MUST print the TagID cell exactly as a dynamic range pattern: `[ARC-START_NUM to ARC-END_NUM]`.
  3. *DevOps Layer:* Group all cross-cutting deployment concerns. You MUST explicitly map ALL matching non-functional compliance tokens (`[NFR-XXX]`) directly into this standalone infrastructure cell.
  4. *Exception Layer:* Locate all validation handling codes matching `[EXC-XXX]`. Inline and attach these tracking tokens directly into the cell of their respective functional parent requirement rows.
- **INDEPENDENT AUDIT MATRIX:** Before emitting the table SUMMARY row (latest row of the Master Product Tasks Backlog table), you MUST declare and calculate exactly some distinct internal mathematical variables within your execution memory layer:
  1. Let **Global_Source_Total** = Perform a comprehensive pass over the entire `--- RAW REQUIREMENTS ---` section. Count every single unique tracking symbol present in the raw corpus (explicitly summing all unique [REQ-XXX], [EXC-XXX], [ARC-XXX], [NFR-XXX] and [DAT-XXX] tags found).
  2. Let **Global_Covered_Total** = Completely ignore your source count and perform a fresh, independent pass over the columns of the table you just generated above. Manually sum every unique tag explicitly written inside the cells. For consolidated rows, you MUST add the full weight of the range index (e.g., counting `[DAT-ALL (1 to D)]` with the full mathematical weight of the max index value D).
  3. Let **Coverage_Status** column: Compute (`Global_Covered_Total` / `Global_Source_Total`) * 100. If `Global_Covered_Total` does not equal `Global_Source_Total`, the output percentage MUST reflect the deficit and set STATUS to `FAILED` in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
  4. Let **Verified_Status** column: If `Global_Covered_Total` is exactly equal to `Global_Source_Total`, output the translated word for `Verified` in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}". Otherwise, output the translated word for `FAILED` in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
  5. Let `Source_REQ` = Perform a comprehensive pass over the entire `--- RAW REQUIREMENTS ---` section. Count every single unique tracking symbol present in the raw corpus (explicitly summing all unique [REQ-XXX] tags found).
  6. Let `Source_EXC` = Perform a comprehensive pass over the entire `--- RAW REQUIREMENTS ---` section. Count every single unique tracking symbol present in the raw corpus (explicitly summing all unique [EXC-XXX] tags found). (You MUST actively harvest them from the exception section).
  7. Let `Source_ARC` = Perform a comprehensive pass over the entire `--- RAW REQUIREMENTS ---` section. Count every single unique tracking symbol present in the raw corpus (explicitly summing all unique [ARC-XXX] tags found).
  8. Let `Source_DAT` = You MUST dynamically analyze the complete `--- RAW REQUIREMENTS ---` section to identify the absolute total number of core logical relational database entities (tables) required to support the functional architecture scope. You MUST allocate exactly one (1) unique tag count per independent logical data entity discovered (e.g., counting the distinct business domains needing dedicated persistence layer tables). Execute a strict real-time count of these core tables and assign the final computed integer value directly to this `Source_DAT` variable.
  9. Let `Source_NFR` = Perform a comprehensive pass over the entire `--- RAW REQUIREMENTS ---` section. Count every single unique tracking symbol present in the raw corpus (explicitly summing all unique [NFR-XXX] tags found).
- **CRITICAL DATA ASSIGNMENT MANDATE:** You MUST preserve these two variables in memory and inject their exact calculated integer values directly into their designated matching slots inside the table summary row layout below.
- **STRICT UNIQUE TASK MAPPING LAW:** You MUST enforce a strict 1:1 mathematical ratio between unique functional requirement tags ([REQ] and [EXC]) and the generated table rows. Every single unique [REQ-XXX] and [EXC-XXX] identifier found in the text MUST yield exactly one (1) single dedicated task row. You ARE ABSOLUTELY BANNED from splitting a single REQ tag into multiple separate frontend/backend rows.
</RULE>

<!--START_BACKLOG_SYNOPSIS_GRID-->

### [SYSTEM ARITHMETIC MATRIX]
> - **Total [REQ] Tags:** [Insert calculated integer of `Source_REQ`] Tags
> - **Total [EXC] Tags:** [Insert calculated integer of `Source_EXC`] Tags
> - **Total [ARC] Tags:** [Insert calculated integer of `Source_ARC`] Tags
> - **Total [DAT] Tags:** [Insert calculated integer of `Source_DAT`] Tags
> - **Total [NFR] Tags:** [Insert calculated integer of `Source_NFR`] Tags
> - ➡️ **Total SRS Tags:** [Insert computed integer of `Global_Source_Total`] Tags

| No. | Task | Technical Purpose / Deliverables Summary | Type | TagID |
| :--- | :--- | :--- | :--- | :--- |
| [Index] | [Task Title] | [Technical Objective] | [Type] | [Tag IDs] <!--REGISTERED_BACKLOG_TASK_ROW--> |
| **SUMMARY** | **Total Tracking Tags Covered:** [Insert computed integer of `Global_Covered_Total`] | **Total Tasks:** [Compute the absolute mathematical sum of all listed task rows and output the integer sum] | **Status:** [Insert computed value of `Verified_Status`] | **Coverage:** [Insert computed value of `Coverage_Status`] |

<!--END_BACKLOG_SYNOPSIS_GRID-->

{% endif %}
{# ─── END:CHUNK:PART_1_BACKLOG_4_1 ─── #}

{# ======================================================= #}
{# ─── START:CHUNK:PART_1_MATRIX_4_2 ─── #}
{% if force_full_export or (target_segment and target_segment.strip() == "PART_1_MATRIX_4_2") %}
### 🔭 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly the structured SynOpSis Matrix Phases table (inside the hidden HTML tags from `<!--START_PHASE_SYNOPSIS_GRID-->` to `<!--END_PHASE_SYNOPSIS_GRID-->`) mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= {{ num_phases }}) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
[STRICT TABLE EMITTING MANDATE]
- You MUST dynamically analyze the comprehensive tasks generated in the {{ phases_and_tasks_section }} section immediately to identify and break down the implementation tasks for the unified SynOpSis Matrix Phases table directly under this section (inside the hidden HTML tags from `<!--START_PHASE_SYNOPSIS_GRID-->` to `<!--END_PHASE_SYNOPSIS_GRID-->`).
- You MUST systematically divide and CONSOLIDATE the entire workload into EXACTLY AND ONLY {{ num_phases }} distinct rows. 
- CRITICAL INDEX CEILING: The maximum phase index allowed is {{ num_phases }}. You are ABSOLUTELY FORBIDDEN from generating Phase {{ num_phases + 1 }} or creating a separate phase row for every single backlog task. You MUST group and aggregate multiple tasks from {{ phases_and_tasks_section }} milestones.
- For each phase row, you are critically ordered to enforce absolute information symmetry by scanning all Tag IDs and Task types from the {{ phases_and_tasks_section }} section.
- CRITICAL INFRASTRUCTURE RULE: If you detect any DevOps, Cloud, Deployment, CI/CD, Containerization, or Infrastructure tasks in {{ phases_and_tasks_section }} (such as Docker, GCP, GKE, Kubernetes, or Git pipelines), you MUST explicitly list the path (e.g., './sources/infrastructure/devops/') in the Component column (the 4th column), and you MUST permanently declare 'DevOps' alongside Coder, Tester, Reviewer, and Doc in the 'Assigned Sub-Agent' column (the 6th column) for that targeted phase. DevOps agent could be [Docker], [GCP], or [GKE] belongs to its active operating persona. Do not drop the DevOps ([Docker], [GCP], or [GKE]) agent under any circumstance.
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of {{ max_days_per_phase }} days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than {{ num_phases }} phases, terminate the matrix setup immediately at phase N.
- LOCALIZED TABLE SCHEMA: The markdown table structure MUST match this layout exactly, with the bracketed header text translated into the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
- The SynOpSis Matrix Phases table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below (inside the hidden HTML tags from `<!--START_PHASE_SYNOPSIS_GRID-->` to `<!--END_PHASE_SYNOPSIS_GRID-->`).
- **SEQUENTIAL WORKLOAD EXHAUSTION LAW:** You MUST execute a strict sequential cursor loop scanning all registered tasks in the {{ phases_and_tasks_section }} section (the registered task rows contains the `<!--REGISTERED_BACKLOG_TASK_ROW-->` tag) without skipping any row. You ARE CRITICALLY BANNED from activating early termination filters upon discovering the final functional requirement tag (`[REQ-XXX]`). All non-functional, security, database, infrastructure, and documentation tasks located at the tail end of the backlog MUST be explicitly mapped into your phase matrices.
- **COMPREHENSIVE TAG WEIGHT AUDIT RAIL:** When evaluating your distribution metrics, every consolidated token notation (such as `[DAT-ALL (1 to X)]` or `[NFR-001 to NFR-Y]`) MUST be mathematically unrolled and counted at its full individual declaration weight. The total distributed tasks count must equals exactly with the total task rows in the {{ phases_and_tasks_section }} section (the registered task rows contains the `<!--REGISTERED_BACKLOG_TASK_ROW-->` tag).
- **DYNAMIC DEPENDENCY-DRIVEN STRATIFICATION LAW:** You MUST algorithmically distribute all backlog tasks discovered via {{ phases_and_tasks_section }} across the designated phase rows based strictly on their structural engineering hierarchy:
    * All foundational identity authorization middleware configurations, security schemas, and core routing architectures tagged with `[ARC]` or fundamental application code setup indicators MUST be chronologically routed into the initial slots (Phase 1 and Phase 2) to establish a secure API boundary.
    * All system data lifecycle persistence frameworks and structural database initializations tagged with `[DAT]` MUST be sequenced immediately following the core security boundary setup.
    * All high-level analytics, external integrations, user interface presentations, and scalable cloud/infrastructure automation components tagged with `[NFR]` MUST be consolidated strictly within the concluding phase rows (the final milestones of the project matrix).
- The SynOpSis Matrix Phases table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below (inside the hidden HTML tags from `<!--START_PHASE_SYNOPSIS_GRID-->` to `<!--END_PHASE_SYNOPSIS_GRID-->`).
- IMMUTABLE SYNOPSIS GRID WRAPPER MANDATE: When generating this section (inside the hidden HTML tags from `<!--START_PHASE_SYNOPSIS_GRID-->` to `<!--END_PHASE_SYNOPSIS_GRID-->`) SynOpSis Matrix Phases table, you ARE ABSOLUTELY AND CRITICALLY BANNED from dropping, omitting, or filtering out the technical hidden HTML comment anchors. You MUST explicitly enclose the entire generated table structure strictly between the literal tokens `<!--START_PHASE_SYNOPSIS_GRID-->` and `<!--END_PHASE_SYNOPSIS_GRID-->`.
- **MANDATORY ROW ANCHOR INJECTION:** Every single generated phase row inside the SynOpSis Matrix Phases table under this section (inside the hidden HTML tags from `<!--START_PHASE_SYNOPSIS_GRID-->` to `<!--END_PHASE_SYNOPSIS_GRID-->`) MUST contain the literal hidden HTML comment tag `<!--REGISTERED_PHASE_ROW-->`. You MUST explicitly place this tag inside the final cell (the Targeted Tag IDs, the 7th column), positioning it immediately after the tracking tags and right before the closing vertical pipe character `|` of that row (exact syntax pattern format: ` | ... [Tag IDs] <!--REGISTERED_PHASE_ROW--> |`). Any generated row that drops or filters out this structural comment anchor will cause a fatal deployment pipeline failure.
- **DYNAMIC DAY-RANGE MATCHING, TIMELINE QUANTIZATION AND FORMAT ENFORCEMENT LAWS:**:
    1. Every phase duration is strictly bound. You MUST evaluate the structural density of the generated matrix in the {{ phases_and_tasks_section }} section. Count the total unique Tag IDs mapped to each phase. Calculate the exact duration value K for that phase using the formula: K = Max(1, RoundUp(`Matrix_Source_Total_Tags` / 3)). The value of K MUST NOT exceed {{ max_days_per_phase }}.
    2. In the "Day Range" column (the 2nd column) of this table, you MUST format the day sequence starting from relative integer 1 to K for EACH individual phase row (e.g., Phase N: Day 1 - K). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
    3. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2). You are BANNED from hardcoding 'Day 1 - {{ max_days_per_phase }}' if the actual workload finishes earlier.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across {{ num_phases }} without any artificial padding or redundant agent forcing:
    1. Dynamic Resource Allocation Rule: A sub-agent (such as [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in this section table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps (such as [Docker], [GCP], or [GKE]) agents MUST be completely omitted from that specific row.
    2. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
    3. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
- STRICT SUB-AGENT FILE-EXTENSION & MARKDOWN FENCE COMPLIANCE LAW: You MUST strictly isolate physical file extensions based on the active operating persona and protect layout rendering from syntax breakage:
    1. For [Coder] and [Reviewer]: The target_component MUST strictly point to a physical executable source file ending with valid production extensions (e.g., .java, .ts, .sql).
    2. For [Tester]: The target_component MUST strictly utilize the semicolon pair format containing valid test suffix extensions (e.g., .java, .ts, .spec.ts) matching Case 1 or Case 2 patterns.
    3. For [Doc]: The target_component MUST permanently target granular, individual documentation files ending strictly with the .md extension, located inside ./sources/docs/.
    4. Markdown Render Integrity: You ARE ABSOLUTELY BANNED from outputting naked triple backticks (``` ...```) for inner specifications (such as ```sql:matrix ...``` or ```json ...```) inside an active root code fence. Every inner code segment block embedded within the day-by-day logs MUST utilize distinct delimiter tokens to ensure parsing isolation. You MUST strictly use exactly four backticks (````) or five backticks (`````) for the top-level parent envelope if the interior values require a three-backtick string literal expression.
- CRITICAL COMPACT PATCH & REVIEWER PARADIGM DIRECTIVE: The [Reviewer] MUST operate strictly in a sequential multi-step gating paradigm immediately following the [Coder] execution block inside the daily sub-task sequence. The Reviewer MUST systematically analyze the Coder's generated source assets to verify compiler stability and architectural compliance. If the compiler audit passes with zero issues, the Reviewer task freezes instantly with a no-op status. If and ONLY IF an explicit syntax anomaly, structural bottleneck, or compilation breakdown is detected, the Reviewer MUST trigger a defensive patching directive to execute immediate, target-specific code corrections. All patch instructions MUST be written as concise, structural pseudo-steps or high-density technical instructions; you are absolutely banned from embedding long walls of duplicate raw source code blocks inside the instruction description.
- GRANULAR DELIVERABLE CHECKLIST MANDATE: You MUST inject multiple verification and architectural tasks into the "Technical Deliverables Summary" column (the 5th column) for every phase row:
    1. For Tester: Force the inclusion of concrete validation targets, explicitly stating the production of JUnit suites, Integration Tests, and end-to-end (E2E) automation execution profiles.
    2. For Doc: Force the inclusion of architecture alignment requirements, explicitly stating the generation of system technical documentation blueprints and API technical specifications.
- BALANCED MULTI-AGENT TIMELINE PACKING: To fit multiple required agents within narrow day-ranges without inflating the timeline or violating the dynamic technical density ceiling, you MUST execute compact parallel or sequential distribution:
    1. Early phase timeline segments MUST be optimized for application-layer loops where [Coder] and [Doc] execute in parallel sub-tasks, immediately followed sequentially by [Reviewer] quality gates and [Tester] automated suites.
    2. Concluding phase timeline segments MUST be strictly cleared of application tasks and dedicated to sequential infrastructure workflows handled exclusively by [Docker], [GCP], and [GKE] sub-agents to deliver automated environment setups and deployment manifests.
- **ZERO OMISSION RULE:** If a Tag ID exists in the {{ phases_and_tasks_section }} section, it MUST appear in this section `4.2. MULTI-PHASE SYNOPSIS MATRIX`. Truncating or omitting tags to save space is a fatal error.
- **DYNAMIC SUB-AGENT ALLOCATION LAW:** The "Assigned Sub-Agent" column (the 6th column) MUST NOT be hardcoded. You MUST dynamically compute the exact subset of agents required based strictly on the "Type" column (the 4th column) values of all tasks mapped into that specific phase from {{ phases_and_tasks_section }}
    1. If the mapped tasks contain 'Application Code' -> Include: Coder, Tester, Reviewer, Doc.
    2. If the mapped tasks contain ONLY 'Enterprise Documentation' -> Include ONLY: Doc (Exclude Coder, Tester, Reviewer).
    3. If the mapped tasks contain 'DevOps Infrastructure' -> Include: Docker, GCP, GKE.
- **SOME SYNOPSIS MATRIX AUDIT ENGINE:** Before emitting the SynOpSis Matrix Phases table audit row (latest row of the SynOpSis Matrix Phases table), you MUST declare, calculate, and lock exactly two distinct internal mathematical variables within your execution memory layer based on real-time text parsing:
    1. Let **Matrix_Source_Total_Tags** = Dynamically scan the incoming `--- BACKLOG TASKS ---` section block. Parse every single task row's TagID column (the 5th column) to compute the absolute mathematical sum of all registered tracking tags (where any consolidated token like `[DAT-ALL (1 to X)]` MUST hold its full declaration weight of exactly X unique tags).
    2. Let **Matrix_Source_Tasks_Count** = Count the absolute total of discrete tasks successfully distributed from the incoming `--- BACKLOG TASKS ---` section block.
    3. Let **Matrix_Covered_Total_Tags** = Completely ignore your source count and perform a fresh, independent pass over the dynamic phase rows you generated inside this active table matrix above. Parse and manually calculate the absolute sum of all unique tracking tokens distributed inside the "Targeted Tag IDs" column (the 7th column) cells (enforcing true tag weight for consolidated tokens).
    4. Let **Matrix_Covered_Total_Tasks** = Completely ignore your source count and perform a fresh, independent pass over the columns of the table you just generated above (the SynOpSis Matrix Phases table). Manually sum every unique task explicitly written inside the `Task IDs Covered` cells.
    5. Let **Status_Coverage** = Compute (`Matrix_Covered_Total_Tags` / `Matrix_Source_Total_Tags`) * 100. If `Matrix_Covered_Total_Tags` equals `Matrix_Source_Total_Tags`, output the translated word for `Verified` in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}", followed by "(100%)". Otherwise, you MUST output the translated word for `FAILED` in the designated target language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}", followed by the exact calculated percentage fraction deficit.
    6. **CRITICAL DATA ASSIGNMENT MANDATE:** You MUST preserve these calculated variables in memory and inject their exact final values directly into their designated matching slots inside the table audit row (the lastest row of the SynOpSis Matrix Phases table).
- **ACTUAL PAYLOAD INTERPOLATION MANDATE:** You ARE STRICTLY BANNED from outputting raw template placeholders or generic bracketed strings like `[Phase N]` or `[List aggregated task numbers]`. You MUST dynamically iterate through the actual dataset rows computed in the baseline backlog section, extract the concrete module paths (e.g., `./sources/backend/...`), and compile real operational values for every cell.
- **TOTAL CELL TRANSLATION LAW:** Before committing the table to the output stream, you MUST completely translate and localize 100% of the newly generated table headers, cell values, technical summaries, and audit row text strings into the designated Target Output Language: "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}".
</RULE>

<!--START_PHASE_SYNOPSIS_GRID-->

### [MATRIX ARITHMETIC LIFECYCLE]
> - **Total Backlog Tasks:** [Insert calculated integer of `Matrix_Source_Tasks_Count`] Tasks
> - **Total Backlog Tags:** [Insert calculated integer of `Matrix_Source_Total_Tags`] Tags
> - **Total Distributed Tasks:** [Insert calculated integer of `Matrix_Covered_Total_Tasks`] Tasks
> - **Total Distributed Tags:** [Insert calculated integer of `Matrix_Covered_Total_Tags`] Tags

| Phase | Day Range | Task IDs Covered | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Phase N] | [Day 1 - KN] | [List aggregated task numbers, e.g., Task 1, Task 2] | [Group repository paths from baseline backlog section] | [Consolidate specialized engineering deliverables summary] | [Map required active agent signatures based on task type] | [Map individual tracking Tag IDs inline] <!--REGISTERED_PHASE_ROW--> |
| **Audit** | **Master Backlog Distribution Verification** | **Total Phases:** {{ num_phases }} | **Total BackLog Tags:** [Insert the calculated integer value of `Matrix_Source_Total_Tags`] | **Total Distributed Tags:** [Insert the calculated integer value of `Matrix_Covered_Total_Tags`] | **Total Distributed Tasks:** [Insert the calculated integer value of `Matrix_Covered_Total_Tasks`] | **Status & Compliance:** [Insert the calculated value of `Status_Coverage`] |

<!--END_PHASE_SYNOPSIS_GRID-->

{% endif %}
{# ─── END:CHUNK:PART_1_MATRIX_4_2 ─── #}

{# ======================================================= #}
{# ─── START:CHUNK:PART_2_PHASE_LOOP ─── #}
{% if force_full_export or (target_segment and target_segment.strip() == "PART_2_PHASE_LOOP") %}

{% if not target_phase_index or target_phase_index == 1 %}
## 🔬 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
{% endif %}
<COMMAND>
{# ────── START:CHUNK:PART_2_PHASE_LOOP:MANDATORY PROGRESSIVE GATING ENGINE ────── #}
{% if (target_segment and target_segment.strip() == "PART_2_PHASE_LOOP") %}
# STRICT OPERATIONAL AND SYNOPSIS MIRROR MANDATE FOR PHASE {{ target_phase_index }} OUT OF {{ num_phases }}:
  - OPERATIONAL SCOPE: You are now executing target segment '{{ target_segment }}' exclusively for Phase {{ target_phase_index }} out of {{ num_phases }}.
  - TIME BOUNDARY: You are strictly capped to generate chronological daily logs exactly from Day 1 to Day {{ max_days_per_phase }}. Absolutely FORBIDDEN from generating any text, sub-headers, or tasks for Day {{ max_days_per_phase + 1 }} or beyond. Match this duration with your declaration from Section `4.2. MULTI-PHASE SYNOPSIS MATRIX` in the {{ phases_and_tasks_section }} section. This phase MUST act as a strict structural mirror of the specific phase calculated from Section `4.2. MULTI-PHASE SYNOPSIS MATRIX` in the {{ phases_and_tasks_section }} section. You MUST generate an independent, complete detailed block below for this phase.
  - DYNAMIC MATRIX AUDIT: Scan the historic '## 4.2 MULTI-PHASE SYNOPSIS MATRIX' table generated in the previous step. Locate the exact row matching the phase rows that contains the `<!--REGISTERED_PHASE_ROW-->` tag.
  - AGENT ENFORCEMENT: Extract all assigned roles from the 'Assigned Sub-Agent' column (the 6th column) in that specific row (including Coder, Tester, Reviewer, Doc, Docker, GCP, GKE). You MUST explicitly output separate chronological sub-task blocks for EVERY single sub-agent declared in that row. If Docker/GCP/GKE infrastructure tokens are active, you are strictly commanded to engineer their cloud deployment and cluster setup logs inline. Do not drop any role.
  - COMPONENT ENFORCEMENT: Extract the exact 'Architectural Component / Module Path' from that row. All generated repository paths, migrations, and file configurations in this chunk MUST target that path.
  - REAL-TIME MATHEMATICAL SELF-AUDIT (CRITICAL): 
      * If this is the FINAL phase (Phase {{ num_phases }}), you MUST look inside the `--- HISTORY LEDGER MAP ---` section.
      * Count the total number of `<!--START_ATOMIC_SUB_TASK_NODE-->` string instances printed inside that map block (which represents the exact count of sub-tasks from all previous phases).
      * Mentally add the count of new sub-tasks you are currently generating in this exact response.
      * You MUST compute the absolute total sum integer and output it directly into the `TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5` field inside the properties block (```properties:cross_audit_ledger block). No formulas or string placeholders allowed.
  - OUTPUT RESTRICTION: Absolutely DO NOT output or duplicate the main global document titles, table controls, project context overviews, or other phases. Start your generation immediately from the localized sub-header: '### Phase {{ target_phase_index }}'. You MUST wrap your output by the hidden HTML anchors `<!--START_PHASE_INDEX-->` and `<!--END_PHASE_INDEX-->`

# DYNAMIC CEILING BOUNDARY ENFORCEMENT:
  - The day-by-day logs of this phase MUST strictly map to the exact day range defined for this phase from Section `4.2. MULTI-PHASE SYNOPSIS MATRIX` in the {{ phases_and_tasks_section }} section.
      * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
      * You ARE ABSOLUTELY AND CRITICALLY BANNED from copy paste, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
  - **BLOCK DAY ENCAPSULATION PARADIGM:** For every individual day-by-day log block generated, you MUST strictly execute this exact sequence: first, completely compile and format the daily content; second, fully translate that entire day block (including headers, sub-tasks, and labels) into the designated Target Output Language; and third, tightly encapsulate that finalized translated day block inside the exact matching metadata comment tags (`<!--START_DAY_LOG_INDEX-->` on its own standalone line immediately BEFORE the day block, and `<!--END_DAY_LOG_INDEX-->` on its own standalone line immediately AFTER the day block) before streaming the finished block to the output pipeline.
  - **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside this section (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for this phase block. You are permanently forbidden from bleeding the global progressive timeline into these sections.
  - The total days of this phase MUST NOT exceed the absolute upperbound of {{ max_days_per_phase }} days.
  - You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for this phase are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to {{ max_days_per_phase }} is completely banned.
  - **STRICT PHASE INDEX COUPLING MANDATE:** You ARE STRICTLY FORBIDDEN from generating any text, sub-headers, logs, or sub-task blocks for other phases. You MUST contextually freeze your execution cursor and apply a hard system stop the exact microsecond you complete the output buffer wrapper for Phase {{ target_phase_index }}.
  - **TARGETED SINGLE-PHASE ISOLATION RAIL:** Your entire response stream MUST focus exclusively on the requirements, tasks, components, and tag identifiers allocated to Phase {{ target_phase_index }}. 
{% endif %}
{# ────── END:CHUNK:PART_2_PHASE_LOOP:MANDATORY PROGRESSIVE GATING ENGINE ────── #}

{% if force_full_export %}
# STRICT 1:1 SYNOPSIS MIRROR MANDATE:
- Section 5 MUST act as a strict structural mirror of the dynamic phases calculated in Section 4. You MUST generate an independent, complete detailed block below for EVERY phase sequence from Phase 1 up to Phase N (where N <= {{ num_phases }}). Absolutely no phase that has been calculated in section 4 can be omitted.
- Truncating, omitting, or combining phases is an absolute pipeline violation. You are strictly commanded to detail every phase that appeared in your Section 4 table.

# DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- For each active Phase [X], the day-by-day logs MUST strictly map to the exact day range defined for that phase in Section 4.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from chép lặp lại, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside Section 5 (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for EVERY single phase block (e.g., Phase 1 contains DAY 1, DAY 2; Phase 2 MUST restart and contain exactly DAY 1, DAY 2). You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days within any single phase MUST NOT exceed the absolute upperbound of {{ max_days_per_phase }} days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for Phase [X] are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to {{ max_days_per_phase }} is completely banned.

- **MONOLITHIC GENERATION EXECUTION RAIL:** You MUST sequentially execute and expand the following structural block for EVERY calculated phase from Phase 1 up to Phase N (where N = {{ num_phases }}) in a continuous stream. For each iteration, dynamically substitute the index X with the current phase number.
{% endif %}
</COMMAND>

{# ─── START:CHUNK:PART_2_PHASE_LOOP:PHASE_INDEX ─── #}
<!--START_PHASE_INDEX-->

{# ─── START:CHUNK:PART_2_PHASE_LOOP:PHASE_X ─── #}
### 📈 [Translate "Phase" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"] {% if force_full_export %}[X]{% else %}{{ target_phase_index }}{% endif %} - [Emit the translated of this phase from Section `4.2. MULTI-PHASE SYNOPSIS MATRIX` in the {{ phases_and_tasks_section }} section]
- **[Translate "Phase Core Objective & Purpose" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"]:** [Detailed technical explanation of what this phase achieves and its functional goals, fully translated into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}]
- **[Translate "Target Physical Directory Matrix Map" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"]:** List all specific file paths underneath `./sources/` initialized or modified in this phase. Every single line path generated MUST be appended with its tracking Tag IDs inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.
- **[Translate "Database Schema DDL SQL Specification" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"] [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
    * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ` ```sql:matrix ` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
    * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>
- **[Translate "API and Event Routing Contracts" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"] [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).
- **[Translate "Phase Localized Exception Handlers" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"] [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into {% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}.

{# ─── START:CHUNK:PART_2_PHASE_LOOP:PHASE_X:DAY_Y ─── #}
#### 📅 [Translate "Chronological Day-by-Day Sub-Agent Task Distribution Logs (Phase {% if force_full_export %}[X]{% else %}{{ target_phase_index }}{% endif %})" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"]

<!--START_DAY_LOG_INDEX-->

##### 📅 [Translate "DAY" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"] [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
<RULE>
- **SUB-TASK ATOMIC WRAPPER LAW:** Every single sub-task node MUST be explicitly and strictly wrapped within its own dedicated opening (`<!--START_ATOMIC_SUB_TASK_NODE-->`) and closing (`<!--END_ATOMIC_SUB_TASK_NODE-->`) markers. You are PERMANENTLY FORBIDDEN from generating a new sub-task header until the previous sub-task node has been legally closed with its dedicated newline tag. Follow this exact raw structure layout:
</RULE>

###### 🌿 [Translate "SUB-TASKS" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"] [Z]: SHORT SPECIFIC SUB-TASK TITLE
<!--START_ATOMIC_SUB_TASK_NODE-->
<RULE>
- **Local Sub-Task Chrono Reset Law:** The sub-task index variable Z MUST natively reset and restart from 1 for EACH individual calendar day element generated (e.g., Day 1 contains SUB-TASK 1, SUB-TASK 2; Day 2 MUST strictly restart and contain exactly SUB-TASK 1, SUB-TASK 2). Progressively compounding or accumulating sub-task indices across daily boundaries is a critical framework violation.
<RULE>
* **[Translate "Sub-Agent Workflow Specialization" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"]:**
<RULE>
You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.
</RULE>
* **[Translate "Targeted Tag IDs" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"]:**
<RULE>
Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].
</RULE>
* **[Translate "Target Component file path" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"] (target_component):**
<RULE>
Insert the explicit physical path starting with `./sources/` or Tester semi-colon pair syntax based strictly on the active persona domain. Append its targeted Tag IDs inline here.
</RULE>
* **[Translate "Low-Level Technical Task Instruction" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"]:**
<RULE>
Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs.
</RULE>

# DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
- STRICT TAG FILTER LAW: You are ABSOLUTELY FORBIDDEN from outputting or mapping any Tag IDs ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX]) inside this active phase block UNLESS that specific Tag ID was explicitly assigned to 'Phase {% if force_full_export %}[X]{% else %}{{ target_phase_index }}{% endif %}' inside the Section 4.2 Multi-Phase Synopsis Matrix table. Completely isolate the data architecture of this targeted phase.
* **[Translate "Database Schema DDL SQL Specification" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"] [DAT-XXX]:**
<RULE>
You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the specific sub-task execution involves physical database migrations, DDL scripts, index creations, or schema constraints, you MUST dynamically render the complete, production-ready ANSI SQL blocks inside this section. If the targeted sub-task handles FrontendUI, document updates, or cloud pipelines with NO database mutations, you MUST completely delete and purge this entire bullet point from the daily output buffer.
</RULE>
* **[Translate "API and Event Routing Contracts" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"] [REQ-XXX], [ARC-XXX]:**
<RULE>
You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the sub-task execution directly involves backend application controllers, routing protocols, microservice API specifications, or event-driven topic bindings, you MUST dynamically generate the complete contract schemas or payload objects inside this section. If the task covers infrastructure or frontend styling alone, you MUST completely prune and delete this entire bullet point from the daily output buffer.
</RULE>
* **[Translate "Phase Localized Exception Handlers" into the target language "{% if language and language.strip() != "" %}{{ language }}{% else %}English{% endif %}"] [EXC-XXX]:**
<RULE>
You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
</RULE>

<!--END_ATOMIC_SUB_TASK_NODE-->

<!--END_DAY_LOG_INDEX-->
{# ─── END:CHUNK:PART_2_PHASE_LOOP:PHASE_X:DAY_Y ─── #}

{# ─── START:CHUNK:PART_2_PHASE_LOOP:AUDIT ─── #}
{% if force_full_export or target_phase_index == num_phases %}

### 🕵️ MANDATORY REAL-TIME ARCHITECTURAL CROSS-AUDIT LEDGER REPORT:
- **TIMING LOCATION:** This compliance ledger MUST be rendered exclusively at the absolute bottom of Section 5, immediately following the final day log of the final phase.
- Immediately beneath the final Phase log (Phase {{ num_phases }}) and before closing Section 5, you MUST execute a strict internal mathematical self-audit of the entire assembled architecture. 
- You MUST compile and render an isolated, clean Markdown Compliance Report block utilizing the exact Technical English structure below. 
- You are critically ordered to dynamically compute the real-world values based strictly on the current generation instance metrics—no hardcoding or static placeholder strings.

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2={% if force_full_export %}{{ num_phases }}{% else %}computed_integer_N{% endif %}
TOTAL_PHASES_EXPECTED_BY_PARAMETERS={{ num_phases }}
PHASE_COUNT_COMPLIANCE_STATUS=Verified_{{ num_phases }}
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER={{ max_days_per_phase }}
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE={% if force_full_export %}{{ max_days_per_phase }}{% else %}computed_highest_day_integer_found_in_section_5{% endif %}
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1={{ total_tasks_registered }}
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=[Compute the exact final unified integer sum of all listed atomic sub-task nodes generated across all phases]
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

- **MANDATORY CRITICAL FAILURE CRITERIA:** If your calculated total discrete sub-tasks across all phases does not mathematically match the exact count of tasks registered in the master backlog, or if any individual phase duration breaks the ceiling of `{{ max_days_per_phase }}`, you MUST instantly trigger an internal framework exception, re-compile your attention heads, and dynamically re-distribute the allocation matrix to enforce 100% plan symmetry before emitting the final text stream.

{% endif %}
{# ─── END:CHUNK:PART_2_PHASE_LOOP:AUDIT ─── #}

<!--END_PHASE_INDEX-->
{# ─── END:CHUNK:PART_2_PHASE_LOOP:PHASE_INDEX ─── #}

{% endif %}
{# ─── END:CHUNK:PART_2_PHASE_LOOP ─── #}

{# ======================================================= #}
{# ─── START:CHUNK:PART_3_FINAL ─── #}
{% if force_full_export or target_segment == "PART_3_FINAL" %}

### GROUNDING CONTEXT FROM PREVIOUS STEPS
{% if not force_full_export %}
<RULE>
All the detailed phase logs generated in the `--- GENERATED PHASES CONTEXT ---` section. You MUST review them to ensure the universal security codes match the tech stack implemented.
</RULE>
{% endif %}

## ☣️ 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
- **SQL Injection (SQLi) Absolute Countermeasures:** Rule parameters for prepared statements, positional query parameters, and dynamic sorting input Whitelists.
- **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Layout standards for automated context sanitization, JSX auto-escaping, and dynamic injection of strict CSP headers (`unsafe-inline` restriction).
- **Multi-Tenant CORS Security Rails:** Configurations for origin wildcard prohibitions and dynamic tenant origin database metrics validation.
- **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Rules for automated masking interceptors (`@JsonSerialize`) and log scrubbing thresholds.

## 📱 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
- **Capacitor Mobile Hybrid Compliance Rails:** [IF Mobile active] Rules for dynamic client-side fetching, absolute URL addressing, hydration safeguards, native storage abstractions (`@capacitor/preferences`), and hardware back-button interception.
- **Internationalization (i18n) & Dynamic SEO Injection:** Edge-layer locale recognition middleware architectures, hreflang dynamic hypermedia control injection, and search crawler robots indexing limits.

## 🚀 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
- **Daily Workspace Forking Isolation:** Programmatic forking controls for branch `features/development-phase-X-day-Y` (`X` is the number of phase, from 1 to N, where N <= {{ num_phases }}; `Y` is the day number in phase, it will start from 1 for each phase).
- **Validation Guard Pipeline Gates:** Execution rules for compilation verification, automated code coverage goals (`>= 85%`), and context summary serialization logs.

### 📊 MATRIX COVERAGE CHECK MANDATE

`[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: X, TOTAL ARC TAGS: Y, TOTAL EXC TAGS: Z, TOTAL DAT TAGS: V, TOTAL NFR TAGS: W. ZERO UNASSIGNED CODES FOUND.]`

{% endif %}
{# ─── END:CHUNK:PART_3_FINAL ─── #}

{% if not force_full_export %}
<!--END_{{ target_segment }}-->
{% endif %}

{# ======================================================= #}
{# ─── INJECTED REFERENCE CONTEXT ─── #}

<PROJECT_SOURCE_GROUNDING_DATA>
--- RAW REQUIREMENTS ---
{{ project_requirements }}
--- END REQUIREMENTS ---
</PROJECT_SOURCE_GROUNDING_DATA>

{% if not force_full_export and target_segment and (target_segment.strip() in ["PART_1_MATRIX_4_2", "PART_2_PHASE_LOOP"]) %}
<PROJECT_BACKLOG_TASKS_DATA>
--- BACKLOG TASKS ---
{{ master_backlog_context }}
--- END BACKLOG TASKS ---
</PROJECT_BACKLOG_TASKS_DATA>
{% endif %}

{% if not force_full_export and target_segment and target_segment.strip() == "PART_2_PHASE_LOOP" %}
<HISTORIC_LEDGER_MAP>
--- HISTORY LEDGER MAP ---
{{ historic_ledger_map }}
--- END HISTORY LEDGER MAP ---
</HISTORIC_LEDGER_MAP>
{% endif %}

{% if not force_full_export and target_segment and target_segment.strip() == "PART_3_FINAL" %}
<GENERATED_PHASES_CONTEXT>
--- GENERATED PHASES CONTEXT ---
{{ generated_phases_context }}
--- END GENERATED PHASES CONTEXT ---
</GENERATED_PHASES_CONTEXT>
{% endif %}
