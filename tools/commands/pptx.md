---
name: pptx
description: Create, edit, and analyze PowerPoint presentations (.pptx). Supports layouts, templates, charts, and OOXML manipulation.
---

# PPTX Processing

## Capabilities

- **Reading**: Convert to markdown, or unpack for raw XML
- **Creating**: Build from scratch or use templates
- **Editing**: Unpack OOXML, modify, validate, repack

## Creating Without Templates

1. State design approach first
2. Select web-safe fonts
3. Choose appropriate color palette
4. Convert HTML slides to PowerPoint (html2pptx)

## Using Templates

1. Extract template content
2. Analyze layouts with thumbnail grids
3. Select appropriate slide designs
4. Duplicate slides via rearrange script
5. Extract text inventory
6. Generate replacement content
7. Apply updates with replace script

## Editing Existing

Follow OOXML workflow:
1. Unpack
2. Edit XML
3. Validate
4. Repack

## Best Practices

- Analyze content before choosing design
- Use two-column layouts for charts/tables
- Validate immediately after edits
- Create thumbnail grids for visual analysis
- Match layout structures to content precisely

## Dependencies

- markitdown
- pptxgenjs
- playwright
- sharp
- LibreOffice
- Poppler
- defusedxml
