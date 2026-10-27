---
name: <kebab-case-name>
description: Use when <the job this skill does, in trigger terms>.
metadata:
  reconstructed-from: <N> outputs (<train count> train, <held-out count> held out)
  method: reverse-engineer-skill v0.3
---

# <Skill title>

Input: <what the brief contains>. Output: <what is produced, format only>.

## Template

<The skeleton with placeholders, one block per line, blank lines as seen.
Fixed strings appear verbatim. Everything else is a placeholder.
If shapes differ by brief type, use a menu: one named skeleton per type, each
with its trigger.>

## Rules

Structure, required parts, fixed strings, conditionals. Each ends with its
evidence tag: [observed N/N], [conditional k/N: <brief property>],
[tendency k/N], [range observed a to b, N=n], [capped max k].

1. <rule> [tag]

## Defaults

Habits seen in the sample that the source may not require. Follow them unless
the user's voice says otherwise. Same evidence tags.

1. <default> [tag]

## Example

<One new example on a topic none of the source outputs use. Optional.>

## Unknowns

Questions the outputs cannot answer. Do not act on these as rules.

- <for example: Are AI-tell patterns like "not X, it's Y" banned? Is there a
  per-user voice file? What happens for content types not seen?>