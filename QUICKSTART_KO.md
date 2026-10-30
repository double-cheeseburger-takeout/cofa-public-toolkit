# 공개 저장소 준비와 시험 중 사용

## 1. 시험 전에 GitHub에 올리기

1. 이 ZIP을 개인 PC에서 압축 해제합니다.
2. GitHub에 로그인하고 새 저장소를 만듭니다. 이름 예: cofa-public-toolkit.
3. 공개 범위를 **Public**으로 선택합니다. Public은 로그인하지 않은 사람도 읽을 수 있다는 뜻입니다.
4. 저장소의 Add file → Upload files에서 압축을 푼 **cofa-public-toolkit 폴더 안의 파일과 하위 폴더**를 올립니다. 빈 저장소에서는 uploading an existing file 링크가 보일 수 있습니다.
5. Commit changes로 저장합니다. Commit은 파일의 현재 상태를 변경 이력으로 남기는 작업입니다.
6. 저장소 첫 화면에서 README.md, AGENTS.md, skills/, scripts/가 바로 보이는지 확인합니다.
7. 시험 전에 로그아웃한 창에서 같은 저장소 주소가 열리는지 확인합니다.

ZIP 파일 하나만 업로드해도 공개 파일은 되지만, clone 후 추가 압축 해제가 필요합니다. 여기서는 파일을 풀어 올리는 방법을 권합니다. .gitignore가 파일 선택에서 보이지 않으면 숨김 파일 표시를 켜고 포함합니다. 제공 ZIP에는 .git 폴더가 없습니다.

README·LICENSE를 자동 생성하는 선택지는 비워두어도 됩니다. 이 묶음에 이미 파일이 들어 있습니다. 테스트 데이터는 examples/의 합성 예제이며 실제 시험 데이터가 아닙니다.

## 2. 시험 환경에서 가져오기

Git Clone은 공개 저장소의 파일을 현재 환경으로 복제하는 명령입니다. 사용자명 YOUR_ID를 실제 계정명으로 바꿉니다. 아래 주소는 예시입니다.

~~~bash
git clone --depth 1 https://github.com/YOUR_ID/cofa-public-toolkit.git _reference/cofa-public-toolkit
~~~

--depth 1은 현재 버전 중심으로 가져와 과거 변경 기록 다운로드를 줄이는 선택지입니다. 없어도 clone은 가능합니다. 목적 폴더가 이미 있으면 덮어쓰지 말고 먼저 내용을 확인합니다.

제공 환경에서 경로·명령이 달라질 수 있으므로 플랫폼 Codex에게 다음과 같이 요청하는 것이 기본입니다.

~~~text
다음 공개 저장소를 기존 과제 파일과 겹치지 않는 허용된 작업 폴더로 가져와 주세요.
https://github.com/YOUR_ID/cofa-public-toolkit

가져온 폴더의 AGENTS.md와 skills/task-plan/SKILL.md를 읽어 주세요.
과제 README와 운영 규칙을 우선하고, 필요한 문서만 단계별로 읽어 주세요.
내 과제의 목표·필수 조건·검증 계획을 정리한 뒤 구현을 진행해 주세요.
~~~

시험 중 외부 브라우저에서 GitHub를 직접 열어 작업하는 절차를 뜻하지 않습니다. 제공 환경 내 AI와 허용된 터미널 경로를 사용합니다. 차단되면 우회하지 않고 환경 내 도움말·문의 절차를 이용합니다.

## 3. 자동 적용을 기다리지 않기

별도 폴더에 clone한 AGENTS.md는 현재 과제 전체에 자동 적용된다고 보장할 수 없습니다. 기존 과제 AGENTS.md를 덮어쓰지 말고 **파일 경로를 지정해 읽게** 하세요.

skills/ 폴더도 자동 설치용 위치로 가정하지 않습니다. 필요한 SKILL.md를 직접 읽히면 됩니다. 최신 Codex 문서의 자동 검색 경로와 시험에 제공된 버전이 다를 수 있습니다. Skill을 쓰기 위해 Codex를 업데이트하거나 전역 설정을 변경하지 않습니다.

## 4. 필요한 단계만 선택하기

| 상황 | 읽을 파일 |
|---|---|
| 시작·요구 정리 | skills/task-plan/SKILL.md |
| 코드와 결과 확인 | skills/verify-result/SKILL.md |
| 다른 관점에서 검토 | skills/review-changes/SKILL.md |
| 세션 전환·맥락 정리 | skills/handoff-task/SKILL.md |
| 구현 이유 설명 연습 | skills/explain-work/SKILL.md |
| 제출 전 최종 확인 | skills/prepare-submission/SKILL.md |

설명 연습은 AI 사용이 허용된 과제 수행 중에 합니다. 후속 서술형이 시작된 뒤에는 그 단계의 AI·복사·붙여넣기 규칙을 따릅니다.

## 5. 작업 기록을 어디에 둘까요?

templates/는 빈 양식입니다. 실제 과제의 판단·데이터·결과는 시험 작업 폴더 안의 별도 메모에 작성합니다. 기본은 WORKLOG.md 한 개면 충분합니다. 필요할 때만 테스트 보고서나 인수인계 문서로 나눕니다.

실제 시험 기록을 공개 저장소에 올리지 않습니다. Git Push는 저장소로 변경을 전송하는 동작이며, 공개 자료를 가져오는 Clone과 다릅니다.

## 6. 시험 전 10분 연습

- README와 AGENTS를 읽고 필요한 문서를 찾습니다.
- scripts/README.md의 합성 CSV 예제를 한 번 실행합니다.
- 도구의 출력이 무엇을 의미하는지 확인합니다. 도구는 채점 점수를 예측하지 않습니다.
- 제출 체크의 required 파일 목록을 실제 과제에서 채워야 함을 이해합니다.
- 공개 저장소 주소와 파일 구조를 알아둡니다.

이 툴킷의 테스트를 시험 시간에 전부 실행할 필요는 없습니다. 시험에서 필요한 실제 과제의 동작 확인을 우선합니다.

## 외부자료 보완 목록

[외부자료 안내](external-resources/README.md)에서 과제에 필요한 자료만 고릅니다. 공개 저장소에 이 폴더를 함께 올리면 시험 환경에서 같은 방식으로 가져와 읽을 수 있습니다. 외부 라이브러리의 전체 소스를 모두 Clone할 필요는 없습니다.
