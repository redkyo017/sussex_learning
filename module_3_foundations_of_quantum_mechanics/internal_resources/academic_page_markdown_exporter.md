# Skill: Academic Page Markdown Exporter

## Goal
Extract and format the complete text, mathematical equations, figures, long descriptions, and structural elements of an academic web page or lecture module into a clean, fully formatted Markdown (.md) document.

---

## Content Extraction & Formatting Rules

### 1. Structural Completeness
- Extract **all** core content sequentially, from the Introduction through the main sections, Summary, and References.
- Do NOT skip or condense prose, introductory explanations, intermediate algebraic steps, or figure captions.
- Exclude web page navigation chrome (e.g., top menus, sidebars, breadcrumbs, "Back to top" links, and page navigation buttons like "Next/Previous").

### 2. Mathematics and Physics Equations (LaTeX)
- **Inline Math:** Enclose standard inline variables, parameters, and expressions in single dollar signs `$...$` (e.g., `$V(x)$`, `$\hat{a}^\dagger$`, `$\hbar\omega$`).
- **Display Equations:** Enclose standalone equations, derivations, multi-line matrices, and commutators in double dollar signs `$$...$$`.
- **Equation Labels/Numbers:** Preserve equation tags and numbers as written on the page using `\tag{X.Y}` inside display blocks where appropriate.
- **Operator Notation:** Ensure quantum mechanical hats (`\hat{x}`, `\hat{p}`, `\hat{H}`, `\hat{N}`, `\hat{a}`) and Dirac notation (`|\psi\rangle`, `\langle\psi|`) are rendered accurately.

### 3. Figures and Accessible Media Descriptions
- Preserve all figure captions and titles using blockquotes (`> **Figure X.Y:** ...`).
- Include any "Long description" or accessible image text directly beneath the figure caption in the same blockquote structure so no descriptive content is lost.

### 4. Tables & Lists
- Convert tabular data or operator listings into standard Markdown tables (`| Header 1 | Header 2 |`).
- Convert lists into proper bulleted (`-`) or numbered (`1.`) Markdown lists.

### 5. Links and References
- Retain external hyperlinked citations (e.g., lecture notes, Stanford Encyclopedia of Philosophy) using standard Markdown links `[Title](URL)`.
- Reconstruct the References section cleanly at the bottom of the file.

---

## Output Delivery Format
- Present the final complete content wrapped inside a single block code block (` ```markdown ... ``` `) so the user can easily copy and save it as a `.md` file, or save it directly to output if tool functions allow.