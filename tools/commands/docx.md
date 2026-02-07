---
name: docx
description: Create, edit, and analyze Word documents (.docx files). Supports tracked changes, comments, formatting, and text extraction.
---

# DOCX Processing

## Capabilities

- **Reading**: Convert to markdown with pandoc, or access raw XML
- **Creating**: Use docx-js library (JavaScript/TypeScript)
- **Editing**: Use Python Document library for OOXML manipulation
- **Redlining**: Implement tracked changes systematically

## Quick Reference

### Reading
```bash
pandoc document.docx -o document.md
```

### Creating (docx-js)
```javascript
const doc = new Document({
  sections: [{
    properties: {},
    children: [
      new Paragraph({ children: [new TextRun("Hello")] })
    ]
  }]
});
```

### Editing Workflow
1. Unpack OOXML
2. Modify XML files
3. Validate changes
4. Repack

## Redlining Best Practices

- Convert to markdown first
- Plan edits in batches of 3-10 changes
- Apply precisely to XML
- **Only mark text that actually changes**
- Preserve unchanged text structure

## Dependencies

- pandoc
- docx npm package
- LibreOffice
- Poppler utilities
- defusedxml (Python)

## Important

When creating or editing, read the full documentation files completely - no range limits.
