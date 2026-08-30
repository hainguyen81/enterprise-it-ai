{% set target_language = language if language and language.strip() != "" else "English" %}
# CONTEXT
I have a raw, high-level product idea that needs to be engineered into a rigorous, Enterprise-grade Software Requirements Specification (SRS) document.

# INPUTS
- **Project Codename (Optional)**: {{ project_name }} (Note: This can be blank or omitted. If blank, apply the strict generation rule defined in the system prompt).
- **Raw Idea & Requirements**: 
---------
{{ raw_idea_content }}
---------
- **Target Language**: {{ target_language }}

# ROLE AND OBJECTIVE
Act as an Elite Principal Business Analyst and Enterprise Software Architect. Your sole mission is to decompose 100% of the raw text into an airtight, end-to-end spec document organized strictly by logical Functional Modules/Epics. You must map out all implicit technical gaps, business logic holes, infrastructure needs, and data structural linkages required to implement the features flawlessly.

# BOUNDARIES & ANTI-LAZINESS DIRECTIVES (ZERO LOOPHOLES)
1. **NO HALLUCINATION & ZERO WASTE**: Do NOT invent features, screens, or integrations outside the scope of the raw text. Do NOT include fluff, filler, or essays. Focus purely on technical and business specification details.
2. **100% EXHAUSTIVE COVERAGE (NO SUMMARIZATION)**: You must process every single sentence, role, permission, screen, and technology framework provided in the input. You are STRICTLY FORBIDDEN from combining, compressing, or summarizing requirements. Every requested screen or feature must have its own dedicated subsection.
3. **GRANULAR INLINE SPECIFICATION**: For EACH logical module/screen, you MUST inline its specific functional behaviors [REQ-XXX], its validation rules/exception flows [EXC-XXX], and its localized database schema [DAT-XXX].
4. **COMPACT TECHNICAL TELEGRAPHY**: Use concise, high-density technical engineering language. Eliminate passive voice and decorative adjectives to maximize output capacity and prevent token truncation.

# SYSTEMATIC TRACEABILITY MATRIX (TAG ID RULES)
Every single line item, functional requirement, acceptance rule, exception handler, architectural trigger, and database column description MUST be strictly prefixed with a unique, incremental Tag ID. No token of information is allowed to exist without an identifier.

# SYSTEMATIC TRACEABILITY MATRIX (TAG ID RULES)
Every single line item, functional requirement, acceptance rule, exception handler, architectural trigger, and database column description MUST be strictly prefixed with a unique, incremental Tag ID. No token of information is allowed to exist without an identifier.

CRITICAL ID GENERATION & AUTO-TAGGING LAW: 
1. TAG PRESERVATION & INHERITANCE: If a feature, requirement, exception, or data table in the raw input ALREADY has an explicit Tag ID (e.g., [REQ-001], [DAT-001] from the input text), you MUST preserve and use that EXACT Tag ID natively. You are STRICTLY FORBIDDEN from altering, re-indexing, or replacing existing IDs.
2. STRICT ID UNIQUENESS & AUTO-GENERATION: For any elements or implicitly deduced technical specifications (such as new validation flows or table definitions) that LACK an explicit ID in the raw input, you MUST dynamically auto-generate a new incremental Tag ID. 
3. ANTI-COLLISION CONSTRAINT: Every auto-generated Tag ID MUST be completely unique and MUST NOT collide or overlap with any pre-existing Tag IDs found in the raw input document.
4. You are STRICTLY REQUIRED to systematically deduce and generate the necessary [EXC-XXX] (Exception Flows) and [DAT-XXX] (Database Schemas) to support every identified [REQ-XXX]. If the parent requirement already has an ID, nest the new deduced technical sub-elements under it using unique, non-colliding IDs.
5. A single requirement, rule, trigger, or data field without its tracking Tag ID is a fatal structural failure. Tag IDs must cover the entire generated document comprehensively from top to bottom.

You must use this exact taxonomy from top to bottom:
- `[REQ-XXX]`: Functional Requirements, User Stories, Screen Interactions, and Feature Behaviors.
- `[EXC-XXX]`: Business Rule Validations, Edge Cases, Error Codes, and Exception Flows.
- `[DAT-XXX]`: Database Tables, Column Definitions, Keys (PK/FK), Constraints, and Data Mappings.
  * Every compiled database schema under `[DAT-XXX]` MUST include an embedded Technical English Mermaid.js `erDiagram` block visualization mapping keys (PK/FK) and explicit relational attributes clearly underneath the localized definitions text.
- `[ARC-XXX]`: Architectural Constraints, Tech Stack Specs, Infrastructure, and Integration Triggers.
- `[NFR-XXX]`: Non-Functional Metrics (Security, Scalability, Performance, Multi-tenancy Isolation, Localization).

CRITICAL POLICY: A single requirement, rule, trigger, or data field without its tracking Tag ID is a fatal structural failure. Tag IDs must cover the entire document comprehensively.

# ZERO-THINKING OUTPUT CONFIGURATION
- Do NOT output any introductory text, concluding notes, explanations, or conversational filler.
- Do NOT include <think> tags or intermediate reasoning tokens.
- Your entire response MUST start directly on Line 1 with the primary Markdown header text: `# SOFTWARE REQUIREMENTS SPECIFICATION: [Apply POLYMORPHIC_SLUG_EXTRACTION_ENGINE here]`, after evaluting raw value, then translating it fully 100% into the requested target language "{{ target_language }}". You are strictly forbidden from leaving this header title with a blank trailing parameter or a mismatched codename variation.
- Exhaustively detail and tag every single logical component from top to bottom.
- Conclude the entire stream response directly with the mandatory raw delimiter token `[EXECUTION_REMEDIATION_PAYLOAD_START]` followed immediately on the next line by the flat valid JSON metadata block containing the collected "requirement_tags" array without any markdown code block backticks wrapping around the JSON payload.
