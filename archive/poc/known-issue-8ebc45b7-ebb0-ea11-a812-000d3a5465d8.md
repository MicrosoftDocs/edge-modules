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
azs.issue-id: known-issue-8ebc45b7-ebb0-ea11-a812-000d3a5465d8
azs.status: active
azs.topic-schema: known-issue
azs.audience: Operator
azs.highlight: False
---
### Access Control (IAM)

- Applicable to: all
- Description: The IAM extension is out of date. The Ibiza portal that shipped with Azure Stack Hub introduces a new behavior that causes the RBAC extension to fail if the user is opening the Access Control (IAM) blade for a subscription that is not selected in the global subscription selector ( Directory + Subscription in the user portal). The blade displays Loading in a loop, and the user cannot add new roles to the subscription. The Add blade also displays Loading in a loop.
- Remediation: Ensure that the subscription is checked in the Directory + Subscription menu. The menu can be accessed from the top of the portal, near the Notifications button, or via the shortcut on the All resources blade that displays Don't see a subscription? Open Directory + Subscription settings . The subscription must be selected in this menu
- Occurrence: NA