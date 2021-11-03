# paper-megameta-hyperparameter-training
Hyperparameter-training for the Mega-Meta project

This repository stores the scripts and plugins that were used for the creation
of the three final project files. These final project files were based on a
convolutional neural network, optimized using Optuna.

## content
The `Plugins` folder contains the 2 used ASReview plugins. `asreview-cnn-hpo`
was used to find the optimal settings for each dataset, and
`asreview-model-cnn-17-layer` was used to implement these settings.

The `Scripts` folder contains a Jupyter Notebook that can be run in Google Colab. This script installs the plugins, and creates an 