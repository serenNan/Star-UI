#!/usr/bin/env python3
"""
社交媒体链接生成器
根据 social-links.config.json 生成 sections/links/links.html
"""

import json
from pathlib import Path

def generate_social_links():
    """从配置文件生成社交媒体链接 HTML"""

    # 读取配置文件
    config_file = Path(__file__).parent / 'social-links.config.json'
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)

    # 过滤启用的链接
    enabled_links = [link for link in config['links'] if link.get('enabled', True)]

    if not enabled_links:
        print('[warn] 警告: 没有启用的社交媒体链接')
        return

    # 生成 HTML
    html_parts = [
        '<!-- 社交媒体链接区域 -->',
        '<!-- 此文件由 tools/generate-social-links.py 自动生成 -->',
        '<!-- 请勿手动编辑! 修改 tools/social-links.config.json 然后重新运行构建 -->',
        '',
        '<style>',
        '.social-links {',
        '  padding: var(--spacing-xl) 0;',
        '  background: var(--color-bg);',
        '}',
        '',
        '.social-links-container {',
        '  max-width: var(--container-width);',
        '  margin: 0 auto;',
        '  padding: 0 var(--spacing-lg);',
        '  display: flex;',
        '  justify-content: space-between;',
        '  align-items: center;',
        '  flex-wrap: wrap;',
        '  gap: 2rem;',
        '}',
        '',
        '.social-link {',
        '  display: flex;',
        '  align-items: center;',
        '  gap: 0.75rem;',
        '  text-decoration: none;',
        '  transition: all var(--transition);',
        '  opacity: 0.8;',
        '}',
        '',
        '.social-link:hover {',
        '  opacity: 1;',
        '  transform: translateY(-2px);',
        '}',
        '',
        '.social-link-icon {',
        '  width: 32px;',
        '  height: 32px;',
        '  fill: var(--color-text);',
        '  flex-shrink: 0;',
        '}',
        '',
        '.social-link-text {',
        '  color: var(--color-text);',
        '  font-size: 1rem;',
        '  font-weight: 500;',
        '  white-space: nowrap;',
        '}',
        '',
        '/* 响应式设计 */',
        '@media (max-width: 991px) {',
        '  .social-links-container {',
        '    justify-content: center;',
        '    gap: 1.5rem;',
        '  }',
        '}',
        '',
        '@media (max-width: 767px) {',
        '  .social-links-container {',
        '    gap: 1rem;',
        '  }',
        '  ',
        '  .social-link-icon {',
        '    width: 28px;',
        '    height: 28px;',
        '  }',
        '  ',
        '  .social-link-text {',
        '    font-size: 0.9rem;',
        '  }',
        '}',
        '</style>',
        '',
        '<section class="social-links">',
        '  <div class="social-links-container">',
    ]

    # 生成每个链接
    available_icons = config['available_icons']
    for link in enabled_links:
        icon_name = link['icon']
        icon_path = available_icons.get(icon_name, '')

        if not icon_path:
            print(f'[warn] 警告: 找不到图标 "{icon_name}"')
            continue

        html_parts.extend([
            f'    <a href="{link["url"]}" class="social-link" target="_blank" rel="noopener noreferrer">',
            f'      <svg class="social-link-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">',
            f'        {icon_path}',
            f'      </svg>',
            f'      <span class="social-link-text">{link["name"]}</span>',
            f'    </a>',
        ])

    html_parts.extend([
        '  </div>',
        '</section>',
    ])

    # 写入文件
    output_file = Path(__file__).parent.parent / 'sections' / 'links' / 'links.html'
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))

    print('[done] 成功生成社交媒体链接 HTML')
    print(f'   文件: {output_file}')
    print(f'   链接数: {len(enabled_links)}')
    for link in enabled_links:
        print(f'   - {link["name"]}')

if __name__ == '__main__':
    generate_social_links()
