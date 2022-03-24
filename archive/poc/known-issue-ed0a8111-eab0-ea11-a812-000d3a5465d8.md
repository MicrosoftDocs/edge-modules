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
azs.issue-id: known-issue-ed0a8111-eab0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### Virtual machine scale set: Create failures during patch and update on 4-node Azure Stack Hub environments

- Applicable to: all
- Description: Creating VMs in an availability set of 3 fault domains and creating a virtual machine scale set instance fails with a FabricVmPlacementErrorUnsupportedFaultDomainSize error during the update process on a 4-node Azure Stack Hub environment.
- Remediation: You can create single VMs in an availability set with 2 fault domains successfully. However, scale set instance creation is still not available during the update process on a 4-node Azure Stack Hub deployment
- Occurrence: NA