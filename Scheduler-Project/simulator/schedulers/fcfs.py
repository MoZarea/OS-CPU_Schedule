from simulator.schedulers.scheduler import Scheduler

from simulator.schedulers.scheduler import Scheduler

class FCFS(Scheduler):
    """First Come First Serve (FCFS) scheduler."""

    def __init__(self):
        super().__init__()

    def perform_schedule(self):
        """
        We simply change process as the currently active process finishes its
        execution on the CPU.
        """
        # If there is no active process, dequeue the next process
        if not self.active:
            if self.q:
                self.active = self.q.popleft()

        # If there is an active process, keep running it
        elif self.active.burst_time > 0:
            pass

        # If the active process has finished, dequeue the next process
        else:
            self.active = None
            if self.q:
                self.active = self.q.popleft()

        return self.active