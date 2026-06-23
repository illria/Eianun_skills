#!/usr/bin/env bash
# Eianun Skills - local installer
# Usage:
#   bash setup.sh
#   bash setup.sh ai-tool-viral-post-writer youtube-thumbnail-producer-codex-v4

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

info()  { echo -e "${GREEN}[✓]${NC} $*"; }
warn()  { echo -e "${YELLOW}[!]${NC} $*"; }
error() { echo -e "${RED}[✗]${NC} $*"; }

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/skills"

SKILLS=("ai-tool-viral-post-writer" "youtube-thumbnail-producer-codex-v4" "seedance-storyboard-prompt")

if [[ $# -gt 0 ]]; then
  SKILLS=("$@")
fi

echo ""
echo "========================================="
echo "  Eianun Skills 安装助手"
echo "========================================="
echo ""

mkdir -p "$TARGET_DIR"
info "目标目录：$TARGET_DIR"

for skill in "${SKILLS[@]}"; do
  src="$ROOT_DIR/$skill"
  dest="$TARGET_DIR/$skill"

  if [[ ! -d "$src" ]]; then
    error "未找到 skill：$skill"
    exit 1
  fi

  rm -rf "$dest"
  mkdir -p "$dest"
  cp -R "$src"/. "$dest"/
  info "已安装：$skill"
done

echo ""
echo "安装完成。"
echo ""
warn "如果你的 Agent 已经在运行，可能需要重启会话后才能看到新 Skill。"
echo ""
