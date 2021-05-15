import datetime
import sys


n_batches = 3002530
batch = int(sys.argv[1])
time = float(sys.argv[2])
estimated = time * n_batches / batch
remaining = estimated - time

print(f'Running: {datetime.timedelta(seconds=time)}',
      f'Remaining: {datetime.timedelta(seconds=remaining)}',
      f'Total: {datetime.timedelta(seconds=estimated)}',
      f'Progress: {100 * batch / n_batches:.2f}%',
      sep='\n')

