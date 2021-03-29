GAN
generative Adversarial Nets
생산적 적대적 신경망

저자 이안 굿 펠로우

<h1>Introduction</h1>

**The promise of deep learning is to discover rich, hierarchical models that**

**represent probability distributions over the kinds of data encountered in**

**artificial intelligence applications, such as natural images, audio waveforms**

**containing speech, and symbols in natural language corpora.**

이미지, 'speech' 가 포함된 음성의 파형 오디오, 자연어 말뭉치와 같은 인공지능 응용 프로그램에서

발생하는 데이터의 종류에 대한 확률 분포를 나타내는 풍부하고 계층적 모델을 발견하는 것이다. 2021.03.04

**So far, the most striking successes in deep learning have involved discriminative**

**models, usually those that map a high-dimensional, rich sensory input to a class label.**

지금까지는, 딥러닝에서 가장 놀라운 성공은 보통 고차원의 입력 클래스 라벨에 매핑하는 조건부 모델이다. 2021.03.05

**These striking successes have primarily been based on the backpropagation and dropout algorithms,**

**using piecewise linear units of an impact, due to the difficulty of approximate  many intractable**

**probabilistic computations that arise in maximum likelihood estimation and related strategies, and**

**due to difficulty of leveraging the benefits of piecewise linear units in the generative context.**

이러한 놀라운 성공은 주로 최대 우도 추정(최대 가능도 추정)법 및 관련 전략에서 발생하는 난치 확률 계산의 어려움과 생성 맥락에서 비선형 단위의 

이점을 활용하기 어렵기 때문에 충격의 단편 선형 단위를 사용하는 역전파 및 드롭아웃 알고리즘에 기초해 왔다.