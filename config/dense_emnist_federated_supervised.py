import tensorflow as tf
from tensorboard.plugins.hparams import api as hp
from parameter_handler import ParameterHandler


######### GENERAL CONFIG ###############
config = {}

config['experiment'] = 'SupervisedLearningFL'
config['model_fn'] = 'DenseSupervisedModel'
config['sample_client_data'] = False      # must set to False when running real experiments
config['curr_run_number'] = 0                  # always initialize as 0, unless starting from a certain run

# data loading
config['shuffle_buffer'] = 500

# training
config['num_rounds'] = 100
config['log_every'] = 10
config['model_fp'] = 'dense_emnist_federated_supervised_{}.h5'

config['optimizer'] = 'SGD'
config['nesterov'] = False
config['momentum'] = 0.99
config['decay'] = 0.0

######### EXPERIMENTAL PARAMETERS ###############
hparam_map = {}

hparam_map['supervised_mask_ratio'] = hp.HParam('supervised_mask_ratio', hp.Discrete([0.0, 0.8, 0.9, 0.95, 0.98, 0.99]))
hparam_map['unsupervised_mask_ratio'] = hp.HParam('unsupervised_mask_ratio', hp.Discrete([0.0]))
hparam_map['mask_by'] = hp.HParam('mask_by', hp.Discrete(['example']))
hparam_map['dataset'] = hp.HParam('dataset', hp.Discrete(['emnist']))

hparam_map['batch_size'] = hp.HParam('batch_size', hp.Discrete([20]))
hparam_map['learning_rate'] = hp.HParam('learning_rate', hp.Discrete([0.001]))

hparam_map['num_clients_per_round'] = hp.HParam('num_clients_per_round', hp.Discrete([100]))
hparam_map['num_epochs'] = hp.HParam('num_epochs', hp.Discrete([10]))

######### METRICS ###############################
metric_map = {}

metric_map['train_loss'] = hp.Metric('train_loss', display_name='Train Loss')
metric_map['train_accuracy'] = hp.Metric('train_accuracy', display_name='Train Accuracy')
metric_map['test_loss'] = hp.Metric('test_loss', display_name='Test Loss')
metric_map['test_accuracy'] = hp.Metric('test_accuracy', display_name='Test Accuracy')

#################################################
ph = ParameterHandler(config, hparam_map, metric_map)
ph.hparam_sets = list(ph.gen_hparam_cartesian_product())
print(len(ph.hparam_sets))