from pyghey.individuals import print_line,break_line

def print_loss(epoch, loss_value, accuracy=None, learning_rate=None, 
               batch_size=None, dataset_size=None, model_name=None, 
               optimizer_name=None, loss_function_name=None):
    print_line(20)
    print(f"EPOCH: {epoch}")
    print(f"LOSS: {loss_value:.4f}")
    if accuracy is not None:
        print(f"ACCURACY: {accuracy:.4f}")
    if learning_rate is not None:
        print(f"LEARNING RATE: {learning_rate:.4f}")
    if batch_size is not None:
        print(f"BATCH SIZE: {batch_size}")
    if dataset_size is not None:
        print(f"DATASET SIZE: {dataset_size}")
    if model_name is not None:
        print(f"MODEL: {model_name}")
    if optimizer_name is not None:
        print(f"OPTIMIZER: {optimizer_name}")
    if loss_function_name is not None:
        print(f"LOSS FUNCTION: {loss_function_name}")
    print_line(20)
    break_line()