{% set target_device = device if device and device.strip() != "" else "Web_Desktop" %}
**Target Device:** {{ target_device }}

**BA SRS Markdown Content:**
<SRS_MARKDOWN_BOUND>
--- SRS REQUIREMENTS ---
{{ raw_srs_content }}
--- END SRS REQUIREMENTS ---
</SRS_MARKDOWN_BOUND>

**UI/UX Readiness Audit BluePrint Markdown Content:**
<UI_UX_READINESS_AUDIT>
--- UI/UX READINESS AUDIT ---
{{ raw_uiux_audit_content }}
--- END UI/UX READINESS AUDIT ---
</UI_UX_READINESS_AUDIT>
