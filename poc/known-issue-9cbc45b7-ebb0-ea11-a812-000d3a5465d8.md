---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-08-14
ms.author: mabrigg
ms.reviewer: kivenkat
ms.lastreviewed: 2020-08-14
ms.sub-service: Virtual Machines
azs.tracking: 123456
azs.issue-id: known-issue-9cbc45b7-ebb0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### Capacity monitoring in SQL resource provider keeps loading

- Applicable to: 1910
- Description: The current version of the SQL resource provider is not compatible with some of the latest portal changes in the 1910 update.
- Remediation: Follow the resource provider update process to apply the SQL resource provider hotfix 1.1.47.0 after Azure Stack Hub is upgraded to the 1910 update ( SQL RP version 1.1.47.0 ). For the MySQL resource provider, it is also recommended that you apply the MySQL resource provider hotfix 1.1.47.0 after Azure Stack Hub is upgraded to 1910 update ( MySQL RP version 1.1.47.0 ).
- Occurrence: Common