{% set target_device = device if device and device.strip() != "" else "Web_Desktop" %}
{% set target_language = language if language and language.strip() != "" else "English" %}

# TASK

Compile the authoritative BA Software Requirements Specification and UI/UX Readiness Audit Blueprint into the JSON object required by the active UI/UX Compiler System Instruction and Global Master Rules.

# RUNTIME INPUTS

- **Target Device:**
  {{ target_device }}

- **Target Language:**
  {{ target_language }}

# AUTHORITATIVE BA SRS

The following block contains the complete authoritative BA Software Requirements Specification for this execution.

<SRS_MARKDOWN_BOUND>
--- SRS REQUIREMENTS START ---
{{ raw_srs_content }}
--- SRS REQUIREMENTS END ---
</SRS_MARKDOWN_BOUND>

# AUTHORITATIVE UI/UX READINESS AUDIT

The following block contains the complete authoritative UI/UX Readiness Audit Blueprint produced from the BA SRS for this execution.

<UI_UX_READINESS_AUDIT>
--- UI/UX READINESS AUDIT START ---
{{ raw_uiux_audit_content }}
--- UI/UX READINESS AUDIT END ---
</UI_UX_READINESS_AUDIT>

# COMPILATION OBJECTIVE

Compile both authoritative upstream artifacts into the JSON structure defined by the active `uiux_json_schema`.

The compilation MUST:

- preserve source-defined meaning;
- preserve source Tag IDs exactly;
- preserve applicable traceability relationships;
- preserve source-defined technical identifiers;
- compile applicable UI/UX structures represented by the upstream artifacts;
- maintain consistency with the BA SRS;
- respect the target device when applicable to source-defined UI/UX behavior;
- follow the target-language rules defined by the Global Master Rules;
- follow the exact active JSON schema contract.

Use the BA SRS as the authority for business and technical meaning.

Use the UI/UX Readiness Audit Blueprint as the authority for its documented UI/UX representation.

Do NOT invent missing source information.

# OUTPUT

Return exactly one JSON object conforming to the active `uiux_json_schema`.

The response MUST be the JSON object itself.

Start directly with `{`.

End directly with `}`.

Output nothing else.