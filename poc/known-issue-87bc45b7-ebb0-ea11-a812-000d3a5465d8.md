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
azs.issue-id: known-issue-87bc45b7-ebb0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### Administrative subscriptions

- Applicable to: all
- Description: The two administrative subscriptions that were introduced with version 1804 should not be used. The subscription types are Metering subscription, and Consumption subscription.
- Remediation: If you have resources running on these two subscriptions, recreate them in user subscriptions.
- Occurrence: Common