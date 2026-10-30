# 외부자료 전체 목록

확인일: 2026-10-31 (한국 시간). 총 25종. 우선순위는 이번 준비를 위한 추천 판단입니다.

## 01. Superpowers 선택 문서

**선택 시점:** 오류가 반복되거나 완료를 검증할 때 / **분류:** 우선

오류 메시지와 재현 조건으로 원인을 좁히고, 수정 뒤 실제 실행 결과로 성공을 확인하도록 AI 작업을 정리합니다.

**추천 적용:** 전체 프레임워크를 켜기보다 아래 두 문서를 필요할 때 읽게 하세요. 기존 준비 ZIP의 verify-result·debugging과 겹치므로 둘을 동시에 길게 적용할 필요는 없습니다.

**읽을 부분:** skills/systematic-debugging/SKILL.md / skills/verification-before-completion/SKILL.md

**조건:** 제공 Codex의 버전을 바꾸지 않고 읽기 자료로 활용합니다. 최신 README의 플러그인 설치 절차를 Cofa에서도 지원한다고 단정할 수 없습니다. 저장소의 모든 지시보다 대회 규칙과 실제 과제 조건을 우선합니다.

**함께 볼 파일:** verification-before-completion은 독립 문서입니다. systematic-debugging은 깊은 호출 원인 추적 시 같은 폴더의 root-cause-tracing.md를 참조하고, 관련 TDD/검증 Skill도 언급합니다. 소스 복사 시 해당 폴더와 LICENSE를 보존하면 상대 경로가 유지됩니다. 무조건 전체 Skill 설치가 필요한 것은 아닙니다.

**원문 사용 조건 확인:** MIT; LICENSE 실제 확인

- [공식 원문 1](https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md)
- [공식 원문 2](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md)

확인 범위: 공개 원문 열람; Cofa 설치·실행 검증은 하지 않음

## 02. Vercel Web Interface Guidelines

**선택 시점:** 입력·결과·오류 화면을 점검할 때 / **분류:** 웹 과제 우선

입력란, 버튼, 오류 안내, 빈 결과, 긴 글, 키보드 조작 등 실제 사용 중 발생하는 화면 문제를 점검합니다.

**추천 적용:** 웹 화면을 만든 뒤 사용 흐름을 방해하는 문제부터 점검하는 데 쓰세요. 시각적 장식보다 기능과 안내의 누락을 먼저 잡는 자료로 추천합니다.

**읽을 부분:** command.md / LICENSE

**조건:** 코드를 읽어 점검하는 방식은 브라우저 자동 조작이 필요 없습니다. 실제 화면은 응시자가 내부 Browser에서 직접 확인합니다. 모든 스타일 규칙을 억지로 맞추기보다 과제와 사용자 흐름에 관련된 항목을 고릅니다.

**함께 볼 파일:** vercel-labs/agent-skills의 skills/web-design-guidelines/SKILL.md는 실제 규칙을 포함하지 않고 위 저장소 command.md를 가져오라고 지시합니다. 따라서 command.md 자체가 핵심 자료입니다.

**원문 사용 조건 확인:** MIT; web-interface-guidelines/LICENSE 실제 확인. agent-skills 전체 저장소의 일괄 라이선스라고 확장해서 말하지 않습니다.

- [공식 원문 1](https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md)

확인 범위: 공개 원문 열람; Cofa 설치·실행 검증은 하지 않음

## 03. Vercel React Best Practices

**선택 시점:** 제공 앱이 React 또는 Next.js일 때 / **분류:** 조건부

React/Next.js에서 불필요한 요청 대기, 반복 렌더링, 과도한 코드 로딩 등 성능 문제를 피하는 지침입니다.

**추천 적용:** SKILL.md의 항목 목록을 보고 현재 코드와 관련된 rules 문서만 읽으세요. 단순 Python/데이터 분석 과제에는 필요 없습니다.

**읽을 부분:** skills/react-best-practices/SKILL.md / skills/react-best-practices/rules/async-parallel.md / skills/react-best-practices/rules/bundle-dynamic-imports.md / skills/react-best-practices/rules/rerender-derived-state-no-effect.md

**조건:** 프로젝트에 설치된 React/Next.js 버전에 맞는 규칙만 적용합니다. 최적화를 위해 기술 구성을 바꾸거나 Vercel에 배포할 필요가 없습니다. 같은 저장소의 deploy-to-vercel 기능과는 구분합니다.

**함께 볼 파일:** 자세한 예시는 같은 Skill 폴더의 rules/*.md에 있습니다. 모든 규칙을 펼친 AGENTS.md도 있지만 처음부터 통째로 읽힐 필요는 없습니다.

**원문 사용 조건 확인:** 해당 SKILL.md의 frontmatter에 MIT 명시. 현재 agent-skills GitHub 트리에서 별도 LICENSE 파일은 찾지 못했으므로 이번 전달물에는 원문 재배포 대신 링크와 활용 설명을 담는 편이 명확합니다.

- [공식 원문 1](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md)
- [공식 원문 2](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices/rules)

확인 범위: 공개 원문 열람; Cofa 설치·실행 검증은 하지 않음

## 04. Anthropic Frontend Design

**선택 시점:** 필수 기능 완성 후 배치와 문구를 다듬을 때 / **분류:** 선택

사용자와 과제의 성격에 맞는 배치·글꼴·색상·문구를 정해 화면을 다듬는 자료입니다.

**추천 적용:** 업무용 대시보드라면 읽기 쉬운 수치, 일관된 버튼 이름, 설명 가능한 빈 상태를 중심으로 참고하세요. 독특한 디자인 자체가 이번 대회의 가점이라는 근거는 없습니다.

**읽을 부분:** skills/frontend-design/SKILL.md / skills/frontend-design/LICENSE.txt

**조건:** Claude용 설치 명령을 Codex에 그대로 적용하지 않습니다. 문서의 스크린샷 검토 제안은 Cofa의 Computer Use 금지 규정에 맞춰 제외하고 응시자가 직접 화면을 확인합니다. 기능 완성 시간을 침해할 정도로 장식 작업을 늘리지 않습니다.

**함께 볼 파일:** 핵심 지침은 SKILL.md에 있습니다. 고유한 Claude 서비스 사용이나 API 호출이 필수인 문서가 아닙니다. 이미지·글꼴·기타 자산을 추가하면 각각의 사용 조건을 확인해야 합니다.

**원문 사용 조건 확인:** Apache License 2.0; 해당 Skill의 LICENSE.txt 실제 확인

- [공식 원문 1](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)

확인 범위: 공개 원문 열람; Cofa 설치·실행 검증은 하지 않음

## 05. OpenAI Plugins 데이터 점검 지침

**선택 시점:** 데이터 품질·분석 결과 검토가 필요할 때 / **분류:** 조건부

Codex 플러그인 구조와 여러 업무 지침을 확인할 수 있는 공식 예시 저장소입니다. 데이터 과제에는 analyze-data-quality와 validate-data가 참고가 됩니다.

**추천 적용:** 데이터 품질과 분석 검증의 체크 항목만 읽는 용도로 권합니다. 외부 데이터 연결, 보고서 게시, 전체 플러그인 설치를 이번 시험의 기본 준비로 삼지는 마세요.

**읽을 부분:** plugins/data-analytics/skills/analyze-data-quality/SKILL.md / plugins/data-analytics/skills/validate-data/SKILL.md

**조건:** 현재 Cofa의 고정 Codex 버전에서 최신 플러그인 지원 여부는 확인되지 않았습니다. 분석 자료는 시험 작업 환경 안에서 처리하고 외부 문서/클라우드 보고서로 게시하지 않습니다.

**함께 볼 파일:** 문서에서 다른 Skills, 데이터/로그 연결 도구, build-report를 참조합니다. 검사 원칙만 참고하면 이러한 도구 전체를 설치할 필요는 없습니다.

**원문 사용 조건 확인:** 플러그인별 확인 필요. 저장소 API의 대표 license는 null이며, data-analytics 아래의 별도 LICENSE는 트리에서 발견하지 못했습니다. 공개 원문 열람 링크를 제공하며 자료 전체를 재배포하지 않습니다.

- [공식 원문 1](https://github.com/openai/plugins/blob/main/README.md)
- [공식 원문 2](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/analyze-data-quality/SKILL.md)
- [공식 원문 3](https://github.com/openai/plugins/blob/main/plugins/data-analytics/skills/validate-data/SKILL.md)

확인 범위: 공개 원문 열람; Cofa 설치·실행 검증은 하지 않음

## 06. pandas | CSV·엑셀 분석

**선택 시점:** 표 데이터 과제 / **분류:** A

CSV나 엑셀 파일을 읽고, 필요한 행을 고르고, 묶어서 합계·평균을 계산하고 표끼리 연결합니다.

**추천 적용:** 설치된 pandas를 우선 사용합니다. merge 후 행 수·키 중복·합계가 예상대로인지 점검하세요. 전체 pandas 소스 저장소를 복제할 필요는 없습니다.

**읽을 부분:** How do I read and write tabular data? / Merge, join, concatenate and compare: validate / indicator

**조건:** 엑셀 읽기는 파일 형식별 추가 의존성이 필요할 수 있습니다. 최신 문서의 기능이 시험 버전에 모두 있는지는 확인해야 합니다.

**입력과 결과:** CSV/엑셀 → 메모리의 표(DataFrame) → 검증·집계 → 결과 CSV/표

- [공식 원문 1](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)
- [공식 원문 2](https://pandas.pydata.org/docs/user_guide/merging.html)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 07. pytest | 실제 결과 검사

**선택 시점:** Python 과제 / **분류:** A

예상한 답과 프로그램이 낸 답을 비교하고 성공·실패를 기록합니다.

**추천 적용:** 문제에 직접 연결되는 정상 입력, 경계값, 잘못된 입력부터 확인합니다. 이미 제공된 테스트를 먼저 실행하세요.

**읽을 부분:** Get Started: Create your first test / How to parametrize fixtures and test functions

**조건:** 테스트 수가 많다는 이유만으로 결과가 옳아지는 것은 아닙니다. 실제 요구사항에서 예상값을 정해야 합니다.

**입력과 결과:** 입력 사례+예상값 → 함수 실행 → 통과/실패 및 오류 위치

- [공식 원문 1](https://docs.pytest.org/en/stable/getting-started.html)
- [공식 원문 2](https://docs.pytest.org/en/stable/how-to/parametrize.html)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 08. scikit-learn | 예측 모델 검증

**선택 시점:** 표 데이터 예측/분류 과제 / **분류:** A

전처리와 모델 학습을 일관되게 묶고, 평가 데이터가 학습에 섞여 성능이 부풀려지는 실수를 막습니다.

**추천 적용:** 데이터 누출은 정답을 예측할 때 알 수 없는 정보를 학습 때 쓰는 것입니다. 전처리 기준은 학습 데이터로만 정하고 Pipeline(전처리와 모델을 묶은 절차)을 검토하세요.

**읽을 부분:** Common pitfalls: Inconsistent preprocessing / Common pitfalls: Data leakage / How to avoid data leakage

**조건:** 이 문서 자체가 특정 대회 평가지표나 정답 모델을 정해 주지는 않습니다. 시계열·같은 대상의 반복 측정은 과제에 맞는 분리 방식이 필요합니다.

**입력과 결과:** 학습 데이터 → 전처리 기준 학습+모델 학습 → 분리된 평가 데이터에 적용 → 성능 계산

- [공식 원문 1](https://scikit-learn.org/stable/common_pitfalls.html)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 09. FastAPI | 요청을 받아 결과 반환

**선택 시점:** 제공 프로젝트가 FastAPI이거나 API 과제 / **분류:** A

웹 화면이나 다른 프로그램이 보낸 요청을 받고 계산 결과를 반환하는 서버를 만듭니다. API는 프로그램끼리 요청과 결과를 주고받는 접점입니다.

**추천 적용:** 기존 프로젝트의 구조와 버전을 유지하면서 필요한 경로와 입력 검사를 추가합니다. TestClient는 브라우저 조작 없이 응답 코드와 내용을 검사합니다.

**읽을 부분:** First Steps: Path / Operation / Testing: Using TestClient

**조건:** 문서의 클라우드 배포 절차는 시험 작업에 적용할 필요가 없습니다. 기존 프레임워크를 바꾸기 위해 새로 도입하지 마세요.

**입력과 결과:** 요청 경로+입력 데이터 → Python 처리 함수 → 응답 데이터

- [공식 원문 1](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [공식 원문 2](https://fastapi.tiangolo.com/tutorial/testing/)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 10. React | 화면 구성·입력 상태

**선택 시점:** 제공 프로젝트가 React일 때 / **분류:** A

검색창·표·버튼을 나눠 만들고 사용자가 입력했을 때 화면이 어떻게 바뀌는지 설계합니다.

**추천 적용:** 검색 가능한 상품 표 예제가 데이터 화면 과제에 유용합니다. 화면 상태(state)는 입력값·선택값처럼 시간에 따라 변하는 값입니다.

**읽을 부분:** Thinking in React: component hierarchy / Thinking in React: static version / minimal state / data flow

**조건:** React가 없는 과제에 학습 목적으로 새 도입하면 준비 시간이 늘어납니다. 제공 환경의 화면 기술을 우선합니다.

**입력과 결과:** 원본 데이터+사용자 입력 상태 → 화면 구성요소 → 필터링된 결과 화면

- [공식 원문 1](https://react.dev/learn/thinking-in-react)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 11. MDN Fetch | 화면과 서버 연결

**선택 시점:** 웹 화면이 서버를 호출할 때 / **분류:** B

버튼 클릭 때 서버로 데이터를 보내고 받은 결과를 화면에 표시하는 방법을 확인합니다.

**추천 적용:** fetch는 서버가 404 같은 오류 응답을 보내도 항상 예외가 나지는 않으므로 response.ok 등을 검사해야 합니다.

**읽을 부분:** Using the Fetch API: Making a request / Checking response status / Reading the response body

**조건:** 예제의 외부 주소로 과제 데이터를 보내지 않습니다. 기존 프로젝트의 서버 주소·경로에 맞춰 적용합니다.

**입력과 결과:** 화면의 입력 → HTTP 요청 → 응답 상태 확인 → 응답 데이터 읽기

- [공식 원문 1](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 12. Vite | 웹 개발 서버 주소·포트

**선택 시점:** Vite 프로젝트가 Browser에서 안 열릴 때 / **분류:** B

만든 웹 화면을 개발 서버로 띄우고 연결 주소·포트를 설정합니다.

**추천 적용:** server.host 또는 --host 0.0.0.0의 의미와 설정 방법을 확인할 때 유용합니다. 실제 시작 로그의 포트를 확인합니다.

**읽을 부분:** Server Options: server.host / Server Options: server.port / server.strictPort

**조건:** 문서의 최신 버전에 맞추려고 Node나 제공 도구를 무조건 업데이트하지 않습니다. hosted sandbox·외부 배포 예제는 이 목적에 필요하지 않습니다.

**입력과 결과:** 웹 소스 → 개발 서버 → 플랫폼 Browser에서 접속

- [공식 원문 1](https://vite.dev/config/server-options)
- [공식 원문 2](https://vite.dev/guide/)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 13. Streamlit | Python 분석 화면

**선택 시점:** 새 분석 화면이 필요하고 기술 선택이 자유로울 때 / **분류:** B

Python 코드로 표·그래프·입력창을 붙여 분석 결과를 확인하는 웹 화면을 만듭니다.

**추천 적용:** CSV 분석 대시보드 같은 간단한 과제의 후보입니다. 기본적으로 입력이 바뀌면 스크립트를 다시 실행하므로 중복 계산·상태 처리를 이해해야 합니다.

**읽을 부분:** Basic concepts: Run a local server / Data flow / Display and style data

**조건:** 제공된 React/다른 앱을 갈아엎는 용도로 권하지 않습니다. 실제 환경에서 설치·연결 가능 여부를 확인해야 합니다.

**입력과 결과:** Python 분석 결과+사용자 입력 → 표/그래프/입력 위젯

- [공식 원문 1](https://docs.streamlit.io/get-started/fundamentals/main-concepts)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 14. Pydantic | 입력값 형식·범위 검사

**선택 시점:** 구조화된 입력 검사가 필요할 때 / **분류:** B

필수 항목, 숫자·문자 유형, 값의 범위 같은 입력 규칙을 선언하고 잘못된 데이터를 찾아냅니다.

**추천 적용:** FastAPI와 함께 쓰거나 입력 구조가 복잡할 때 유용합니다. 숫자처럼 보이는 문자열을 숫자로 바꾸는 자동 변환이 요구사항에 맞는지도 확인합니다.

**읽을 부분:** Models: Basic model usage / Data conversion / Error handling

**조건:** 버전1/2 코드 차이가 있으므로 설치 버전에 맞는 문서를 선택합니다. 모델을 정의하는 것만으로 업무 규칙 전체가 검증되지는 않습니다.

**입력과 결과:** 사전/JSON 입력 → 규칙에 따라 변환·검사 → 정해진 구조의 값 또는 오류

- [공식 원문 1](https://docs.pydantic.dev/latest/concepts/models/)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 15. DuckDB | CSV를 SQL로 집계

**선택 시점:** SQL이 편하거나 여러 표를 집계할 때 / **분류:** B

CSV 파일을 데이터베이스처럼 읽어 조건 검색·집계·표 결합을 합니다. SQL은 표에서 원하는 데이터를 고르는 질의 언어입니다.

**추천 적용:** pandas로 충분하면 추가하지 않습니다. 구분자·자료형 자동 추정 결과를 실제 파일과 비교합니다.

**읽을 부분:** CSV Import: read_csv / Explicit CSV options / Multiple files

**조건:** 문서 stable 주소가 버전 문서로 이동합니다. 시험 환경의 설치 버전에 맞는 기능을 씁니다.

**입력과 결과:** 로컬 CSV → SQL 질의 → 집계 결과 표

- [공식 원문 1](https://duckdb.org/docs/stable/data/csv/overview)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 16. Matplotlib | 근거가 되는 그래프

**선택 시점:** 분석 결과·성능을 그래프로 제출할 때 / **분류:** B

날짜별 추세, 집단 비교, 예측값과 실제값 차이를 그래프로 만듭니다.

**추천 적용:** 장식보다 무엇을 비교하는지, 축 단위와 기준이 무엇인지 보여 주는 데 씁니다.

**읽을 부분:** Quick start guide: simple example / Parts of a Figure / Coding styles

**조건:** 한글 글꼴과 저장 경로는 환경에서 확인해야 합니다. 그림만으로 계산 정확성을 입증하지는 못합니다.

**입력과 결과:** 계산된 수치 → 축·제목·단위가 있는 그림 → 파일 저장/앱 표시

- [공식 원문 1](https://matplotlib.org/stable/users/explain/quick_start.html)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 17. Ruff | Python 코드의 흔한 실수 검사

**선택 시점:** 이미 있거나 짧게 추가 가능한 보조 검사 / **분류:** C

쓰지 않는 import나 일부 코드 오류·규칙 위반을 정적으로 찾아줍니다. 정적 검사는 프로그램을 실제 업무 입력으로 실행하지 않고 소스를 살피는 검사입니다.

**추천 적용:** 이미 프로젝트에 설정되어 있으면 기존 설정을 유지합니다. 결과 확인부터 하고 필요한 수정만 반영합니다.

**읽을 부분:** Tutorial: ruff check / Rule Selection / Configuration

**조건:** 동작 정확성 테스트를 대신하지 않습니다. 시험 말미에 전체 코드 자동 포맷·대규모 자동 수정을 하느라 시간을 쓰지 마세요.

**입력과 결과:** Python 소스 → 규칙 검사 → 파일·위치·문제 목록

- [공식 원문 1](https://docs.astral.sh/ruff/tutorial/)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 18. pdfplumber | PDF 표·텍스트 추출

**선택 시점:** 제공 PDF에서 표를 뽑아야 할 때 / **분류:** B

PDF 안의 문자와 표 구조를 읽어 Python에서 처리할 수 있는 텍스트·행·열 형태로 꺼냅니다.

**추천 적용:** 표가 여러 개인 경우 페이지·표 선택과 합쳐진 셀 결과를 원본과 대조합니다. 과제 자료를 외부 PDF 변환 서비스에 올릴 필요가 없습니다.

**읽을 부분:** README: Extracting text / README: Extracting tables / extract_tables

**조건:** 프로젝트는 스캔 PDF보다 프로그램으로 만든 PDF에 적합하다고 명시합니다. 추출 결과가 비어 있으면 자동으로 올바른 데이터가 되는 것은 아닙니다.

**입력과 결과:** 문자 정보가 있는 PDF → 페이지별 텍스트/표 → 검증 후 분석 입력

- [공식 원문 1](https://github.com/jsvine/pdfplumber)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 19. pypdf | PDF 텍스트 읽기

**선택 시점:** 단순 텍스트 추출 또는 이미 설치된 대안 / **분류:** C

PDF의 페이지를 읽고 텍스트를 꺼냅니다.

**추천 적용:** 텍스트만 필요하고 이미 설치되어 있으면 pdfplumber를 추가하는 대신 사용할 수 있습니다.

**읽을 부분:** Extract Text from a PDF: PdfReader / extract_text / Image-only/scanned document limitations

**조건:** 그림으로만 된 스캔 PDF는 텍스트가 비거나 적게 나올 수 있습니다. OCR은 이미지 속 글자를 문자로 읽는 별도 작업이며 이 문서 추출만으로 해결되지 않습니다.

**입력과 결과:** PDF 파일 → 페이지 → 추출된 텍스트

- [공식 원문 1](https://pypdf.readthedocs.io/en/stable/user/extract-text.html)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 20. Python sqlite3 | 간단한 로컬 데이터 저장

**선택 시점:** 저장·조회 기능이 필요할 때 / **분류:** B

항목을 파일 기반 데이터베이스에 저장하고 다시 조회합니다. 별도 데이터베이스 서버 없이 작은 앱의 상태를 보관하는 후보입니다.

**추천 적용:** 제공 프로젝트에 데이터베이스가 있으면 그것을 유지합니다. 값은 문자열로 SQL에 이어 붙이지 말고 문서의 placeholder 방식을 참고합니다.

**읽을 부분:** sqlite3: Tutorial / How to use placeholders to bind values in SQL queries

**조건:** 시험 Python에서 sqlite3 사용 가능 여부와 과제의 저장 방식 조건을 확인합니다. 다중 사용자 규모 등 과제 밖 요구를 미리 확장하지 않습니다.

**입력과 결과:** 입력 레코드 → SQLite 파일 → 조건에 맞는 레코드 조회

- [공식 원문 1](https://docs.python.org/3/library/sqlite3.html)

확인 범위: 공식 문서 본문 열람; Cofa 설치·실행 검증은 하지 않음

## 21. Context7

**선택 시점:** 허용된 연결이 이미 있고, 개발 문서 조회가 병목일 때 / **분류:** 조건부

AI가 라이브러리의 버전에 맞는 개발 문서와 예제를 찾아 읽도록 연결하는 도구입니다.

**추천 적용:** 연결이 없으면 제공 AI로 공식 문서를 읽는 방법부터 사용합니다. 이미 연결돼 있다면 일반적인 라이브러리명·버전·기능만 질문합니다.

**읽을 부분:** README.md / docs/clients/codex.mdx / packages/mcp/README.md

**조건:** 로컬 MCP여도 문서 조회 요청은 외부 서비스로 전달됩니다. 문제·제공 데이터·코드·로그를 보내지 않습니다. 현재 setup은 OAuth 로그인과 설정 파일 변경을 포함하므로 시험에서 일괄 실행하지 않습니다.

**원문 사용 조건 확인:** MIT. 서비스 이용 조건과 시험 허용 범위는 별도 확인.

- [공식 원문 1](https://github.com/upstash/context7)
- [공식 원문 2](https://github.com/upstash/context7/blob/master/docs/clients/codex.mdx)
- [공식 원문 3](https://github.com/upstash/context7/blob/master/packages/mcp/README.md)

확인 범위: 공식 README·Codex 연결 문서 열람; 시험 연결은 검증하지 않음

## 22. Work Practice Lab

**선택 시점:** 본시험 전, 지원되는 개인 환경에서 연습할 시간이 있을 때 / **분류:** 사전 연습만

업무 담당자에게 질문하고 구현·검증·제출·사후 설명까지 연습하는 독립적인 로컬 앱입니다.

**추천 적용:** 새 설치에 시간을 쓰기보다 이미 실행 가능한 지원 환경일 때 연습에 활용합니다. 시험 환경 안에서 실행할 도구로 추천하지 않습니다.

**읽을 부분:** README.md의 설치 조건·평가의 의미 / docs/INSTALL.md

**조건:** README는 Node.js 24 이상·개인 Codex 로그인을 요구하고 기본 설치의 네이티브 Windows 미지원, Linux 전체 흐름 미검증을 명시합니다. 자체 점수는 공식 Cofa 점수 예측치가 아닙니다.

**원문 사용 조건 확인:** 확인 시 GitHub API license:null, 루트 LICENSE 파일 미발견. 이번 묶음에는 원문 코드 대신 링크만 포함.

- [공식 원문 1](https://github.com/JakeB-5/work-practice-lab)
- [공식 원문 2](https://github.com/JakeB-5/work-practice-lab/blob/main/docs/INSTALL.md)

확인 범위: 공식 GitHub API와 raw README/설치 문서 HTTP 200 확인; 설치·실행은 하지 않음

## 23. Cofa Probe 공식 평가 설명

**선택 시점:** 무엇을 잘 보여 줘야 하는지 확인할 때 / **분류:** 사전 읽기 우선

결과물과 함께 AI 대화·작업 기록·검증·사후 설명을 살펴보는 평가 방향을 확인합니다.

**추천 적용:** 자료를 선택한 이유, 적용 결과, 실제 확인한 사실을 과제 수행 중 짧게 남기는 기준으로 삼습니다.

**읽을 부분:** 평가 진행 방식 / 평가 리포트 / 자주 묻는 질문

**조건:** 공개 제품 소개와 예시 리포트는 이번 SK하이닉스 시험의 세부 배점 확정 공지가 아닙니다.

- [공식 원문 1](https://www.getcofa.com/ko/probe)

확인 범위: 공식 페이지 본문 열람

## 24. Cofa 제작진 인터뷰

**선택 시점:** 문제 정의·AI 통제·설명 역량의 의미를 이해할 때 / **분류:** 사전 읽기

제품 책임자와 엔지니어가 실제 업무 요구 파악, 과도한 구현의 조절, 결과물 설명을 어떻게 보는지 설명합니다.

**추천 적용:** 적절한 질문과 검증을 통해 요구사항을 좁히고, 내가 고른 해결책의 이유를 이해하는 연습에 씁니다.

**읽을 부분:** 결과물, AI를 이끈 방식, 그리고 설명할 수 있는가 / 가방에서 자기 장비를 꺼내는 사람들

**조건:** 인터뷰의 사례와 의견을 이번 시험의 확정 문제·점수 공식으로 바꾸어 해석하지 않습니다.

- [공식 원문 1](https://maily.so/josh/posts/x1zg69d3rqg)

확인 범위: 제작진 인터뷰 원문 열람

## 25. Cofathon Top 6 참가 후기

**선택 시점:** 실제 참가자의 준비·작업·회고 흐름을 보고 싶을 때 / **분류:** 사전 읽기 보조

과거 FDE 트랙 참가자가 준비와 구현 과정, 관찰한 평가와 아쉬운 점을 설명한 직접 경험담입니다.

**추천 적용:** 요구사항을 파악하고 작업 맥락을 유지하며 결과를 설명하는 행동을 참고합니다.

**읽을 부분:** 준비 기간 / 본선 과정과 회고 / 평가에 대한 관찰

**조건:** 과거 별도 행사이며 시간·모델·문항·허용 도구가 이번 시험과 다를 수 있습니다. 개인 경험담은 공식 운영 공지가 아닙니다.

- [공식 원문 1](https://brunch.co.kr/@luma/5)

확인 범위: 참가자 직접 작성 후기 본문 열람
