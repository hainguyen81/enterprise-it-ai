{% set target_language = language if language and language.strip() != "" else "English" %}
# TASK

Generate exactly `{{ quantity }}` project concepts according to the active Idea Agent System Instruction and the Global Master Rules.

## RUNTIME INPUTS

- **Domain:** {% if domain and domain|trim != "" %}{{ domain }}{% else %}Auto-Select{% endif %}
- **Quantity:** {{ quantity }}
- **Language:** {{ target_language }}

## IDEAS HISTORY

{% if ideas_history %}
{% for idea in ideas_history %}
- {{ idea }}
{% endfor %}
{% else %}
- None
{% endif %}

## OUTPUT STRUCTURE

For each project concept, output the following structure exactly:

#### [IDEA_X] [Clear, technical, plain-text project concept name]

- **[Localized equivalent of "Domain"]:** [Output ONLY the resolved business domain value. Do NOT repeat, prepend, or append the field label to the value.]

- **[Localized equivalent of "Technical Codename"]:** <!--TECHNICAL_CODENAME_START-->[Output ONLY one concise machine-friendly CamelCase identifier derived from the project concept. The identifier MUST contain ASCII letters and digits only, with no spaces, accents, punctuation, symbols, hyphens, underscores, Markdown styling, explanatory text, or repeated field label.]<!--TECHNICAL_CODENAME_END-->

- **[Localized equivalent of "Brand Name"]:** <!--BRAND_NAME_START-->[Output ONLY the professional commercial brand name aligned with the project concept. Do NOT repeat, prepend, or append the field label to the value.]<!--BRAND_NAME_END-->

- **[Localized equivalent of "Problem Statement"]:** [Output ONLY a precise 1–2 sentence description of the target problem. Do NOT repeat, prepend, or append the field label to the value.]

- **[Localized equivalent of "Solution & Workflow"]:** [Output ONLY a concise description of the proposed solution and its operational workflow. Do NOT repeat, prepend, or append the field label to the value.]

- **[Localized equivalent of "Target Audience"]:** [Output ONLY the primary user or stakeholder groups. Do NOT repeat, prepend, or append the field label to the value.]

- **[Localized equivalent of "Unique Selling Proposition (USP)"]:** [Output ONLY a concise and differentiated value proposition explaining why the proposed solution is meaningfully valuable. Do NOT repeat, prepend, or append the field label to the value.]

##### [Localized equivalent of the Lean & Rapid Execution Requirements Contracts heading]

* **[REQ-001]** [Atomic MVP functional requirement]
* **[REQ-002]** [Additional necessary MVP functional requirement]
* **[DAT-001]** [Necessary MVP data or persistence requirement]
* **[EXC-001]** [Necessary MVP exception, validation, or failure-handling behavior]

## OUTPUT RULES

- Generate exactly `{{ quantity }}` project concepts.
- Number project concepts sequentially beginning with `[IDEA_1]`.
- Use only requirement identifiers that correspond to actual requirements of the proposed MVP.
- Use sequential numbering within each requirement identifier type.
- Do NOT create filler requirements merely to reach a numeric quota.
- Keep requirements at the MVP capability level and do NOT introduce physical source files, directory structures, or implementation-specific file boundaries.
- Begin the response directly with the first `#### [IDEA_1]` heading.
- Do NOT include conversational filler, introductions, conclusions, explanations, or post-generation remarks.