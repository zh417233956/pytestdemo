# pytestdemo
```python
'''
测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 init 方法
测试函数以test_开头
断言使用基本的assert即可
'''
```

```shell
pip install -r requirements.txt
```
## 运行
```shell
pytest
# -q即-quiet 控制台不显示详情
pytest -q
```
> 运行pytest时会找当前目录及其子目录中的所有test_*.py 或 *_test.py格式的文件以及以test开头的方法或者class

## 运行后生成测试报告（htmlReport）
安装pytest-html
```shell
pip install pytest-html
# 生成报告
pytest .\testCase\test_class.py --html=html/reprot.html
```

## 运行指定的case
```shell
# 指定py运行
pytest .\testCase\test_class.py
# 指定类测试
pytest .\testCase\test_class.py::TestClass
# 指定类中的方法测试
pytest .\testCase\test_class.py::TestClass::test_one
```
## 多进程运行cases
```shell
# 安装pytest-xdist
pip install pytest-xdist
# 指定2个进程数
pytest -n 2
```
## 重试运行cases
> 在做接口测试时，有事会遇到503或短时的网络波动，导致case运行失败，而这并非是我们期望的结果，此时可以就可以通过重试运行cases的方式来解决

```shell
# 安装pytest-rerunfailures
pip install pytest-rerunfailures
# 执行重试2次
pytest --reruns 2
```
## 显示print内容
> 在运行测试脚本时，为了调试或打印一些内容，我们会在代码中加一些print内容，但是在运行pytest时，这些内容不会显示出来。如果带上-s，就可以显示了

```shell
pytest -s
```