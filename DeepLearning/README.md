# Optimizer
- Optimizer란? - loss function을 통해 구한 차이를 사용해 기울기를 구하고 Network의 parameter(W, b)를 학습에 어떻게 반영할 것인지를 결정하는 방법
- GD(Gradient Decent), SGD(Stochastic Gradient Descent)


## SGD
- Gradient : Momentum, NAG, NADam
- Learning rate : Adagrad, AdaDelta, RMSProp
- All : Adam




### Momentum
- 이전 step의 방향과 현재 상태의 gradient를 더해 현재 학습할 방향과 크기를 정함.
- Local Minimum, Oscillation 문제 해결
- 문제점 : 과거에 이동했던 양을 변수별로 저장해야하므로 변수에 대한 메모리가 기존의 두배로 필요
