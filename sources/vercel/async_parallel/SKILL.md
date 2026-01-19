---
description: Imported skill async_parallel from vercel
name: async_parallel
signature: 6d2f841896279e976dfcdc1ac89e70771ac188baadfd43c096b5706cb838b961
source: /a0/tmp/skills_research/vercel/skills/react-best-practices/rules/async-parallel.md
---

---
title: Promise.all() for Independent Operations
impact: CRITICAL
impactDescription: 2-10× improvement
tags: async, parallelization, promises, waterfalls
---

## Promise.all() for Independent Operations

When async operations have no interdependencies, execute them concurrently using `Promise.all()`.

**Incorrect (sequential execution, 3 round trips):**

```typescript
const user = await fetchUser()
const posts = await fetchPosts()
const comments = await fetchComments()
```

**Correct (parallel execution, 1 round trip):**

```typescript
const [user, posts, comments] = await Promise.all([
  fetchUser(),
  fetchPosts(),
  fetchComments()
])
```
