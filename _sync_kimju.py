# kimju.kr/baseball 에 같은 앱을 올린다 (주소창에 kimju.kr/baseball 이 보이게)
# - 화면(index.html)·앱 정보·아이콘·서비스 워커만 kimju.kr(ac 저장소)에 복사
# - 음원·그림은 <base>로 kimju1416.github.io/baseball 에서 그대로 받아 300MB를 두 번 올리지 않는다
# 쓰는 법: 이 저장소에서 고치고 푸시한 뒤 `python _sync_kimju.py` → ac 저장소 커밋·푸시
import shutil, pathlib, re
SRC = pathlib.Path(__file__).parent
DST = pathlib.Path(r'C:/Users/USER/Downloads/ac/baseball')
DST.mkdir(exist_ok=True)
html = (SRC / 'index.html').read_text(encoding='utf-8')
html = html.replace('<meta charset="utf-8">',
    '<meta charset="utf-8">\n<base href="https://kimju1416.github.io/baseball/">', 1)
for f in ['manifest.webmanifest', 'icon-180.png', 'icon-192.png']:
    html = html.replace(f'href="{f}"', f'href="https://kimju.kr/baseball/{f}"')
html = html.replace('content="https://kimju1416.github.io/baseball/"', 'content="https://kimju.kr/baseball/"')
assert html.count('<base ') == 1 and 'https://kimju.kr/baseball/manifest.webmanifest' in html
(DST / 'index.html').write_text(html, encoding='utf-8', newline='\n')
for f in ['manifest.webmanifest', 'sw.js', 'icon-180.png', 'icon-192.png', 'icon-512.png', 'icon-maskable-512.png']:
    shutil.copy2(SRC / f, DST / f)
print('kimju.kr 사본 갱신:', DST)
