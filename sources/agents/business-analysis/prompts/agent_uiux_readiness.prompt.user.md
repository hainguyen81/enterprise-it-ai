{% set target_language = language if language and language.strip() != "" else "English" %}

# TASK

Analyze the authoritative BA Software Requirements Specification and produce the UI/UX Readiness Audit and Wireframe Blueprint according to the active UI/UX Audit System Instruction and Global Governance Rules.

# RUNTIME INPUTS

- Target Language:
  {{ target_language }}

- Document ID:
  {{ doc_id }}

- Project Codename:
  {{ project_name }}

# AUTHORITATIVE BA SRS

The following block is the single authoritative project source for this execution.

---------------- SRS START ----------------

{{ raw_srs_content }}

----------------- SRS END -----------------

# OUTPUT OBJECTIVE

Transform the authoritative SRS into the required UI/UX Readiness Audit and Wireframe Blueprint.

The output MUST:

- remain grounded in the authoritative SRS;
- preserve source Tag IDs exactly;
- maintain traceability between SRS requirements and UI/UX structures;
- identify applicable screens, sections, components, interactions, states, validation behavior, responsive behavior, accessibility considerations, and design-token requirements;
- identify unresolved UI/UX readiness gaps without inventing unsupported requirements;
- localize all human-readable content, headings, labels, table headers, and descriptions according to the target language;
- preserve protected machine-readable identifiers and technical artifacts exactly;
- use the canonical cross-agent Document Control structure defined by the Global Governance Rules when Document Control is required;
- follow the exact output structure required by the active UI/UX Audit System Instruction.

# OUTPUT

Begin directly with the required UI/UX Blueprint.

Do NOT emit conversational introductions, explanations, conclusions, generation-process commentary, or content outside the declared UI/UX Blueprint structure.
