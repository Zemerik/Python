# Day 20: Package Management

## What You'll Learn:
- Installing/uninstalling packages with `pip`
- Managing dependency versions
- Creating and using `requirements.txt`
- Resolving dependency conflicts
- Using pip cache and version specifiers

## Files:
1. `pip_commands.sh` - Common pip operations
2. `requirements_example.txt` - Dependency specification
3. `version_handling.py` - Version checking
4. `dependency_conflicts.md` - Conflict resolution guide

## Exercises:
1. Create a project that:
   - Installs 3 packages with specific versions
   - Generates requirements.txt automatically
   - Replicates environment on another machine
2. Resolve a simulated version conflict:
   - Package A requires libX>=2.0
   - Package B requires libX<2.0
   - Find compatible versions