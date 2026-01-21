#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

TARGET="${1:-main.py}"
case "$TARGET" in
  main|main.py) TARGET="main.py" ;;
  example|example.py) TARGET="example.py" ;;
  *.py) ;;
  *)
    echo "Usage: ./run.sh [main|example|path/to/script.py]" >&2
    exit 2
    ;;
esac

ENV_NAME="${GEMINI_CONDA_ENV:-pytorch-cu128}"

if [[ "${CONDA_DEFAULT_ENV:-}" == "$ENV_NAME" ]]; then
  exec python "$TARGET"
fi

if command -v conda >/dev/null 2>&1; then
  exec conda run -n "$ENV_NAME" python "$TARGET"
fi

exec python "$TARGET"
