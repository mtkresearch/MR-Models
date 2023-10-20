CUR_DIR=$(pwd)

SRC_DIR=$CUR_DIR/../../src

python3 $SRC_DIR/generation_routine.py --config tmmlu_task_config.json
python3 $SRC_DIR/generation_routine.py --config tasks_config.json

python3 $SRC_DIR/aggregate_results.py --result_dir ./outputs --model_name 'my_model'

