from simulator.schedulers.scheduler import Scheduler

class RoundRobin(Scheduler):
    """Constant time quantum Round Robin scheduler."""

    def __init__(self, time_quantum=4):
        super(RoundRobin, self).__init__()

        # Constant time quantum
        self.time_q = time_quantum

        # Tracks the current interval in a time quantum
        self.curr_q = 0

    def perform_schedule(self):
        """
        Returns the next job to execute in the round robin algorithm.

        In this case we simply take the next item in the queue to be the new
        active queue (if there exist one) and push the active item back into
        the queue.
        """
        
        # TODO: Implement your code here.
        # If there is no active process, dequeue the next process

        if not self.active:
            self.curr_q = 0
            if self.q:
                self.active = self.q.popleft()

        # If there is an active process, keep running it
        elif self.active.burst_time>0 :
            self.curr_q = 0
            if self.active.burst_time > 0:
                self.q.append(self.active)
            self.active = None
            if self.q:
                self.active = self.q.popleft()
        elif  self.active.burst_time==0:

            # if self.curr_q<self.time_q-1:
            self.curr_q = 0
            self.active = None
            if self.q:
                self.active = self.q.popleft()
            else:
                self.active = None
                if self.q:
                    self.active = self.q.popleft()

        return self.active


    def timer_interrupt(self):
        """
        Timer interrupts only when the current active task has ran out of
        its time quantum or has stopped execution.
        """
        default = super(RoundRobin, self).timer_interrupt()
        depleted = self.curr_q == 0

        return default or depleted

    def step(self):
        super(RoundRobin, self).step()

        self.curr_q = (self.curr_q + 1) % self.time_q
