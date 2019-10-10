import os
import subprocess
import threading
from pathlib import Path


class SetUpSamLocal:
    end_process = False
    proc = None

    def output_reader(self, proc):
        for line in iter(proc.stdout.readline, b''):
            print('got line: {0}'.format(line.decode('utf-8')), end='')

    def run_sam_local(self):
        path = Path(os.path.dirname(__file__))
        template_path = os.path.join(path.parent, "template.yml")
        command = ["sam", "local", "start-api", "--template", template_path]
        self.proc = subprocess.Popen(command, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, shell=True)

        t = threading.Thread(target=self.output_reader, args=(self.proc,))
        t.start()

    def set_up(self):
        self.run_sam_local()

    def tear_down(self):
        self.proc.terminate()
