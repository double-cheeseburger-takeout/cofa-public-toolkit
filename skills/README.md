# 필요한 Skill만 읽기

Skill은 특정 작업의 진행 절차를 담은 문서입니다. 이 폴더는 공개 배포용 원본이며 개인 계정에 설치된 상태가 아닙니다.

| Skill | 목적 | 기본 호출 방법 |
|---|---|---|
| [task-plan](task-plan/SKILL.md) | 요구·범위·검증 계획 | 과제 시작에 해당 파일 읽기 |
| [verify-result](verify-result/SKILL.md) | 실제 결과와 오류 검증 | 기능을 만들거나 바꾼 뒤 읽기 |
| [review-changes](review-changes/SKILL.md) | 독립적인 코드·요구 검토 | 리뷰할 변경 범위와 함께 읽기 |
| [handoff-task](handoff-task/SKILL.md) | 맥락·판단·남은 일 정리 | 세션 전환·재개 시 읽기 |
| [explain-work](explain-work/SKILL.md) | 본인 구현 설명 연습 | AI 허용 과제 시간 안에 읽기 |
| [prepare-submission](prepare-submission/SKILL.md) | 제출 요구·실행·문서 확인 | 제출 전 읽기 |

예: “가져온 툴킷의 skills/verify-result/SKILL.md를 읽고, 지금 만든 CSV 집계의 정확성과 중요한 예외를 확인해 주세요.”

자동 검색 위치나 호출 문법은 제공 Codex 버전에 따라 다를 수 있습니다. 여기서는 파일 경로를 명시하는 방법을 기본으로 합니다. agents/openai.yaml은 지원 도구가 표시할 이름과 설명을 담은 선택 메타데이터입니다. 이를 쓰기 위한 업데이트나 전역 설정 변경은 필요하지 않습니다.

각 Skill은 스스로 읽을 수 있도록 작성했습니다. 루트 README의 추가 양식·도구는 필요할 때만 사용합니다.
