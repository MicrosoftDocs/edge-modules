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
azs.issue-id: known-issue-ee0a8111-eab0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### VM boot diagnostics

- Applicable to: all
- Description: When creating a new Windows virtual machine (VM), the following error may be displayed: Failed to start virtual machine 'vm-name'. Error: Failed to update serial output settings for VM 'vm-name' . The error occurs if you enable boot diagnostics on a VM, but delete your boot diagnostics storage account.
- Remediation: Recreate the storage account with the same name you used previously.
- Occurrence: Common