# OSI 7계층

컴퓨터들이 네트워크 사이에서 정보를 주고받을 때, 어떤 정보를 어떻게 풀어읽을 것인가 하는 규칙이 없다면 유의미한 통신이 이루어지기 힘들 것입니다.
더군다나 네트워크를 이용하는 시스템들은 물리적으로, 소프트웨어적으로 굉장히 다양한 환경에 처해 있습니다.
예를 들면 리눅스 서버에서 출발한 데이터가 해저 광케이블을 지나, 안드로이드 OS가 설치된 어느 집 셋업박스에 닿을 수도 있습니다.
한편 같은 내용이 들은 데이터가 무선 통신을 통해 10m 남짓 떨어진 윈도우 PC에 설치된 랜카드에 닿을 수도 있겠습니다.

이러한 통신 과정의 난점을 피하기 위해, 컴퓨터는 통신의 여러 단계를 거치며 데이터의 송수신과 관련된 메타데이터를 헤더에 기록하여 하위 통신에 담아 보냅니다.
이렇게 데이터는 여러 단계의 통신을 거치며 여러 개의 헤더를 갖게 되는데요, 이 단계들을 OSI 7계층이라고 부릅니다.

## OSI란

**OSI 모형(Open System interconnection Reference Model)** 이란 이렇게 다양한 개방형 시스템(Open Systems) 간의 상호연결(Interconnection)을 위해 ISO에서 마련한 규칙입니다.

## 7계층

7계층은 가장 물리적인 계층에서, 가장 논리/추상적인 계층까지 숫자가 올라가도록 구성되어 있습니다.
1~3계층을 미디어 계층, 4~7계층을 호스트 계층이라고 나누기도 합니다.

1. Physical 물리 계층
2. Data link 데이터 링크 계층
3. Network 네트워크 계층
4. Transport 전송 계층
5. Session 세션 계층
6. Presentation 표현 계층
7. Application 응용 계층

| 레이어 | 프로토콜 데이터 단위 | 기능 |
| --- |            --- | --- |
| 7 응용 | Data           | 자원 공유, 원격 파일 접근 등의 고수준 API |
| 6 표현 | Data           | 문자열 인코딩, 데이터 압축 및 암호/복호화 같은 네트워크 서비스와 애플리케이션 간 데이터 변환 |
| 5 세션 | Data           | 연결 세션 관리 (연속적 정보 교환) |
| 4 전송 | Segment / Datagram | 네트워크 지점 간 신뢰할만한 데이터 묶음 전송 |
| 3 네트워크 | Packet | 다중 노드 네트워크의 구조화와 관리 (주소 / 라우팅 / 트래픽 관리) |
| 2 데이터 링크 | Frame | 물리 계층으로 연결된 두 노드 간의 데이터 프레임들 |
| 1 물리 | Bit / Symbol | 물리적 매체를 통한 Bit 흐름 등 |

참조: https://en.wikipedia.org/wiki/OSI_model