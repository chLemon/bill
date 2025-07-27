from pathlib import Path

cur = Path()

for item in cur.rglob('*'):
    if item.is_file():
        item.rename(cur / item.name)

# 删除所有空目录（从深到浅）
for folder in sorted([p for p in cur.rglob('*') if p.is_dir()], key=lambda x: -len(x.parts)):
    try:
        folder.rmdir()
    except OSError:
        pass  # 非空目录跳过
