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
azs.issue-id: known-issue-97bc45b7-ebb0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### Incorrect tooltip when creating VM

- Applicable to: all
- Description: In the user portal, when you select a managed disk, with disk type Premium SSD, the drop-down list shows OS Disk . The tooltip next to that option says Certain OS Disk sizes may be available for free with Azure Free Account ; however, this is not valid for Azure Stack Hub. In addition, the list includes Free account eligible which is also not valid for Azure Stack Hub. 
- Remediation: NA
- Occurrence: Common