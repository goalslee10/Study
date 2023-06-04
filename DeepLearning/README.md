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
### Weight Decay
- 데이터가 단순하고 모델이 복잡하면, 학습을 하면서 굉장히 작은 값이었던 weight들의 값이 점점 증가하게 되면서 Overfitting이 발생함. weight값이 커질수록 학습데이터에 영향을 많이 받게 되고, 학습데이터에 모델이 딱 맞춰지게 된다. 한마디로 local noise의 영향을 받아 outlier들에 모델이 맞춰지는 현상
- 학습된 모델의 복잡도를 줄이기 위해서 학습 중 weight가 너무 큰 값을 가지지 않도록 Loss function에 weight가 커질 경우에 대한 패널티 항목을 집어 넣어 weight들의 값이 필요이상으로 커지는 것을 방지하는 것
