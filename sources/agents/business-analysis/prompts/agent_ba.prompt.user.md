{% set target_language = language if language and language.strip() != "" else "English" %}

# CONTEXT

Transform the authoritative project source into an implementation-ready Software Requirements Specification (SRS).

# RUNTIME INPUTS

- **Project Codename (Optional):**
  {{ project_name }}

  If a valid technical codename is supplied, preserve its technical meaning.
  If absent or insufficient, derive a concise English technical codename from the authoritative source block according to the active BA System Instruction.

- **Target Language:**
  {{ target_language }}

## SOURCE PROJECT IDEA & REQUIREMENTS

The following block is the single authoritative project source for this execution.

---------------- SOURCE START ----------------

{{ raw_idea_content }}

----------------- SOURCE END -----------------

# TASK OBJECTIVE

Transform the authoritative `SOURCE PROJECT IDEA & REQUIREMENTS` block into an implementation-ready SRS organized by logical Functional Modules/Epics.

The generated SRS MUST:

- preserve all explicit source requirements and their semantic meaning;
- identify logically necessary derived requirements without introducing speculative functionality;
- decompose business capabilities into clear, testable functional requirements;
- identify applicable business rules, validations, exceptions, data relationships, architectural constraints, integrations, and non-functional requirements;
- preserve source traceability;
- distinguish source-derived requirements from BA-derived specifications;
- produce the terminal metadata payload required by the active BA System Instruction.

# SOURCE ANALYSIS & DERIVATION

- Treat `SOURCE PROJECT IDEA & REQUIREMENTS` as the authoritative source for this execution.
- Process the complete source block before finalizing the SRS.
- Do not replace, silently rewrite, or reinterpret explicit source requirements.
- Do not rely on cached, previously generated, unrelated, or inferred project content when the required information exists in the source block.
- Preserve explicit source Tag IDs exactly.
- A derived requirement MAY be created only when it is logically necessary to implement an explicitly defined source capability.
- Every derived requirement MUST remain traceable to the source capability that necessitated it.
- Do NOT introduce speculative features, integrations, roles, screens, reports, workflows, business policies, technology choices, infrastructure, or data entities without sufficient source support or logical implementation necessity.
- Enterprise controls such as authentication, authorization, tenant isolation, auditability, secure data handling, session management, and API boundaries MUST NOT be represented as source-derived unless explicitly supported by the source.
- When an enterprise control is inferred, classify it according to the active BA System Instruction.

# SOURCE COVERAGE

Every explicit source capability, requirement, role, workflow, validation, exception, data requirement, architectural constraint, technology reference, protected technical identifier, and source Tag ID MUST be handled.

Each source element MUST be:

- represented directly in the SRS;
- decomposed into traceable child specifications; or
- explicitly classified according to the applicable uncertainty or coverage rules.

Do NOT silently omit, erase, overwrite, or replace source content.

Multiple source statements MAY be consolidated when semantic meaning and traceability are preserved.

Source Tag IDs are traceability references and MUST NOT automatically define module boundaries.

# TAG ID HANDLING

- Treat the project's Tag ID taxonomy as extensible rather than closed.
- Preserve every explicitly declared source Tag ID exactly, regardless of prefix or taxonomy.
- Do NOT alter, rename, translate, normalize, re-index, replace, or delete source Tag IDs.
- Additional source-defined Tag ID families MUST remain preserved according to their source-defined semantics or the applicable Active Task System Instruction.
- Do NOT assume that `[REQ-XXX]`, `[EXC-XXX]`, `[DAT-XXX]`, `[ARC-XXX]`, or `[NFR-XXX]` are an exhaustive whitelist.
- If an explicit source Tag ID has an unknown semantic category, preserve it exactly and do not silently convert it into another taxonomy.
- Generate a new Tag ID only when a new traceable specification requires one and no applicable source Tag ID exists.
- Generated Tag IDs MUST use an applicable existing taxonomy whenever one is defined.
- Generated Tag IDs MUST NOT collide with any source Tag ID.
- The final traceability ledger and terminal metadata MUST account for applicable source-defined Tag IDs from all taxonomies.

# ACCEPTANCE CRITERIA

For each applicable `[REQ-XXX]` functional requirement:

- Provide testable acceptance criteria.
- Maintain direct traceability to the parent requirement.
- Cover applicable user interaction, workflow, validation, state transition, success, failure, API, persistence, authorization, and integration behavior.
- Follow the localization and technical-token preservation rules defined by the active BA System Instruction and Global Governance Rules.
- Do NOT invent acceptance criteria that imply unsupported functionality.

# DATABASE & MERMAID OUTPUT

When persistence requirements are applicable, follow the database and Mermaid governance defined by the active BA System Instruction.

The required database output sequence is:

1. Tier 1 preliminary data dictionary.
2. Tier 1 global system-wide `erDiagram`.
3. Tier 2 Entity A property matrix.
4. Tier 2 Entity A isolated `erDiagram`.
5. Tier 2 Entity B property matrix.
6. Tier 2 Entity B isolated `erDiagram`.
7. Continue the same pattern for every remaining unique database entity.

For every unique database entity identified in Tier 1:

- provide its complete applicable property matrix;
- provide its mandatory isolated entity-level `erDiagram`;
- include the active entity;
- include all directly connected neighboring entities required to represent its defined relationships;
- maintain consistency with the Tier 1 global ERD and property matrix;
- do NOT omit the isolated ERD merely because the global ERD already represents the relationship;
- do NOT invent entities, fields, keys, or relationships solely for diagram completeness.

Mermaid syntax, entity names, field names, database types, key tokens, relationship operators, and other protected technical artifacts MUST follow the active BA System Instruction and Global Governance Rules.

# SRS DOCUMENT STRUCTURE

Generate the SRS using the following logical structure unless the authoritative source clearly requires another structure.

## DOCUMENT CONTROL

When Document Control is applicable:

- emit a visible Markdown section heading immediately before the Document Control table;
- localize human-readable heading, labels, descriptions, and statuses according to `{{ target_language }}`;
- preserve protected machine-readable values exactly;
- keep the heading and table as one continuous structural unit.

Use this structural baseline:

| Item | Details |
| :--- | :--- |
| SRS ID | SRS-{{ doc_id }} |
| Project Name | [Resolved canonical project technical codename] |
| Version | 1.0 ([Localized baseline status]) |
| Date Time | {{ current_timestamp }} |
| Author | Principal Business Analyst (BA) / Product Strategist (BA Agent) |
| Approval | [Localized governance-review status] |

Do NOT emit instructional placeholders literally.

## 1. PROJECT OVERVIEW & GLOBAL ARCHITECTURE

Include applicable:

- Product Objectives & Core Values.
- Target User Personas.
- Business Context.
- System Scope.
- Global Role-Based Access Control (RBAC) Matrix.
- Global Architectural Constraints.
- Technology Context.
- Infrastructure Requirements.
- Integration Requirements.

Use only source-supported or logically necessary content.

## 2. ENHANCED EPIC MODULES

Organize the project into logical Functional Modules/Epics.

For each applicable module include:

### Core Functional Requirements

- Distinct functional capabilities using applicable `[REQ-XXX]` identifiers.
- Concise feature descriptions.
- Clear User Stories.
- Direct traceability to source requirements.

### Acceptance Criteria & Interactions

- Fine-grained acceptance criteria.
- Applicable UI, workflow, validation, state, API, persistence, authorization, and integration behavior.
- Direct traceability to the parent requirement.

### Module Exception Flows

- Applicable `[EXC-XXX]` exception flows.
- Validation failures.
- Invalid states.
- Business rule violations.
- Boundary conditions.
- Integration failures.
- Applicable fallback behavior.

Do NOT create speculative exceptions.

### Module Data Specification

- Applicable database entities.
- Fields.
- Relationships.
- Constraints.
- Data mappings.
- Required Tier 1 and Tier 2 database artifacts.

## 3. GLOBAL NON-FUNCTIONAL REQUIREMENTS

Include applicable `[NFR-XXX]` requirements for areas such as:

- Performance.
- Security.
- Privacy.
- Access Control.
- Data Protection.
- Scalability.
- Availability.
- Resilience.
- Multi-Tenant Isolation.
- Observability.
- Maintainability.
- Reliability.
- Localization.

Only include requirements supported by the source or logically necessary for the defined system capabilities.

Do NOT invent arbitrary numeric targets, certifications, security standards, vendors, infrastructure technologies, or policies.

# TRACEABILITY COVERAGE LEDGER

Before finalizing the SRS, provide a traceability coverage ledger for every explicit source Tag ID.

Use:

| Source Tag ID | Generated Section or Module | Generated Traceability Tag(s) | Coverage Status |
| :--- | :--- | :--- | :--- |
| [SOURCE-TAG] | [Generated section/module] | [Generated tag(s)] | [VERIFIED / FAILED] |

Rules:

- `[VERIFIED]` means the source element is represented or appropriately decomposed.
- `[FAILED]` means the source element has no valid representation or classification.
- Every explicit source Tag ID MUST be accounted for regardless of taxonomy.
- Do NOT use unstable generated line numbers as the primary traceability mechanism.
- Traceability MUST be semantic and structural.

# PROJECT IDENTITY

Resolve one canonical project technical codename.

- If `{{ project_name }}` contains a valid technical codename, preserve its technical meaning.
- If it contains a mixed technical and descriptive phrase, extract the core technical identity.
- If absent or insufficient, derive a concise English technical codename from the authoritative source block.
- The canonical technical codename MUST use lowercase, hyphen-separated ASCII words only.
- Do NOT append arbitrary suffixes such as `-system`, `-platform`, `-cms`, or `-app` unless required by the resolved identity.
- Use the same canonical technical codename in the Document Control project identity and terminal metadata.

# LOCALIZATION & TECHNICAL PRESERVATION

Generate all human-readable SRS content in `{{ target_language }}`.

Follow the Global Governance Rules and active BA System Instruction for:

- heading localization;
- table localization;
- User Story localization;
- acceptance-criteria localization;
- business descriptions;
- exception descriptions;
- validation descriptions;
- workflow descriptions;
- data descriptions;
- architectural explanations;
- traceability descriptions;
- uncertainty statements.

Preserve protected machine-readable content exactly, including:

- source Tag IDs;
- generated Tag IDs;
- technical identifiers;
- variable names;
- field names;
- enum values;
- status values;
- state identifiers;
- API paths;
- HTTP methods;
- file paths;
- JSON keys;
- schema keys;
- Mermaid syntax;
- Mermaid entity names;
- Mermaid field names;
- Mermaid types;
- Mermaid key tokens;
- Mermaid relationship operators;
- terminal delimiters;
- required HTML anchors;
- other explicitly protected machine-readable tokens.

Technical terminology MAY remain in canonical technical form when required for accuracy, but surrounding human-readable prose MUST follow `{{ target_language }}`.

# SOURCE BLOCK REFERENCE

- The `SOURCE PROJECT IDEA & REQUIREMENTS` block is the single authoritative source for this execution.
- References to "the source", "source content", "source requirements", "source Tag IDs", or "source material" refer to that block.
- Do NOT duplicate or re-inject the complete source block.
- Do NOT rely on cached, previously generated, unrelated, or inferred project content when source information is available.
- If information is genuinely absent, follow the uncertainty and missing-data rules of the active BA System Instruction.

# OUTPUT CONTRACT

The final response MUST contain exactly:

1. The generated SRS Markdown document.
2. One occurrence of:
   `[EXECUTION_REMEDIATION_PAYLOAD_START]`
3. One flat valid JSON metadata object immediately following the delimiter.

The terminal JSON MUST contain exactly:

{
  "technical_codename": "string",
  "descriptive_name": "string",
  "brand_name": "string",
  "requirement_tags": ["string"]
}

Rules:

- `"technical_codename"` MUST contain the canonical lowercase-hyphenated project technical codename.
- `"descriptive_name"` MUST contain the resolved descriptive or commercial project name.
- `"brand_name"` MUST contain the supplied project brand name when available.
- Do NOT invent a brand name merely to populate the field.
- If no brand name exists, use the missing-data representation permitted by the active BA System Instruction.
- `"requirement_tags"` MUST contain all applicable Tag IDs emitted throughout the SRS, including source-defined Tag IDs from taxonomies not explicitly listed in this prompt.
- Preserve Tag IDs exactly, including square brackets.
- Do NOT translate Tag IDs.
- Do NOT add additional JSON keys.
- Do NOT wrap the JSON object in Markdown code fences.
- Do NOT emit any text between the delimiter and the JSON object.
- Do NOT emit any character after the closing `}` of the terminal JSON object.

# FINAL EXECUTION CHECK

Before emission, verify only the following task-critical invariants:

- The complete authoritative source block has been processed.
- Every applicable source requirement is represented, decomposed, or classified.
- Every explicit source Tag ID is preserved regardless of taxonomy.
- Source-derived and BA-derived requirements remain distinguishable.
- No unsupported functionality has been introduced.
- Generated Tag IDs do not collide with source Tag IDs.
- Acceptance criteria remain traceable to their parent requirements.
- Database entities and fields remain consistent across their representations.
- Every unique database entity has a Tier 2 property matrix.
- Every unique database entity has its mandatory isolated entity-level `erDiagram`.
- Tier 1 and Tier 2 database artifacts remain mutually consistent.
- Mermaid artifacts comply with the active BA System Instruction.
- Human-readable content follows `{{ target_language }}`.
- Protected technical artifacts remain unchanged.
- The canonical technical codename is consistent across the SRS and terminal metadata.
- The terminal delimiter appears exactly once.
- The terminal JSON contains exactly the four declared keys.
- The terminal JSON is valid and flat.
- No characters appear after the closing `}` of the terminal JSON object.
