#!/usr/bin/env python3
"""Patch pandoc's default reference.docx into a clean, readable handout style."""
import re, shutil, subprocess, os, sys

D = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(D, 'refdoc')
OUT = os.path.join(D, 'reference.docx')

BLUE = '00618A'      # MySQL blue - headings
DARK = '1A1A1A'      # body text
GREY = '44546A'      # sub-headings
RULE = 'D5DDE5'      # table borders
TINT = 'F2F7FA'      # callout background

p = os.path.join(SRC, 'word/styles.xml')
s = open(p, encoding='utf-8').read()


def style(sid, body):
    """Replace the inner content of a <w:style> block, keeping its <w:name>."""
    global s
    m = re.search(r'(<w:style [^>]*w:styleId="%s">)(.*?)(</w:style>)' % sid, s, re.S)
    if not m:
        sys.exit('missing style: ' + sid)
    inner = m.group(2)
    name = re.search(r'<w:name [^>]*/>', inner).group(0)
    based = re.search(r'<w:basedOn [^>]*/>', inner)
    nxt = re.search(r'<w:next [^>]*/>', inner)
    link = re.search(r'<w:link [^>]*/>', inner)
    keep = name + (based.group(0) if based else '') + (nxt.group(0) if nxt else '') \
        + (link.group(0) if link else '')
    s = s[:m.start()] + m.group(1) + keep + body + m.group(3) + s[m.end():]


# --- document defaults: 11pt, comfortable line spacing -----------------------
s = s.replace('<w:sz w:val="24" /><w:szCs w:val="24" />'.replace('><', '>\n        <'),
              '<w:sz w:val="22" />\n        <w:szCs w:val="22" />')
s = re.sub(r'(<w:rPrDefault>.*?)<w:sz w:val="24" />\s*<w:szCs w:val="24" />',
           r'\1<w:sz w:val="22" /><w:szCs w:val="22" />', s, flags=re.S)
s = re.sub(r'(<w:pPrDefault>\s*<w:pPr>\s*)<w:spacing w:after="200" />',
           r'\1<w:spacing w:after="160" w:line="276" w:lineRule="auto" />', s)

# --- body text ---------------------------------------------------------------
style('BodyText', f'<w:pPr><w:spacing w:before="0" w:after="160" w:line="276" '
                  f'w:lineRule="auto"/></w:pPr><w:rPr><w:color w:val="{DARK}"/></w:rPr>')

# --- title block -------------------------------------------------------------
style('Title', f'<w:pPr><w:spacing w:before="0" w:after="80"/>'
               f'<w:contextualSpacing/></w:pPr>'
               f'<w:rPr><w:b/><w:color w:val="{BLUE}"/><w:sz w:val="56"/>'
               f'<w:szCs w:val="56"/></w:rPr>')
style('Subtitle', f'<w:pPr><w:spacing w:before="0" w:after="360"/>'
                  f'<w:contextualSpacing/></w:pPr>'
                  f'<w:rPr><w:color w:val="{GREY}"/><w:sz w:val="28"/>'
                  f'<w:szCs w:val="28"/></w:rPr>')

# --- headings: H1 gets a rule under it, H2 blue, H3 grey ---------------------
style('Heading1', f'<w:pPr><w:keepNext/><w:pageBreakBefore/>'
                  f'<w:pBdr><w:bottom w:val="single" w:sz="8" w:space="4" '
                  f'w:color="{BLUE}"/></w:pBdr>'
                  f'<w:spacing w:before="0" w:after="240"/></w:pPr>'
                  f'<w:rPr><w:b/><w:color w:val="{BLUE}"/><w:sz w:val="36"/>'
                  f'<w:szCs w:val="36"/></w:rPr>')
style('Heading2', f'<w:pPr><w:keepNext/><w:spacing w:before="360" w:after="120"/></w:pPr>'
                  f'<w:rPr><w:b/><w:color w:val="{BLUE}"/><w:sz w:val="28"/>'
                  f'<w:szCs w:val="28"/></w:rPr>')
style('Heading3', f'<w:pPr><w:keepNext/><w:spacing w:before="280" w:after="100"/></w:pPr>'
                  f'<w:rPr><w:b/><w:color w:val="{GREY}"/><w:sz w:val="24"/>'
                  f'<w:szCs w:val="24"/></w:rPr>')
style('Heading4', f'<w:pPr><w:keepNext/><w:spacing w:before="240" w:after="80"/></w:pPr>'
                  f'<w:rPr><w:b/><w:i/><w:color w:val="{GREY}"/><w:sz w:val="22"/></w:rPr>')

# --- blockquote -> callout box ----------------------------------------------
style('BlockText', f'<w:pPr>'
                   f'<w:pBdr>'
                   f'<w:top w:val="single" w:sz="4" w:space="8" w:color="{RULE}"/>'
                   f'<w:left w:val="single" w:sz="24" w:space="10" w:color="{BLUE}"/>'
                   f'<w:bottom w:val="single" w:sz="4" w:space="8" w:color="{RULE}"/>'
                   f'<w:right w:val="single" w:sz="4" w:space="8" w:color="{RULE}"/>'
                   f'</w:pBdr>'
                   f'<w:shd w:val="clear" w:color="auto" w:fill="{TINT}"/>'
                   f'<w:spacing w:before="160" w:after="160" w:line="276" w:lineRule="auto"/>'
                   f'<w:ind w:left="170" w:right="170"/></w:pPr>'
                   f'<w:rPr><w:color w:val="{DARK}"/></w:rPr>')

# --- inline code -------------------------------------------------------------
style('VerbatimChar', '<w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" '
                      '<w:cs="Consolas"/><w:shd w:val="clear" w:color="auto" '
                      'w:fill="F0F3F6"/><w:color w:val="9B2C2C"/>'
                      '<w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr>'
                      .replace('<w:cs=', 'w:cs='))

# --- code blocks -------------------------------------------------------------
if 'w:styleId="SourceCode"' not in s:
    s = s.replace('</w:styles>',
                  f'<w:style w:type="paragraph" w:customStyle="1" w:styleId="SourceCode">'
                  f'<w:name w:val="Source Code"/><w:basedOn w:val="Normal"/>'
                  f'<w:pPr><w:pBdr>'
                  f'<w:top w:val="single" w:sz="4" w:space="6" w:color="{RULE}"/>'
                  f'<w:left w:val="single" w:sz="4" w:space="6" w:color="{RULE}"/>'
                  f'<w:bottom w:val="single" w:sz="4" w:space="6" w:color="{RULE}"/>'
                  f'<w:right w:val="single" w:sz="4" w:space="6" w:color="{RULE}"/>'
                  f'</w:pBdr>'
                  f'<w:shd w:val="clear" w:color="auto" w:fill="F7F9FB"/>'
                  f'<w:spacing w:before="120" w:after="120" w:line="240" w:lineRule="auto"/>'
                  f'<w:ind w:left="170" w:right="170"/></w:pPr>'
                  f'<w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/>'
                  f'<w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr></w:style></w:styles>')

# --- tables ------------------------------------------------------------------
style('Table', f'<w:tblPr><w:tblBorders>'
               f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{RULE}"/>'
               f'<w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
               f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="{RULE}"/>'
               f'<w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
               f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{RULE}"/>'
               f'<w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>'
               f'</w:tblBorders>'
               f'<w:tblCellMar>'
               f'<w:top w:w="72" w:type="dxa"/><w:left w:w="108" w:type="dxa"/>'
               f'<w:bottom w:w="72" w:type="dxa"/><w:right w:w="108" w:type="dxa"/>'
               f'</w:tblCellMar></w:tblPr>')

# --- TOC heading -------------------------------------------------------------
style('TOCHeading', f'<w:pPr><w:keepNext/><w:pBdr><w:bottom w:val="single" w:sz="8" '
                    f'w:space="4" w:color="{BLUE}"/></w:pBdr>'
                    f'<w:spacing w:before="0" w:after="240"/></w:pPr>'
                    f'<w:rPr><w:b/><w:color w:val="{BLUE}"/><w:sz w:val="36"/>'
                    f'<w:szCs w:val="36"/></w:rPr>')

open(p, 'w', encoding='utf-8').write(s)

# --- page margins ------------------------------------------------------------
dp = os.path.join(SRC, 'word/document.xml')
d = open(dp, encoding='utf-8').read()
d = re.sub(r'<w:pgMar[^/]*/>',
           '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" '
           'w:header="709" w:footer="709" w:gutter="0"/>', d)
open(dp, 'w', encoding='utf-8').write(d)

if os.path.exists(OUT):
    os.remove(OUT)
subprocess.run(['zip', '-q', '-r', '-X', OUT, '.'], cwd=SRC, check=True)
print('built', OUT, os.path.getsize(OUT), 'bytes')
