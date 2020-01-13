## queue_plus
a simple self-use class

**Install and use:**
```shell
pip install queue-plus
```

**example:**
```python
from queue_plus import QueuePlus


class Test(QueuePlus):

    def produce_item(self):
        self.item_queue.put(item={"name":"Tom"})

    def consumer_item(self, item):
        print(item)


if __name__ == '__main__':
    test = Test()
    test.run(thread_num=20)