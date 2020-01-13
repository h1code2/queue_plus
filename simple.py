from queue_plus import QueuePlus


class Test(QueuePlus):

    def produce_item(self):
        self.item_queue.put(1)

    def consumer_item(self, item):
        print(item)


if __name__ == '__main__':
    test = Test()
    test.run(thread_num=20)
