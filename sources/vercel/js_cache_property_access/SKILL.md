---
description: Imported skill js_cache_property_access from vercel
name: js_cache_property_access
signature: 73e47431e74878a927061bf0ddc7cd91a7556cb35d2573f3421e82300d9ae311
source: /a0/tmp/skills_research/vercel/skills/react-best-practices/rules/js-cache-property-access.md
---

---
title: Cache Property Access in Loops
impact: LOW-MEDIUM
impactDescription: reduces lookups
tags: javascript, loops, optimization, caching
---

## Cache Property Access in Loops

Cache object property lookups in hot paths.

**Incorrect (3 lookups × N iterations):**

```typescript
for (let i = 0; i < arr.length; i++) {
  process(obj.config.settings.value)
}
```

**Correct (1 lookup total):**

```typescript
const value = obj.config.settings.value
const len = arr.length
for (let i = 0; i < len; i++) {
  process(value)
}
```
