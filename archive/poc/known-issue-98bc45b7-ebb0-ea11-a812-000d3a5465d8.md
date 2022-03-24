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
azs.issue-id: known-issue-98bc45b7-ebb0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### Delete a storage container

- Applicable to: all
- Description: In the user portal, when a user attempts to delete a storage container, the operation fails when the user does not toggle Override Azure Policy and RBAC Role settings .
- Remediation: Ensure that the box is checked for Override Azure Policy and RBAC Role settings .
- Occurrence: Common