---
author: mattbriggs
ms.service: azure-stack
ms.topic: include
ms.date: 2020-08-14
ms.author: mabrigg
ms.reviewer: avishwan
ms.lastreviewed: 2020-08-14
ms.sub-service: Patch and Update
azs.tracking: 123456
azs.issue-id: known-issue-a9bc45b7-ebb0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### Update fails

- Applicable to: all
- Description: When attempting to install the Azure Stack Hub update, the status for the update might fail and change state to PreparationFailed . This is caused by the update resource provider (URP) being unable to properly transfer the files from the storage container to an internal infrastructure share for processing.
- Remediation: Starting with version 1901 (1.1901.0.95), you can work around this issue by clicking Update now again (not Resume ). The URP then cleans up the files from the previous attempt, and restarts the download. If the problem persists, we recommend manually uploading the update package by following the Install updates section .
- Occurrence: Common