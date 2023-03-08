# 3. AWS EC2 기초

*AWS*



## EC2 (Elastic Compute Cloud)

> #### 서비스로 인프라를 작업하는 방법



#### EC2는 해당 기능들을 포함하고 있다

- **EC2** : 가상으로 기기를 빌려주는 것
- **EBS (Elastic Block Storage)** : 데이터를 가상 드라이브에 저장하는 것
- **ELB (Elastic Load Balancer)** : 어플리케이션 트래픽을 자동으로 분산해준다
- **ASG (Auto-Scaling Group)** : 사용자 정의 정책, 상태 확인 및 일정에 따라 EC2 인스턴스를 자동으로 시작하거나 종료한다



#### EC2 사이징과 환경 설정 옵션

> 어플리케이션에 적합한 EC2 인스턴스를 선택할 수 있다 / 주문형 클라우드
>
> 즉, AWS에서 한번에 주문형 클라우드, 즉 가상 저장소를 쉽고 빠르게 만들 수 있다

- EC2 인스턴스로 선택할 수 있는 응용 체제는 Linux, Window 또는 Mac OS가 있다
- 가상 컴퓨터의 CPU를 설정할 수 있다
- 가상 컴퓨터의 메모리, RAM을 설정할 수 있다
- 저장 공간을 선택할 수 있다
  - 네트워크와 연결된 저장소 (EBS & EFS)
  - 하드웨어로 연결된 저장소 (EC2 인스턴스 저장)
- 네트워크 카드 : 속도, 공공 IP 주소
- Firewall rules : **Security Group**
- Bootstrap Script (처음 실행할 때 확인) : **EC2 User Data**
  - Bootstrap : 기계가 시작할 때에, 명령을 실행하는 것



### EC2 User Data

- 인스턴스가 시작할 때만 Bootstrap Script가 작동한다
- EC2 User Data는 부팅 테스크 (Boot Task)를 자동화 할 수 있다
  - 업데이트를 다운 받을 수 있다
  - 소프트웨어 다운로드를 받을 수 있다
  - 인터넷에서 명령 파일을 다운로드 받을 수 있다, 등
- EC2 User Data Script는 루트 유저만 작동 할 수 있다



### EC2 인스턴스 종류

<img src="3_AWS_EC2_기초.assets/The-naming-principle-of-AWS-EC2-instance-types-1.png" alt="The-naming-principle-of-AWS-EC2-instance-types-1" style="zoom:50%;" />

- **R** : 인스턴스 클래스다 (일반 목적의 인스턴스)
- **5** : 세대 (AWS는 계속 인스턴스를 업데이트 시킨다)
- **d** : 추가적인 기능
- **xLarge** : 인스턴스 클래스 안의 사이즈
  - size가 클 수록 기능적인 면에서 더 좋을 것이다



![typesofec2instances768x384](3_AWS_EC2_기초.assets/typesofec2instances768x384.png)

#### EC2 인스턴스 종류 - General Purpose

- 웹 서버 또는 코드 저장소 같은 다양한 작접량을 처리할 때 유용한 EC2 인스턴스다
- Compute, Memory, Networking 간에 균형이 잡힌 인스턴스다



#### EC2 인스턴스 종류 - Compute Optimized

- 고성능 프로세서가 필요할 때에 사용되는 인스턴스다
  - 일괄 처리 작업량
  - 고성능 웹 서버
  - 고성능 컴퓨팅 (HPC)
  - 머신 러닝
  - 게임 등
- 주로 Compute Optimized 인스턴스는 C로 시작한다



#### EC2 인스턴스 종류 - Memory Optimized

- 굉장히 많은 양의 데이터를 처리할 때 Memory Optimized 인스턴스가 좋다
  - 고성능, 관계형, 비관계형 데이터 베이스
  - Distributed web scale cache stores
  - BI (Business Intelligence)에 적합한 인메모리 데이터 베이스
  - 체계가 없는 실시간 빅데이터
- Memory Optimized 인스턴스는 RAM의 앞 부분을 따서 R로 많이 시작하지만, 그보다 더 높은 메모리를 사용할 수 있는, X와 Z도 있다



#### EC2 인스턴스 종류 - Storage Optimized

- 로컬 저장소의 많은 데이터를 접근할 때 유용하다
  - 고주파 온라인 거래 프로세싱 (OLTP, Online Transaction Processing)
  - 관계형 & NoSQL 데이터베이스
  - 인메모리 데이터베이스을 위한 캐싱 (Redis)
  - 데이터 창고 어플리케이션
  - 파일 분산 시스템
- I, D, H로 주로 시작한다





## Security Groups

![aws-security-groups-filtering](3_AWS_EC2_기초.assets/aws-security-groups-filtering.webp)
