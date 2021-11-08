# Git

Free, and open-source distributed version control system (VCS)
https://git-scm.com/

WARNING
1. Never init on ~ Directory
2. Repo in repo

## 3 spaces

Working Directory
Staging Area
Commits

----

- git: 분산형 버전 관리 프로그램!
  버전 관리:
  코드의 history를 기록해주고 비교해주고 복구할 수도 있게
  (캡처)
  분산형: (vs. 중앙집중형)
  모든 작업자가 변동내역을 들게 된다 (매 버전을 들고 있는 것이 아님)
  isnot github (저장소)



repository 버전 저장소
: 전체 작업공간 중에서 .git
commit message: 버전 변동사항의 기록 (사진)
commit (verb) 

git의 흐름
Working dir: 작업

git add: 무엇을 커밋할 것인가 결정 (staging area에 누가 올라갈 것인가)
staging area: add된 요소들이
git commit: 기록 (캡처)
push: 원격 저장소에 commit된 사항을 게시

git이 wd의 모든 파일들에게 부여하는 상태

1. Tracked: 기록될 파일들, git의 관리 대상이 된 파일들
   A. unmodified - 안 바뀐 파일들
   B. modified - 수정된 파일들
   C. staged - 현재 staging area에 올라온 파일들
2. Untracked: 너네 누구니? - 기록되지 않는 파일들

vi text.txt
i 편집
esc 기본 모드로 나가기
:wq 나가기



## git status
https://git-scm.com/docs/git-status

```
$ git status
```
-s --short
: 짧은 설명

## git log

## git remote add \<name> \<url>


## git push \<name> \<branch>
https://git-scm.com/docs/git-push

## git clone \<url>

## git pull \<> \<>



# Appendix

git commit -m --date

