## multiprocessing에서 Pool로 멀티프로스세스 할때는 
from multiprocessing import Pool, Manager

m = Manager()
lock = m.Lock() 
que = m.Queue() 
## 이런식으로 Manager를 통해서 lock과 queue를 사용해야 한다.