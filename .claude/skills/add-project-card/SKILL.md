---
name: add-project-card
description: index.html의 #portfolio 섹션에 새 프로젝트 `.pf-card`를 프로젝트 컨벤션(클래스 구조·troubleshoot row 하단 배치·reveal 애니메이션·링크 버튼 활성화)에 맞춰 삽입한다. 사용자가 "포트폴리오 카드 추가", "새 프로젝트 올려줘", "add project card", "새 작업물 추가", "Project NN 추가" 등을 말할 때 사용한다. GitHub/사이트/기획서 중 일부만 주어지더라도 비어있는 버튼은 렌더하지 않고 주어진 링크만 삽입한다.
---

# add-project-card

이 스킬은 이 저장소(`pf/`) 전용이다. 정적 HTML + Tailwind + 커스텀 `style.css` + GSAP 스크롤 애니메이션 컨벤션에 맞춰 포트폴리오 섹션에 새 카드를 추가한다.

## 언제 호출되나

사용자가 다음과 비슷한 요청을 할 때:

- "포트폴리오에 새 프로젝트 추가해줘"
- "Project 04 / 05 카드 만들어줘"
- "새 작업물 올려줘 — 제목은 …, 이미지는 img/…, 깃허브 주소 …"
- "add project card", "append a new pf-card"
- 기존 카드에서 특정 링크(깃허브/사이트/기획서)만 "활성화"해달라는 후속 요청

## 필수 입력

스킬을 시작하기 전에 아래가 모두 있어야 한다. 하나라도 빠지면 **한 번에 묶어서** 사용자에게 물어본다(개별 질문 금지).

| 항목 | 예시 | 필수 여부 |
|---|---|---|
| 프로젝트 번호 | `04` | 선택 (미지정 시 마지막 카드 +1 자동) |
| 제목 (`pf-title`) | `모바일 웹 구현` | 필수 |
| 서브타이틀 (`pf-subtitle`) | `(VODA)` | 필수 |
| 이미지 파일 | `img/P4.png` 또는 새 업로드 경로 | 필수 |
| 이미지 alt | `VODA 프로젝트 이미지` | 선택 (미지정 시 `"{서브타이틀} 프로젝트 이미지"`) |
| 스펙 행 4개 | 작업기간 / 기여도 / 주요기술(또는 사용도구·사용기술) / 배포 매체(또는 핵심기능·영상길이) | 필수 |
| 트러블 슈팅 문구 | 2줄 권장, `<br>`로 줄바꿈 | 필수 |
| 링크 (1~3개) | `github`, `site`, `plan`(기획서), `prototype` 중 해당하는 것만 | 최소 1개 |
| 블러 배경 적용 | `true` / `false` (기본 `false`, Project 01처럼 배경 블러 원할 때 `true`) | 선택 |

## 수행 절차

1. **현재 상태 파악**
   - `index.html`에서 `<!-- Project NN -->` 주석들을 찾아 마지막 번호 + 1 을 결정.
   - 삽입 지점: 마지막 `</div> <!-- /pf-card -->` 바로 다음, `</section>` 이전.
2. **이미지 확인**
   - `img/` 안에 해당 파일이 실제로 존재하는지 검사. 없으면 **카드를 삽입하지 말고** 사용자에게 이미지 업로드를 먼저 요청.
   - 파일명에 공백/한글/대문자 혼용이 있으면(예: `image 15.png`) 안전한 kebab-case로 리네이밍 제안.
3. **HTML 생성** — 아래 템플릿을 그대로 사용하고, 조건부 블록(`[[...]]`)은 값이 있을 때만 렌더.
4. **삽입** — Edit 도구로 `index.html`의 정확한 위치에 추가. 전체 파일 재작성 금지.
5. **사후 검증**
   - `reveal` 또는 `reveal-toss` 클래스 존재 확인(카드는 기본적으로 `reveal` 필요 없음 — 기존 카드들도 미적용. 임의로 추가하지 말 것).
   - 링크가 URL만 placeholder(`#`, 빈 문자열)면 버튼을 렌더하지 말고 생략(과거 커밋 `fix: activate VODA site button link`가 바로 이 실수 교정).
   - `pf-spec-row--troubleshoot`는 **반드시 스펙 목록의 맨 마지막**에 둔다(커밋 `style: move troubleshooting row to the bottom for all projects` 참조).
   - 새로 추가한 이미지 경로가 실제 파일과 일치하는지 재확인.
6. **보고** — 삽입된 카드 번호, 이미지 경로, 활성화된 링크 개수를 한두 문장으로 요약. 추가 리팩터/설명 금지.

## HTML 템플릿

들여쓰기와 속성 순서는 기존 카드와 동일하게 유지한다. 2스페이스 들여쓰기.

```html
<!-- Project {{NN}} -->
<div class="pf-card">
  <div class="pf-left">
    <div class="pf-title-wrap">
      <h3 class="pf-title">{{TITLE}}</h3>
      <span class="pf-subtitle">({{SUBTITLE}})</span>
    </div>
    <div class="pf-specs">
      <div class="pf-spec-row">
        <span class="pf-label">{{LABEL_1}}</span><span class="pf-val">{{VAL_1}}</span>
      </div>
      <div class="pf-spec-row">
        <span class="pf-label">{{LABEL_2}}</span><span class="pf-val">{{VAL_2}}</span>
      </div>
      <div class="pf-spec-row">
        <span class="pf-label">{{LABEL_3}}</span><span class="pf-val">{{VAL_3}}</span>
      </div>
      <div class="pf-spec-row">
        <span class="pf-label">{{LABEL_4}}</span><span class="pf-val">{{VAL_4}}</span>
      </div>
      <div class="pf-spec-row pf-spec-row--troubleshoot">
        <span class="pf-label">트러블 슈팅</span><span class="pf-val pf-val--troubleshoot">{{TROUBLESHOOT_LINE_1}}<br>{{TROUBLESHOOT_LINE_2}}</span>
      </div>
    </div>
    <div class="pf-links">
      [[IF github]]
      <a href="{{GITHUB_URL}}" target="_blank" class="pf-link-btn">
        <svg viewBox="0 0 24 24" aria-hidden="true">
          <path d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34-.45-1.15-1.11-1.46-1.11-1.46-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.87 1.52 2.34 1.07 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.92 0-1.11.38-2 1.03-2.71-.1-.25-.45-1.29.1-2.64 0 0 .84-.27 2.75 1.02.79-.22 1.65-.33 2.5-.33.85 0 1.71.11 2.5.33 1.91-1.29 2.75-1.02 2.75-1.02.55 1.35.2 2.39.1 2.64.65.71 1.03 1.6 1.03 2.71 0 3.82-2.34 4.66-4.57 4.91.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2z"/>
        </svg>
        Github
      </a>
      [[/IF]]
      [[IF plan]]
      <a href="{{PLAN_URL}}" target="_blank" class="pf-link-btn">
        <svg viewBox="0 0 24 24" aria-hidden="true">
          <path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/>
        </svg>
        기획서
      </a>
      [[/IF]]
      [[IF site]]
      <a href="{{SITE_URL}}" target="_blank" class="pf-link-btn">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M5 12h14M12 5l7 7-7 7"/>
        </svg>
        사이트
      </a>
      [[/IF]]
      [[IF prototype]]
      <a href="{{PROTO_URL}}" target="_blank" class="pf-link-btn">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M5 12h14M12 5l7 7-7 7"/>
        </svg>
        프로토 타입
      </a>
      [[/IF]]
    </div>
  </div>
  <div class="pf-right[[IF blur]] pf-right--blur[[/IF]]"[[IF blur]] style="background-image: url('./{{IMG_PATH}}')"[[/IF]]>
    <img src="./{{IMG_PATH}}" alt="{{IMG_ALT}}" />
  </div>
</div>
```

## 컨벤션 고정 규칙

- **스펙 라벨은 한글**, 기존 사용 어휘 재사용: `작업기간 / 기여도 / 주요기술 / 사용도구 / 사용기술 / 배포 매체 / 핵심기능 / 영상길이`. 새 라벨을 도입하기 전에 사용자에게 확인.
- **트러블 슈팅은 무조건 마지막 행** (`pf-spec-row pf-spec-row--troubleshoot`). 두 줄 문장에 `<br>` 사용.
- **링크 버튼 순서**: GitHub → 기획서 → 사이트/프로토 타입. 데모 영상·리포트 등 신규 라벨을 추가할 때만 사용자에게 확인.
- **절대 추가하지 말 것**: 인라인 `style="color: ..."`, 임의 Tailwind 임의값, `reveal` 클래스를 카드에 부착(기존 카드들도 미부착 — 섹션 타이틀만 `reveal-toss`).
- **블러 우측 패널**: `pf-right--blur` + 동일 이미지를 `background-image`로 중복 선언. Project 01의 패턴을 그대로 따른다.
- **포인트 컬러**는 `#2D7FF9`(상단 GNB) / `var(--toss-blue)`(본문). 새 색 하드코딩 금지.

## 실패 조건 — 스킬을 중단하고 사용자에게 되돌릴 것

- 이미지 파일이 `img/`에 없음
- 유효 링크가 0개 (전부 `#`이거나 비어 있음)
- 트러블 슈팅 문구 미제공
- 동일 `<!-- Project NN -->` 주석이 이미 존재 (중복 번호)

## 보고 형식

삽입 완료 후 정확히 이 형태로만 답한다. 부가 설명·다음 단계 제안·diff 재출력 금지:

```
Project {{NN}} 카드를 #portfolio 섹션 끝에 추가했습니다.
- 이미지: ./{{IMG_PATH}}
- 활성 링크: {{N}}개 ({{GitHub/기획서/사이트/프로토 타입 중 실제 렌더된 것 나열}})
```
