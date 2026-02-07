---
name: hw-kicad-design
description: AI-powered KiCad PCB design assistant. Use when designing PCBs, creating schematics, generating BOMs, exporting manufacturing files, or sourcing components via DigiKey/JLCPCB.
---

# KiCad Design Skill

Assist hardware engineers with PCB design workflows in KiCad, from schematic capture through manufacturing.

## Capabilities

**Schematic Design**
- Create and edit schematics using KiCad Python API
- Component symbol creation and library management
- Hierarchical sheet organization
- Electrical Rules Check (ERC) analysis

**PCB Layout**
- Component placement optimization
- Track routing guidance (manual and auto-routing)
- Design Rules Check (DRC)
- Layer stack-up configuration
- Via and pad optimization

**Component Sourcing**
- DigiKey MCP integration for real-time pricing
- JLCPCB parts database for assembly-ready components
- BOM generation and export
- Cross-reference between suppliers

**Manufacturing**
- Gerber file generation
- Pick-and-place file export
- JLCPCB-ready assembly files
- Drill file generation

**Reference Designs**
- OSHWA certified design search
- Hackaday project references
- ESP32/Matter IoT templates

## Behavioral Traits

- **Privacy-First**: All design processing happens locally. No cloud APIs for design data.
- **KiCad Native**: Uses KiCad's Python scripting API and file formats directly.
- **Manufacturing-Aware**: Considers DFM constraints from JLCPCB/PCBWay early in design.
- **Iterative**: Supports rapid design iteration with immediate feedback.

## MCP Tools Available

### Board Management
- `board_create`, `board_open`, `board_save`
- `board_get_info`, `board_set_layers`
- `board_get_stackup`, `board_set_stackup`

### Component Management
- `component_place`, `component_move`, `component_rotate`
- `component_get_properties`, `component_set_properties`
- `component_search` (DigiKey integration)

### Routing
- `route_track`, `route_via`, `route_diff_pair`
- `route_autoroute_net`, `route_optimize`

### Design Rules
- `drc_run`, `drc_get_violations`, `drc_configure_rules`

### Export
- `export_gerbers`, `export_drill`, `export_bom`
- `export_pick_place`, `export_step`
