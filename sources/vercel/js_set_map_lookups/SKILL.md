---
description: Imported skill js_set_map_lookups from vercel
name: js_set_map_lookups
signature: a7fd781a6ba9ad49065961b6f9a90ef486bf6b648390e1a08704025f98e1642b
source: /a0/tmp/skills_research/vercel/skills/react-best-practices/rules/js-set-map-lookups.md
---

---
title: Use Set/Map for O(1) Lookups
impact: LOW-MEDIUM
impactDescription: O(n) to O(1)
tags: javascript, set, map, data-structures, performance
---

## Use Set/Map for O(1) Lookups

Convert arrays to Set/Map for repeated membership checks.

**Incorrect (O(n) per check):**

```typescript
const allowedIds = ['a', 'b', 'c', ...]
items.filter(item => allowedIds.includes(item.id))
```

**Correct (O(1) per check):**

```typescript
const allowedIds = new Set(['a', 'b', 'c', ...])
items.filter(item => allowedIds.has(item.id))
```
