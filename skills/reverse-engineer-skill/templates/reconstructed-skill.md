---
name: <kebab-case-name>
description: Use when <the job this skill does, in trigger terms>.
metadata:
  reconstructed-from: <N> outputs (<train count> train, <held-out count> held out)
  method: reverse-engineer-skill v0.1
---

# <Skill title>

Input: <what the brief contains>. Output: <what is produced, format only>.

## Template

<The skeleton with placeholders, one block per line, blank lines as seen.
Fixed strings appear verbatim. Everything else is a placeholder.>

## Rules

Each rule ends with its evidence tag: [observed N/N], [conditional k/N: <brief property>],
[tendency k/N], [range observed a to b, N=n], [absent 0/N].

1. <rule> [tag]
2. ...

## Example

<One new example on a topic none of the source outputs use. Optional.>

## Unknowns

What the source skill may contain that the outputs cannot show. Do not act on these as rules.

- <for example: word bans, persona backstory, behavior for briefs unlike the sources>
