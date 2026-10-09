# Codex permissions

Project Git rules live in `.codex/rules/git.rules`:

- Allow `git add` and `git commit` without approval outside the sandbox.
- Require approval for `git push` outside the sandbox.

Trust the project configuration and restart Codex to load these rules.
Managed policies may impose additional restrictions.

Ordinary file creation inside the workspace is covered by workspace write
permissions. Command rules do not grant file access to protected directories.

Validate a command without running it:

```sh
codex execpolicy check --pretty --rules .codex/rules/git.rules -- git add -A
```
