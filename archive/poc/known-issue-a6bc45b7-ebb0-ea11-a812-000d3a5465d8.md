---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-08-14
ms.author: mabrigg
ms.reviewer: avishwan
ms.lastreviewed: 2020-08-14
ms.sub-service: SQL and MySQL
azs.tracking: 123456
azs.issue-id: known-issue-a6bc45b7-ebb0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### SQL/MySQL

- Applicable to: 2002
- Description: If the stamp contains SQL resource provider (RP) version 1.1.33.0 or earlier, upon update of the stamp, the blades for SQL/MySQL will not load.
- Remediation: Update the RP to version 1.1.47.0
- Occurrence: NA