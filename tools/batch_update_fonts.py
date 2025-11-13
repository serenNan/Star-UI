#!/usr/bin/env python3
"""
批量更新模块字体样式脚本
自动修改标签/标题/副标题的字体、字号和权重
"""

import re
import os
from pathlib import Path

# 定义需要修改的模块列表
MODULES = [
    'styles',
    'style_cea',
    'pic_wall',
    'question',
    'explore_more',
    'exp_2',
    'brand-control_cmps',
    'built_for_speed',
    'calculator',
    'brand-control',
    'assistant',
    'ai_creative_suite',
    'adaptation',
    'ROI',
    'APIs',
]

# 字体修改规则
FONT_RULES = {
    'label': {
        'font-family': "'Sora', sans-serif",
        'font-size': 'clamp(1rem, 2vw, 1.5rem)',
        'font-weight': '400',
    },
    'title': {
        'font-family': "'Poppins', sans-serif",
        'font-size': 'clamp(2rem, 5vw, 3.75rem)',
        'font-weight': '700',
    },
    'description': {
        'font-family': "'Sora', sans-serif",
        'font-size': 'clamp(1.125rem, 2vw, 1.75rem)',
        'font-weight': '300',
    },
    'subtitle': {
        'font-family': "'Sora', sans-serif",
        'font-size': 'clamp(1.125rem, 2vw, 1.75rem)',
        'font-weight': '300',
    },
}


def update_font_properties(css_content, class_name, element_type):
    """更新CSS中的字体属性"""
    rules = FONT_RULES.get(element_type, {})
    if not rules:
        return css_content

    # 查找class定义块
    pattern = rf'(\.{re.escape(class_name)}\s*\{{[^}}]*?\}})'

    def replace_properties(match):
        block = match.group(1)

        # 更新或添加 font-family
        if 'font-family' in rules:
            if 'font-family' in block:
                block = re.sub(
                    r'font-family:\s*[^;]+;',
                    f"font-family: {rules['font-family']};",
                    block
                )
            else:
                # 在开始的大括号后添加
                block = block.replace('{', '{\n  font-family: ' + rules['font-family'] + ';', 1)

        # 更新 font-size
        if 'font-size' in rules:
            if 'font-size' in block:
                block = re.sub(
                    r'font-size:\s*[^;]+;',
                    f"font-size: {rules['font-size']};",
                    block
                )

        # 更新 font-weight
        if 'font-weight' in rules:
            if 'font-weight' in block:
                block = re.sub(
                    r'font-weight:\s*[^;]+;',
                    f"font-weight: {rules['font-weight']};",
                    block
                )
            else:
                # 如果没有font-weight,在font-size后添加
                if 'font-size' in block:
                    block = re.sub(
                        r'(font-size:\s*[^;]+;)',
                        r'\1\n  font-weight: ' + rules['font-weight'] + ';',
                        block
                    )

        return block

    result = re.sub(pattern, replace_properties, css_content, flags=re.DOTALL)
    return result


def process_module(module_name):
    """处理单个模块文件"""
    base_path = Path(__file__).parent.parent
    file_path = base_path / 'sections' / module_name / f'{module_name}.html'

    if not file_path.exists():
        print(f"⚠️  文件不存在: {file_path}")
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 查找可能的class命名模式
        module_prefix = module_name.replace('-', '_')

        # 尝试匹配各种可能的class名称模式
        patterns = [
            (f'{module_prefix}_label', 'label'),
            (f'{module_prefix}-label', 'label'),
            (f'{module_prefix}__label', 'label'),
            (f'{module_prefix}_subtitle', 'subtitle'),
            (f'{module_prefix}-subtitle', 'subtitle'),
            (f'{module_prefix}__subtitle', 'subtitle'),
            (f'{module_prefix}_title', 'title'),
            (f'{module_prefix}-title', 'title'),
            (f'{module_prefix}__title', 'title'),
            (f'{module_prefix}_description', 'description'),
            (f'{module_prefix}-description', 'description'),
            (f'{module_prefix}__description', 'description'),
            (f'{module_prefix}_tag', 'label'),
            (f'{module_prefix}-tag', 'label'),
        ]

        modified = False
        for class_name, element_type in patterns:
            if f'.{class_name}' in content:
                content = update_font_properties(content, class_name, element_type)
                modified = True

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {module_name}")
            return True
        else:
            print(f"⏭️  {module_name} (未找到匹配的class)")
            return False

    except Exception as e:
        print(f"❌ {module_name}: {e}")
        return False


def main():
    """主函数"""
    print("🚀 开始批量更新模块字体...")
    print(f"📦 需要处理 {len(MODULES)} 个模块\n")

    success_count = 0
    for module in MODULES:
        if process_module(module):
            success_count += 1

    print(f"\n✨ 完成! 成功修改 {success_count}/{len(MODULES)} 个模块")


if __name__ == '__main__':
    main()
