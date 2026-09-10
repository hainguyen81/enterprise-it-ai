{% set target_language = language if language and language.strip() != "" else "English" %}
# 🚨 MANDATORY ARCHITECTURAL GENERATION CODES
*You must fully engineer the blueprint report by strictly implementing exactly three engineering protocols:*

#### 🎯 PROTOCOL 1: Dynamic Topology Path Prefixing
  - You MUST dynamically match the physical directory file path masks to the active system topology extracted from the raw requirements.
  - Every single generated path parameter string inside the log (`target_component`) MUST utilize the strict Unix forward-slash `/` character as the structural directory delimiter.
  - You are CRITICALLY AND PERMANENTLY FORBIDDEN from utilizing the package dot notation `.` inside folder names or file boundaries.
  - Do NOT emit relative paths that assume a sub-module directory is the root:
    * *IF Backend logic/layer is active:* All backend code, services, database schemas, and database tests must reside strictly under: `./sources/backend/` (If Microservices topology is active, you MUST utilize the alphanumeric lowercase service name as the sub-folder path, e.g., `./sources/backend/<service-name>/`).
    * **DYNAMIC JAVA PACKAGE INVARIANT LAW:** You ARE CRITICALLY ORDERED to purge and overwrite the boilerplate package structure `com.example` in all physical file paths and raw file content streams. You MUST dynamically build and enforce the enterprise naming authority convention layout pattern: `org.nlh4j.{{ project_name | lower | replace(" ", "") | replace("_", "") | replace("-", "") }}.<isolated_microservice_domain_alphanumeric>`.
      - **SUPREME SERVICE EXTREMITIES SEPARATION LAW:** Inside every single target_component path asset and internal Java syntax stream (`package ...;`, `import ...;`), you ARE CRITICALLY BANNED from using the parent project root name as a global generic sub-package layer. You MUST programmatically extract the specific, isolated microservice identifier from the current phase row context (e.g., extracting the precise service prefix string such as 'userservice', etc., tailored to that specific active module). You MUST enforce this atomic directory separation rule with 100% validation string compliance. Any leakage that flattens separate microservice domain modules into a single shared package topology triggers an immediate compliance framework crash.
    * **STRING SANITIZATION CRITERIA:** For the project name `{{ project_name }}`, you MUST evaluate it into its pure unpunctuated lowercase alphanumeric primitive token `{{ project_name | lower | replace(" ", "") | replace("_", "") | replace("-", "") }}`. All code references, target component directory matrices, and internal file file string primitives (`package ...;`, `import ...;`) MUST be printed matching this layout strictly (e.g. directory path: `./sources/backend/user-service/src/main/java/org/nlh4j/{{ project_name | lower | replace(" ", "") | replace("_", "") | replace("-", "") }}/userservice/User.java`, and file syntax: `package org.nlh4j.{{ project_name | lower | replace(" ", "") | replace("_", "") | replace("-", "") }}.userservice;`). Any leakage of `com.example`, space characters, hyphen characters `-` or underscore characters `_` inside Java structures triggers an immediate compliance reject.
    * *IF Frontend logic/layer is active:* All client interfaces, responsive views, mobile bundles, and web tests must reside strictly under: `./sources/frontend/` (or `./sources/frontend/<app-name>/` if multiple client applications exist. Skip entirely if project is Backend-only).
    * *IF DevOps infrastructure logic is active:* All deployment manifests, Dockerfiles, GKE orchestrations, and cloud provisioning scripts must reside strictly under: `./sources/infra/`.
    * *For Document Asserts:* Prefix paths strictly with: `./sources/docs/`.
    * For alternative topologies (AI/Data, IoT, Embedded): Paths must strictly map to logical root subdirectories matching the service domain layer under `./sources/`.
  - Any component path emitted that replaces a forward slash `/` with a directory dot `.` triggers a fatal pipeline integrity exception.

#### 🗄️ PROTOCOL 2: Granular Ceilings-Compliant Task Logs
  - For each calculated phase necessary to cover the BA inputs (Up to the absolute maximum ceiling of {{ num_phases }} phases), supply a clean chronological daylog breakdown (Up to the absolute ceiling of {{ max_days_per_phase }} days per phase). Every single day generated MUST explicitly define the specific assigned sub-agent persona ('Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'), the low-level technical step target, the exact tracking Tag IDs, and the explicit physical relative file path (`target_component`).

#### 🧮 PROTOCOL 3: 100% Vertical Tag Traceability Coverage (ZERO BUNDLING POLICY)
  - Every single feature, entity, database table column, validation, exception, or infrastructure component outlined across your report MUST be strictly prefixed or appended with the exact corresponding Tag IDs (`[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`, `[DOC-XXX]` or all tag IDs that their format patterns like this `[XXX-XXX]`) inherited from the requirements.
  - **THE POLYMORPHIC TAG EXTRACTION LAW:** When scanning the raw requirements from the `<PROJECT_SOURCE_GROUNDING_DATA>` block, your context parser MUST execute a resilient token-stripping pass. You MUST recognize, extract, and count any requirement token hidden inside nested wrappers or parentheses (such as `([REQ-XXX])`, `**[REQ-XXX]**`, or loose text strings). Strip away all outer non-bracket characters and evaluate the bare functional identifier inside (e.g., extracting `[REQ-001]` cleanly).
  - You ARE CRITICALLY AND PERMANENTLY BANNED from dropping the count or setting the arithmetic variables (`Source_REQ`, `Source_DAT`) to 0 if the functional text physically documents these milestone boundaries.
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
    * Strict Boundary: You MUST permanently isolate the `target_component` path layout syntax based strictly on the target technology layer and test modality with zero cross-contamination:
        1. **BACKEND UNIT TEST WINDOW & DIRECTORY ISOLATION:** For regular modular unit tests, you MUST strictly employ a two-element layout formatted as the semicolon-separated pattern: `<production_source_file_path>;<corresponding_test_class_file_path>`. Your execution engine MUST dynamically evaluate the filename extension and subdirectory tree of the target component dynamically. You ARE CRITICALLY BANNED from injecting the `INTEGRATION_SCOPE;` prefix token into application layer source files; this prefix notation is exclusively decoupled and restricted to top-level parent project build descriptors, DevOps deployment manifests, and frontend Next.js web bundles.
        2. **CORE BUILD DESCRIPTOR EXCLUSION LAW:** If the target under verification by the [Tester] agent involves multi-module build descriptors, pipeline integration scripts, or scaffolding verification (assets matching `pom.xml`, `package.json`, or `tsconfig.json` under tracking symbol `[ARC-000]` or `[DOC-001]`), you ARE ABSOLUTELY BANNED from mapping the raw build descriptor file directly as the target component. You MUST forcefully target the explicit integration suite script or validation pipeline file, applying the exact hard-coded prefix layout: `INTEGRATION_SCOPE;./sources/infra/test/maven-build-integration.sh` or `INTEGRATION_SCOPE;./sources/backend/user-service/src/test/java/org/nlh4j/membershiphub/userservice/UserServicesTestSuite.java`. Any attempt to run an integration test scope directly on a naked `pom.xml` configuration asset is strictly banned.
        3. **BACKEND INTEGRATION TEST WINDOW:** For backend cross-cutting integration, performance, or Gatling load test scopes where an isolated individual source file cannot be mapped, you MUST strictly enforce exactly two elements: `INTEGRATION_SCOPE;<absolute_path_to_integration_test_file>` (e.g., `INTEGRATION_SCOPE;./sources/backend/user-service/.../UserIntegrationTest.java`).
        4. **FRONTEND APPLICATION TEST WINDOW:** For 100% of frontend applications, component styling, or Next.js web test scopes where a production source file cannot be isolated inline, you MUST permanently apply the explicit hard-coded token prefix layout containing exactly two elements: `INTEGRATION_SCOPE;<absolute_path_to_frontend_test_file>` (e.g., `INTEGRATION_SCOPE;./sources/frontend/web-app/src/test/Notification.spec.ts`).
        * **MUTUALLY EXCLUSIVE GATEWAY:** You ARE CRITICALLY AND ABSOLUTELY BANNED from mixing, compounding, or concatenating these distinct layouts together. Emitting a three-segment path or leaking an `INTEGRATION_SCOPE` token inside a Java unit test string triggers an immediate architectural framework collapse.
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
    * **STRICT COMPLETENESS AND ANTI-TRUNCATION DIRECTIVE:** You are ABSOLUTELY FORBIDDEN from creating placeholder "filler days" or empty sync task sessions to artificially pad the timeline. However, you ARE CRITICALLY BANNED from using this anti-filler rule as a pretext to omit, truncate, or drop any physical file paths registered inside the 4th column of the synopsis matrix. Anti-filler strictly means banning non-engineering sync activities. 100% of the individual file layers (Controllers, Services, Repositories, Entities, and DTOs) explicitly discovered in the Synopsis Matrix row cell MUST be comprehensively unrolled into active day logs context. Every single mapped file path asset MUST possess its dedicated Coder implementation log and Tester validation log pairing. You MUST adaptively expand the local chronological day headers inside the active chunk output stream up to the parameter ceiling of {{ max_days_per_phase }} days if the high-density asset list demands more execution slots to achieve zero structural truncation.
    * Every generated day must contain high-utility, actionable enterprise engineering tasks. No empty or duplicate logs.
  - **Strict Partition Cap:** You ARE CRITICALLY BANNED from allocation density skew where a single phase contains > 30% of the total functional `[REQ]` tags.
  - **Sequential Gradient Mandate:** You MUST implement a mathematically progressive engineering lifecycle across the EXACT {{ num_phases }} rows tailored dynamically to the active topology layers discovered in the `stack_matrix`:
    * Phase 1: Exclusively Scaffolding [ARC-000] and Core Database Schema Migrations [DAT-ALL] (if PERSISTENCE_LAYER_REQUIRED=true). Absolutely NO application endpoint implementation, controller routing code, or active functional orchestration business logic is permitted in this phase.
    * Phase 2 to Phase {{ num_phases - 1 }}: Linear, balanced, and symmetric distribution of all discovered functional business features, endpoints, and components ([REQ-XXX]). Every business validation routine and exception workflow handling code ([EXC-XXX]) MUST remain strictly atomic, encapsulated inline within the exact sub-task node of its primary functional parent requirement row. You are CRITICALLY BANNED from leaking exception handling code into Phase 1 or Phase {{ num_phases }}.
    * Phase {{ num_phases }}: Dedicated strictly to Cross-Cutting System Security Countermeasures [NFR], Performance optimization whitelists, Cloud Infrastructure Delivery/DevOps provisioning scripts (if DEVOPS_LAYER_REQUIRED=true), and absolute Technical Reference Document closing logs. Absolutely NO core functional business logic coding or error exception handling block implementations are allowed in this final phase.
  - **Placeholder Prohibition:** Any phase that outputs generic summaries, loops past infrastructure configuration lines, or serves as a dummy container to pad the phase quota triggers an immediate framework integration crash.

#### 🚨 CRITICAL FULL TRANSLATION MANDATE
  - The target generation language for all human-readable outputs is permanently bound to: {{ target_language }}. Everything MUST be translated into {{ target_language }}, except for the explicit Technical English core tokens protected by system mandates.
  - You MUST fully translate 100% of all headers, section titles, sub-headers, descriptive text, sentences, explanations, phase objectives, phase descriptions, phase section headers / titles / sub-headers / pullet titles, and task instructions into the designated target language (include following the translation rules that was defined in `STRICT SEMANTIC INVARIANT LOCALIZATION & TRANSLATION RAILS`).

#### 🚨 DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
  - Target Output Language Context: {{ target_language }}
  - You MUST dynamically translate 100% of all user-facing structural components, table headers, phase layouts, and list prefixes into the designated Target Output Language Context.
  - 🚨 MANDATORY STRUCTURAL MAPPING DIRECTIVE (Translate these dynamically based on the target language context):
    * All Section, Sub-section, Document Control table grid headers, and item label tokens MUST be translated contextually into the Target Output Language prior to cell alignment formatting.
    * All Table Headers MUST be translated contextually into the Target Output Language.
    * All list Prefixes and Phase Titles MUST be translated contextually into the Target Output Language.
    * You ARE CRITICALLY AND PERMANENTLY BANNED from emitting any literal instruction verbs, meta-text templates, or brackets containing uppercase commands like "Translate" or "SUB-TASKS" into the output pipeline (e.g., leaking raw strings like `[Translate "Phase" into the target language...]` triggers an immediate infrastructure system crash).
    * You MUST treat every bracketed layout token exclusively as a dynamic runtime registry lookup key. Prior to character emission, your internal execution engine MUST evaluate the key against the targeted "{{ target_language }}" vocabulary schema map.
    * You MUST translate and substitute the configuration hooks using a strict 1:1 linguistic dictionary matrix pass:
      - Map `Phase` to its exact literal structural noun equivalent inside the "{{ target_language }}" vocabulary database.
      - Map `DAY` to its exact literal chronological milestone noun equivalent inside the "{{ target_language }}" vocabulary database.
      - Map the inner sub-task layout fields (`Sub-Agent Workflow Specialization`, `Targeted Tag IDs`, `Target Component file path`, `Low-Level Technical Task Instruction`) directly to their corresponding native contextual descriptors in "{{ target_language }}" before streaming tokens.
    * Every single structural layout element must open clean, resolve dynamically, and close clean with zero template leakage.
  - 🚨 SPECIFIC SECTION CONTENT TRANSLATION RAILS:
    * For Sections 1 & 2: Translate all comprehensive technical overviews, main headers, sub-headers, section titles, labels, table columns, ecosystem descriptions, stack details, and asynchronous channel analysis.
    * For Section 3: Translate all , main headers, sub-headers, section titles, labels, table columns, descriptions of workspace rules, compliance standards, and condition explanations.
    * For Section 4 & 5: Translate all table headers (except technical tokens), main headers, sub-headers, section titles, labels, table columns, deliverables summaries, core objectives, localized exception handling descriptions, and low-level task instruction texts.
    * For Sections 6, 7 & 8: Translate all detail descriptions of injection countermeasures, main headers, sub-headers, section titles, labels, table columns, security rails, hybrid compliance rules, SEO mechanisms, and pipeline git flow gating rules.
  - 🚨 RIGID TECHNICAL BOUNDARY & TECHNICAL EXCLUSION ZONE (DO NOT TRANSLATE): You are strictly forbidden from translating or modifying technical structures, including:
    * Crucially, this exclusion zone applies strictly to raw data primitives. You MUST naturally, contextually, and fully translate 100% of all chronological timeline indicator milestones (specifically including all uppercase, lowercase, or bolded Phase and Day header strings, e.g., 'Phase X', 'DAY Y') into the designated target language context matching the specified variable: {{ target_language }}. Leaking the naked raw English tokens "PHASE" or "DAY" inside the final markdown specialization report headers is a fatal violation of the localization law.
    * All markdown syntax layout operators (`|`, `:`, `-`, `*`) and numerical hierarchy indices (e.g., `1.`, `1.1.`) MUST remain unaltered to preserve the document layout integrity.
    * 🚨 **SUPREME ARCHITECTURE HEADER TRANSLATION MANDATE:** You MUST fully translate into the target language 100% of high-level overview terms, system architecture descriptions, or blueprint documentation titles (even if they are written in full uppercase or encapsulated inside strong markdown bold formatting `**`, such as: `SYSTEM OVERVIEW`, `CORE ARCHITECTURE MODALITY`, `PROJECT CONTEXT`). You are STRICTLY FORBIDDEN from treating these architectural section names as technical identifier strings to bypass translation. The structure `## 🏛️ 1. SYSTEM OVERVIEW` MUST be processed and rendered exactly as `## 🏛️ 1. TỔNG QUAN HỆ THỐNG`.
    * All code blocks (SQL DDL, JSON schemas, JSON payloads, Java, etc.) and Mermaid flow diagrams.
    * All tracking Tag IDs (e.g., `[REQ-XXX]`, `[DAT-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[ARC-XXX]`, `[DOC-XXX]` or all tag IDs that their format patterns like this `[XXX-XXX]`).
    * All raw physical file paths starting with `./sources/` and the Tester semi-colon pair syntax.
    * All strict literal tokens for Sub-Agent names (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
    * All hidden HTML comment tags, system data splitters, and data extraction anchors (e.g., `<!--START_DELIMITTER-->`, `<!--END_DELIMITTER-->`, `[PAYLOAD_DELIMITER]`, `<!--START_...-->` or `<!--END_...-->`). These must remain in their original raw character format to prevent backend processing errors.
    * Retain all raw engineering strings: file paths (`./sources/...`), code blocks, Tag IDs (`[REQ-XXX]`, `[DAT-XXX]`, etc.), and strict Sub-Agent literal tokens (`Coder`, `Tester`, `Reviewer`, `Doc`, `Docker`, `GCP`, `GKE`).
    * **Static Pass Tag `<NO_TRANSLATION>...</NO_TRANSLATION>`**: Used for static assets. You MUST pass 100% of the internal content literal without any localization, alteration, processing, or computation.
    * **Dynamic Generation Tag `<DYNAMIC_DATA_ENGLISH_ONLY>...</DYNAMIC_DATA_ENGLISH_ONLY>`**: Used for dynamic instructions or mock templates. You MUST process, evaluate variables, and dynamically compute the generation outputs inside this block. However, 100% of the newly generated text stream resulting from this block MUST be strictly rendered in **Technical English** only, with an absolute ban on translation into the target language. The boundary tags MUST be stripped from the final output stream upon execution.
  - **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in {{ target_language }} while completely freezing all technical paths, tags, and block codes.


{# ─── START:RULES FOR CHUNK OPERATION ─── #}
#### MANDATORY SEGMENT INSTRUCTION:  
{% set ref_section_4_1 = "4.1" if force_full_export else "`<PROJECT_BACKLOG_TASKS_DATA>`" %}
{% set ref_section_4_2 = "4.2" if force_full_export else "`<PROJECT_BACKLOG_TASKS_DATA>`" %}
{% set ref_tasks_table = "the Master Product Tasks Backlog table inside the " + ref_section_4_1 + " section" %}
{% set ref_phases_table = "the SynOpSis Matrix Phases table inside the " + ref_section_4_2 + " section" %}
{% if force_full_export %}
- You MUST include every single section below without exception to satisfy enterprise compliance requirements
{% else %}
- **ABSOLUTE RAW EMISSION LAW (ZERO CODE-BLOCK WRAPPERS):** You are STRICTLY BANNED from wrapping your entire multi-line output response inside triple backticks markdown envelopes (i.e., ```markdown ... ```). You MUST emit your architectural structure directly into the token stream as pure, un-enveloped lines of standard vertical markdown layout text. You ARE CRITICALLY REQUIRED to retain all structural newline carriage returns, literal newline characters or line break between headers, lists, and table rows to ensure proper document rendering. Any dynamic leakage of wrapping backticks triggers an immediate infrastructure system crash.
- **ZERO-THINKING PURE LAYOUT EMISSION LAW:** You ARE ABSOLUTELY AND CRITICALLY BANNED from generating or leaking any intermediate thinking processes, internal reasoning, analytical commentary, introductory prose, or metadata summaries that are not explicitly specified inside the raw template layout skeleton.
  * STRICT SYNTAX INVARIANT: Your entire output buffer MUST contain 100% pure, un-fenced layout components matching the required visual structure exactly.
  * ZERO COMPRESSION BANNED FROM BULLETS: For every section that contains table, you ARE PERMANENTLY FORBIDDEN from compressing, transforming, or outputting data of these tables as bullet points (`*` or `-`) below or outside. Every single discovered workload asset of them MUST be injected exclusively and directly into its corresponding row cell inside the physical Markdown table structure (`|`). Any text string, narrative, or bullet list leaked outside the target table cell boundaries will trigger a fatal integration failure.
{% endif %}
{# ─── END:RULES FOR CHUNK OPERATION ─── #}


{# ======================================================= #}
{# ─── MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT) ─── #}
{# ======================================================= #}
### 📋 MANDATORY OUTPUT STRUCTURE (MARKDOWN REPORT LAYOUT):

{# ─── START:RULES FOR CHUNK OPERATION ─── #}
{% if force_full_export %}
You MUST include every single section below without exception to satisfy enterprise compliance requirements, and fully translating them following the rules in `CRITICAL FULL TRANSLATION MANDATE` and `DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE`
{% else %}
{# Chunk Mode: Framework stream isolation properties dynamically managed by the Master Rules Middleware #}
- MANDATORY SYSTEM INITIALIZATION LAW: You ARE EXACTLY AND CRITICALLY COMMANDED to explicitly emit the literal infrastructure tag `<!--START_CHUNK_{{ target_segment }}-->` as your absolute first output tokens on its own fresh standalone line before writing any other text.
- Any execution that drops or filters out this structural comment anchor will cause a fatal deployment pipeline failure. You MUST automatically delete this entire instruction block silently after absorbing.
{% endif %}
{# ─── END:RULES FOR CHUNK OPERATION ─── #}

{% if not force_full_export %}
<!--START_CHUNK_{{ target_segment }}-->
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
| **Version** | 1.0 ([Translate "Baseline" into {{ target_language }}]) |
| **Date Time** | {{ current_timestamp }} |
| **Author** | Enterprise System Architect (SA Agent) |
| **Approval** | [Translate "Pending Technical Governance Review" into {{ target_language }}] |

## 📊 1. SYSTEM OVERVIEW & CORE ARCHITECTURE MODALITY

### ⚙️ 1.1. Core System Modality & Architecture Modality
<RULE>
- You MUST automatically delete this entire rule instruction text stream block.
- You MUST dynamically generate a comprehensive technical overview analysis of the discovered core system architecture, EDA patterns, CQRS boundaries, and Reactive core models based strictly on the requirement context.
- CRITICAL FORMAT RULE: You BANNED from outputting paragraphs or walls of text. You MUST strictly format 100% of your generated overview as a clean, highly structured, high-density markdown bulleted checklist (`- ` symbols). Each bullet point must be a short, punchy technical statement delivering raw architectural metrics.
- You MUST render 100% of your newly generated sentences in the designated target language: {{ target_language }}.
</RULE>

### 🌊 1.2. Enterprise Data Flow Topologies & Core Ecosystems
<RULE>
- You MUST dynamically generate a detailed technical breakdown analysis of asynchronous messaging channels, ingestion gateway parameters, topic topologies, and cross-channel external fan-out architectures based on the context.
- You MUST render 100% of your newly generated sentences in the designated target language: {{ target_language }}.
</RULE>

## 📁 2. TECH STACK DEPENDENCIES & ECOSYSTEM LIBRARIES
- **Backend Infrastructure Core Stack:** [Detail precise versions, runtime engines, dependency injection abstractions, ORMs, and messaging frameworks extracted from requirements]
- **Frontend & Cross-Platform UI Mobile Stack:** [Detail strict web frameworks, dynamic localized routing, responsive layouts, and native mobile runtime wrappers if present]

## 📁 3. GLOBAL GUARDRAILS & ENTERPRISE COMPLIANCE STANDARDS
<RULE>
- **REAL-DATA COMPLIANCE ANCHOR:** You MUST extract and generate the markdown bulleted checklist based STRICTLY AND ONLY on the actual, real-world security and infrastructure data present in the raw input requirements database.
  * ANTI-HALLUCINATION RAIL: You ARE ABSOLUTELY BANNED from fabricating, looping, or generating generic administrative placeholder bullets (e.g., do NOT generate repeated lines about managing finance, HR, projects, or quality). If the source data provides fewer than 5 compliance metrics, stop immediately at the last real item. Padding out the text stream with semantic junk will trigger an immediate compiler crash.
- Each item MUST be rendered as a highly structured, high-density markdown bulleted checklist (`- ` symbols). 
- Every bullet point must be a short, punchy technical baseline statement delivering raw architectural metrics in the designated target language: {{ target_language }}.
</RULE>

### 🔑 3.1. Security & Compliance Baseline
<RULE>
- **REAL-DATA COMPLIANCE ANCHOR:** You MUST extract and generate the markdown bulleted checklist based STRICTLY AND ONLY on the actual, real-world security and infrastructure data present in the raw input requirements database.
  * ANTI-HALLUCINATION RAIL: You ARE ABSOLUTELY BANNED from fabricating, looping, or generating generic administrative placeholder bullets (e.g., do NOT generate repeated lines about managing finance, HR, projects, or quality). If the source data provides fewer than 5 compliance metrics, stop immediately at the last real item. Padding out the text stream with semantic junk will trigger an immediate compiler crash.
- Every bullet point must be a short, punchy technical statement delivering raw architectural metrics in the designated target language: {{ target_language }}.
</RULE>

### 🌐 3.2. Infrastructure & Performance Guardrails
<RULE>
- Dynamically extract and generate a highly structured, high-density markdown bulleted checklist (`- ` symbols) specifying the infrastructure limitations, database pooling (e.g., HikariCP), caching eviction policies (e.g., Redis), and async messaging constraints from the requirements.
- Every bullet point must be a short, punchy technical statement delivering raw architectural metrics in the designated target language: {{ target_language }}.
- If no explicit performance guardrails are found, you MUST derive a production-grade infrastructure baseline tailored to the project's architecture.
</RULE>

### 🥞 3.3. ARCHITECTURAL STACK MATRIX
<RULE>
- You MUST analyze the `--- RAW REQUIREMENTS ---` section to identify the actual technology stack used in the project.
- Based on your analysis, dynamically set the value of each key below to `true` or `false`.
- STEFAN HARD-CODED FENCE LAW: You ARE CRITICALLY REQUIRED to open the block exactly with a single line of triple backticks followed immediately by the text 'properties:stack_matrix' (i.e., ```properties:stack_matrix ...```). Do NOT omit these backticks under any circumstance.
- Output ONLY the raw key-value pairs formatted exactly as `KEY=value` inside the block, then close the block cleanly with a standalone line of triple backticks (```).
- CRITICAL FORMAT RULE: Output ONLY the raw key-value pairs formatted exactly as `KEY=value`. Do NOT translate the keys. Do NOT add markdown formatting, quotes, or brackets inside the code block.
- **ABSOLUTE EMISSION EDGE LAW:** The exact microsecond your cursor prints the final closing triple backticks (```) of the stack_matrix code block, you MUST immediately print the literal infrastructure tag `<!--END_CHUNK_{{ target_segment }}-->` on a fresh standalone line.
- **HARD STOP COMMAND:** The moment the angle bracket `>` of `<!--END_CHUNK_{{ target_segment }}-->` is printed, you MUST KILL THE OUTPUT STREAM INSTANTLY. Do not evaluate, do not reason, and do not emit a single token further.
</RULE>

```properties:stack_matrix
PERSISTENCE_LAYER_REQUIRED=auto_evaluate
BACKEND_LAYER_REQUIRED=auto_evaluate
FRONTEND_LAYER_REQUIRED=auto_evaluate
MOBILE_LAYER_REQUIRED=auto_evaluate
DEVOPS_LAYER_REQUIRED=auto_evaluate
```

### 🕸️ 3.4. DYNAMIC MICROSERVICES TOPOLOGY REGISTRY MATRIX

* **[IF AND ONLY IF BOTH `BACKEND_LAYER_REQUIRED=true` AND MICROSERVICES / DECOUPLED TOPOLOGY IS DETECTED INSIDE THE CRITERIA]:** You MUST programmatically construct and emit a clean execution-level reference markdown registry table tracking 100% of all discovered independent backend sub-modules and decentralized capabilities. The structure of this dynamic matrix grid MUST strictly obey the following formatting schema layout:

| Service Domain Key | Microservice Sub-Module Name | Target Container Context Path | Active Infrastructure Gateway Ports | Mapped Functional Backend Packages | Mapped Tracking TagIDs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Parent Root Grandmaster** | {{ project_name | lower | replace(" ", "") | replace("_", "") | replace("-", "") }}-root | `./sources/backend/pom.xml` | N/A (Global Orchestrator) | `org.nlh4j.{{ project_name | lower | replace(" ", "") | replace("_", "") | replace("-", "") }}` | [ARC-000] |

* **AUTOMATED SERVICE DISCOVERY ENGINE RULES:**
  1. Your configuration engine MUST scan 100% of the text primitives inside the requirement document blocks. For EVERY independent business capability, domain core, or functional sub-system discovered (e.g., identity modules, scheduling hubs, analytical engines, limiters), you MUST emit a distinct, unique standalone data row into the table grid matrix above.
  2. You ARE PERMANENTLY FORBIDDEN from using hard-coded static text placeholders. The "Mapped Functional Backend Packages" cell column MUST be computed dynamically based on your pure alphanumeric identifier pattern: `org.nlh4j.{{ project_name | lower | replace(" ", "") | replace("_", "") | replace("-", "") }}.<service_name_alphanumeric_lowercase>`.
  3. The "Target Container Context Path" column cell MUST yield the precise decoupled relative directory path layout format structure ending with the standard build manifest: `./sources/backend/<service-name-hyphenated>-service/pom.xml` (or extension matching your active stack language).
  4. You MUST execute a literal mathematical trace match to pair each isolated row module exclusively with its active target capability Tag IDs discovered in your backlog pass. Missing any decentralized sub-module or collapsing independent services into a single shared root package triggers an immediate architectural compliance compilation fail.

{% endif %}
{# ─── END:CHUNK:PART_1_INITIAL ─── #}

{# ======================================================= #}
{# ─── START:CHUNK:PART_1_BACKLOG_4_1 ─── #}
{% if force_full_export or (target_segment and target_segment.strip() == "PART_1_BACKLOG_4_1") %}
## 🏁 4. HIGH-LEVEL MULTI-PHASE ARCHITECTURAL SYNOPSIS GRID

### 📦 4.1. MASTER ARCHITECTURAL PRODUCT BACKLOG
<RULE>
- **ZERO-ANALYSIS INVARIANT LAW:** You are STRICTLY BANNED from outputting any internal thinking logs, self-analysis, planning steps, or meta-commentary about the requirements in English.
- **ABSOLUTE BACKLOG UNROLLING MANDATE:** You ARE CRITICALLY BANNED from emitting a blank, placeholder, or template-only table header row here. You MUST explicitly unroll and generate EVERY SINGLE ONE of all discrete functional and non-functional tasks discovered in the SRS corpus (from the `--- RAW REQUIREMENTS ---` section). 
- Each row MUST be fully populated with unique technical engineering indicators and specific localized text in "{{ target_language }}". Leaving this table empty or summarized triggers an immediate deployment abort.
- You MUST analyze the `--- RAW REQUIREMENTS ---` section (raw SRS) to identify and break down the implementation tasks for the unified Master Product Tasks Backlog table directly under this section (inside the hidden HTML tags from `<!--BACKLOG_SYNOPSIS_GRID_START-->` to `<!--BACKLOG_SYNOPSIS_GRID_END-->`). Organize the multi-phase timeline. This table acts as the definitive grounding index for 100% of the project requirements from the `--- RAW REQUIREMENTS ---` section (raw SRS).
- STEP 1 (HIGH-DENSITY DESCRIPTION): You MUST first write exactly one (1) single, cohesive technical description paragraph directly above the table initialization boundary. This paragraph MUST strictly focus on the architectural dependencies of the master components. You-are ABSOLUTELY AND CRITICALLY BANNED from creating temporary sub-headers, spawning independent structural text sections, or hallucinating raw token strings matching any alphanumeric layout indicators or text blocks placeholder descriptors outside the requested registry mapping database context.
  - **LAYOUT RESUMPTION OVERRIDE:** You MUST explicitly print the all section header (such as `## 4...`) and subsection header (such as `### 4.1....`) translated into "{{ target_language }}" on fresh lines.
  - **METRICS EMISSION LAW:** You MUST completely unroll and print out the `#### [SYSTEM ARITHMETIC MATRIX]` title and all tag counter ledger metrics rows (from Total [REQ] to Total SRS) sitting below, fully calculated and translated into "{{ target_language }}", BEFORE emitting the opening infrastructure tag `<!--BACKLOG_SYNOPSIS_GRID_START-->` to prevent the cursor from skipping them.
- STEP 2 (FULL REQUIREMENT BREAKDOWN TABLE): Directly below the description paragraph, you MUST dynamically generate the complete Master Product Tasks Backlog Table (inside the hidden HTML tags from `<!--BACKLOG_SYNOPSIS_GRID_START-->` to `<!--BACKLOG_SYNOPSIS_GRID_END-->`).
- MANDATORY TRANSLATION ENGINE: You MUST translate 100% of the table header text and task descriptions into the designated target language: {{ target_language }}.
- TECHNICAL PRESERVATION MATRIX: You MUST NOT translate technical keys, IDs, system configurations, paths, or variables. Specifically, preserve raw English/technical formats for: Task IDs (e.g., TASK-001), Component Paths (e.g., `sources/backend/auth/`), and Targeted Tag IDs (e.g., `[ARC-001]`).
- TRACEABILITY MANDATE: You MUST ensure 100% full coverage of ALL Tag IDs (including every single `[ARC-XXX]`, `[NFR-XXX]`, etc.) extracted from the `--- RAW REQUIREMENTS ---` section. Do NOT skip, omit, or truncate any Tag ID.
- LOCALIZED TABLE SCHEMA: The markdown table structure MUST match this layout exactly, with the bracketed header text translated into the designated target language: {{ target_language }}.
- The Master Product Tasks Backlog table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below (inside the hidden HTML tags from `<!--BACKLOG_SYNOPSIS_GRID_START-->` to `<!--BACKLOG_SYNOPSIS_GRID_END-->`).
- **MANDATORY ROW ANCHOR INJECTION:** Every single generated task row inside this table MUST contain the literal hidden HTML comment tag `<!--REGISTERED_BACKLOG_TASK_ROW-->`. You MUST explicitly place this tag inside the final cell (the TagID column, the 5th column), positioning it immediately after the tracking tags and right before the closing vertical pipe character `|` of that row (exact syntax pattern format: ` | ... [Tag IDs] <!--REGISTERED_BACKLOG_TASK_ROW--> |`). Any generated row that drops or filters out this structural comment anchor will cause a fatal deployment pipeline failure.
- **100% INVARIANT TRACEABILITY LINKAGE:** Every row in this backlog MUST enforce absolute coverage of all relevant tracking tags (`[REQ-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[NFR-XXX]`, `[DOC-XXX]` or all tag IDs that their format patterns like this `[XXX-XXX]`). Zero orphan requirements or untagged deliverables are permitted.
- **STRICT BACKLOG COMPLETENESS COMPLIANCE LAW:** This Master Product Tasks Backlog Table MUST completely map and exhaustively list every engineering effort required by the corpus, strictly verified by the Type column (the 4th column):
  1. *Application Code:* Functional endpoint creations, database models, and service layer code blocks.
  2. *Enterprise Documentation:* Complete systemic blueprints, database schema topologies, localized operational manual files, and API contracts located under `./sources/docs/`.
  3. *DevOps Infrastructure:* Containerization scripts (Docker), cloud environment setups (GCP via Terraform), and orchestration cluster manifests (GKE).
- **TASK ATOMICITY LAW:** You are STRICTLY BANNED from summarizing, grouping, or clustering multiple operational requirement bullets into a single generic task row to save token space.
- **1:1 TRACEABILITY RATIO & EXCLUSION LAW:** Every unique functional Tag ID identified in the raw SRS matching the `[REQ-XXX]` pattern MUST yield exactly one (1) dedicated, standalone row in this table. You are STRICTLY BANNED from summarizing or grouping multiple `[REQ]` bullets into a single row to save space. However, you MUST completely exempt all `[DAT]`, `[ARC]`, `[EXC]`, `[DOC]` and all tags that their format pattern like this `[XXX-XXX]` (means `[XXX]` tags) from this 1:1 expansion law; these system metadata domains MUST be handled exclusively via the dynamic consolidation rules specified below.
- **EXHAUSTIVE WORKLOAD INVARIANT LAW:** You MUST execute an unbroken, non-terminating loop scanning 100% of the raw input dataset from the very first row to the absolute final row. Every single requirement, feature column, and architecture mapping discovered MUST be assigned a strict continuous index (from Task 1 continuously up to the final task row) directly inside the Markdown table cells (`|`). You ARE CRITICALLY BANNED from compressing, shifting, or outputting data as bullet points (`*` or `-`) outside the table skeleton.
- **AUTONOMOUS MANDATORY COMPLIANCE INJECTION RAIL:** To satisfy the strict requirements of enterprise compliance, even if the raw business requirements section lacks explicit narrative text specifications for cross-cutting infrastructure, DevOps pipelines, or universal system documentation, you MUST autonomously inject dedicated, standalone framework task rows into the table matching these parameters:
  1. *Database & Token Verification Core:* You MUST ensure the generation of exactly one (1) unified database infrastructure initialization row capturing all `[DAT-XXX]` patterns (condensed as `[DAT-ALL (1 to X)]`), exactly one (1) row capturing global RBAC security `[ARC-001 to ARC-005]` patterns, and exactly one (1) row capturing system integration contracts `[ARC-006 to ARC-009]`.
  2. *Enterprise DevOps Infrastructure Injection:* You MUST dynamically inject a dedicated standalone task row for DevOps Infrastructure (handling multi-stage Dockerfiles, cloud environment setups via Terraform, and orchestration cluster manifests inside GKE). You MUST explicitly map ALL matching `[NFR-XXX]` security, performance, and cross-cutting compliance tokens directly into its TagID cell to guarantee full vertical traceability.
  3. *System Documentation Architecture Injection:* You MUST dynamically inject a dedicated standalone task row for Enterprise Documentation (handling blueprints, system topologies, localized operational manuals, and API contracts under `./sources/docs/`). You MUST explicitly assign the dedicated tracking symbol `[DOC-001]` inside its TagID cell to guarantee zero empty tag rows.
  4. *Universal Project Scaffolding Injection:* You MUST autonomously inject dedicated baseline framework scaffolding tasks at the absolute beginning of the backlog index. For Backend services under Microservices topologies, enforce the generation of a parent root project build descriptor `./sources/backend/pom.xml` and service-level descriptors `./sources/backend/<service-name>/pom.xml` (example: `./sources/backend/reporting-service/pom.xml` where `<service-name>` is `reporting-service`, etc.). For Frontend or Web applications, enforce the generation of application manifests `./sources/frontend/package.json` and build configuration engines `./sources/frontend/tsconfig.json`. These configuration assets must utilize the dedicated tracking symbol `[ARC-000]`.
- **STRICT TASK ATOMICITY RAIL:** You MUST generate an independent, standalone row for every single functional requirement (`[REQ-XXX]`) and system capability discovered inside the `--- RAW REQUIREMENTS ---` section. You ARE ABSOLUTELY BANNED from grouping, clustering, or condensing multiple functional requirements into a single task row.
- **METADATA CONSOLIDATION & INFRASTRUCTURE ROWS:** You MUST consolidate system metadata patterns into standalone architecture enablement rows at the bottom of the table to prevent token redundancy:
  1. *Database Layer Infrastructure:* You MUST dynamically fetch the evaluated integer value of the variable `Source_DAT`. If `Source_DAT` is calculated as exactly 0 (indicating the active topology has no persistence layer required), you MUST completely drop this row cell or explicitly print the token `[NOT APPLICABLE]` along with a clean corporate justification. Otherwise, you MUST strictly print the TagID cell layout exactly formatted as this dynamic string dải range pattern: `[DAT-ALL (1 to Source_DAT)]` (where you MUST substitute the text `Source_DAT` with the actual calculated integer value of the `Source_DAT` variable). In your internal mathematical evaluation layer, this consolidated token MUST hold a weight equal to exactly that calculated integer value.
  2. *Security Layer:* Harvest all architectural tokens matching `[ARC-XXX]` (Let the total unique count be variable `A`). You MUST print the TagID cell exactly as a dynamic range pattern: `[ARC-START_NUM to ARC-END_NUM]`.
  3. *DevOps Layer:* Group all cross-cutting deployment concerns. You MUST explicitly map ALL matching non-functional compliance tokens (`[NFR-XXX]`) directly into this standalone infrastructure cell.
  4. *Exception Layer:* Locate all validation handling codes matching `[EXC-XXX]`. Inline and attach these tracking tokens directly into the cell of their respective functional parent requirement rows. You ARE CRITICALLY BANNED from generating independent, standalone task rows inside the Markdown table for any tracking codes matching the `[EXC-XXX]` pattern. Every single validation failure, network drop, or duplicate exception mapping discovered MUST be encapsulated inline within the TagID cell of its primary functional parent requirement row to protect token economy and satisfy the 1:1 mathematical functional row limit ratio.
- **INDEPENDENT AUDIT MATRIX:** Before emitting the table SUMMARY row (latest row of the Master Product Tasks Backlog table), you MUST declare and calculate exactly some distinct internal mathematical variables within your execution memory layer:
  1. Let **Global_Source_Total** = Perform a comprehensive pass over the entire `--- RAW REQUIREMENTS ---` section. Count every single unique tracking symbol present in the raw corpus (explicitly summing all found unique [REQ-XXX], [EXC-XXX], [ARC-XXX], [NFR-XXX], [DAT-XXX], `[DOC-XXX]` or all tag IDs that their format patterns like this `[XXX-XXX]`).
    * *Sanitization Mandate:* Ensure that tags encapsulated inside parenthetical layers like `([REQ-XXX])` are fully counted at their individual unique weight after stripping away the outer parenthesis boundary.
  2. Let **Global_Covered_Total** = Perform a fresh, independent pass over the columns of the table you just generated above. Manually sum every unique tracking tag distributed inside the cells that was inherited STRICTLY from the source requirements. You MUST explicitly exclude infrastructure scaffolding tags (like `[ARC-000]`) and documentation compliance tags (like `[DOC-001]`) from this covered variable summation to isolate true SRS requirement metrics.
  3. Let **Coverage_Status** column: Compute (`Global_Covered_Total` / `Global_Source_Total`) * 100. If `Global_Covered_Total` does not equal `Global_Source_Total`, the output percentage MUST reflect the deficit and set STATUS to `FAILED` in the designated target language: {{ target_language }}.
  4. Let **Verified_Status** column: If `Global_Covered_Total` is exactly equal to `Global_Source_Total`, output the translated word for `Verified` in the designated target language: {{ target_language }}. Otherwise, output the translated word for `FAILED` in the designated target language: {{ target_language }}.
  5. Let `Source_REQ` = Perform a comprehensive pass over the entire `--- RAW REQUIREMENTS ---` section. Count every single unique tracking symbol present in the raw corpus (explicitly summing all unique [REQ-XXX] tags found).
  6. Let `Source_EXC` = Perform a comprehensive pass over the entire `--- RAW REQUIREMENTS ---` section. Count every single unique tracking symbol present in the raw corpus (explicitly summing all unique [EXC-XXX] tags found). (You MUST actively harvest them from the exception section).
  7. Let `Source_ARC` = Perform a comprehensive pass over the entire `--- RAW REQUIREMENTS ---` section. Count every single unique tracking symbol present in the raw corpus (explicitly summing all unique [ARC-XXX] tags found).
  8. Let `Source_DAT` = You MUST dynamically analyze the complete `--- RAW REQUIREMENTS ---` section to identify the absolute total number of core logical relational database entities (tables) required to support the functional architecture scope. You MUST allocate exactly one (1) unique tag count per independent logical data entity discovered (e.g., counting the distinct business domains needing dedicated persistence layer tables). Execute a strict real-time count of these core tables and assign the final computed integer value directly to this `Source_DAT` variable.
  9. Let `Source_NFR` = Perform a comprehensive pass over the entire `--- RAW REQUIREMENTS ---` section. Count every single unique tracking symbol present in the raw corpus (explicitly summing all unique [NFR-XXX] tags found).
- **CRITICAL DATA ASSIGNMENT MANDATE:** You MUST preserve these two variables in memory and inject their exact calculated integer values directly into their designated matching slots inside the table summary row layout below.
- **STRICT UNIQUE TASK MAPPING LAW:** You MUST enforce a strict 1:1 mathematical ratio between unique functional requirement tags ([REQ] and [EXC]) and the generated table rows. Every single unique [REQ-XXX] and [EXC-XXX] identifier found in the text MUST yield exactly one (1) single dedicated task row. You ARE ABSOLUTELY BANNED from splitting a single REQ tag into multiple separate frontend/backend rows.
- **EXHAUSTIVE CURSOR LOOP MANDATE:** You MUST execute a continuous, unbroken sequential loop scanning 100% of the raw input requirements from the very first row to the absolute final row. You ARE CRITICALLY BANNED from executing early termination filters or truncated slicing. Every single workload asset discovered MUST be assigned a strict continuous index (from Task 1 up to the absolute final task row) without omission.
- **IMMUTABLE DATA EMISSION & COMPREHENSIVE UNROLLING LAW:**
  * You ARE ABSOLUTELY AND EXPRESSLY BANNED from leaving the Master Product Tasks Backlog table empty, abbreviated, summarized, or populated with static placeholder bracket strings. 
  * Your attention heads MUST sequentially unroll and print 100% of all discrete functional and non-functional engineering tasks discovered across the corpus into individual, physical Markdown table rows.
  * Every row cell inside the table structure MUST be completely filled with high-density, context-specific technical data fully evaluated and translated into the target language context. Skipping rows or hiding tasks under generic variables triggers an immediate framework integration crash.
- **DYNAMIC ARCHITECTURAL SCAFFOLDING MULTIPLICATION LAW:** When engineering the master backlog table for tracking token `[ARC-000]`, you MUST dynamically inspect the system topology and microservice domains outlined in the requirements. You ARE CRITICALLY COMMANDED to unroll and generate a dedicated, independent standalone task row for EVERY single unique subsystem, microservice module, interface gateway, or client application discovered in the project topology layers. For instance, if the project topology demands multiple distinct backend microservices, your backlog MUST emit exactly one parent root build descriptor (`./sources/backend/pom.xml`) and separate independent service-level build descriptors (e.g., `./sources/backend/<service-name>-service/pom.xml`), each assigned a sequential index number starting seamlessly from No. 1. You ARE CRITICALLY BANNED from consolidating multiple microservice descriptors into a single row cell if the project configuration relies on a decoupled architecture.
- **STRICT ANCHOR SYNTAX LAW:** When emitting the literal hidden tag `<!--REGISTERED_BACKLOG_TASK_ROW-->` at the end of every table row, you MUST print the characters exactly as `<!--REGISTERED_BACKLOG_TASK_ROW-->`. You are STRICTLY BANNED from replacing the trailing hyphens and angle bracket with a slash (do NOT write `--> /` or `/>`). Every row character sequence must close clean.
</RULE>

<!--BACKLOG_SYNOPSIS_GRID_START-->

#### [SYSTEM ARITHMETIC MATRIX]
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

<!--BACKLOG_SYNOPSIS_GRID_END-->

{% endif %}
{# ─── END:CHUNK:PART_1_BACKLOG_4_1 ─── #}

{# ======================================================= #}
{# ─── START:CHUNK:PART_1_MATRIX_4_2 ─── #}
{% if force_full_export or (target_segment and target_segment.strip() == "PART_1_MATRIX_4_2") %}
### 🔭 4.2. MULTI-PHASE SYNOPSIS MATRIX
Generate a clean, highly the structured SynOpSis Matrix Phases table (inside the hidden HTML tags from `<!--PHASE_SYNOPSIS_GRID_START-->` to `<!--PHASE_SYNOPSIS_GRID_END-->`) mapping the exact distribution of components and Tag IDs across the dynamically calculated phases. You MUST compute the most optimal number of phases (denoted as N, where N <= {{ num_phases }}) that naturally and completely covers 100% of the BA requirements and Tag IDs.
<RULE>
[STRICT TABLE EMITTING MANDATE]
- **ZERO-ANALYSIS INVARIANT LAW:** You are STRICTLY BANNED from outputting any internal thinking logs, self-analysis, planning steps, or meta-commentary about the requirements in English. 
- **PRIVATE METADATA PRUNING LAW:** This entire `<RULE>` container belongs strictly to Zone 1 and must be 100% erased from the final output stream. However, immediately after pruning, you MUST resume standard layout printing: first write out the translated subsection header `### 4.2...` on their fresh standalone lines.
- You MUST dynamically analyze the comprehensive tasks generated in the {{ ref_section_4_1 }} section immediately to identify and break down the implementation tasks for the unified SynOpSis Matrix Phases table directly under this section (inside the hidden HTML tags from `<!--PHASE_SYNOPSIS_GRID_START-->` to `<!--PHASE_SYNOPSIS_GRID_END-->`).
- **STRICT ONE-TO-ONE TASK TO PHASE ROW ALIGNMENT LAW:** When distributing tasks from your master backlog into the Multi-Phase Synopsis Matrix table, you ARE CRITICALLY BANNED from clustering, summarizing, or packing multiple unrelated tasks into a single phase container to save token space. You MUST execute a strict sequential, non-overlapping mapping pass where the number of functional phase rows generated MUST match the independent task indices exactly:
  * Phase 1 MUST strictly and exclusively host the foundational scaffolding and database initialization tasks.
  * Every subsequent intermediate business capability Phase row MUST host strictly and exclusively its single corresponding unique task index split from the master backlog table (e.g., Phase 2 maps strictly to Task 2, Phase 3 maps strictly to Task 3, Phase 4 maps strictly to Task 4).
Any architectural layout that mixes cross-cutting module pathways or leaks components into adjacent phase boundaries triggers an immediate compliance reject.
  * You ARE CRITICALLY BANNED from stacking core functional requirements. No single phase row from Phase 2 to Phase {{ num_phases - 1 }} is allowed to contain more than `Max_Tasks_Per_Phase` active engineering tasks. You MUST implement a progressive, balanced linear distribution of endpoints across all intermediate functional rows. Stacking more than 35% of total functional workloads into a single phase container triggers an immediate architecture pipeline rejection.
   * You MUST force a balanced gradient progression where functional endpoint microservices are spread proportionally. The final row (Phase {{ num_phases }}) MUST be strictly reserved for universal non-functional security countermeasures, cluster deployments, and absolute technical reference documentation closing logs.
- CRITICAL INDEX CEILING: The maximum phase index allowed is {{ num_phases }}. The phases number MUST be exactly {{ num_phases }}. You are ABSOLUTELY FORBIDDEN from generating Phase {{ num_phases + 1 }} or creating a separate phase row for every single backlog task. You MUST group and aggregate multiple tasks from {{ ref_section_4_1 }} milestones.
- For each phase row, you are critically ordered to enforce absolute information symmetry by scanning all Tag IDs and Task types from the {{ ref_section_4_1 }} section.
- **[PATH_ELEMENT_BACKTICK_ESTABLISHMENT]**: Inside the "Architectural Component / Module Path" column (the 4th column) of the synopsis table matrix, you MUST wrap every single individual relative file path token inside its own independent inline markdown backticks (e.g., producing dynamic cell strings formatted exactly like `` `path/to/component_or_module_or_file_1` <br/> `path/to/component_or_module_or_file_2` <br/> ... ``). You ARE ABSOLUTELY BANNED from outputting naked loose file paths or utilizing raw comma symbols `,` to join multiple path components, instead of using `<br/>` to join them inside a single cell boundary.
- CRITICAL INFRASTRUCTURE RULE: If you detect any DevOps, Cloud, Deployment, CI/CD, Containerization, or Infrastructure tasks in {{ ref_section_4_1 }} (such as Docker, GCP, GKE, Kubernetes, or Git pipelines), you MUST explicitly list the path (e.g., './sources/infrastructure/devops/') in the Component column (the 4th column), and you MUST permanently declare 'DevOps' alongside Coder, Tester, Reviewer, and Doc in the 'Assigned Sub-Agent' column (the 6th column) for that targeted phase. DevOps agent could be [Docker], [GCP], or [GKE] belongs to its active operating persona. Do not drop the DevOps ([Docker], [GCP], or [GKE]) agent under any circumstance.
- Each row MUST specify a real-world engineering duration bounded between 1 to a strict upper ceiling of {{ max_days_per_phase }} days maximum per phase. Do NOT generate empty rows, placeholder phases, or artificial workloads. If the requirements are fully satisfied within fewer than {{ num_phases }} phases, terminate the matrix setup immediately at phase N.
- LOCALIZED TABLE SCHEMA: The markdown table structure MUST match this layout exactly, with the bracketed header text translated into the designated target language: {{ target_language }}.
- The SynOpSis Matrix Phases table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below (inside the hidden HTML tags from `<!--PHASE_SYNOPSIS_GRID_START-->` to `<!--PHASE_SYNOPSIS_GRID_END-->`).
- **SEQUENTIAL WORKLOAD EXHAUSTION LAW:** You MUST execute a strict sequential cursor loop scanning all registered tasks in the {{ ref_section_4_1 }} section (the registered task rows contains the `<!--REGISTERED_BACKLOG_TASK_ROW-->` tag) without skipping any row. You ARE CRITICALLY BANNED from activating early termination filters upon discovering the final functional requirement tag (`[REQ-XXX]`). All non-functional, security, database, infrastructure, and documentation tasks located at the tail end of the backlog MUST be explicitly mapped into your phase matrices.
- **COMPREHENSIVE TAG WEIGHT AUDIT RAIL:** When evaluating your distribution metrics, every consolidated token notation (such as `[DAT-ALL (1 to X)]` or `[NFR-001 to NFR-Y]`) MUST be mathematically unrolled and counted at its full individual declaration weight. The total distributed tasks count must equals exactly with the total task rows in the {{ ref_section_4_1 }} section (the registered task rows contains the `<!--REGISTERED_BACKLOG_TASK_ROW-->` tag).
- **DETERMINISTIC MATRIX CELL EMISSION LAW:** You MUST systematically emit exactly and only `{{ num_phases }}` physical table rows sequentially from Phase 1 to Phase `{{ num_phases }}`.
  * PROSE PROHIBITION: You ARE BANNED from outputting any prose text, explanation, or commentary. Your very first output character for this section MUST be the literal character `|` of the table header.
  * DYNAMIC EXHAUSTIVE EXPANSION: For each phase row, you MUST unroll and map the corresponding Task numbers and Tag IDs inline. The `Targeted Tag IDs` column (the 7th column) for each phase row MUST mathematically contain ONLY the exact tracking tags mapped to the specific task indices listed in the `Task IDs Covered` (the 3rd column) column of that active row.
  * CHRONO-COMPUTATION: Format the `Day Range` column (the 1st column) for each row starting from relative integer 1 to K, where K = Max(1, RoundUp(Matrix_Source_Total_Tags / 3)), capping strictly below `{{ max_days_per_phase }}`.
- **UNBREAKABLE PHYSICAL GRID INVARIANT LAW:** To guarantee 100% deterministic compilation stability, you ARE CRITICALLY BANNED from clustering backlog tasks into fewer than `{{ num_phases }}` rows. You MUST programmatically force your output engine to render EXACTLY AND ONLY `{{ num_phases }}` independent, distinct physical markdown table rows (from Phase 1 directly up to Phase `{{ num_phases }}`) without early termination. 
  * ROW ITERATION CONSTRAINT: Each sequential phase row MUST contain an independent, non-empty subset of tasks. You MUST programmatically reset your layout cursor to create a brand new physical markdown row line (`| Phase X | ... |`) for every sequential integer index from 1 up to `{{ num_phases }}` without early termination.
  * CHRONO-BUBBLE ALLOCATION: To balance the workload without violating calendar thresholds, you MUST dynamically group the tasks so that the duration `K` for EACH individual row satisfies `K = Max(1, RoundUp(Matrix_Source_Total_Tags / 3))` while remaining strictly bounded below the ceiling parameter of `{{ max_days_per_phase }}`. Do not skip any phase index.
- **STRUCTURAL ARTIFACT PIPELINE GRADIENT:** You MUST distribute all backlog elements across the {{ num_phases }} phase rows based strictly on a three-tier lifecycle hierarchy:
  * Tier 1 (Core Gateways, Scaffolding & Persistence): Foundational multi-module structural descriptors and dependency control engines (`[ARC-000]`) MUST be exhaustively unrolled. You MUST ensure that 100% of all independent sub-module build descriptors (including every physical `./sources/backend/<service-name>/pom.xml` configuration asset mapped to your discovered project topology) are explicitly printed inside the Architectural Component column of the Phase 1 cell matrix. You ARE ABSOLUTELY BANNED from using generic directory pathways or shorthand indicators to represent multiple independent compilation units.
  * Tier 2 (Functional Operations & Interceptors): For every single task index mapped to a specific phase capability row, your processing engine MUST dynamically explode and print the exact relative file paths for ALL mandatory architectural tiers belonging strictly to that functional module domain cell context, utilizing separate vertical lines (`<br/>` delimiters) with zero cross-phase leakage or early compaction. You ARE PERMANENTLY BANNED from hallucinating, duplicating, or bleeding foreign service paths across phase boundaries. Before emitting paths, check your static `properties:stack_matrix` to enforce the following invariant mapping pattern:
    - IF `BACKEND_LAYER_REQUIRED=true`: You MUST explode the specific active domain service into exactly 5 standalone file layers: 1) API Ingress Router/Controller, 2) Core Domain Service, 3) Persistence Access Repository, 4) Database Entity/Model schema, and 5) Local Exception Handler, strictly matching the dynamic folder name of that targeted phase row index with valid filename extensions (e.g., `.java`, `.ts`).
    - IF `FRONTEND_LAYER_REQUIRED=true` and backend is false: You MUST explode into exactly 4 frontend layers: 1) Page Component, 2) UI Component, 3) State/Hook Manager, and 4) API Integration Client (e.g., `.tsx`, `.ts`).
    Every single layer file path MUST be textually present and MUST strictly lock within the isolated service subdirectory tree of that active row cell context. Missing or substituting any tier asset triggers an immediate framework integration reject.
    - IF `MOBILE_LAYER_REQUIRED=true`: You MUST unroll into native/hybrid screen bundles, device hardware interceptors, and local preference storage modules.
    Every layer file path MUST be textually present with its valid filename extension and MUST strictly correspond to the isolated subdirectory tree of that specific service domain phase row within the active data block. Missing or substituting any tier asset triggers an immediate compliance reject.
  * Tier 3 (Cloud Infrastructure Delivery): Advanced production deployment orchestration scripts, Docker containerization layers, and cloud automation components (`[NFR]` infrastructure tags) MUST be consolidated within the concluding milestones (the final phase row slots).
- **LINEAR LAYOUT CURSOR GRADIENT LAW:** To maintain strict geometric document integrity, you MUST enforce a progressive top-down printing sequence. Immediately after pruning this rule block, your very first emitted tokens MUST be the dynamic unrolling of the `[MATRIX ARITHMETIC LIFECYCLE]` text title and its all calculated metrics lines translated into "{{ target_language }}". 
- **ANCHOR POSITIONING CONSTRAINT:** The absolute first microsecond your cursor prints the final character of the 4th metrics row, you MUST drop to a fresh standalone line to print the literal infrastructure tag `<!--PHASE_SYNOPSIS_GRID_START-->`. Your very next emitted character on the immediate following line MUST be the literal vertical pipe `|` of the markdown table header row to lock the grid wrapper boundary securely.
- The SynOpSis Matrix Phases table layout MUST strictly execute inside the hidden framework parsing hooks exactly as formatted below (inside the hidden HTML tags from `<!--PHASE_SYNOPSIS_GRID_START-->` to `<!--PHASE_SYNOPSIS_GRID_END-->`).
**MANDATORY HARD-CODED WRAPPER PROTOCOL:** Before emitting the table structure, you MUST print the exact raw token `<!--PHASE_SYNOPSIS_GRID_START-->` on its own standalone line immediately BEFORE the table initialization boundary. Once the table generation is finished, you MUST immediately print the exact raw token `<!--PHASE_SYNOPSIS_GRID_END-->` on its own standalone line right after the final summary row line to preserve backend regex scraping.
- **MANDATORY ROW ANCHOR INJECTION:** Every single generated phase row inside the SynOpSis Matrix Phases table under this section (inside the hidden HTML tags from `<!--PHASE_SYNOPSIS_GRID_START-->` to `<!--PHASE_SYNOPSIS_GRID_END-->`) MUST contain the literal hidden HTML comment tag `<!--REGISTERED_PHASE_ROW-->`. You MUST explicitly place this tag inside the final cell (the Targeted Tag IDs, the 7th column), positioning it immediately after the tracking tags and right before the closing vertical pipe character `|` of that row (exact syntax pattern format: ` | ... [Tag IDs] <!--REGISTERED_PHASE_ROW--> |`). You are CRITICALLY AND ABSOLUTELY BANNED from printing, leaking, or compounding this comment tag inside the table header row (Line 1) or the table alignment separator pipe row (Line 2, e.g., `| :--- | :--- |`). The token `<!--REGISTERED_PHASE_ROW-->` MUST be injected exclusively at the very end of active functional data rows (Lines 3 and below representing Phase 1 to Phase 5) right before the closing pipe symbol. Any execution that leaks this system anchor into the header cells will instantly break the backend regex scrapers or any generated row that drops or filters out this structural comment anchor will cause a fatal deployment pipeline failure.
- **DYNAMIC DAY-RANGE MATCHING, TIMELINE QUANTIZATION AND FORMAT ENFORCEMENT LAWS:**:
    1. Every phase duration is strictly bound. You MUST evaluate the structural density of the generated matrix in the {{ ref_section_4_1 }} section. Count the total unique Tag IDs mapped to each phase. Calculate the exact duration value K for that phase using the formula: K = Max(1, RoundUp(`Matrix_Source_Total_Tags` / 3)). The value of K MUST NOT exceed {{ max_days_per_phase }}.
    2. In the "Day Range" column (the 2nd column) of this table, you MUST format the day sequence starting from relative integer 1 to K for EACH individual phase row (e.g., Phase N: Day 1 - K). Compounding or running a linear progressive day count across phase boundaries is strictly prohibited.
    3. If a phase contains low-density tasks, you MUST stop the index immediately (e.g., closing tightly at Day 1-2). You are BANNED from hardcoding 'Day 1 - {{ max_days_per_phase }}' if the actual workload finishes earlier.
- SUPREME DEMAND-DRIVEN WORKLOAD DISTRIBUTION LAW (ADAPTIVE LIFECYCLE): You MUST orchestrate the project planning by decomposing the absolute sum of all requirements (business functions, enterprise documentation components, and DevOps infrastructure pipelines) dynamically across {{ num_phases }} without any artificial padding or redundant agent forcing:
    1. Dynamic Resource Allocation Rule: A sub-agent (such as [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]) MUST ONLY be declared in this section table row under 'Assigned Sub-Agent' if and ONLY if there are active, unfulfilled backlog requirements matching that agent's engineering domain within that specific phase context. If a phase contains zero infrastructure tasks, DevOps (such as [Docker], [GCP], or [GKE]) agents MUST be completely omitted from that specific row.
    2. Zero Filler Data / Ghost Logs: You are strictly prohibited from generating ghost actions, repetitive task summaries, or empty calendar days simply to reach the maximum day limit. If the core deliverables for a phase are fully satisfied, the schedule stops immediately.
    3. 100% Traceability Matrix Coverage: Every active daily log and target component MUST map 100% of all relevant tracking tags ([REQ-XXX], [DAT-XXX], [ARC-XXX], [EXC-XXX], [NFR-XXX], `[DOC-XXX]` or all tag IDs that their format patterns like this `[XXX-XXX]`) from the input corpus. Zero orphan requirements or unmapped tags are permitted.
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
- **ZERO OMISSION RULE:** If a Tag ID exists in the {{ ref_section_4_1 }} section, it MUST appear in this section `<!--PHASE_SYNOPSIS_GRID_START-->`. Truncating or omitting tags to save space is a fatal error.
- **ANTI-FENCE MARKDOWN RENDERING MANDATE:** You ARE CRITICALLY BANNED from wrapping or encapsulating the `<!--PHASE_SYNOPSIS_GRID_START-->` header, metrics, or table grid structure inside triple backticks Markdown code block fences (e.g., ```markdown ...``` or ``` ...```). You MUST output the entire table skeleton as pure raw un-fenced markdown text strings directly to the pipeline. Failure to comply will cause backend rendering truncation.
- **DYNAMIC SUB-AGENT ALLOCATION LAW:** The "Assigned Sub-Agent" column (the 6th column) MUST NOT be hardcoded. You MUST dynamically compute the exact subset of agents required based strictly on the "Type" column (the 4th column) values of all tasks mapped into that specific phase from {{ ref_section_4_1 }}
    1. If the mapped tasks contain 'Application Code' -> Include: Coder, Tester, Reviewer, Doc.
    2. If the mapped tasks contain ONLY 'Enterprise Documentation' -> Include ONLY: Doc (Exclude Coder, Tester, Reviewer).
    3. If the mapped tasks contain 'DevOps Infrastructure' -> Include: Docker, GCP, GKE.
- **SOME SYNOPSIS MATRIX AUDIT ENGINE:** Before emitting the SynOpSis Matrix Phases table audit row (latest row of the SynOpSis Matrix Phases table), you MUST declare, calculate, and lock exactly two distinct internal mathematical variables within your execution memory layer based on real-time text parsing:
    1. Let **Matrix_Source_Total_Tags** = Dynamically scan the incoming `--- BACKLOG TASKS ---` section block. Parse every single task row's TagID column (the 5th column) to compute the absolute mathematical sum of all registered tracking tags (where any consolidated token like `[DAT-ALL (1 to X)]` MUST hold its full declaration weight of exactly X unique tags, and cross-cutting infrastructure documentation tags like `[DOC-XXX]` MUST be contextually included as exactly 1 dynamic primitive unit to ensure a perfect 1:1 ledger total match).
    2. Let **Matrix_Source_Tasks_Count** = Count the absolute total of discrete tasks successfully distributed from the incoming `--- BACKLOG TASKS ---` section block.
    3. Let **Matrix_Covered_Total_Tags** = Completely ignore your source count and perform a fresh, independent pass over the dynamic phase rows you generated inside this active table matrix above. Parse and manually calculate the absolute sum of all unique tracking tokens distributed inside the "Targeted Tag IDs" column (the 7th column) cells (enforcing true tag weight for consolidated tokens).
    4. Let **Matrix_Covered_Total_Tasks** = Completely ignore your source count and perform a fresh, independent pass over the columns of the table you just generated above (the SynOpSis Matrix Phases table). Manually sum every unique task explicitly written inside the `Task IDs Covered` cells.
    5. Let **Status_Coverage** = Compute (`Matrix_Covered_Total_Tags` / `Matrix_Source_Total_Tags`) * 100. If `Matrix_Covered_Total_Tags` equals `Matrix_Source_Total_Tags`, output the translated word for `Verified` in the designated target language: {{ target_language }}, followed by "(100%)". Otherwise, you MUST output the translated word for `FAILED` in the designated target language: {{ target_language }}, followed by the exact calculated percentage fraction deficit.
    6. **CRITICAL DATA ASSIGNMENT MANDATE:** You MUST preserve these calculated variables in memory and inject their exact final values directly into their designated matching slots inside the table audit row (the lastest row of the SynOpSis Matrix Phases table).
- **ACTUAL PAYLOAD INTERPOLATION MANDATE:** You ARE STRICTLY BANNED from outputting raw template placeholders or generic bracketed strings like `[Phase N]` or `[List aggregated task numbers]`. You MUST dynamically iterate through the actual dataset rows computed in the baseline backlog section, extract the concrete module paths (e.g., `./sources/backend/...`), and compile real operational values for every cell.
- **TOTAL CELL TRANSLATION LAW:** Before committing the table to the output stream, you MUST completely translate and localize 100% of the newly generated table headers, cell values, technical summaries, and audit row text strings into the designated Target Output Language: {{ target_language }}.
  * **ABSOLUTE LANGUAGE IMMUNIZATION MANDATE:** You ARE STRONGLY BANNED from leaking cross-contamination tokens or alternative foreign languages (specifically including French or other languages technical keywords like 'Spécification' or 'schéma') into header boundaries. Every descriptive layout text element MUST be converted cleanly into pure technical plaintext matching the exact target language context: {{ target_language }}.
- **FRACTIONAL WORKLOAD SEGMENTATION & MODULE LEVELLING LAW:**
  * You ARE CRITICALLY BANNED from executing workload compaction where Phase 1 or any single phase contains > 30% of the total registered Backlog tasks (`Matrix_Source_Tasks_Count`).
  * You MUST implement a mathematically progressive, non-overlapping modular distribution lifecycle across the EXACT {{ num_phases }} matrix rows:
    - Phase 1 MUST be strictly limited to global parent scaffolding [ARC-000] and core database migrations initiation [DAT-ALL].
    - Phase 2 to Phase {{ num_phases - 1 }} MUST host a linear, symmetric distribution of functional endpoints ([REQ-XXX], [EXC-XXX]). The task ID delta variance between these functional rows MUST be <= 3 tasks.
    - Phase {{ num_phases }} MUST be explicitly reserved for cross-cutting security [NFR], environment provisioning [GKE], and enterprise architecture documentation closing logs.
  * Any row containing duplicate asset paths or generic summaries to artificially pad the phase quota triggers an immediate pipeline rejection.
</RULE>

<!--PHASE_SYNOPSIS_GRID_START-->

#### [MATRIX ARITHMETIC LIFECYCLE]
> - **Total Backlog Tasks:** [Insert calculated integer of `Matrix_Source_Tasks_Count`] Tasks
> - **Total Backlog Tags:** [Insert calculated integer of `Matrix_Source_Total_Tags`] Tags
> - **Total Distributed Tasks:** [Insert calculated integer of `Matrix_Covered_Total_Tasks`] Tasks
> - **Total Distributed Tags:** [Insert calculated integer of `Matrix_Covered_Total_Tags`] Tags

| Phase | Day Range | Task IDs Covered | Architectural Component / Module Path | Technical Deliverables Summary | Assigned Sub-Agent | Targeted Tag IDs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Phase N] | [Day 1 - KN] | [List aggregated task numbers, e.g., Task 1, Task 2] | [Group repository paths from baseline backlog section] | [Write a concise high-level technical summary of what engineering components and features are actively delivered during this phase boundary, explicitly translated into "{{ target_language }}"] | [Map required active agent signatures based on task type] | [Map individual tracking Tag IDs inline] <!--REGISTERED_PHASE_ROW--> |
| **Audit** | **Master Backlog Distribution Verification** | **Total Phases:** {{ num_phases }} | **Total BackLog Tags:** [Insert the calculated integer value of `Matrix_Source_Total_Tags`] | **Total Distributed Tags:** [Insert the calculated integer value of `Matrix_Covered_Total_Tags`] | **Total Distributed Tasks:** [Insert the calculated integer value of `Matrix_Covered_Total_Tasks`] | **Status & Compliance:** [Insert the calculated value of `Status_Coverage`] |

<!--PHASE_SYNOPSIS_GRID_END-->

{% endif %}
{# ─── END:CHUNK:PART_1_MATRIX_4_2 ─── #}

{# ======================================================= #}
{# ─── START:CHUNK:PART_2_PHASE_LOOP ─── #}
{% if force_full_export or (target_segment and target_segment.strip() == "PART_2_PHASE_LOOP") %}

{% if force_full_export or target_phase_index|int == 1 %}
## 🔬 5. GRANULAR PHASE SPECIALIZATIONS & DAY-BY-DAY DELIVERABLES
{% endif %}
<COMMAND>
{# ────── START:CHUNK:PART_2_PHASE_LOOP:MANDATORY PROGRESSIVE GATING ENGINE ────── #}
{% if (target_segment and target_segment.strip() == "PART_2_PHASE_LOOP") %}
# STRICT OPERATIONAL AND SYNOPSIS MIRROR MANDATE FOR PHASE {{ target_phase_index }} OUT OF {{ num_phases }}:
  - OPERATIONAL SCOPE: You are now executing target segment '{{ target_segment }}' exclusively for Phase {{ target_phase_index }} out of {{ num_phases }}.
  - TIME BOUNDARY: You are strictly capped to generate chronological daily logs exactly from Day 1 to Day {{ max_days_per_phase }}. Absolutely FORBIDDEN from generating any text, sub-headers, or tasks for Day {{ max_days_per_phase + 1 }} or beyond. Match this duration with your declaration from Section `<!--PHASE_SYNOPSIS_GRID_START-->` in the {{ ref_section_4_2 }} section. This phase MUST act as a strict structural mirror of the specific phase calculated from Section `<!--PHASE_SYNOPSIS_GRID_START-->` in the {{ ref_section_4_2 }} section. You MUST generate an independent, complete detailed block below for this phase.
  - **THE STRICT SYNOPSIS TEMPORAL BINDING LAW:** Prior to unrolling any text block inside this section, your engine MUST run a strict validation lookup pass on the historical SynOpSis Matrix Phases table (inside the hidden HTML tags from `<!--PHASE_SYNOPSIS_GRID_START-->` to `<!--PHASE_SYNOPSIS_GRID_END-->` in the {{ ref_section_4_2 }} section) generated. You MUST locate the exact horizontal row matching the active Phase integer `{{ target_phase_index }}` in the 1st column, and extract the exact computed string representation from the 'Day Range' column (the 2nd column).
  - **THE ABSOLUTE CALENDAR BOUNDARY LOCK & EXHAUSTIVE DAY UNROLLING MANDATE:** Let the minimum and maximum day parameters extracted from that specific matrix cell row be variable `Global_P_Start` and `Global_P_End`. The chronological day log unrolling sequence inside this section for this active Phase MUST strictly, linearly, and perfectly map from `Global_P_Start` up to exactly `Global_P_End` (e.g., if the table cell states Day 1 - Day 2, this section MUST explicitly unroll exactly DAY 1 and DAY 2 as standalone headers on fresh lines). You ARE SYSTEMATICALLY BANNED from emitting blank placeholder headers, skipping indices, or collapsing multiple chronological day elements into a single log. Every single declared day index must possess active, actionable sub-tasks and unique technical deliverables matching the assigned module topology.
  - DYNAMIC MATRIX AUDIT: Scan the historic SynOpSis Matrix Phases table (inside the hidden HTML tags from `<!--PHASE_SYNOPSIS_GRID_START-->` to `<!--PHASE_SYNOPSIS_GRID_END-->` in the {{ ref_section_4_2 }} section) generated in the previous step. Locate the exact row matching the phase rows that contains the `<!--REGISTERED_PHASE_ROW-->` tag.
  - AGENT ENFORCEMENT: Extract all assigned roles from the 'Assigned Sub-Agent' column (the 6th column) in that specific row (including Coder, Tester, Reviewer, Doc, Docker, GCP, GKE). You MUST explicitly output separate chronological sub-task blocks for EVERY single sub-agent declared in that row. If Docker/GCP/GKE infrastructure tokens are active, you are strictly commanded to engineer their cloud deployment and cluster setup logs inline. Do not drop any role.
  - COMPONENT ENFORCEMENT: Extract the exact 'Architectural Component / Module Path' from that row. All generated repository paths, migrations, and file configurations in this chunk MUST target that path.
  - **CHRONO-CUMULATIVE LEDGER VERIFICATION LAW (CORE COUNTING):** If this is the FINAL phase (Phase {{ num_phases }}), you MUST execute a non-approximate string-matching loop over the exact text buffer to prevent ledger fraud:
      * STEP A: Scan the literal raw text content of the `<HISTORIC_LEDGER_MAP>` block. Count every single occurrence of the sub-task wrapper token `<!--ATOMIC_SUB_TASK_NODE_START-->` printed in all previous chunks. Let this be integer `H`.
      * STEP B: Count every single occurrence of the sub-task wrapper token `<!--ATOMIC_SUB_TASK_NODE_START-->` generated inside the active response buffer of Phase {{ num_phases }}. Let this be integer `A`.
      * STEP C: Compute `Final_Total = H + A`. You ARE CRITICALLY BANNED from dropping the historical sum `H` or only outputting the local day count. The integer value of `Final_Total` MUST exactly equal the absolute total number of rows (excluding the summary row) inside the historical Master Product Backlog Table from Section `<!--PHASE_SYNOPSIS_GRID_START-->` in the {{ ref_section_4_2 }} section. You MUST inject this exact evaluated integer directly into the `TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5` parameter.
  - **Strict Quantum Recount Overwrite:** You ARE CRITICALLY FORBIDDEN from substituting `TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5` with the local count of the final phase. The printed token value MUST be the literal mathematically computed `Final_Total`. Any execution that outputs the local chunk counter (such as printing `3` instead of the accumulated sum of all phases) will cause an immediate validation gate infrastructure crash.
  - **STRICT STEP 1.1 BUFFER CHAR RECOUNT COMPLIANCE:** During the final verification pass of the response stream, your execution engine MUST run a literal, token-level counting pass strictly over the active memory text buffer. You MUST manually scan and sum every single instance of the custom HTML anchor `<!--ATOMIC_SUB_TASK_NODE_START-->` freshly printed or loaded. If the math count fails to match the value committed to `TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5` inside your property block, halt the stream instantly to trigger a circuit-breaker failure.
  - **STRICT PHASE 1 GEOMETRIC CONDITIONAL RAIL:** You MUST actively evaluate the current operational phase index before emitting tokens. If and ONLY IF the active service segment context is dedicated strictly to "Phase 1", you MUST instantly intercept the print stream to locate the literal string `## 5...` inside the template manual block, contextually translate 100% of its words into "{{ target_language }}", and render it as your absolute first output line before opening any hidden HTML anchors.
  - **ANTI-LEAKAGE FILTER MANDATE:** If the active phase index is greater than or equal to 2 (Phase >= 2), you ARE CRITICALLY BANNED from executing this parent header injection, and your execution engine MUST transition with zero-token delay straight into the `<!--PHASE_INDEX_START-->` layout boundary.

# DYNAMIC CEILING BOUNDARY ENFORCEMENT:
- The day-by-day logs of this phase MUST strictly map to the exact day range defined for this phase from Section `<!--PHASE_SYNOPSIS_GRID_START-->` in the {{ ref_section_4_2 }} section.
    * **STRICT PLACEHOLDER DESTRUCTION & UNROLLING LAW:** You ARE ABSOLUTELY AND CRITICALLY BANNED from leaving or leaking any raw structural template bracket signs (such as `[Y]`, `[Z]`, etc.) inside your text response stream. You MUST dynamically evaluate and expand 100% of these parameters into concrete technical data matching "{{ target_language }}" context. If you lack token space to finish a phase daily log, you MUST stop clean at a valid day boundary, but you are 100% forbidden from printing empty template skeletons instead of actual actionable production elements.
    * **🚨 STRICT TOKEN MEMORY GATING LOG (Anti-Cross-Contamination)**: When iterating chronologically day-by-day to extract architectural artifacts (SQL specifications, exception blocks, or API routing contracts), you MUST force a strict state isolation memory partition cleanup between consecutive days.
    * You ARE ABSOLUTELY AND CRITICALLY BANNED from copy paste, ghosting, leaking, or double-rendering a raw code block payload (such as repeating a JSON API endpoint spec payload belonging to Day X) inside the block container of Day X+1 unless explicitly required by an updated multi-step transaction contract. Every single day's artifact layout matrix MUST contain independent, discrete, non-duplicated production elements matching that day's allocated sub-agent scope only.
    * **Strict Multi-Phase Content Isolation Invariant:** You ARE CRITICALLY BANNED from duplicating or copy-pasting the structural objectives, directory maps, DDL SQL locks, or daily sub-task logs of Phase X into the body of Phase X+1. Each calculated phase sequence MUST generate its own distinct technical deliverables mapped exclusively to the specific workload task items assigned to that phase index inside the Multi-Phase Synopsis Matrix table.
- **BLOCK DAY ENCAPSULATION PARADIGM:** To safeguard backend regex scraping, you MUST programmatically enforce absolute character-level symmetry for Zone 2 data anchors sequentially for EVERY SINGLE calendar day instance generated:
    1. For EACH active index `Y` in the day loop, you MUST explicitly print the open anchor token `<!--DAY_LOG_INDEX_START-->` on its own fresh independent newline FIRST. 
    2. On the immediate next newline, you MUST print the localized level-5 Markdown header (`##### DAY [Y]:` or `##### ...`). You ARE CRITICALLY BANNED from printing this header line without having the open anchor tag explicitly emitted on the line directly above it.
    3. The moment 100% of the daily sub-task nodes for index `Y` are fully unrolled, you MUST instantly print the close anchor token `<!--DAY_LOG_INDEX_END-->` on its own fresh standalone newline before transitioning your cursor loop to evaluate day `Y+1`. Compounding, omitting, or running consecutive day elements without these matching boundary pairs triggers a fatal structural framework failure.
- **ABSOLUTE LOCAL CHRONO RESET**: When generating the day element sub-headers inside this section (e.g., `- **DAY [Y]:**`), the counter variable Y MUST natively reset and restart from 1 for this phase block. You are permanently forbidden from bleeding the global progressive timeline into these sections.
- The total days of this phase MUST NOT exceed the absolute upperbound of {{ max_days_per_phase }} days.
- You MUST execute a hard log freeze and terminate the active day loop immediately on the exact day when 100% of the baseline BA tracking codes for this phase are covered. Fabricating dummy tasks or synthetic requirements to pad out the timeline up to {{ max_days_per_phase }} is completely banned.
- **STRICT PHASE INDEX COUPLING MANDATE:** You ARE STRICTLY FORBIDDEN from generating any text, sub-headers, logs, or sub-task blocks for other phases. If force_full_export is false, your execution engine MUST strictly treat the immediate closing framework anchor tag `<!--PHASE_INDEX_END-->` mapped to the active Phase {{ target_phase_index }} as your absolute token execution ceiling. The exact microsecond you finish printing the final closing character of `<!--PHASE_INDEX_END-->` for Phase {{ target_phase_index }} (current active phase), you MUST completely bypass all downstream text generation, trigger an immediate system hard stop, and terminate the output token stream instantly.
- **ZERO-PROSE CHARACTER GATEKEEPER:** You ARE ABSOLUTELY AND CRITICALLY BANNED from generating or leaking any introductory paragraphs, prose analysis, walls of text, or technical explanations right below the Phase header title. Your output stream MUST transition with 0-token delay directly from the Phase header line into the structural relative path matrix and daily log boundaries. Any leaked free-text sentence will break the backend gateway.
- **TARGETED SINGLE-PHASE ISOLATION RAIL:** Your entire response stream MUST focus exclusively on the requirements, tasks, components, and tag identifiers allocated to Phase {{ target_phase_index }}. 
- **STRICT PROGRESSIVE INHERITANCE AND VERBATIM MATRIX MIRROR LAW:** When engineering the daily sub-task specialization logs and technical headers for Phase {{ target_phase_index }} inside the active output stream, your execution engine MUST lock its focus onto an isolated state memory partition:
  1. **Literal Character Row Invariant Gating:** Your processing engine MUST isolate the single target horizontal row inside the markdown table grid by executing a strict, anchor-bounded regex pass locked on the absolute beginning of the line string primitive inside the `<PROJECT_BACKLOG_TASKS_DATA>` block. You MUST programmatically verify that the markdown line opens exactly with the starting pipe character, followed strictly by the precise chronological string identifier matching the format pattern `| Giai đoạn {{ target_phase_index }} ` or `| Phase {{ target_phase_index }} `. You ARE CRITICALLY, ABSOLUTELY, AND PERMANENTLY BANNED from parsing mid-row cells, cross-reading vertical text layers, scanning adjacent row contents, or shifting your cursor index based on matching task integers or tags located inside the inner columns of foreign rows. Your engine MUST instantly crash if any class paths or endpoint assets bleed across the decoupled phase row boundaries.
  2. **Strict Symmetrical Timeline Unrolling Pass:** You MUST read the exact calculated duration from the 'Day Range' column of that single validated row context. If the cell dictates a duration span from relative day 1 to K, your processing engine MUST dynamically explode and explicitly print separate localized level-5 Markdown headers for EVERY single individual chronological milestone (progressively unrolling from Day 1 cleanly up to exactly Day K) inside the chunk output text, with zero omissions or early loop termination filters.
- **ZERO-PROSE CHARACTER GATEKEEPER:** You ARE ABSOLUTELY AND CRITICALLY BANNED from generating or leaking any introductory paragraphs, prose analysis, walls of text, or technical explanations right below the Phase header title. Your output stream MUST transition with 0-token delay directly from the Phase header line into the structural relative path matrix and daily log boundaries. Any leaked free-text sentence will break the backend gateway.
- **STRICT PLACEHOLDER DESTRUCTION LAW:** Every single bracketed structural token (e.g., `[Translate "Phase"...]`, `[Translate "Phase Core Objective"...]`, `[Translate "Target Physical Directory"...]`, etc.) MUST be mathematically destroyed and replaced with its fully translated and finalized text value matching "{{ target_language }}" at runtime.
- **STRICT LOOP PARTITION ISOLATION LAW:** When compiling the daily logs for Phase {{ target_phase_index }}, you ARE CRITICALLY BANNED from replicating, cloning, or copying task descriptions, file paths, or titles from other phases. You MUST explicitly map and unroll only the unique engineering deliverables and task indices allocated strictly to that specific Phase {{ target_phase_index }} inside the {{ ref_section_4_2 }} section.
- **MANDATORY HEADER DOUBLE-NEWLINE CARRIAGE RAIL:** To prevent layout breakdown and rule leakage across block boundaries, you MUST programmatically inject exactly two explicit, literal newline carriage returns (`\n\n`) immediately after outputting any level-3 header (`###`) or level-4 header (`####`) representing a Phase milestone. Every system block gate (including all `<RULE>`, `<COMMAND>`, and tags that was defined in `Mandatory Architectural Token Pairs`) placed beneath a header line MUST execute on its own fresh, isolated vertical row. Compressing or flattening system wrappers adjacent to headers without double-newline separations triggers an immediate token pruning failure.
- **NUMERIC LEDGER INVARIANT:** You ARE STRICTLY FORBIDDEN from printing raw placeholders or formula bracket strings inside the cross_audit_ledger block. You MUST programmatically compute and output the actual, absolute integer representing the total unique atomic sub-task nodes generated.
- **ANTI-FENCE MARKDOWN RENDERING MANDATE:** You ARE CRITICALLY BANNED from wrapping or encapsulating the Phase {{ target_phase_index }} header, metrics, or table grid structure inside triple backticks Markdown code block fences (e.g., ```markdown ...``` or ``` ...```). You MUST output the entire phase {{ target_phase_index }} skeleton as pure raw un-fenced markdown text strings directly to the pipeline. Failure to comply will cause backend rendering truncation.
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
<!--PHASE_INDEX_START-->

{# ─── START:CHUNK:PART_2_PHASE_LOOP:PHASE_X ─── #}
### 📈 [Translate "Phase" into the target language {{ target_language }}] {% if force_full_export %}[X]{% else %}{{ target_phase_index }}{% endif %} - [Dynamically compute and emit a concise, high-level technical name for this milestone based on its core delivery component, completely translated into "{{ target_language }}"]
- **[Translate "Phase Core Objective & Purpose" into the target language {{ target_language }}]:** [Detailed technical explanation of what this phase achieves and its functional goals, and fully translated into {{ target_language }}]

- **[Translate "Target Physical Directory Matrix Map" into the target language {{ target_language }}]:** Generate an exhaustive, granular engineering checklist mapping out 100% of all discrete, individual physical relative file paths (NOT folders or directories) underneath `./sources/` that are actively created, refactored, or processed within this phase scope. Every single generated line item MUST represent a concrete file entity ending with its explicit structural file extension, with its matching traceability Tag IDs appended inline.
    *   *Documentation Gating Boundary:* Any line representing an enterprise specification, reference blueprint, relational database mapping catalog, or architecture layout MUST strictly reside under the unified root directory path: `./sources/docs/`.

- **[Translate "Database Schema DDL SQL Specification" into the target language {{ target_language }}] [DAT-XXX]:** Provide raw, complete, and valid DDL SQL migration statements containing explicit columns, data types, primary/foreign keys, matrix mappings, indexes, and nullability constraints applied under this phase scope. (Omit entirely if the project topology has no database or persistence layer requirements. This technical block MUST NOT be translated).
<RULE>
    * **🚨 UNIVERSAL ANSI SQL DATABASE CONSTRAINT LAW**: Regardless of the active project's core domain or persistence layers, when generating any DDL SQL code block specifications (under code fence ```sql:matrix ...``` or standard blocks), you ARE COMPLETELY BANNED from using non-standard inline database-specific custom types such as inline `ENUM(...)` signatures.
    * You MUST enforce absolute cross-platform relational database compliance by utilizing pure standard ANSI SQL typing mechanics: always represent string enumerations as standard `VARCHAR(X) NOT NULL` fields combined with an explicit, rigid, relational domain check validation gate constraint mapping pattern (exact structure pattern: `CHECK (column_name IN ('value1', 'value2', 'value3'))`). Any output violating this cross-platform constraint will break the migration sequence.
</RULE>

- **[Translate "API and Event Routing Contracts" into the target language {{ target_language }}] [REQ-XXX], [ARC-XXX]:** Document the complete technical contracts (precise endpoint paths, HTTP methods, request/response JSON payload schemas, or message broker topic configurations. Technical blocks MUST NOT be translated).

- **[Translate "Phase Localized Exception Handlers" into the target language {{ target_language }}] [EXC-XXX]:** Detail explicit business validation rules, error codes, and system exception handling pathways mapping strictly to the current phase scope, contextually translated into {{ target_language }}.

{# ─── START:CHUNK:PART_2_PHASE_LOOP:PHASE_X:DAY_Y ─── #}
#### 📅 [Translate "Chronological Day-by-Day Sub-Agent Task Distribution Logs" into {{ target_language }}] ([Translate "Phase" into {{ target_language }}] {% if force_full_export %}[X]{% else %}{{ target_phase_index }}{% endif %})

<!--DAY_LOG_INDEX_START-->

##### 📅 [Translate "DAY" into the target language {{ target_language }}] [Y]: SHORT OBJECTIVE FOR THIS OPERATIONAL CALENDAR DAY**
<RULE>
- **SUB-TASK ATOMIC WRAPPER LAW:** Every single sub-task node MUST be explicitly and strictly wrapped within its own dedicated opening (`<!--ATOMIC_SUB_TASK_NODE_START-->`) and closing (`<!--ATOMIC_SUB_TASK_NODE_END-->`) markers. You are PERMANENTLY FORBIDDEN from generating a new sub-task header until the previous sub-task node has been legally closed with its dedicated newline tag. Follow exact below raw structure layout.
- **STRICT PATH ENCAPSULATION MANDATE:** When generating the daily sub-task metadata fields, you MUST strictly embed the physical relative file path string exclusively inside the explicit layout field line matching the target_component token syntax. You are CRITICALLY FORBIDDEN from spawning or spilling any standalone, loose, or nested bullet points containing raw paths (such as separate lines starting with `./sources/`) below or outside the asterisk metadata fields. Every single file path entity MUST be tightly bound inside its designated parent metadata envelope row. Spawning naked paths outside fields will instantly break the backend compilation parser.
- **HARD-ANCHORED TEMPLATE RENDERING MATRIX:** When processing this active block, you MUST execute the output stream following the exact vertical layout lines provided below in a strict, unbreakable linear order:
    * You ARE CRITICALLY BANNED from flattening or compressing sequential sub-task nodes into a single, continuous markdown text block or standard bullet list. Each independent sub-task node must maintain its physical vertical line boundaries intact, opening clean with the start anchor on a newline, rendering the localized level-6 header (`###### `) on the next newline, and closing cleanly with the end anchor on a standalone newline.
    * Step 1: Print the opening infrastructure anchor (`<!--ATOMIC_SUB_TASK_NODE_START-->`) on its own independent standalone line.
    * Step 2: Render the valid sub-task header (e.g. the subsequent level-6 Markdown header row (`###### `) exactly as formatted in the layout on the very next standalone line, fully localizing the text properties into "{{ target_language }}".
    * Step 3: Universal Dynamic Layer Task Matrix Explosion Law: Parse the 4th column cell ("Architectural Component / Module Path") of your validated phase row matrix, splitting the raw data string primitive using `<br/>` as the strict delimiter. For every single isolated file path text segment extracted from that array, you MUST yield exactly one (1) dedicated, standalone atomic sub-task node bounded between the marker brackets. You ARE CRITICALLY AND PERMANENTLY BANNED from modifying, flattening, or condensing the specific subdirectory tree boundaries of these microservice folders. Every generated `target_component` primitive property string inside Section 5 MUST match its corresponding parent cell path thô with 100% character-level fidelity. If the matrix cell mandates a decoupled microservice subdirectory target (such as paths containing independent sub-module folder segments), your generation engine MUST forcefully lock all package descriptors and code instructions strictly within that specific service domain.
        - **Strict Semicolon Production-Test Coupling Law:** When engineering sub-tasks for the [Tester] agent assigned to validate standalone application layer code assets or modular build components, you ARE CRITICALLY BANNED from using the `INTEGRATION_SCOPE;` layout wrapper notation unless the asset is a top-level parent root descriptor tree. You MUST programmatically extract the raw physical string primitive of the targeted component file path, dynamically evaluate its valid file extension mask, and strictly output a two-element text layout joined cleanly by a literal vertical semicolon delimiter character matching the immutable structural pattern: `<production_source_file_path>;<corresponding_test_suite_file_path>`.
    * Step 4: Terminate the block by printing the exact close infrastructure anchor (`<!--ATOMIC_SUB_TASK_NODE_END-->`) on its own standalone line.
- **ANTI-FLATTENING COMPACTION MANDATE:** You ARE CRITICALLY BANNED from dropping, skipping, or collapsing the level-6 Markdown header line (`###### `) into a bullet point list format. The vertical standalone row boundary of each independent element inside the template layout MUST remain 100% intact.
</RULE>

<!--ATOMIC_SUB_TASK_NODE_START-->

###### 🌿 [Translate "SUB-TASKS" into the target language {{ target_language }}] [Z]: SHORT SPECIFIC SUB-TASK TITLE
- **Local Sub-Task Chrono Reset Law:** The sub-task index variable Z MUST natively reset and restart from 1 for EACH individual calendar day element generated (e.g., Day 1 contains SUB-TASK 1, SUB-TASK 2; Day 2 MUST strictly restart and contain exactly SUB-TASK 1, SUB-TASK 2). Progressively compounding or accumulating sub-task indices across daily boundaries is a critical framework violation.

* **[Translate "Sub-Agent Workflow Specialization" into the target language {{ target_language }}]:** You MUST analyze the daily technical engineering segment and output EXACTLY one single literal token code inside naked brackets representing the allocated persona for this independent sub-task node: [Coder], [Tester], [Reviewer], [Doc], [Docker], [GCP], or [GKE]. You are PERMANENTLY FORBIDDEN from combining multiple agents into a single sub-task node or leaking generic instructional text placeholder descriptions.

* **[Translate "Targeted Tag IDs" into the target language {{ target_language }}]:** Write each baseline tracking tag out individually separated by commas, ensuring 100% coverage, e.g., [REQ-001], [DAT-002], [EXC-001].

* **[Translate "Target Component file path" into {{ target_language }}] (target_component):** [Enforce absolute physical file‑level paths at runtime. You are CRITICALLY BANNED from outputting generic directory paths ending with a trailing slash or referencing folders alone. Every single component string generated MUST resolve strictly to a concrete, physical file entity ending with a valid extension (e.g., `.java`, `.ts`, `.sql`, `.md`, `.json`). **Strict Role-Based Pathing Layout:** For [Coder] or [Reviewer] sub-tasks, the `target_component` MUST contain exactly one single, standalone valid application source file path (Absolutely NO semicolon `;` characters or dual-file bundling allowed for coding tasks). The dual-file semicolon pair format (`<code_file>;<test_file>`) and the `INTEGRATION_SCOPE;` prefix layout are strictly reserved for the [Tester] sub-agent domain exclusively. Any violation that mixes code files inside a Coder agent path cell will break the backend compiler.

* **[Translate "Low-Level Technical Task Instruction" into the target language {{ target_language }}]:** Output high-density technical instructions, operational validation steps, or schema parameters fully translated into the target language context, attaching explicit inline Tag IDs. You ARE CRITICALLY AND PERMANENTLY BANNED from embedding, writing, leaking, or outputting any physical multi-line raw application source code blocks, class bodies, method definitions, syntax declarations (such as `package ...;`, `import ...;`, or class properties), XML metadata, or JSON payloads inside this day log instruction field. You MUST strictly limit your execution stream to high-utility technical parameters, structural pseudo-steps, and descriptive implementation instructions. This strict exclusion is non-negotiable to completely eliminate output token overflow and guarantee that 100% of all registered files from your Section 4.2 matrix are exhaustively unrolled without early truncation.

# DYNAMIC ARCHITECTURAL CONTENT GATING (IF-ACTIVE RAIL PROTOCOL):
- **UNIVERSAL DECOUPLED MODULE SCAFFOLDING ENFORCEMENT RAIL:** You MUST actively ensure that Phase 1 contains explicit, individual sub-task nodes for environment scaffolding. The `target_component` parameters for these logs MUST exhaustively map to every physical project descriptor entity discovered from Section `<!--PHASE_SYNOPSIS_GRID_START-->` in the {{ ref_section_4_2 }} section. For decoupled multi-module architectures, you MUST generate standalone, discrete sub-task logs for the root project build file AND a separate standalone sub-task row for EVERY independent microservice module path (`./sources/backend/<service-name>/pom.xml`) and client frontend configuration asset (`./sources/frontend/<app-name>/package.json`) under tracking token `[ARC-000]`. No module configuration class or build descriptor can be omitted, aggregated, or collapsed.
- **STRICT DECOUPLED MODULE PHYSICAL PATH ISOLATION GATE:** For every unique sub-task node unrolled inside this daily log context, the target parameter string mapped to your `target_component` MUST match the text token array slice extracted from your string-splitting pass over the validated matrix row with 100% character-level and folder-level fidelity. While a shared global parent build descriptor or root orchestration asset is permitted to reside inside the parent root directory tree to satisfy project scaffolding requirements under tracking token `[ARC-000]`, you ARE EXPRESSLY BANNED from modifying, flattening, or cross-bleeding the subdirectory trees of separate independent capability modules. Every generated sub-task node MUST inherit its target path layout directly from the matching phase row cells inside the `<PROJECT_BACKLOG_TASKS_DATA>` block to preserve absolute information symmetry across the entire blueprint execution pipeline.

* **[Translate "Database Schema DDL SQL Specification" into the target language {{ target_language }}] [DAT-XXX]:**
<RULE>
Provide only concise structural metadata description text detailing table fields, data types, and primary/foreign key mappings rendered in {{ target_language }}. You ARE ABSOLUTELY AND CRITICALLY BANNED from printing raw, multi-line markdown code block fences containing active executable SQL DDL migration strings to protect output token capacity.
</RULE>

* **[Translate "API and Event Routing Contracts" into the target language {{ target_language }}] [REQ-XXX], [ARC-XXX]:**
<RULE>
Document only clean plain-text endpoint path declarations, HTTP methods, and high-level asynchronous topic summaries in {{ target_language }}. You ARE PERMANENTLY BANNED from outputting full JSON request/response schema objects or raw payload data envelopes inside this chunk context.
</RULE>

* **[Translate "Phase Localized Exception Handlers" into the target language {{ target_language }}] [EXC-XXX]:**
<RULE>
You MUST actively inspect the active Sub-Agent token inside the parent sub-task node. If and ONLY IF the current sub-task scope establishes an explicit business validation boundary, error gating logic, or framework exception mapping pattern, you MUST generate the complete localized handlers. Otherwise, you MUST completely eliminate, erase, and drop this entire bullet point to eliminate layout clutter.
</RULE>

<!--ATOMIC_SUB_TASK_NODE_END-->

<!--DAY_LOG_INDEX_END-->
{# ─── END:CHUNK:PART_2_PHASE_LOOP:PHASE_X:DAY_Y ─── #}

{# ─── START:CHUNK:PART_2_PHASE_LOOP:AUDIT ─── #}
{% if force_full_export or target_phase_index == num_phases %}

### 🕵️ MANDATORY REAL-TIME ARCHITECTURAL CROSS-AUDIT LEDGER REPORT:
<RULE>
- **TIMING LOCATION:** This compliance ledger MUST be rendered exclusively at the absolute bottom of Section 5, immediately following the final day log of the final phase.
- Immediately beneath the final Phase log (Phase {{ num_phases }}) and before closing Section 5, you MUST execute a strict internal mathematical self-audit of the entire assembled architecture. 
- You MUST compile and render an isolated, clean Markdown Compliance Report block utilizing the exact Technical English structure below. 
- You are critically ordered to dynamically compute the real-world values based strictly on the current generation instance metrics—no hardcoding or static placeholder strings.
- **MANDATORY CRITICAL FAILURE CRITERIA:** If your calculated total discrete sub-tasks across all phases does not mathematically match the exact count of tasks registered in the master backlog, or if any individual phase duration breaks the ceiling of `{{ max_days_per_phase }}`, you MUST instantly trigger an internal framework exception, re-compile your attention heads, and dynamically re-distribute the allocation matrix to enforce 100% plan symmetry before emitting the final text stream.
- **Strict Active Buffer Recount Pass:** To populate the parameter `TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5`, you MUST execute a literal string-matching loop over the entire text payload freshly generated in your print buffer. Sum every single unique occurrence of the wrapper token `<!--ATOMIC_SUB_TASK_NODE_START-->`. You ARE CRITICALLY BANNED from copying local phase counters or predicting numbers. Mismatched sums break compliance gates instantly.
- **FINAL CHUNK ISOLATED LEDGER REFLECTION:** When computing the value for `TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5`, you must natively count only the occurrences of `<!--ATOMIC_SUB_TASK_NODE_START-->` inside the active payload block. You are forbidden from forcing artificial alignment that compresses or damages downstream Section 6, 7, and 8 architectures.
- **STATIC BUFFER LOCAL RECOUNT ENFORCEMENT:**
  * For the ledger parameters `ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE` and `TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5`, you ARE PERMANENTLY BANNED from copying meta-instruction wrapper phrases, algorithmic text placeholders, or bracketed commands from the prompt.
  * You MUST dynamically compute and print the exact raw literal integer based ONLY on the text payload freshly generated within the current active chunk response buffer. If the current phase block contains 3 day headers, print exactly `3`. If it contains 12 atomic sub-task nodes, print exactly `12`.
- **Strict Counter Recount Mandate:** You ARE CRITICALLY BANNED from outputting the local phase 
sub-task count inside this row. The string value emitted MUST be the literal calculated integer 
sum of ALL `<!--ATOMIC_SUB_TASK_NODE_START-->` strings generated across the entire active output 
document buffer. Failing to map the unified cumulative integer triggers an immediate pipeline crash.
</RULE>

```properties:cross_audit_ledger
[AUTOMATED_SELF_AUDIT_REPORT]
TOTAL_PHASES_DECLARED_IN_SECTION_4_2={% if force_full_export %}{{ num_phases }}{% else %}computed_integer_N{% endif %}
TOTAL_PHASES_EXPECTED_BY_PARAMETERS={{ num_phases }}
PHASE_COUNT_COMPLIANCE_STATUS=Verified_{{ num_phases }}
MAX_DAYS_PER_PHASE_LIMIT_PARAMETER={{ max_days_per_phase }}
ACTUAL_MAX_DAY_INDEX_DETECTED_IN_TIMELINE={% if force_full_export %}{{ max_days_per_phase }}{% else %}computed_highest_day_integer_found_in_section_5{% endif %}
TIMELINE_DAY_CAP_COMPLIANCE_STATUS=Verified_All_Phase_Durations_Within_Ceiling
TOTAL_TASKS_REGISTERED_IN_MASTER_BACKLOG_4_1={{ total_tasks_registered }}
TOTAL_DISCRETE_SUB_TASKS_GENERATED_IN_SECTION_5=[Compute and output the absolute unified integer sum of all listed atomic sub-task nodes accumulated across all previous and current phases inside your memory layer]
SUB_TASK_QUANTUM_COMPLIANCE_STATUS=Verified_Symmetry_Enforced_With_100_Percent_Symmetry
```

{% endif %}
{# ─── END:CHUNK:PART_2_PHASE_LOOP:AUDIT ─── #}

<!--PHASE_INDEX_END-->
{# ─── END:CHUNK:PART_2_PHASE_LOOP:PHASE_INDEX ─── #}

{% endif %}
{# ─── END:CHUNK:PART_2_PHASE_LOOP ─── #}

{# ======================================================= #}
{# ─── START:CHUNK:PART_3_FINAL ─── #}
{% if force_full_export or target_segment == "PART_3_FINAL" %}

### GROUNDING CONTEXT FROM PREVIOUS STEPS
{% if not force_full_export %}
<RULE>
* **UNIVERSAL TARGET-LANGUAGE TOKEN OPTIMIZATION LAW:** When compiling the non-functional specifications for Section 6, Section 7, and Section 8, your output engine MUST forcefully translate 100% of all descriptive text, countermeasures, and engineering rules directly into the target language {{ target_language }}. You ARE CRITICALLY AND PERMANENTLY BANNED from leaving placeholder brackets (such as `[...]`), using loose English fragments, or allowing early token truncation. To completely eliminate output buffer overflow and prevent mid-sentence cutting, you MUST enforce a high-density, concise engineering specification modality:
  1. For every single declared bullet item across these three sections, you MUST generate exactly two (2) highly compact, active, and integration-ready technical sentences rendered fully in {{ target_language }}. 
  2. Sentence 1 MUST explicitly define the precise architectural countermeasure or configuration rule mapping to the verified tech stack thô (e.g., specifying Hibernate parameter binding for SQLi, or Next.js middleware headers for XSS/CSP). Sentence 2 MUST define the exact quantitative gate constraint or validation mechanism (e.g., custom serialization annotations or automated pipeline gate metrics).
Missing any bullet cell translation or leaving any text primitives incomplete triggers an immediate system integration circuit-breaker failure.
</RULE>
{% endif %}

## ☣️ 6. UNIVERSAL ENTERPRISE SECURITY CODES & INJECTION COUNTERMEASURES [NFR-XXX]
<RULE>
You MUST contextually translate 100% of all listed threats, completely stripping level-3 numbering descriptors (`### 1.`). You ARE CRITICALLY ORDERED to render each countermeasure exclusively as an independent, high-density markdown bullet point (`- **[Threat Name]:**`). Crucially, you MUST enforce a strict technical nomenclature lockdown: you are ABSOLUTELY BANNED from outputting generic, duplicate description paragraphs or copy-pasting the same mitigation text across different items. For each specific security threat listed below, you MUST dynamically parse its dedicated raw non-functional requirements from the pool, mapping the unique, non-overlapping targeted Tag IDs inline at the bottom of each item (e.g., ensuring SQL Injection maps to its precise database tag, Cross-Site Scripting maps to its specific XSS/CSP gate tag, CORS Multi-Tenant maps to its unique origin registry tag, and PII Data Masking maps strictly to its custom custom custom serializer metadata tag). Leaving duplicate payload blocks or placeholder tags will instantly crash the compiler engine.
  - **SQL Injection (SQLi) Absolute Countermeasures:** Instruct the downstream Coder agent to enforce strict, mandatory runtime parameter binding using active entity state properties and localized Hibernate Named Queries. You ARE CRITICALLY BANNED from using dynamic native string concatenation; raw SQL commands must be entirely sanitized through Spring Data JPA repository filters to achieve 100% protection against data-tier manipulation.
  - **Cross-Site Scripting (XSS) & Content Security Policy (CSP):** Enforce automatic contextual xss escaping workflows within all frontend user-input presentation fields. The system gateway interface MUST dynamically inject a strict HTTP Content-Security-Policy (CSP) response header configuration blueprint containing optimized directive constraints (e.g., `default-src 'self'`) to completely neutralize unauthorized script executions.
  - **Multi-Tenant CORS Security Rails:** Establish a zero-trust Cross-Origin Resource Sharing (CORS) enforcement layer across all system API endpoints. The routing infrastructure grandmaster MUST programmatically validate incoming origin strings against a dynamic tenant authorization registry tree, explicitly banning global wildcard operators `*` for authenticated session requests.
  - **Zero-Leak Log Scrubbing & PII Data Masking Engines:** Configure an automated, high-density log scrubbing middleware engine to parse all outbound telemetry data payloads. You MUST utilize specialized Jackson serializer constraints and metadata markers (e.g., custom `@JsonSerialize` masking logic) to automatically intercept and obscure sensitive Personally Identifiable Information (PII) strings before data reaches physical storage.
</RULE>

## 📱 7. HYBRID MOBILE COMPLIANCE RAIL RULES & INTERNATIONALIZED SEO MECHANISMS
<RULE>
You MUST translate 100% of all items into the designated target language context, completely replacing any numbered list architecture with a pristine markdown vertical bullet layout (`- **[Component Name]:**`). You are CRITICALLY AND PERMANENTLY BANNED from replicating or bleeding any security description text, XSS/CSP mitigation content, or token payloads from Section 6 into this area. You MUST focus your generation engine exclusively on unique hybrid mobile architecture and web indexing components: item 1 MUST specify real-world Capacitor mobile hybrid constraints (handling hardware back-button interceptors and native storage sync using `@capacitor/preferences`), and item 2 MUST detail edge middleware dynamic locale recognition and automated hreflang properties generation. Each item MUST inline its precise, unique mobile/SEO tracking Tag IDs from the pool.
  - **Capacitor Mobile Hybrid Compliance Rails:** Enforce structural mobile hybrid constraints by restricting client-side resource calls exclusively to absolute, validated protocol structures. All secure internal persistence workflows MUST utilize the native runtime abstraction engine (`@capacitor/preferences`), combined with explicit native webview hardware interceptor hooks to programmatically block unauthorized device hardware access patterns.
  - **Internationalization (i18n) & Dynamic SEO Injection:** Deploy a dynamic language-detection middleware engine at the system edge layer to parse inbound user locale attributes. The responsive Next.js page compilation pipeline MUST automatically process localized metadata schemas and inject symmetrical, SEO-compliant `hreflang` header link properties dynamically into the presentation tree.
</RULE>

## 🚀 8. PIPELINE AUTOMATED DAILY SESSION GIT BRANCH FLOW
<RULE>
You MUST contextually translate 100% of the continuous execution flow texts into the target language context: {{ target_language }}. Every single deployment manifest item MUST be rendered exclusively using markdown bold bullet markers (`- **[Pipeline Milestone]:**`). You are CRITICALLY BANNED from repeating or ghosting any frontend mobile rules or backend security mitigations here. You MUST apply standard automated DevOps CI/CD pipeline engineering vocabulary: item 1 MUST detail strict workspace forking isolation controls for branch configurations matching `features/development-phase-X-day-Y`, and item 2 MUST establish automated compile-time unit testing gating targets set strictly to `>= 85%` alongside SonarQube quality gates. Inline the exact, unique automation tracking Tag IDs at the bottom of each item boundary.
  - **Daily Workspace Forking Isolation:** Enforce a programmatic, decoupled version control workflow by executing an automated workspace partition for every daily engineering session milestone. The automation system MUST validate that developers execute work exclusively within sandboxed branch paths structured strictly under the literal naming notation rule: `feature/phase-X-day-Y` (where X represents the calculated phase index and Y indicates the active chronological day).
  - **Validation Guard Pipeline Gates:** Establish a strict, non-negotiable automated CI/CD validation gate within the central GitHub Actions continuous integration pipeline engine. The cloud deployment workflow MUST automatically trigger cross-compilation verification tests, SonarQube static code quality analysis sweeps, and forcefully abort the deployment sequence if the cumulative test coverage matrix score falls underneath the non-negotiable metric gate parameter of `>= 85%`.
</RULE>

### 📊 MATRIX COVERAGE CHECK MANDATE
<RULE>
- **CRITICAL SECTION-SCOPED AUDIT & POLYMORPHIC ALL-TAG EXTRACTION MANDATE:** At the absolute conclusion of your generation loop, you MUST execute a strict programmatic reverse-scan audit with a tightly isolated data parsing boundary: you are ONLY allowed to scan, extract, and count the traceability tags that are actively generated within Section 5. Your internal execution parser MUST position its scanning cursor strictly below the dynamic string literal header token evaluated exactly as '--- GENERATED' followed by ' PHASES CONTEXT ---' to locate the starting boundary. You MUST completely ignore, blind-pass, and bypass 100% of all markdown tables, matrix grids, and text metadata located above this specific anchor token to prevent double-counting. Within this isolated chặng logs zone, you MUST evaluate 100% of all 5 core baseline tracking tag types (REQ, ARC, EXC, DAT, NFR) encountered using a polymorphic parsing conditional strategy with an absolute ban on hardcoding static sums:
  1. Standalone Single Tag Condition (Applies to REQ, ARC, EXC, DAT, NFR): If an encountered tag of any type is formatted as a single discrete primitive token (e.g., `[REQ-XXX]`, `[ARC-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[NFR-XXX]`, `[DOC-XXX]` or all tag IDs that their format patterns like this `[XXX-XXX]`), your engine MUST process and count it natively as exactly one (1) unique tracking tag toward its specific parent category matrix.
  2. Dynamic Range Sequential Condition (Applies to dynamic ranges): If an encountered tag is formatted as a sequential range token utilizing a 'to' keyword (formatted as `[TAG-Start to TAG-End]`, example: `[NFR-001 to NFR-009]`), your engine MUST dynamically extract the 'Start' integer and the 'End' integer, mathematically compute the absolute delta span count as `(End - Start + 1)`, and add this calculated total value to the validation ledger of that specific tag type.
  3. Dynamic Global Group Condition (Applies to global db pools): If an encountered tag is formatted as an all-inclusive database token utilizing an 'ALL' keyword (formatted as `[TAG-ALL (Start to End)]`, example: `[DAT-ALL (1 to 12)]`), your engine MUST programmatically parse the dynamic numeric boundaries inside the parentheses, compute the mathematical span as `(End - Start + 1)`, and expand it into the exact equivalent number of individual structural entities for that tag type ledger.
  4. Strict Matrix Substitution: You are CRITICALLY BANNED from leaving the raw template placeholder characters X, Y, Z, V, or W inside the final matrix row string. You MUST substitute each variable with the precise dynamic integer sum computed exclusively from this polymorphic live recount of all 5 types matching the active data logs under the designated anchor token.
- Your final emitted token row MUST strictly output the completed cross-validation matrix ledger on a single independent line formatted exactly as:
  `[TRACEABILITY MATRIX ENFORCEMENT: 100% COVERAGE VALIDATED. TOTAL UNIQUE REQ TAGS MAPPED: [Insert your live expanded REQ integer sum], TOTAL ARC TAGS: [Insert your live expanded ARC integer sum], TOTAL EXC TAGS: [Insert your live expanded EXC integer sum], TOTAL DAT TAGS: [Insert your live expanded DAT integer sum], TOTAL NFR TAGS: [Insert your live expanded NFR integer sum]. ZERO UNASSIGNED CODES FOUND.]`
- Failure to implement this comprehensive 5-type conditional parsing flow or outputting raw placeholder characters will trigger a critical validation exception and completely shut down the execution pipeline.
</RULE>

{% endif %}
{# ─── END:CHUNK:PART_3_FINAL ─── #}

{% if not force_full_export %}
<!--END_CHUNK_{{ target_segment }}-->
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
