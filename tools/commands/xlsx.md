---
name: xlsx
description: Create, edit, and analyze Excel spreadsheets (.xlsx, .xlsm, .csv, .tsv). Supports formulas, formatting, and data analysis.
---

# XLSX Processing

## Key Requirements

- **ZERO formula errors** (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)
- **Match existing format** when modifying files

## Tools

- **pandas** - Data analysis, bulk operations
- **openpyxl** - Formulas, formatting, cell-level control

## Critical Rule

**Always use Excel formulas instead of calculating in Python and hardcoding.**

```python
# WRONG - hardcoded value
cell.value = 100 + 50

# RIGHT - Excel formula
cell.value = "=A1+B1"
```

This ensures spreadsheets remain dynamic when source data changes.

## Financial Model Standards

### Color Coding
- Blue text: User-changeable inputs
- Black: Formulas and calculations
- Green: Internal worksheet links
- Red: External file references
- Yellow background: Assumptions needing attention

### Number Formatting
- Years: Text format
- Currency: `$#,##0`
- Zeros: Display as `-`
- Percentages: `0.0%`

## Workflow

```python
import openpyxl
wb = openpyxl.load_workbook('file.xlsx')
ws = wb.active
ws['A1'] = "=SUM(B1:B10)"
wb.save('output.xlsx')
```

## Validation

Always recalculate formula-based files and verify zero errors before completion.
