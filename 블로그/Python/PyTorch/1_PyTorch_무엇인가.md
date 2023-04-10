# PyTorch [무엇인가?]



#### 페이스북의 루아 언어로 개발된 Torch를 파이썬 버전으로 바꿔서 PyTorch라고 한다



#### NumPy와 비슷하다



#### GPU를 활용하여 인공 신경망 모델을 만들고 학습시킬 수 있게 도와준다



## PyTorch의 구성요소

- **torch** : 메인 네임스페이스, 텐서 등의 다양한 수학 함수가 포함
  - **텐서 (Tensor) : 수학적인 개념으로 데이터의 배열로 생각할 수 있다**
- **torch.autograd** : 자동 미분 기능을 제공하는 라이브러리
- **torch.nn** : 신경망 구축을 위한 데이터 구조나 레이어 등의 라이브러리
- **torch.multiprocessing** : 병렬처리 기능을 제공하는 라이브러리
- **torch.optim** : SGD (Stochastic Gradient Descent)를 중심으로 한 파라미터 최적화 알고리즘 제공
- **torch.utils** : 데이터 조작 등 유틸리티 기능 제공
- **torch.onnx** : ONNX (Open Neural Network Exchange), 서로 다른 프레임워크 간의 모델을 공유할 때 사용



#### Tensor

- 딥러닝을 할 때에, 데이터를 처리할 때에 가장 기본적인 구조가 텐서이다
- 데이터를 담는 컨테이너(container)로서 일반적으로 수치형 데이터를 저장한다

![Tensors](1_PyTorch_무엇인가.assets/Tensors.png)



