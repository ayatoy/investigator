---
name: investigator
description: Investigate a given topic deeply in the current repository and produce a detailed research report saved at $PWD/docs/notes/yyyy-MM-dd_*.md. Use when the user asks for a deep dive, technical investigation, comparative analysis, root-cause research, or background study and expects a persisted markdown note.
---

# Topic Investigation Reporter

Create a detailed markdown research report for a user-provided topic and save it to `$PWD/docs/notes/`.

## Inputs

- Topic text: can be a single word, phrase, or long sentence.
- Optional constraints: scope, audience, deadline, required format, language.

## Output Contract

- Save exactly one main report file under:
  - `$PWD/docs/notes/yyyy-MM-dd_*.md`
- Use today's local date for `yyyy-MM-dd` unless the user requests another date.
- Keep report content evidence-based and traceable.

## Standard Workflow

1. Determine scope from the topic text.
2. Investigate local repository evidence first.
3. Add external evidence when local data is insufficient or when recency matters.
4. Synthesize findings into a structured report.
5. Save the report file to `$PWD/docs/notes/` and cite all sources.

## Guardrail

- Do not jump into implementation or edit source code after the investigation is complete.

## File Creation and Management

Create the destination path and template with: `$HOME/.codex/skills/investigator/references/TEMPLATE.md` and save the filled report to `$PWD/docs/notes/yyyy-MM-dd_*.md`. Always use the `yyyy-MM-dd_` prefix for filenames. Do not include local paths or environment-specific information in the report; use placeholders like `$PWD` instead. 
This prints the final path and creates a draft markdown file if it does not exist.

## Local Investigation Checklist

- Search broadly with `rg` for topic terms and synonyms.
- Read relevant code, tests, configs, docs, issues, and notes.
- Capture concrete evidence:
  - file paths
  - key behaviors
  - assumptions and gaps

## External Investigation Checklist

- Use web research for unstable or time-sensitive facts.
- Prefer primary sources.
- Record source URLs in the report.
- Distinguish facts from inferences.

## Report Structure

Use this structure in the saved note:

1. Title
2. TL;DR
3. Topic and scope
4. Method (where and how you investigated)
5. Findings (with evidence)
6. Impact / implications
7. Open questions and risks
8. Recommended next actions
9. Sources

## Quality Bar

- Be specific; avoid generic summaries.
- Tie each major claim to explicit evidence.
- Include unknowns explicitly instead of guessing.
- Keep prose concise but complete enough for decision-making.
