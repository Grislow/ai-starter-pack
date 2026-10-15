# ai-starter-pack

Starter pack for setting up popular AI tools to supercharge system / software / ui design, planning work, building, evaluating and research.

- [ai-starter-pack](#ai-starter-pack)
  - [Directories](#directories)
  - [Resources](#resources)
  - [System Design](#system-design)
  - [Software Design](#software-design)
  - [UI Design](#ui-design)
  - [Planning Work](#planning-work)
  - [Building software](#building-software)
  - [Maintenance](#maintenance)
  - [Understanding](#understanding)
  - [Testing](#testing)
  - [Security](#security)
  - [Research](#research)
  - [AI Evaluation / Optimization](#ai-evaluation--optimization)
  - [Conversation Modes](#conversation-modes)
  - [Agent Orchestrators](#agent-orchestrators)

## Directories

Catalogs and marketplaces to discover more plugins and skills.

| Name | Description |
| --- | --- |
| [awesome-claude-plugins](https://github.com/quemsah/awesome-claude-plugins) | Auto-crawled index of Claude Code plugins with adoption metrics. |
| [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Anthropic-curated Claude Code marketplace (`/plugin install x@claude-plugins-official`); also the reference plugin layout. |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's official Agent Skills (skill-creator, frontend-design, docx/pdf/xlsx/pptx); reference format for writing skills. |
| [openai/skills](https://github.com/openai/skills) | Official skills catalog for Codex. |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | `npx skills` CLI: installs skills from any repo into 70+ agents (Claude Code, Cursor, Codex, Copilot…). |
| [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Curated list of Claude skills, resources and tools. |
| [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Curated list of Claude Code resources: commands, hooks, workflows, tooling. |
| [wshobson/agents](https://github.com/wshobson/agents) | Multi-harness plugin marketplace of agents, skills and commands (Claude Code, Codex, Cursor, Copilot, OpenCode…). |
| [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 100+ specialized Claude Code subagents across dev use cases. |
| [claude-code-templates](https://github.com/davila7/claude-code-templates) | CLI to install agents, commands, hooks, MCPs into Claude Code and monitor usage. |

## Resources

| Name | Description | Categories |
| --- | --- | --- |
| [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Anthropic-curated Claude Code marketplace (`/plugin install x@claude-plugins-official`); also the reference plugin layout. | Skill Authoring |
| [superpowers](https://github.com/obra/superpowers) | Full dev methodology: brainstorm → spec → plan → subagent-driven implementation with TDD and review. Skills auto-trigger. | Workflow Framework, Planning Work, Building Software, Testing |
| [spec-kit](https://github.com/github/spec-kit) | GitHub's spec-driven development toolkit: constitution → spec → plan → tasks → implement. | Workflow Framework, Planning Work |
| [agent-skills](https://github.com/addyosmani/agent-skills) | 25 senior-engineer skills + lifecycle commands (`/spec /plan /build /test /review /ship /code-simplify /webperf`). | Workflow Framework, Planning Work, Building Software, Testing, Maintenance |
| [ECC](https://github.com/affaan-m/ECC) | Large "agent harness OS": agents, skills, hooks, rules, cross-session memory, security scanning, token optimization, for many harnesses. | Workflow Framework, Building Software, Testing, Memory / Context, AI Evaluation / Optimization |
| [skills](https://github.com/mattpocock/skills) | Small composable skills: grill-me, to-spec, to-tickets, tdd, diagnosing-bugs, codebase-design, domain-modeling, improve-codebase-architecture, code-review. | Software Design, Planning Work, Building Software, Testing, Maintenance |
| [wondelai/skills](https://github.com/wondelai/skills) | 65 skills condensing classic books into frameworks: system-design, DDIA, clean-architecture, release-it, DDD, refactoring, refactoring-ui, UX heuristics (+ business/marketing). Install per plugin, e.g. `systems-architecture@wondelai-skills`. | System Design, Software Design, UI Design, Maintenance |
| [ponytail](https://github.com/DietrichGebert/ponytail) | "Laziest senior dev" mode: YAGNI, stdlib first, minimal diffs; plus over-engineering review/audit. | Conversation Modes, Building Software, Maintenance |
| [caveman](https://github.com/JuliusBrussee/caveman) | Terse caveman-speak output mode (skill + proxy), cuts ~65% of output tokens. | Conversation Modes, AI Evaluation / Optimization |
| [i-have-adhd](https://github.com/ayghri/i-have-adhd) | Answer-first, ADHD-friendly output; stops the agent burying the point. | Conversation Modes |
| [no-ai-slop](https://github.com/petergyang/no-ai-slop) | Removes 20+ AI-slop patterns from any writing. | Writing |
| [stop-slop](https://github.com/hardikpandya/stop-slop) | Skill file for removing AI tells from prose. | Writing |
| [humanizer](https://github.com/blader/humanizer) | Rewrites text to remove signs of AI writing, based on Wikipedia's "Signs of AI writing" guide. | Writing |
| [Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Turns a codebase (or docs/wiki) into an interactive knowledge graph with architecture layers, domain flows, tours, onboarding, diff analysis. | Understanding, System Design |
| [graphify](https://github.com/Graphify-Labs/graphify) | Deterministic AST-based knowledge graph of code, docs, SQL, PDFs; queryable via skill/MCP, no vector store. | Understanding, Memory / Context |
| [claude-mem](https://github.com/thedotmack/claude-mem) | Captures session activity, compresses it, re-injects relevant context into future sessions. | Memory / Context |
| [headroom](https://github.com/headroomlabs-ai/headroom) | Compresses tool outputs, logs, files and RAG chunks before they hit the LLM (library, proxy, MCP). | AI Evaluation / Optimization, Memory / Context |
| [task-observer](https://github.com/rebelytics/one-skill-to-rule-them-all) | Meta-skill that watches sessions, captures corrections and patterns, and proposes skill improvements / new skills. | Skill Authoring, AI Evaluation / Optimization |
| [Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | Converts docs sites, GitHub repos and PDFs into Claude skills (also MCP server). | Skill Authoring, Research |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) | Gives agents design taste: art direction, reference images, browser check vs. generic AI pages. | UI Design |
| [impeccable](https://github.com/pbakaus/impeccable) | Design language skill: 24 commands (shape, critique, audit, polish, typeset…) + 59 deterministic frontend anti-pattern detectors. | UI Design, Testing |
| [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | UI/UX design intelligence (styles, palettes, fonts, stacks) for web and mobile. | UI Design |
| [last30days-skill](https://github.com/mvanhorn/last30days-skill) | Researches a topic across Reddit, X, YouTube, HN, Polymarket and web; grounded recent-trends summary. | Research |
| [OpenHands](https://github.com/OpenHands/OpenHands) | Open-source autonomous AI dev platform (CLI, GUI, cloud). | Agent Orchestrators |
| [gastown](https://github.com/gastownhall/gastown) | Multi-agent workspace manager: coordinator "Mayor", worker agents, git-backed persistent work state across Claude Code/Codex/Copilot. | Agent Orchestrators |
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic's official Agent Skills (skill-creator, frontend-design, docx/pdf/xlsx/pptx); reference format for writing skills. | Skill Authoring, UI Design |
| [openai/skills](https://github.com/openai/skills) | Official skills catalog for Codex. | Skill Authoring |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | `npx skills` CLI: installs skills from any repo into 70+ agents (Claude Code, Cursor, Codex, Copilot…). | Skill Authoring |
| [wshobson/agents](https://github.com/wshobson/agents) | Multi-harness plugin marketplace of agents, skills and commands (Claude Code, Codex, Cursor, Copilot, OpenCode…). | Building Software |
| [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 100+ specialized Claude Code subagents across dev use cases. | Building Software |
| [claude-code-templates](https://github.com/davila7/claude-code-templates) | CLI to install agents, commands, hooks, MCPs into Claude Code and monitor usage. | AI Evaluation / Optimization |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) | Lightweight spec-driven development: propose → apply → archive change specs. | Workflow Framework, Planning Work |
| [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | Agile AI-driven development with role agents (analyst, PM, architect, dev, QA). | Workflow Framework, Planning Work, System Design |
| [claude-task-master](https://github.com/eyaltoledano/claude-task-master) | Parses a PRD into dependency-aware tasks and tracks them via MCP/CLI. | Planning Work |
| [SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) | Claude Code config framework: specialized commands, cognitive personas, dev methodologies. | Workflow Framework, Conversation Modes |
| [context7](https://github.com/upstash/context7) | MCP serving up-to-date, version-specific library docs to the agent. | Building Software, Research |
| [serena](https://github.com/oraios/serena) | MCP toolkit for semantic (symbol-level) code retrieval and editing. | Building Software, Understanding |
| [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Lets agents drive and inspect Chrome: DOM, console, network, performance traces. | Testing, UI Design |
| [playwright-mcp](https://github.com/microsoft/playwright-mcp) | Playwright browser automation over MCP via accessibility snapshots. | Testing |
| [github-mcp-server](https://github.com/github/github-mcp-server) | GitHub's official MCP server: repos, issues, PRs, Actions. | Maintenance |
| [trailofbits/skills](https://github.com/trailofbits/skills) | Security research, vulnerability detection and audit skills. | Security, Testing |
| [beads](https://github.com/gastownhall/beads) | Git-backed issue tracker / memory for coding agents. | Memory / Context, Planning Work |
| [ccusage](https://github.com/ccusage/ccusage) | Token usage and cost reports from Claude Code / Codex logs. | AI Evaluation / Optimization |
| [promptfoo](https://github.com/promptfoo/promptfoo) | Test and compare prompts, agents, RAG; red-teaming and vulnerability scanning. | AI Evaluation / Optimization, Testing, Security |
| [claude-code-router](https://github.com/musistudio/claude-code-router) | Route Claude Code (and other agents) across different models/providers. | AI Evaluation / Optimization |
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 177 validated skills for scientific research and analysis. | Research |
| [gpt-researcher](https://github.com/assafelovic/gpt-researcher) | Autonomous deep-research agent producing cited reports, any LLM. | Research |
| [ruflo](https://github.com/ruvnet/ruflo) | Multi-agent swarm orchestration with memory (formerly claude-flow). | Agent Orchestrators |
| [claude-squad](https://github.com/smtg-ai/claude-squad) | Run and manage multiple terminal agents (Claude Code, Codex, OpenCode, Amp) in parallel. | Agent Orchestrators |