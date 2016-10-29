#!/usr/bin/python
import threading
import multiprocessing
import time
import random
import glob

def log(string):
    print "%.3f" % time.time(), string

class Producer(object):

    def __init__(self):
        self.id = None
        self.output = "%.8d.dat" % random.randint(0, 100000)
        
    def write(self, probe):
        with open(self.output, "w") as out:
            out.write(probe)
            out.close()
        return True

class Consumer(object):
    result = "-"
    def __init__(self):
        self.id = None
        self.input = None
        self.result = None
        self.job = None
        
    def read(self, queue):
        with open(self.input, 'r') as inp:
            self.result = inp.read()
        queue.put((self.id, self.result))

class ProducerConsumerMap(object):

    PAIRS = 10
    
    def __init__(self):
        self.producers = []
        self.consumers = []
        self.map = {}
        
    def _create_producers(self):
        for _ in range(self.PAIRS):
            producer = Producer()
            producer.id = _
            with open(producer.output, "w") as out:
                out.write("")
                out.close()
            self.producers.append(producer)

    def _create_consumers(self):
        inputs = glob.glob("*.dat")
        random.shuffle(inputs)
        for _ in range(len(inputs)):
            consumer = Consumer()
            consumer.id = _
            consumer.input = inputs[_]
            self.consumers.append(consumer)
            
    def run(self):
        self._create_producers()
        self._create_consumers()

        for producer in self.producers:
            queue = multiprocessing.Queue()
            probe = "%.3f" % time.time()
            producer.write(probe)

            for consumer in self.consumers:
                consumer.job = multiprocessing.Process(target=consumer.read, args=(queue,))
                consumer.job.start() 

            for consumer in self.consumers:
                consumer.job.join()

            while not queue.empty():
                result = queue.get()
                if probe in result[1]:
                    self.map[str(producer.id)] = str(result[0])  # map current producer to current consumer
                    self.consumers = filter(lambda obj: obj.id != result[0], self.consumers)

def main():
    pcmap = ProducerConsumerMap()
    pcmap.run()
    print pcmap.map

if __name__ == '__main__':
    main()
