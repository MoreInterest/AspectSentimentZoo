# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 8:42
# @Author  : Tianchiyue
# @File    : configs.py
# @Software: PyCharm Community Edition
atae_config = {
    'weight_loss':False,
    'noise': 0.3,
    'clipnorm': 0.1,
    'loss_l2': 0.0001,
    'layers': 2,
    'max_length':100,
    'use_mask':True,
    'dropout_words': 0.3,
    'dropout_rate': 0.2,
    'num_classes': 2,
    'rnn_output_size': 100,
    'embed_trainable': True,
    'aspect_emb_trainable':True,
    'connect_aspect':True,
    'batch_size': 32,
    'optimizer': 'adam',
    'learning_rate': 0.0005,
    'epochs': 20,
    'n_stop': 5,
    'hidden_dims': 300,
    'bidirectional': False,
    'rnn': 'gru',
    'activation': 'tanh',
    'use_mlp':False,
    'use_l2': False,
    'l2': 0.0001,
    'lr_decay_epoch': 3,
    'lr_decay_rate': 0.5,
    'han': True
}

tan_config = {
    'weight_loss':False,
    'noise': 0.3,
    'clipnorm': 0.1,
    'loss_l2': 0.0001,
    'layers': 2,
    'max_length':100,
    'use_mask':True,
    'dropout_words': 0.3,
    'dropout_rate': 0.5,
    'num_classes': 2,
    'rnn_output_size': 100,
    'embed_trainable': True,
    'aspect_emb_trainable':True,
    'connect_aspect':True,
    'batch_size': 32,
    'optimizer': 'adam',
    'learning_rate': 0.0005,
    'epochs': 20,
    'n_stop': 5,
    'hidden_dims': 300,
    'bidirectional': True,
    'rnn': 'gru',
    'activation': 'tanh',
    'use_mlp':False,
    'use_l2': True,
    'l2': 0.0001,
    'lr_decay_epoch': 3,
    'lr_decay_rate': 0.5,
    'han': True
}

arcnn_config = {
    'weight_loss':False,
    'noise': 0.3,
    'clipnorm': 0.1,
    'loss_l2': 0.0001,
    'layers': 2,
    'max_length':100,
    'use_mask':True,
    'dropout_words': 0.3,
    'dropout_rate': 0.5,
    'num_classes': 2,
    'rnn_output_size': 100,
    'embed_trainable': True,
    'aspect_emb_trainable':True,
    'connect_aspect':True,
    'batch_size': 32,
    'optimizer': 'adam',
    'learning_rate': 0.0005,
    'epochs': 20,
    'n_stop': 5,
    'hidden_dims': 300,
    'bidirectional': True,
    'rnn': 'gru',
    'activation': 'tanh',
    'use_mlp':False,
    'use_l2': True,
    'l2': 0.0001,
    'lr_decay_epoch': 3,
    'lr_decay_rate': 0.5,
    'kernel_sizes':[2,3,5],
    'filters':200,
}

gcae_config = {
    'weight_loss':False,
    'embed_trainable': True,
    'aspect_emb_trainable':True,
    'filters': 300,
    'kernel_sizes': [2, 3],  # 调整 [2,3,5]
    'layers': 2,
    'spatial_dropout': 0.2,
    'dense_nr': 300,
    'max_length': 1000,
    'num_classes': 2,
    'dropout_rate': 0.2,
    'batch_size': 32,
    'optimizer': 'adam',
    'learning_rate': 0.001,  # 调整 0.0005
    'epochs': 20,
    'n_stop': 5,
    'hidden_dims': 300,
    'activation': 'tanh',
    'use_mlp': True,
    'use_l2': False,
    'l2': 0.0001,
    'lr_decay_epoch': 3,
    'lr_decay_rate': 0.5,
}
