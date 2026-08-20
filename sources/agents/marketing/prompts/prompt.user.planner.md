{% set target_language = language if language and language.strip() != "" else "English" %}
# 📥 SYSTEM DATA INPUT CHANNEL
- **Target Project Identity**: "{{ project_name }}"
- **Document Control Tracking ID**: "MKT-{{ doc_id }}"
- **System Generation Timestamp**: "{{ current_timestamp }}"
- **Raw Core Requirements Data Stack**:
```text
{{ raw_idea_content }}
```
- **Business Analyst (BA) Specification Layer**:
```text
{{ raw_srs_content }}
```
- **System Architect (SA) Infrastructure Blueprint**:
```text
{{ raw_blueprint_content }}
```

# ⚡ EXECUTION INSTRUCTION
Analyze the input data matrix using your corporate strategy framework. Synthesize the requirements, business needs, and architecture patterns into a highly authoritative, presentation-ready enterprise asset.

You MUST completely fulfill the mandatory dual-zone layout specified in the system prompt rules:
1. Construct **ZONE 1: THE C-SUITE GOVERNANCE REPORT** by fully expanding the 9-Section layout with maximum structural and granular data density inside all markdown tables and bullet structures so it remains board-room compliant. Apply the escape URL rails if generating external resources context within the content cells.
2. Construct **ZONE 2: THE RESPONDER KNOWLEDGE PAYLOAD** immediately after Zone 1, keeping it strictly in pristine Technical English with dense, bulleted technical system facts optimized for downstream engagement automation.

🚨 **RIGID MOUNTING DIRECTIVE**: You MUST precisely inject the hidden HTML comment delimiters (`<!--START_GOVERNANCE_REPORT-->`, `<!--END_GOVERNANCE_REPORT-->`, `<!--START_RESPONDER_PAYLOAD-->`, and `<!--END_RESPONDER_PAYLOAD-->`) exactly on their own individual lines enclosing their respective data zones. Do not merge, shuffle, or output any conversational text or prefaces outside these boundaries.

Output the complete multi-zone professional document into the response layer now.

# DYNAMIC INTERNATIONALIZATION & TRANSLATION ENGINE
- Target Output Language Context: "{{ target_language }}"

- **Zone 1 (Markdown) High-Priority Translation Mandate**:
  You MUST dynamically translate 100% of all user-facing content inside the `<!--START_GOVERNANCE_REPORT-->` zone into "{{ target_language }}". This explicitly includes:
  1. All section headers (lines starting with #, ##, ###).
  2. All text within table cells and table column headers (e.g., translate "Item Parameter / Metric" and "Enterprise Governance Details").
  3. All bold markdown text indicators and inline labels used as list headers (e.g., you MUST translate "**Core Business Vision**" and "**The Core Value Hook**" into their exact textual equivalents in "{{ target_language }}").
  
- **Zone 2 (JSON) High-Priority Translation Mandate**:
  Within the `<!--START_RESPONDER_PAYLOAD-->` zone, you MUST dynamically translate 100% of the literal string values (JSON Values) into "{{ target_language }}". 

- **Structural Integrity Restrictions (Do Not Translate)**:
  You are strictly ordered to preserve only the raw mechanical symbols and keys. NEVER translate or modify:
  1. Structural markdown operators (`|`, `---`, `-`, `*`).
  2. Exact JSON Keys (e.g., keep "core_architecture_topology", "database_and_caching_capabilities" exactly in English).
  3. Jinja2 runtime variables (`{{ project_name }}`) or Technical tracking Tag IDs (`[REQ-XXX]`).
  4. Localized double quotes inside JSON values MUST be escaped as `\"`.
