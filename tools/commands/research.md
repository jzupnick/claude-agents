---
name: hardware-research
description: Research open source hardware, electronic components, and certifications. Use when designing hardware projects, sourcing components, or validating open source compliance. Leverages OSHWA and DigiKey MCP servers.
---

# Hardware Research

Research open source hardware projects and electronic components using OSHWA and DigiKey integrations.

## MCP Servers Used

- **oshwa**: Search certified open source hardware projects
- **digikey**: Search electronic components, pricing, and datasheets

## Process

### 1. Understand Requirements
- Hardware type/category needed
- Open source requirements (licenses, certifications)
- Component specifications (if sourcing parts)
- Budget and availability constraints

### 2. Research Open Source Hardware (OSHWA)
Use OSHWA MCP tools:
- `search_projects` - Find certified hardware by keyword, type, country
- `get_project` - Get detailed project info by OSHWA UID
- `search_by_company` - Find projects from specific organizations
- `list_hardware_types` - See available hardware categories
- `get_recent_certifications` - Discover latest certified projects

### 3. Source Components (DigiKey)
Use DigiKey MCP tools:
- `keyword_search` - Find components with filters/sorting
- `product_details` - Get detailed specifications
- `get_product_pricing` - Check volume pricing
- `search_product_substitutions` - Find alternatives
- `get_product_media` - Access datasheets

### 4. Validate & Report
- Verify open source compliance (license compatibility)
- Check component availability and lead times
- Compare pricing across quantities
- Document findings with links to sources

## Example Workflows

### Finding Open Source Reference Designs
```
1. search_projects(keyword="sensor", primary_type="Electronics")
2. get_project(oshwa_uid="US000XXX") for promising results
3. Review documentation URLs for design files
```

### Component Selection for BOM
```
1. keyword_search("STM32F4 LQFP64") for MCU options
2. get_product_pricing() for volume pricing
3. search_product_substitutions() for alternatives
4. get_product_media() for datasheets
```

### Validating Open Source Compliance
```
1. get_certification_options() to understand requirements
2. search_projects() to check if similar projects exist
3. Review hardware/software/documentation licenses
```

## Best Practices

- **Specificity**: Provide detailed specs to reduce API calls
- **License awareness**: Check hardware, software, AND documentation licenses
- **Availability**: Always verify stock levels before committing to components
- **Alternatives**: Always research 2-3 component alternatives
- **Documentation**: Link to official datasheets and design files

## Output Format

When reporting findings, include:
- Project/component name and identifier
- Licenses (hardware, software, documentation)
- Key specifications
- Links to documentation/datasheets
- Availability and pricing summary
- Recommendations with rationale
