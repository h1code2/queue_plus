from queue import Queue
from threading import Thread


class QueuePlus(object):
    STATUS_BREAK = 0
    STATUS_CONTINUE = 1
    item_queue = Queue()
    threads = list()

    def produce_item(self):
        pass

    def _produce_item(self):
        while True:
            status = self.produce_item()
            if status == self.STATUS_BREAK:
                break
            elif status == self.STATUS_CONTINUE:
                continue
            else:
                pass

    def consumer_item(self, item):
        pass

    def _consumer_item(self):
        while True:
            item = self.item_queue.get()
            self.consumer_item(item)
            self.item_queue.task_done()

    def run(self, thread_num=1, daemon=False):
        _produce_item = Thread(target=self._produce_item)
        self.threads.append(_produce_item)

        for i in range(thread_num):
            _consumer_item = Thread(target=self._consumer_item)
            self.threads.append(_consumer_item)

        for t in self.threads:
            t.setDaemon(daemon)
            t.start()

        self.item_queue.join()
