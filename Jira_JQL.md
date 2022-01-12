# JIRA & JQL

Why JIRA?

​	Agile

​	DevOps

​	SRE

​	Issue-Tracking



Issue Tracking

​	현재 프로젝트에서 어떤 작업/과업들이 어떤 상태에 놓여 있는가, 누구의 손에 있는가

Project Management

​	프로젝트 전체를 관리하는 기능들

​	Analysis, Planning, ...



Agile

​	개발 문화로서의 Agile Manifesto

* 상호작용
* 실제 작동
* 협력
* 변화에 대응



Scrum & Kanban

Scrum: Todo Backlog >> 일부 Scrum >> Backlog >> ...

Kanban: WIP



DevOps

Dev and Ops vs. DevOps

"새로운 기능은 운영의 장애물"?

개발과 운영의 통합: 개발, 테스트, 배포, 이슈 반영, ... 반복되는 개발주기

​	How to DevOps

* 배포 등 반복 작업의 자동화
* 팀 내 공유된 지표 필요
* 이슈의 공유 필요



Atlassian DevOps & JIRA



Site Reliability Engineering: SRE

​	서비스 장애 대응, 신뢰성

​	Google의 Dev/Ops Problem > SRE Concept



# Using JIRA

Create Issue

​	Type: Story / Task / Bug / Epic

* Story: User Story (Scenario)
* Task: Other than Dev (but use freely)
* Bug == Bug
* Epic: Big Picture, Categories

​	Summary: Title of the issue

​	Reporter: 보고자

​	Components: 기능

​	Description: 설명

​	Fix Version/s: 버전

​	Priority: 중요도

​	Labels: 태그

​	Linked Issue: 관련 이슈

​	Assignee: 담당자

​	Epic Link

​	Sprint: Scrum Board에 연결



Components: 기능들

Releases: 버전들



# JQL

JIRA Issue를 구조적으로 검색하기 위한 Query Language

JIRA Fields에 맞는 특수 예약어 제공

Gadget, Agile Board 등 Issue를 재가공해 유의미한 데이터 도출에 활용



### JQL Operators

=, !=, >, >=, in, not in, ~, !~ (not-contains)

is empty, is null, is not empty, ...

### JQL Keywords

AND, OR, NOT, EMPTY, NULL, ...

### JQL Dates

-2w, -1w, -1d, today, 1d, w, 2w, ...

### JQL Functions



```
project = PJ1 and updated > startOfWeek(1d) AND status != done
```

Add Viewers



Star: Favorites

참조 Resolution: Done, Depleted, ...





## Dashboard & Gadget

초기 화면: (System) Dashboard

Gadget: Chart, Table 등

여러 제공 Gadget

​	Filter Results

​	Heat Map

​	Pie Chart

​	...



### Agile Board

Quick Filter, ...



# JIRA in Practical Uses

JIRA Linked w/ GitHub, ...

JIRA Plugins
