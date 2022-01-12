Git Flow



협업 속의 Git

​	협업 Workflow

​	커밋 컨벤션

​	배포 자동화

​	코드 리뷰



Repository

​	Local

​		wd

​		staging area

​		localrepo

​	Remote



Git Cheatsheet



Git Branch



Git Flow

(Feature) Develop (Bugfix) Release (Hotfix) Master

->> Stable & Cost

Dev ~ User 

Dev: 신규 기능 등 개발자 사용

Release: 출시 준비 중 기획자 QA 등 작업

Master: 고객에게 서비스하는 서버



Trunk Based Git Flow

​	(Feature) > Master > Release

​	Master를 Fresh하게 유지하면서 빠른 배포



----

```
git add readme.md
git commit -m "init"
git branch develop
git switch develop

echo "1. first code edit" > readme.md

git commit -am "C1"

echo "2. second edit" >> readme.md

git commit -am "C2"

echo "3. 3rd feature" >> readme.md

git commit -am "C3"

git checkout HEAD...

git switch -c bugfix/1
echo "1.1 fix" >> readme.md
git commit -am "C1-B1"
// conflict

git add .
git commit -m "merge branch 'develop' into bugfix/1"



git switch -c feat/2
```



git book



learn git branching



----

commit message

- DON'T add name, date in commit msg
  - 불필요한, 중복된 정보
- Get rid of Unused file, backups from git, ... (keep it clean)
- Use gitignore (i.e. 자동 생성되는 파일들)



JIRA

* 상위 테스크, 하위 테스크 구분
* Git ~ JIRA Integration
  * 수동으로 Comment를 추가하거나
  * 자동 연결을 사용



Conflict

* 설계 Lv에서 review할 필요 있음 (역할 분배가 제대로 되어있는지?)



Hotfix

* 빈번한 Hotfix는 signal (프로세스 재검토 필요)

