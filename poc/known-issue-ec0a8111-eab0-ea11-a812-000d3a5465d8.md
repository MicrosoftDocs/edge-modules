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
azs.issue-id: known-issue-ec0a8111-eab0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### Privileged Endpoint

- Applicable to: 1910
- Description: Unable to connect to the Privileged Endpoint (ERC VMs) from a computer running a non-English version of Windows.
- Remediation: This is a known issue that has been fixed in releases later than 1910. As a workaround you can run the New-PSSession and Enter-PSSession PowerShell cmdlets using the en-US culture; for examples, set the culture using this script: https://resources.oreilly.com/examples/9780596528492/blob/master/Use-Culture.ps1.
- Occurrence: Rare