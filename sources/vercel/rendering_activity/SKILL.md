---
description: Imported skill rendering_activity from vercel
name: rendering_activity
signature: 1e5e7eaf3555e61d6a2e900089c676527d26259501db5594f59544b6c664f85a
source: /a0/tmp/skills_research/vercel/skills/react-best-practices/rules/rendering-activity.md
---

---
title: Use Activity Component for Show/Hide
impact: MEDIUM
impactDescription: preserves state/DOM
tags: rendering, activity, visibility, state-preservation
---

## Use Activity Component for Show/Hide

Use React's `<Activity>` to preserve state/DOM for expensive components that frequently toggle visibility.

**Usage:**

```tsx
import { Activity } from 'react'

function Dropdown({ isOpen }: Props) {
  return (
    <Activity mode={isOpen ? 'visible' : 'hidden'}>
      <ExpensiveMenu />
    </Activity>
  )
}
```

Avoids expensive re-renders and state loss.
