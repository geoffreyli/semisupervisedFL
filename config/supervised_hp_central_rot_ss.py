import tensorflow as tf
from tensorboard.plugins.hparams import api as hp
from parameter_handler import ParameterHandler


######### GENERAL CONFIG ###############
config = {}

config['experiment'] = 'SupervisedLearningCentral'
config['model_fn'] = 'RotationSelfSupervisedModel'
config['sample_client_data'] = True      # must set to False when running real experiments
config['curr_run_number'] = 0            # always initialize as 0, unless starting from a certain run

# data loading
config['shuffle_buffer'] = 100

# training
config['num_epochs'] = 1
config['log_every'] = 1
config['model_fp'] = 'classifier_{}.h5'

######### EXPERIMENTAL PARAMETERS ###############
hparam_map = {'supervised_mask_ratio': hp.HParam('supervised_mask_ratio', hp.Discrete([0.0])),
                'unsupervised_mask_ratio': hp.HParam('unsupervised_mask_ratio', hp.Discrete([0.0])),
                'mask_by': hp.HParam('mask_by', hp.Discrete(['example'])),
                'dataset': hp.HParam('dataset', hp.Discrete(['emnist'])),
                'batch_size': hp.HParam('batch_size', hp.Discrete([256]))
}

######### METRICS ###############################
metric_map = {'train_loss': hp.Metric('train_loss', display_name='Train Loss'),
              'train_accuracy': hp.Metric('train_accuracy', display_name='Train Accuracy'),
              'test_loss': hp.Metric('test_loss', display_name='Test Loss'),
              'test_accuracy': hp.Metric('test_accuracy', display_name='Test Accuracy')
}

#################################################
ph = ParameterHandler(config, hparam_map, metric_map)
ph.hparam_sets = list(ph.gen_hparam_cartesian_product())
print(len(ph.hparam_sets))