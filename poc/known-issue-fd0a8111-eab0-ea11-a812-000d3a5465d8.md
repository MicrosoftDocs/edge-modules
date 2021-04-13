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
azs.issue-id: known-issue-fd0a8111-eab0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### Issues creating resources

- Applicable to: 1906
- Description: There is a known issue in 1906 with custom roles and permission allocation for resource creation. You might face issues creating resources even if you have the correct permissions.
- Remediation: Please update to build 1907 to mitigate this issue.
- Occurrence: Common