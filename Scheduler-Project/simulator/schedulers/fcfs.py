from simulator.schedulers.scheduler import Scheduler

from simulator.schedulers.scheduler import Scheduler

class FCFS(Scheduler):
    """First Come First Serve (FCFS) scheduler."""

    def __init__(self):
        super().__init__()

    def perform_schedule(self):

        if not self.active:
            if self.q:
                self.active = self.q.popleft()

        elif self.active.burst_time > 0:
            pass

        else:
            self.active = None
            if self.q:
                self.active = self.q.popleft()

        return self.active