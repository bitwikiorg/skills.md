---
description: Imported skill client_localstorage_schema from vercel
name: client_localstorage_schema
signature: 0fb7cdf9dc93fdf22f87e3669f953fb9d4ac9b0be42eec4a29fe9a2560610b88
source: /a0/tmp/skills_research/vercel/skills/react-best-practices/rules/client-localstorage-schema.md
---

---
title: Version and Minimize localStorage Data
impact: MEDIUM
impactDescription: prevents schema conflicts, reduces storage size
tags: client, localStorage, storage, versioning, data-minimization
---

## Version and Minimize localStorage Data

Add version prefix to keys and store only needed fields. Prevents schema conflicts and accidental storage of sensitive data.

**Incorrect:**

```typescript
// No version, stores everything, no error handling
localStorage.setItem('userConfig', JSON.stringify(fullUserObject))
const data = localStorage.getItem('userConfig')
```

**Correct:**

```typescript
const VERSION = 'v2'

function saveConfig(config: { theme: string; language: string }) {
  try {
    localStorage.setItem(`userConfig:${VERSION}`, JSON.stringify(config))
  } catch {
    // Throws in incognito/private browsing, quota exceeded, or disabled
  }
}

function loadConfig() {
  try {
    const data = localStorage.getItem(`userConfig:${VERSION}`)
    return data ? JSON.parse(data) : null
  } catch {
    return null
  }
}

// Migration from v1 to v2
function migrate() {
  try {
    const v1 = localStorage.getItem('userConfig:v1')
    if (v1) {
      const old = JSON.parse(v1)
      saveConfig({ theme: old.darkMode ? 'dark' : 'light', language: old.lang })
      localStorage.removeItem('userConfig:v1')
    }
  } catch {}
}
```

**Store minimal fields from server responses:**

```typescript
// User object has 20+ fields, only store what UI needs
function cachePrefs(user: FullUser) {
  try {
    localStorage.setItem('prefs:v1', JSON.stringify({
      theme: user.preferences.theme,
      notifications: user.preferences.notifications
    }))
  } catch {}
}
```

**Always wrap in try-catch:** `getItem()` and `setItem()` throw in incognito/private browsing (Safari, Firefox), when quota exceeded, or when disabled.

**Benefits:** Schema evolution via versioning, reduced storage size, prevents storing tokens/PII/internal flags.
