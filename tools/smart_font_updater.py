#!/usr/bin/env python3
"""
智能字体更新器 - 自动识别并更新各种命名模式的字体样式
"""

import re
from pathlib import Path

# 标签类关键词
LABEL_KEYWORDS = ['label', 'tag', 'subtitle', 'header-label']
# 标题类关键词
TITLE_KEYWORDS = ['title', 'heading']
# 描述类关键词
DESC_KEYWORDS = ['description', 'subtitle', 'desc']

# 字体规则
RULES = {
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
}


def identify_type(class_name):
    """识别class的类型"""
    class_lower = class_name.lower()

    # 优先检查标题,避免与subtitle混淆
    for keyword in TITLE_KEYWORDS:
        if keyword in class_lower and 'subtitle' not in class_lower:
            return 'title'

    # 检查标签
    for keyword in LABEL_KEYWORDS:
        if keyword in class_lower:
            return 'label'

    # 检查描述
    for keyword in DESC_KEYWORDS:
        if keyword in class_lower:
            return 'description'

    return None


def update_css_block(content, class_name, rules):
    """更新单个CSS类的样式块"""
    # 匹配整个CSS类块
    pattern = rf'(\.{re.escape(class_name)}\s*\{{[^}}]*?}})'

    def replacer(match):
        block = match.group(1)

        # 更新font-family
        if 'font-family' in rules:
            if re.search(r'font-family\s*:', block):
                block = re.sub(
                    r'font-family\s*:\s*[^;]+;',
                    f"font-family: {rules['font-family']};",
                    block
                )
            else:
                # 在第一个属性前插入
                block = re.sub(
                    r'(\{)\s*',
                    r'\1\n    font-family: ' + rules['font-family'] + ';',
                    block,
                    count=1
                )

        # 更新font-size
        if 'font-size' in rules:
            if re.search(r'font-size\s*:', block):
                block = re.sub(
                    r'font-size\s*:\s*[^;]+;',
                    f"font-size: {rules['font-size']};",
                    block
                )

        # 更新font-weight
        if 'font-weight' in rules:
            if re.search(r'font-weight\s*:', block):
                block = re.sub(
                    r'font-weight\s*:\s*[^;]+;',
                    f"font-weight: {rules['font-weight']};",
                    block
                )

        return block

    return re.sub(pattern, replacer, content, flags=re.DOTALL)


def process_file(file_path):
    """处理单个HTML文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # 查找所有CSS类名
        class_pattern = r'\.([a-z0-9_-]+(?:__)?[a-z0-9_-]*?(?:label|title|description|subtitle|tag|header-label))\s*\{'
        classes = re.findall(class_pattern, content, re.IGNORECASE)

        modified_classes = []
        for class_name in set(classes):
            element_type = identify_type(class_name)
            if element_type and element_type in RULES:
                content = update_css_block(content, class_name, RULES[element_type])
                modified_classes.append(f"{class_name} -> {element_type}")

        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, modified_classes
        else:
            return False, []

    except Exception as e:
        print(f"❌ {file_path.name}: {e}")
        return False, []


def main():
    """主函数"""
    base_dir = Path(__file__).parent.parent / 'sections'

    # 查找所有HTML文件
    html_files = list(base_dir.glob('**/*.html'))

    print(f"🚀 智能字体更新器启动...")
    print(f"📦 找到 {len(html_files)} 个HTML文件\n")

    success_count = 0
    total_modifications = 0

    for file_path in sorted(html_files):
        modified, classes = process_file(file_path)
        if modified:
            success_count += 1
            total_modifications += len(classes)
            print(f"✅ {file_path.parent.name}/{file_path.name}")
            for cls in classes:
                print(f"   - {cls}")
        else:
            print(f"⏭️  {file_path.parent.name}/{file_path.name}")

    print(f"\n✨ 完成!")
    print(f"   成功修改: {success_count}/{len(html_files)} 个文件")
    print(f"   总修改项: {total_modifications} 处")


if __name__ == '__main__':
    main()
