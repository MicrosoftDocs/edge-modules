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
azs.issue-id: known-issue-8cbc45b7-ebb0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### Create Managed Disk snapshot

- Applicable to: 2002
- Description: In the user portal, when creating a Managed Disk snapshot, the Account type box is empty. When you select the Create button with an empty account type, the snapshot creation fails.
- Remediation: Select an account type from the Account type dropdown list, then create the snapshot.
- Occurrence: Common