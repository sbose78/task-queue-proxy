DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
echo $DIR

sh $DIR/stop_worker.sh
sh $DIR/start_work.sh


