
#!/usr/bin/env bash

# Search for CSV files under $HOME, excluding:
#   - $HOME/.local
#   - $HOME/.vscode
#   - any directory containing "python" (case-insensitive)
# Output: aligned table: FILENAME | MODIFIED DATE
# Sorted by MOST RECENT modification timestamp (descending)

HOME_DIR="${HOME}"

# Header
printf "%-80s  %s\n" "FILE" "MODIFIED DATE"
printf "%-80s  %s\n" "----" "-------------"

# Find CSV files, get modification time in epoch + filename,
# then sort by epoch desc, then print aligned.
find "$HOME_DIR" \
  \( -path "$HOME_DIR/.local" -o \
     -path "$HOME_DIR/.vscode*" -o \
     -iname "*python*" \
  \) -prune \
  -o -type f -name "*.csv" -print0 |
while IFS= read -r -d '' file; do
    epoch="$(stat -c '%Y' "$file")"
    echo "${epoch}|${file}"
done | sort -nr | while IFS='|' read -r epoch file; do
    mod="$(stat -c '%y' "$file")"
    printf "%-80s  %s\n" "$file" "$mod"
done
