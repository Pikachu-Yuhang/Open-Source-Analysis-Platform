# Set batch.
from puller.tasks import create_batch
repos = ['pytorch/pytorch', 'tensorflow/tensorflow']
batch_id = create_batch(repos)

# Start pulling.
import datetime
from puller.tasks import pull_data
from_date, to_date = datetime.date(2015, 1, 1), datetime.datetime.now().date()
pull_data(batch_id, from_date, to_date)