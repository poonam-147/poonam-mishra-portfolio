import re

with open('css/style.css', 'r') as f:
    content = f.read()

# Add new CSS variables to :root
root_replacement = """    --gradient-accent: linear-gradient(135deg, #00FFAA, #00D488);
    
    --border-color: rgba(255, 255, 255, 0.1);
    --border-light: rgba(255, 255, 255, 0.05);
    --glass-bg: rgba(10, 15, 28, 0.7);
    --glass-shadow: rgba(0, 0, 0, 0.5);"""
content = content.replace("    --gradient-accent: linear-gradient(135deg, #00FFAA, #00D488);", root_replacement)

# Add [data-theme="light"]
theme_light = """
[data-theme="light"] {
    --bg-main: #F3F4F6;
    --bg-surface: #FFFFFF;
    --bg-surface-hover: #E5E7EB;
    --text-primary: #111827;
    --text-secondary: #4B5563;
    
    --border-color: rgba(0, 0, 0, 0.1);
    --border-light: rgba(0, 0, 0, 0.05);
    --glass-bg: rgba(255, 255, 255, 0.9);
    --glass-shadow: rgba(0, 0, 0, 0.1);
}
"""
content = content.replace(":root {", ":root {\n" + theme_light)

# Replace hardcoded colors
content = re.sub(r'rgba?\(255,\s*255,\s*255,\s*0\.1\)', 'var(--border-color)', content)
content = re.sub(r'rgba?\(255,\s*255,\s*255,\s*0\.0[58]\)', 'var(--border-light)', content)
content = re.sub(r'rgba?\(10,\s*15,\s*28,\s*0\.[789]5?\)', 'var(--glass-bg)', content)
content = re.sub(r'color:\s*#fff(?:fff)?\b', 'color: var(--text-primary)', content, flags=re.IGNORECASE)
content = re.sub(r'color:\s*#000(?:000)?\b', 'color: var(--bg-main)', content, flags=re.IGNORECASE)

with open('css/style.css', 'w') as f:
    f.write(content)
