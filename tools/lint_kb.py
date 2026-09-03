#!/usr/bin/env python3
"""
School of Teacher Education (STE) Knowledge Base Linter & Health Auditor
Style: Andrej Karpathy LLM Knowledge Base Compiler & Linter

Audits:
1. YAML frontmatter completeness and validity
2. Wikilinks [[...]] and Markdown links [...] target existence
3. Graph connectivity, orphan detection, and bidirectional backlink health
"""

import os
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

EXCLUDED_DIRS = {'.git', 'scratch', 'web-reports', 'web-template', '.gemini', 'tools', '.system_generated', '__pycache__'}

def get_all_md_files():
    md_files = []
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for f in files:
            if f.endswith('.md'):
                md_files.append(Path(root) / f)
    return sorted(md_files)

def parse_frontmatter(content):
    if not content.startswith('---'):
        return None, "Missing frontmatter delimiters"
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, "Malformed frontmatter block"
    fm_text = parts[1]
    data = {}
    for line in fm_text.strip().splitlines():
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val.startswith('[') and val.endswith(']'):
                val = [x.strip().strip('"').strip("'") for x in val[1:-1].split(',') if x.strip()]
            data[key] = val
    return data, None

def normalize_target(target, source_file):
    # Clean target
    target = target.replace('\\', '').split('#')[0].strip()
    if not target:
        return None
    
    # Check if target is already a valid relative path
    source_dir = source_file.parent
    rel_path = (source_dir / target).resolve()
    if rel_path.is_file():
        return rel_path
    if (source_dir / f"{target}.md").resolve().is_file():
        return (source_dir / f"{target}.md").resolve()
    
    # Check if target is root-relative (e.g. overview/about-ste)
    root_rel = (ROOT_DIR / target).resolve()
    if root_rel.is_file():
        return root_rel
    if (ROOT_DIR / f"{target}.md").resolve().is_file():
        return (ROOT_DIR / f"{target}.md").resolve()

    # Check by filename anywhere in kb
    target_name = Path(target).name
    if not target_name.endswith('.md'):
        target_name += '.md'
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        if target_name in files:
            return (Path(root) / target_name).resolve()

    return None

def audit_kb():
    md_files = get_all_md_files()
    file_set = {f.resolve() for f in md_files}
    
    print(f"Auditing STE Knowledge Base across {len(md_files)} markdown files...")
    print("=" * 70)

    inbound_links = {f: set() for f in file_set}
    outbound_links = {f: set() for f in file_set}
    
    frontmatter_errors = []
    broken_links = []
    total_links_found = 0

    valid_types = {
        'overview', 'person', 'program', 'certificate', 'pathway', 
        'funding', 'curriculum', 'center', 'analytics', 'index'
    }

    for file_path in md_files:
        rel_file = file_path.relative_to(ROOT_DIR)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Frontmatter Check
        fm, err = parse_frontmatter(content)
        if err:
            frontmatter_errors.append((str(rel_file), err))
        else:
            required_keys = ['title', 'type', 'tags', 'source_url', 'last_updated', 'summary']
            for k in required_keys:
                if k not in fm or not fm[k]:
                    frontmatter_errors.append((str(rel_file), f"Missing required frontmatter key: '{k}'"))
            if 'type' in fm and fm['type'] not in valid_types:
                frontmatter_errors.append((str(rel_file), f"Invalid type '{fm['type']}'. Must be one of {valid_types}"))

        # Strip code blocks and inline code so examples are not parsed as real links
        content_for_links = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        content_for_links = re.sub(r'`[^`]+`', '', content_for_links)

        # 2. Extract Wikilinks [[target]] or [[target|alias]]
        wikilinks = re.findall(r'\[\[([^\]\|]+)(?:\\?\|[^\]]+)?\]\]', content_for_links)
        for wl in wikilinks:
            total_links_found += 1
            norm = normalize_target(wl, file_path)
            if norm and norm in file_set:
                outbound_links[file_path.resolve()].add(norm)
                inbound_links[norm].add(file_path.resolve())
            else:
                broken_links.append((str(rel_file), f"Broken wikilink: [[{wl}]]"))

        # 3. Extract standard Markdown links [text](path)
        md_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content_for_links)
        for text, link in md_links:
            # Skip web URLs, mailto, tel, sms
            if any(link.startswith(p) for p in ['http://', 'https://', 'mailto:', 'tel:', 'sms:', '#']):
                continue
            total_links_found += 1
            norm = normalize_target(link, file_path)
            if norm and norm in file_set:
                outbound_links[file_path.resolve()].add(norm)
                inbound_links[norm].add(file_path.resolve())
            else:
                broken_links.append((str(rel_file), f"Broken markdown link: [{text}]({link})"))

    # 4. Check for Orphaned Files (In-degree == 0, excluding INDEX.md)
    orphans = []
    for f in file_set:
        rel = f.relative_to(ROOT_DIR)
        if str(rel) in ['INDEX.md']:
            continue
        if len(inbound_links[f]) == 0:
            orphans.append(str(rel))

    # Print Results
    print(f"Total Markdown Files Audited : {len(md_files)}")
    print(f"Total Internal Links Verified: {total_links_found}")
    print(f"Frontmatter Validation Errors: {len(frontmatter_errors)}")
    print(f"Broken Internal Links Found  : {len(broken_links)}")
    print(f"Orphaned Files (0 Inbound)   : {len(orphans)}")
    print("=" * 70)

    if frontmatter_errors:
        print("\n[!] Frontmatter Errors:")
        for f, err in frontmatter_errors[:10]:
            print(f"  - {f}: {err}")
        if len(frontmatter_errors) > 10:
            print(f"  ... and {len(frontmatter_errors) - 10} more")

    if broken_links:
        print("\n[!] Broken Links:")
        for f, err in broken_links[:10]:
            print(f"  - {f}: {err}")
        if len(broken_links) > 10:
            print(f"  ... and {len(broken_links) - 10} more")

    if orphans:
        print("\n[!] Orphaned Documents (No Inbound Links):")
        for o in orphans:
            print(f"  - {o}")

    if not frontmatter_errors and not broken_links and not orphans:
        print("\n✨ SUCCESS: 100% HEALTH SCORE! Knowledge Base link graph and metadata are fully intact. ✨")
        return 0
    else:
        print("\nATTENTION: Please resolve the above issues to achieve 100% graph health.")
        return 1

if __name__ == "__main__":
    sys.exit(audit_kb())
