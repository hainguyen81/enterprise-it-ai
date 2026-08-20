{% set video_type = video_format_type if video_format_type and video_format_type.strip() != "" else "Shorts" %}
# 📥 SYSTEM DATA INPUT CHANNEL
- **Target Project Identity Name**: "{{ project_name }}"
- **Document Control Tracking ID**: "VIDEO-{{ doc_id }}"
- **System Generation Timestamp**: "{{ current_timestamp }}"
- **Target Video Format Layout Type**: "{{ video_type }}" (Shorts / Reels / Long-form)
- **Specific Campaign Target Interval**: "{{ target_interval }}"

# APPROVED MARKETING PLANNED REFERENCE
```markdown
{{ raw_planner_content }}
```

# APPROVED MARKETING DATA ASSET REFERENCE
[CONTEXT STORAGE ONLY - DO NOT ADOPT THIS LAYOUT]
```markdown
{{ raw_asset_content }}
```

# EXECUTIVE TERMINATION CONSTRAINT (ANTI-DUPLICATION)
- **Strict Stop Rule**: You MUST generate the content for "## 🎥 1. VISUAL STORYBOARD & VOICEOVER PLAYBOOK" exactly ONCE. Do NOT re-write, duplicate, or output multiple versions of the article copy under any circumstances. 
- Once the Call-to-Action (CTA) of the article copy is written, you MUST immediately close Section 1, move directly to "## 2. CONTEXTUAL HASHTAGS MATRIX", and then transition straight into the JSON payload inside Zone 2.

# ⚡ EXECUTION INSTRUCTION
Locate the specific target interval row inside the Editorial Calendar of the Approved Marketing Planner Source Reference. Extract the campaign focus and topic specifications.

You MUST fully expand both **ZONE 1: THE C-SUITE GOVERNANCE REPORT** (Markdown presentation playbook) and **ZONE 2: THE RESPONDER KNOWLEDGE PAYLOAD** (JSON schema production pipeline) in a single execution stream. Maintain absolute structural detail. Ensure the number of scenes dynamically satisfies the constraints of the requested format architecture: "{{ video_format_type }}".

🚨 **RIGID MOUNTING DIRECTIVE**: You MUST precisely inject the hidden HTML comment delimiters (`<!--START_GOVERNANCE_REPORT-->`, `<!--END_GOVERNANCE_REPORT-->`, `<!--START_RESPONDER_PAYLOAD-->`, and `<!--END_RESPONDER_PAYLOAD-->`) exactly on their own individual lines enclosing their respective data zones. Do not merge or output any conversational text outside these boundaries.

Output the complete multi-zone video production document now.
