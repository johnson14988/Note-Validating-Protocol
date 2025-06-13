![](https://img.shields.io/badge/Note%20Validating%20Protocol-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Version](https://img.shields.io/badge/version-v1.0.0-blue)
![](https://img.shields.io/badge/status-WIP-red)

# Motive
NVP is aiming to:
- help collaborators share information more accurately using a mutually agreed-upon structure, and they can choose the content and amount to share with finer granularity, which can also help promote fairness.
- benefits information collectors: A clearly defined target structure can prevent feature creep, ensuring that collectors do not excessively gather information deemed useless.

# User's Guide
## Schemas
- [General Concept Schema](./JSON%20Schema/gnrl.concept.json)
- [General Theory Schema](./JSON%20Schema/gnrl.theory.json)
- [Math Formula Schema](./JSON%20Schema/math.formula.json)
- [Math Proposition Schema](./JSON%20Schema/math.proposition.json)
- [Math Proof Schema](./JSON%20Schema/math.proof.json)
- [(cs) Code Schema](./JSON%20Schema/cs.code.json)
- [(cs) Libary Function Schema](./JSON%20Schema/cs.libfunc.json)

## Validation using MongoDB schema
MongoDB schema uses a slightly different schema definition. And corresponding MongoDB schema of each standard JSON Schema can be found in [MongoDB Schema Folder](./JSON%20Schema/MongoDB%20Schema/)

# Developer’s Guide

## Tasks
1. Looking for new schemas
2. Enhance the existing schemas
3. Define input text grammar
4. Validate JSON objects and store them

## Suggested Style for Schemas
(Jump to [sample-schema.json](./JSON%20Schema/sample-schema.json) to see an example)  

1. Contain generic fields:  
   - id -> unique identifier of the instance such as its unique name or a certain index  
   - desc -> description of the instance itself  
   - tags -> an array containing all tags to the instance
2. Avoid schema-specific nomenclature
