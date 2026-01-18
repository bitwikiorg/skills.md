---
description: Imported skill marketplace from anthropic
name: marketplace
signature: 1a6cc07d44200e3688fa3c7c45a2e053f8fd9f0ba186180b681ce14644efc6fe
source: /a0/tmp/skills_research/anthropic/.claude-plugin/marketplace.json
---

{
  "name": "anthropic-agent-skills",
  "owner": {
    "name": "Keith Lazuka",
    "email": "klazuka@anthropic.com"
  },
  "metadata": {
    "description": "Anthropic example skills",
    "version": "1.0.0"
  },
  "plugins": [
    {
      "name": "document-skills",
      "description": "Collection of document processing suite including Excel, Word, PowerPoint, and PDF capabilities",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/xlsx",
        "./skills/docx",
        "./skills/pptx",
        "./skills/pdf"
      ]
    },
    {
      "name": "example-skills",
      "description": "Collection of example skills demonstrating various capabilities including skill creation, MCP building, visual design, algorithmic art, internal communications, web testing, artifact building, Slack GIFs, and theme styling",
      "source": "./",
      "strict": false,
      "skills": [
        "./skills/algorithmic-art",
        "./skills/brand-guidelines",
        "./skills/canvas-design",
        "./skills/doc-coauthoring",
        "./skills/frontend-design",
        "./skills/internal-comms",
        "./skills/mcp-builder",
        "./skills/skill-creator",
        "./skills/slack-gif-creator",
        "./skills/theme-factory",
        "./skills/web-artifacts-builder",
        "./skills/webapp-testing"
      ]
    }
  ]
}
