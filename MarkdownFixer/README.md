# Markdown fixer

## idea
Get md-file as input, fix the line-endings. Problem is that a newline is not a newline in Markdown, but a double space (besides other things).
So check each line-ending if it has double space, else append.
Beware: things like headlines (start with #) or lists (start with *) have already wrapping: so don't handle them.

## gui
Maybe add some PyQt-interface with drop-down and "auto-process feature".
