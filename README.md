![](https://img.shields.io/badge/Note%20Validating%20Protocol-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-v1.0.0-blue)
![](https://img.shields.io/badge/status-WIP-red)

# User's Guide
# Developer’s Guide
## Tasks
Looking for new schemas  
Enhance the existing schemas
Define input text grammar
Validate JSON objects and store them
## Suggested Style for Schemas
1. Contain generic fields:  
   - id -> unique identifier of the instance such as its unique name or a certain index  
   - class -> classification of the instance described by the schema  
   - desc -> description of the instance itself  
   - tags -> an array containing all tags to the instance
2. Avoid schema-specific nomenclature
