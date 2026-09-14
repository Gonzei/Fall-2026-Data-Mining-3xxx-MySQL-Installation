# Fall 2026 — Data Mining 3xxx

Course materials and student-facing handouts.

## Contents

| Path | What it is |
|---|---|
| [docs/MySQL-Setup-Guide.docx](docs/MySQL-Setup-Guide.docx) | **Hand this out.** Word version of the MySQL + Workbench install guide, Windows and Mac. |
| [docs/mysql-setup-guide.md](docs/mysql-setup-guide.md) | Markdown source for the same guide — edit this, then regenerate the .docx. |

## Regenerating the Word document

The `.docx` is built from the Markdown with [pandoc](https://pandoc.org/):

```bash
pandoc docs/mysql-setup-guide.md -o docs/MySQL-Setup-Guide.docx --toc --toc-depth=2
```

## Versions the guide targets

As specified by the instructor:

- MySQL Community Server **26.7.0** — `mysql-26.7.0-winx64.msi`
- MySQL Workbench **8.0.47** — `mysql-workbench-community-8.0.47-winx64.msi`
  (archived release: https://downloads.mysql.com/archives/workbench/)

Mac students need the equivalent `.dmg` files matching their chip (ARM/Apple Silicon vs. x86/Intel).

Note: this pairing makes Workbench display an "incompatible/nonstandard server version"
warning on first connect. It is harmless, and the guide tells students to dismiss it.
Update these version numbers in the guide if the instructor changes them.
