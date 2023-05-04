# Optimizer
- Optimizer란? - loss function을 통해 구한 차이를 사용해 기울기를 구하고 Network의 parameter(W, b)를 학습에 어떻게 반영할 것인지를 결정하는 방법
- GD(Gradient Decent), SGD(Stochastic Gradient Descent)


## SGD
- Gradient : Momentum, NAG, NADam
- Learning rate : Adagrad, AdaDelta, RMSProp
- Both : Adam


### Momentum
- 이전 step의 방향과 현재 상태의 gradient를 더해 현재 학습할 방향과 크기를 정함.
- Local Minimum, Oscillation 문제 해결
- 문제점 : 과거에 이동했던 양을 변수별로 저장해야하므로 변수에 대한 메모리가 기존의 두배로 필요


### NAG

### NADAM

### Adagrad

### AdaDelta

### RMSProp

### Adam

## Overfitting
- (A Simple Weight Decay Can Improve Generalization)
### Weight decay
- 데이터가 단순하고 모델이 복잡하면, 학습을 하면서 굉장히 작은 값이었던 weight들의 값이 점점 증가하게 되면서 Overfitting이 발생함. weight값이 커질수록 학습데이터에 영향을 많이 받게 되고, 학습데이터에 모델이 딱 맞춰지게 된다. 한마디로 local noise의 영향을 받아 outlier들에 모델이 맞춰지는 현상
- 학습된 모델의 복잡도를 줄이기 위해서 학습 중 weight가 너무 큰 값을 가지지 않도록 Loss function에 weight가 커질 경우에 대한 패널티 항목을 집어 넣어 weight들의 값이 필요이상으로 커지는 것을 방지하는 것

# Yolov7
momentum
weight_decay
cls
cls_pw
obj
obj_pw
iou_t

# 시계열 예측 SARIMA
### trend(추세)
- 데이터가 장기적으로 증가하거나 감소할 때, trend가 존재한다. trend가 linear일 필요는 없다. 때때로 어떤 trend가 증가에서 감소로 변화하는 경우에, 그것을 trend의 "방향이 변화했다"라고 한다.
### seasonality(계절성)
- 해마다 어떤 특정한 때나 1주일마다 특정 요일에 나타나는 것 같은 계절성 요인이 시계열에 영향을 줄 때 seasonality pattern이 나타난다. 계절성은 freq의 형태로 나타난다.
### cycle(주기성)
- 고정된 빈도가 아닌 형태로 증가나 감소하는 모습을 보일 때 cycle이 나타난다. 보통 이러한 요동은 경제 상황 때문에 일어나고, 흔히 "business cycle(경기 순환)"과 관련이 있다.
- 일정한 freq로 나타나지 않는 요동은 cycle, freq가 변하지 않고 연중 어떤 시기와 연관되어 있다면 seasonality
### stationarity(정상성)
- stationarity를 나타내는 시계열은 시계열의 특징이 해당 시계열이 관측된 시간에 무관하다. 따라서, trend나 seasonality가 있는 시계열은 stationarity를 나타내는 시계열이 아니다. trend와 seasonality는 서로 다른 시간에 시계열의 값에 영향을 줄 것이기 때문이다. 반면에 white noise(백색잡음) 시계열은 정상성을 나타내는 시계열이다. 언제 관찰하는지에 상관이 없고, 시간에 따라 어떤 시점에서 보더라도 똑같이 보일 것이기 때문이다. 또한, 주기성 행동을 가지고 있는 시계열은 stationarity를 나타내는 시계열이다. 왜냐하면 주기가 고정된 길이를 갖고 있지 않기 때문에, 시계열을 관측하기 전에 주기의 고점이나 저점이 어디일지 확실하게 알 수 없다.
### differencing(차분)
- stationarity을 나타내지 않는 시계열을 stationarity를 나타내도록 하는 방법으로 연이은 관측값들의 차이를 계산하는 것이다.(한마디로, 정상시계열로 변환)
- 시계열의 수준에서 나타내는 변화를 제거하여 시계열의 평균 변화를 일정하게 만드는 것을 도움.(trend or seasonality 제거 or 감소)
- 수열에서 연속하는 두항의 차
### 정상 시계열로 변환하려면
1. 변동폭이 일정하지 않은 경우: 로그 변환
2. 추세, 계절성이 존재하는 경우: 차분(정상성을 띄울때까지 반복 차분)
##### Forecasting: Principles and Practice
***
### AutoRegressive(AR-자동회귀)
- 통계 및 신호 처리에서 AR모델은 random process의 한 타입을 나타내는 것이다. 즉, 특정 시간 변동 프로세스를 설명한다. 자기 회귀 모델은 출력 변수가 자신의 이전 values와 stochastic term에 depends linearly, 따라서 stochastic difference equation의 형태이다.
- 예측하고자 하는 특정 변수의 과거 관측값의 선형결합으로 해당 변수의 미래값을 예측하는 모형
### Moving Average(MA-이동평균)
- 예측 오차를 이용하여 미래를 예측하는 모형
### AutoCorrelation Function(ACF-자기상관함수)
- 시차에 따른 일련의 자기상관으로, 시차가 커질수록 ACF는 0에 가까워진다.
- stationarity 시계열은 상대적으로 빠르게 0에 수렴, 비정상 시계열은 천천히 감소하고, 종종 큰 양의 값을 가짐
### Partial AutoCorreleation Function(PACF-편자기상관함수)
- 시차에 따른 일련의 편자기상관이며, 시차가 다른 두 시계열 데이터 간의 순수한 상호 연관성이다.


