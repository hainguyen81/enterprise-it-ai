{% set target_language = language if language and language.strip() != "" else "English" %}
# CONTEXT INHERITANCE PIPELINE
Project Name: {{ project_name }}
You are tasked to detail **PHASE {{ phase_idx }} OUT OF {{ num_phases }}**. You must align perfectly with the established Global Context, satisfy a subset of the Raw Requirements, and maintain strict continuity of physical files generated in previous phases to avoid collision or duplicate creation.

--- GLOBAL CONTEXT REFERENCE ---
{{ global_markdown_context }}

--- PREVIOUS EXECUTION STATE REFERENCE (DIAGNOSTIC PATHS) ---
{% if previous_phase_context and previous_phase_context|trim != "" %}
{{ previous_phase_context }}
{% else %}
# PRISTINE INITIAL STATE MANDATE: 
# This is PHASE 1 (The Absolute Baseline Generation Step). 
# There are ZERO preceding code assets, directory structures, or legacy dependencies in the workspace.
# You MUST initialize all module definitions, file paths, database schemas, and data boundaries from a pure zero-state architecture baseline. Do not assume or extrapolate any prior system deployment state.
{% endif %}

--- RAW REQUIREMENTS REFERENCE ---
{{ project_requirements }}
----------------------------------

# EXTRACTION RULES FOR DAY-BY-DAY EXECUTION LOGS:
1. **Strict Chronological Expansion Rail:** You MUST programmatically execute a literal text-scanning pass inside the `<PROJECT_BACKLOG_TASKS_DATA>` reference matrix row matching Phase {{ phase_idx }}. You MUST extract the exact calculated day range limits. If the cell dictates a timeline span from relative day 1 to K, your output stream MUST dynamically explode and explicitly generate separate, non-empty level-3 Markdown sub-headers for EVERY single day in that chronological sequence (progressively unrolling from `### [Translate "DAY"] 1:` up to exactly `### [Translate "DAY"] [K]:`) on fresh vertical rows. Truncating the timeline early or omitting planned day blocks is a fatal framework contract violation.
2. **Strict Verbatim Multi-Persona Matrix Law:** Your token engine MUST split the 4th column cell ("Architectural Component / Module Path") of Phase {{ phase_idx }} using `<br/>` as the strict delimiter. For EVERY single individual physical file path primitive discovered in that parsed array, you ARE CRITICALLY AND PERMANENTLY COMMANDED to generate a complete, non-truncating sub-task matrix block containing exactly four (4) separate sequential sub-task nodes on fresh vertical rows. You MUST forcefully distribute these nodes across exactly four distinct assigned persona categories in absolute sequential 1:1 order: Sub-task Z.1 strictly to [Coder], Sub-task Z.2 strictly to [Tester] applying the rigid semicolon-separated syntax layout, Sub-task Z.3 strictly to [Reviewer], and Sub-task Z.4 strictly to [Doc]. Skipping any persona or filtering out registered assets under the assumption of architectural redundancy triggers an immediate system integration crash.
3. **Strict Sub-Agent Persona Allocation:** Each Sub-Task belongs to exactly ONE unique Assigned Sub-Agent literal token: 'Coder' | 'Tester' | 'Reviewer' | 'Doc' | 'Docker' | 'GCP' | 'GKE'.
4. **WORKSPACE PATH BOUNDARY & DYNAMIC TOPOLOGY CONSTRAINTS:**
    - **Absolute Workspace Boundary Rule:** The true repository workspace root is permanently fixed at the project root `./`. All file paths generated MUST strictly begin with `./sources/`.
    - **Dynamic Directory Prefixing Compliance:** You MUST strictly match the file path prefixes to the active system topology mapped in the Global Context. Do NOT generate backend folders for frontend-only projects, and do NOT generate frontend folders for backend-only systems.
    - **[STRICT QA FILE-PAIR LAYOUT LAW]:** The two-element semicolon-separated syntax layout (`<production_source_file_path>;<corresponding_test_file_path>`) is STRICTLY AND EXCLUSIVELY reserved for regular, executable backend source object classes (specifically files ending with the `.java` filename extension mask under a unit testing context). You ARE CRITICALLY AND PERMANENTLY COMMANDED to apply the alternate syntax pattern `INTEGRATION_SCOPE;<test_suite_file_path>` for ALL of the following engineering asset classifications without exception:
      * Global or local module build descriptors and configuration manifests (`pom.xml`, `package.json`).
      * High-level architectural integrations and end-to-end framework validation workflows.
      * All frontend, mobile, or presentation-tier bundles and client-side source scripts (`.ts`, `.tsx`, `.js`).
    Forcing a configuration asset or an integration boundary into a 1:1 functional code-pair model triggers an immediate continuous integration compiler collapse.
    - **[CONDITION: JAVA_STACK_ONLY] Java Package Enforcement Rule:** If a file path targets a Java source or test component (.java) under the backend services layer, you MUST strictly verify and ensure that the folder architecture layout adheres directly to the corporate enterprise package path segment formatting exactly as: `/src/main/java/org/nlh4j/{{ project_name | lower | replace('-', '') | replace('_', '') }}/` (or `/src/test/java/org/nlh4j/{{ project_name | lower | replace('-', '') | replace('_', '') }}/` for automated testing frameworks) followed.
    - **DYNAMIC LEDGER SYMMETRIC LAW:** You ARE CRITICALLY BANNED from outputting mismatched table counts between the summary text and the actual unrolled DDL scripts. The numerical count of entities stated in any architectural summary sentence MUST mathematically and perfectly equal the absolute count of physical database tables successfully defined via Flyway/Liquibase migration paths within that specific phase.

---

Your output MUST follow this exact Markdown layout structure (translate all label tokens but preserve the hidden HTML anchor formatting exactly):

<RULE>
- **🚨 MASTER GOVERNANCE COMPLIANCE MANDATE**: Before generating your final output response, you MUST strictly re-read and enforce the global translation rules defined in the Master Rules section. Ensure 100% of descriptive texts are rendered in {{ target_language }} while completely freezing all technical paths, tags, and block codes.
- **VERBATIM STRUCTURAL ANCHOR PRESERVATION MANTRA:** When rendering the layout structure below, your token generator IS CRITICALLY, ABSOLUTELY, AND PERMANENTLY BANNED from stripping, modifying, translating, or omitting the hidden structural HTML comment delimiters (`<!--PHASE_NAME_START-->`, `<!--PHASE_NAME_END-->`, `<!--PHASE_DESC_START-->`, `<!--PHASE_DESC_END-->`, `<!--DAY_HEADER_START-->`, `<!--DAY_HEADER_END-->`, `<!--START_TAGS-->`, `<!--END_TAGS-->`). They MUST be textually and physically printed character-by-character into the final Markdown stream with 100% fidelity.
</RULE>

# 📶 [Translate "Phase"] {{ phase_idx }}: <!--PHASE_NAME_START-->[Dynamically extract and fully translate the human-readable descriptive title for Phase {{ phase_idx }} into {{ target_language }}]<!--PHASE_NAME_END-->

## 📊 [Translate "Document Control"]

| [Translate "Item"] | [Translate "Details"] |
| :--- | :--- |
| **[Translate "Blueprint ID"]** | ARCH-{{ doc_id }} |
| **[Translate "Project Name"]** | {{ project_name }} |
| **[Translate "Phase"]** | {{ phase_idx }} |
| **[Translate "Phase Name"]** | <!--PHASE_NAME_START-->[Dynamically extract and fully translate the descriptive title string for Phase {{ phase_idx }} into {{ target_language }}]<!--PHASE_NAME_END--> |
| **[Translate "Description"]** | <!--PHASE_DESC_START-->[Dynamically extract and fully translate the comprehensive summary description of the absolute operational scope of Phase {{ phase_idx }} into {{ target_language }}]<!--PHASE_DESC_END--> |
| **[You MUST translate the literal token "Version" into {{ target_language }}]** | 1.0 (Baseline) |
| **[You MUST translate the literal token "Date/Time" into {{ target_language }}]** | {{ current_timestamp }} |
| **[You MUST translate the literal token "Author" into {{ target_language }}]** | Enterprise System Architect (SA Agent) |
| **[You MUST translate the literal token "Approval" into {{ target_language }}]** | Pending Technical Governance Review |

## 1. Phase Operational Scope & Objectives
[Provide a rigorous, detailed architectural summary of what this specific phase must implement based on the distributed requirements allocated for Phase {{ phase_idx }}]

## 2. Allowed Technical Scope & Directory Boundaries (Files, paths, and endpoints)
[List the absolute directory matrices and REST/GraphQL/Event endpoint routing patterns allowed for this phase, matching the detected language and active project stack topology. Every directory matrix path must be bounded under `./sources/`]
* **MANDATORY PLATFORM SKELETON MANIFEST INVARIANTS**:
  - When initializing the operational lifecycle blueprint (specifically bounded inside Phase 1 - DAY 1), you MUST explicitly inject and declare the primary repository infrastructure build descriptors before emitting any application source components.
  - For Microservices backend topologies, you MUST enforce the mandatory path definition of a parent project descriptor `./sources/backend/pom.xml` and isolated sub-module manifests `./sources/backend/<service-name>/pom.xml`.
  - For Frontend interface layer active applications, you MUST enforce the explicit configuration path registration of `./sources/frontend/package.json` and `./sources/frontend/tsconfig.json`. All generated scaffolding assets must map strictly to the architectural system tracking token `[ARC-000]`.

## 3. Dedicated Sub-Agent Functional Directives
[Delineate the explicit operational constraints and duties for each assigned agent persona in this phase, enforcing strict segregation of technical boundaries as defined below. Human-readable directives, descriptions, and task requirements MUST be contextually translated entirely into {{ target_language }} following the transmission rails]:
* **Coder**: Acts as a Senior/Principal Application Developer. Responsible for pure application source code implementation across both backend services and frontend/mobile client applications. Banned from writing test suites or infrastructure manifests.
* **Tester**: Acts as a Lead/Principal QC/QA. Specialized in test suite engineering, validation, and quality gates. Responsible for generating JUnit, integration tests, E2E automation tests, and performance validation scripts. Banned from modifying application production code. If the sub-task target involves an overall integration or end-to-end scope where no single specific code file can be bounded, you MUST strictly output the literal token `INTEGRATION_SCOPE` as the first parameter of the semicolon pair (e.g., `INTEGRATION_SCOPE;./sources/backend/tests/integration/WorkflowTest.java`).
* **Doc**: Functions as a Principal Technical Writer and Enterprise Systems Architect. Specialized in compiling comprehensive Technical Specification documents, schema references, system blueprints, and enterprise architecture catalogs custom-fitted to the active project topology layers. Every single technical document file generated MUST be listed as an explicit file path entity ending with the `.md` extension and reside strictly within the centralized storage layout: `./sources/docs/`.
<RULE>
You MUST strictly execute the CRITICAL SYSTEM PIPELINE RAIL paradigm with zero token leakage to the visible layout stream:
1. You are ABSOLUTELY AND PERMANENTLY BANNED from omitting, dropping, or filtering out the 'Doc' agent persona from any active daily logs stream.
2. For 100% of all executed phase context generations, on exactly "DAY 1" of that phase timeline, you MUST explicitly allocate a foundational system documentation task row assigned entirely to the 'Doc' agent persona.
3. The technical instruction for this Doc item MUST require the agent to initialize, architect, and map out the complete framework markdown documentation files, architectural database schemas, data dictionaries, or cloud deployment topology specifications matching the active architecture stack of the phase context.
Printing this internal routing engine `RULE` wrapper (example: `<RULE> ...</RULE>`) or its inner instruction sentences to the final markdown output constitutes a fatal system compliance breach.
</RULE>
*   **Reviewer**: Responsible for compiler verification, static analysis gating, and defensive patching. Specialized in code quality audits, resolving compilation bugs, fixing OWASP security vulnerabilities, and addressing SonarQube quality gate blockers.
*   **Docker**: Specialized strictly in containerization, multi-stage Dockerfile engineering, package optimization, and pushing verified application image assets to DockerHub.
*   **GCP**: Specialized in cloud automation within Google Cloud Platform. Responsible for building and pushing images to Google Cloud Artifact Registry (GCR), and orchestrating container environments natively on Google Cloud Run.
*   **GKE**: Specialized in production container orchestration inside Google Kubernetes Engine. Responsible for building Kubernetes deployment manifests, routing controls, HPA configurations, Helm charts, and deploying microservices workloads into active GKE clusters.

## 4. Phase Definition of Done (DoD)
[Specify the objective quantitative milestones required to pass this phase successfully, ensuring 100% compliance with OWASP enterprise standards, complete functional test coverage for the allocated requirements, and 100% Tag ID mapping check]

## 5. DAY-BY-DAY ARCHITECTURAL EXECUTION LOGS

# REMINDER: Enforce the 'Longitructural Day Partitioning Guardrail' and 'Anti-Padding Mandate'. Output each active day as an isolated standalone single integer subsection header from DAY 1 up to the dynamic freeze day. Do NOT generate empty padded days.

### 🌤️ [Translate "DAY"] [X]:
<!--DAY_HEADER_START-->[Dynamically extract and translate the capitalized high-density engineering objective title statement for this active calendar day loop into {{ target_language }}]<!--DAY_HEADER_END-->

#### 📝 [TRANSLATED SUB-TASK] [X.Y]: [Clear, low-level engineering description of the specific sub-task goal, explicitly embedding OWASP compliance rules and comprehensive technical implementation details]
##### [Translate "Assigned Sub-Agent"]: [Insert exactly ONE unique literal Agent token: Coder | Tester | Reviewer | Doc | Docker | GCP | GKE]
##### [Translate "Targeted Components & Technical Requirements"]:
* **[Translate "Target Path"]:** [Insert the explicit, decentralized physical file path target. For Coder/Tester/Reviewer agents, you MUST expand generic directory boundaries into precise enterprise layered structures, forcing valid file-level dot extensions like `.java`, `.ts`, `.sql`, etc. If it is a Java application layer, you MUST enforce the strict corporate Maven package layout structure mapping exactly as: `./sources/backend/<module_name>/src/main/java/org/nlh4j/{{ project_name | lower | replace('-', '') | replace('_', '') }}/<layer_package>/<FileName>.java`. For Tester integration scopes without a single source file, output exactly: `INTEGRATION_SCOPE;<relative_test_file_path>`.]

* **Traceability Tag Tokens:**
<!--START_TAGS-->[Enforce absolute granular tag-mapping criteria. You are CRITICALLY BANNED from copy-pasting an entire macro-range or a consolidated multi-tag block (such as replicating the complete array "[ARC-001] to [ARC-009]" repeatedly) across different independent sub-task nodes. You MUST dynamically parse the active day micro-workload and strictly extract and assign ONLY the single, specific, non-overlapping component Tag ID directly under development or verification within this active sub-task node. Output the exact tracking codes inline on this same line with zero structural duplication.]<!--END_TAGS-->

* **Low-Level Technical Task Instruction:** [You MUST dynamically analyze the specific engineering task assigned to the active sub-agent persona for this active day. You MUST write out a comprehensive, high-density, highly actionable technical execution instruction paragraph completely in {{ target_language }} directly below this bullet name before initializing any codeblock fences. This text block MUST explicitly detail the validation logic, parameters filtering criteria, framework components dependencies, or architectural requirements. You are ABSOLUTELY FORBIDDEN from leaving this instructional field blank, omitting the text body, or skipping directly to the three-backtick code primitive markers. Failure to supply unique real-world technical steps will crash the compilation engine.]

# DYNAMIC ARCHITECTURAL CONTENT GATING (CONTEXT-DRIVEN PROTOCOL):
* **Database Schema DDL SQL Specification [DAT-XXX]:**
<RULE>
You MUST programmatically analyze the operational scope of the active day loop. If the active day context involves database architecture, schema migrations, table creation, or DDL SQL execution, you MUST explicitly output this field and inject the raw code primitives inside a clean markdown codeblock wrapped strictly inside a cohesive html comment tag enclosure: you MUST print the opening string literal token `<!--START_DDL_MIGRATION-->` immediately before opening the three-backtick code fence, and you MUST print the exact matching closing string literal token `<!--END_DDL_MIGRATION-->` immediately after closing the three-backtick code fence. You are CRITICALLY BANNED from dropping, skipping, or omitting the opening `START` tag placeholder. All database code blocks MUST remain frozen in Technical English character-by-character. - If and ONLY IF the active day contains absolute zero database modifications, completely purge and erase this entire line and its anchors from the stream buffer with zero token delay.</RULE>
- If and ONLY IF the active day contains absolute zero database modifications, you MUST still output the explicit section title and preserve the paired comment anchors `<!--START_DDL_MIGRATION-->` and `<!--END_DDL_MIGRATION-->` wrapped around a clean markdown code block enclosing the literal technical comment exactly: `-- NO_PERSISTENCE_TIER_CHANGES_REQUIRED` to maintain perfect placeholder compliance without triggering attention blocks.
</RULE>

* **API and Event Routing Contracts [DAT-XXX], [ARC-XXX]:**
<RULE>
You MUST programmatically analyze the operational scope of the active day loop. If the active day context involves network requests, endpoint integration, REST APIs, or HTTP request/response payloads, you MUST explicitly output this field and inject the production-ready schemas inside a clean markdown codeblock wrapped strictly inside a cohesive html comment tag enclosure: you MUST print the opening string literal token `<!--START_API_CONTRACT-->` immediately before opening the three-backtick code fence, and you MUST print the exact matching closing string literal token `<!--END_API_CONTRACT-->` immediately after closing the three-backtick code fence. You are CRITICALLY BANNED from dropping, skipping, or omitting the opening `START` tag placeholder. All payload entities MUST remain frozen in Technical English. If and ONLY IF the active day contains absolute zero API endpoints or web service contracts, you MUST completely purge and erase this entire line and its anchors from the stream buffer with zero token delay.</RULE>
- If and ONLY IF the active day contains absolute zero API endpoints or web service contracts, you MUST still output the explicit section title and preserve the paired comment anchors `<!--START_API_CONTRACT-->` and `<!--END_API_CONTRACT-->` wrapped around a clean markdown code block enclosing the literal technical comment exactly: `# NO_EXTERNAL_API_OR_EVENT_CONTRACTS_REQUIRED` to prevent validation halts.
</RULE>

* **Phase Localized Exception Handlers [EXC-XXX]:**
<RULE>
You MUST programmatically analyze the operational scope of the active day loop. If the active day context involves global exception interceptors, system validation errors, data redundancy catch blocks, or HTTP error status codes, you MUST explicitly output this field and inject the explicit interceptor configuration schemas inside a clean markdown codeblock wrapped strictly inside a cohesive html comment tag enclosure: you MUST print the opening string literal token `<!--START_EXC_HANDLER-->` immediately before opening the three-backtick code fence, and you MUST print the exact matching closing string literal token `<!--END_EXC_HANDLER-->` immediately after closing the three-backtick code fence. You are CRITICALLY BANNED from dropping, skipping, or omitting the opening `START` tag placeholder. All exception classes MUST remain frozen in Technical English. If and ONLY IF the active day contains absolute zero exception logic mapping, completely purge and erase this entire line and its anchors from the stream buffer with zero token delay.</RULE>
- If and ONLY IF the active day contains absolute zero exception logic mapping, you MUST still output the explicit section title and preserve the paired comment anchors `<!--START_EXC_HANDLER-->` and `<!--END_EXC_HANDLER-->` wrapped around a clean markdown code block enclosing the literal technical comment exactly: `// NO_LOCALIZED_EXCEPTION_HANDLERS_REQUIRED` to preserve architectural conformity.
</RULE>
