# paper-megameta-hyperparameter-training
Hyperparameter-training for the Mega-Meta project

This repository stores the scripts and plugins that were used for the creation
of the three final project files. These final project files were created using a
classifier based on a convolutional neural network, optimized using Optuna.

## content
The `Plugins` folder contains the 2 used ASReview plugins. `asreview-cnn-hpo`
was used to find the optimal settings for each dataset, and
`asreview-model-cnn-17-layer` was used to implement these settings.

The `Scripts` folder contains a Jupyter Notebook that can be run in Google
Colab. This script installs the plugins found in the plugins folder and then
creates an ASReview lab instance that can be used to employ these plugins,
find the optimal hyperparameters, and create the final project files.

## Step-by-step guide
This guide details how the CNN was optimized and trained.

1. The process started with 3 different excel files containing ASReview output. 


2. In google Colab, upload and run the `cnn_training_script_for_use_in_google_colab.ipynb` file in found in the folder called `scripts`. This file is used to optimize the CNNs for the later processing.

    A custom-made version of the HPO-CNN was used to determine the optimal hyperparameters for each of the project files. These hyperparameters were then applied to the CNN classifier model. 

        To use this custom-made version of the HPO-CNN, upload the folder containing the HPO-CNN version to Colab. A quick way of doing this is by zipping-up the folder and uploading this zip file. 

        The notebook contains code for unzipping, and then installing the plugin automatically. 

    The notebook uses NGROK to access the ASReview frontend. A personal NGROK token is needed for the `NGROK_AUTH_TOKEN` variable. A link with instructions can be found in the notebook. 

    After running the notebook, there will be a link produced by NGROK. This link will open the ASReview frontend.  

    In this front end, create a new project file with one of the excel files 

    When the training of the new project file is finished (after a long time), the still processing colab cell running ASReview will print the optimal parameters in the output.  

3. These parameters are used to optimize the CNN used for the final project files. 

    For the training of these project files, the parameters that resulted as an output of the HPO are used for the CNN. The output is set by filling in the results into the `nlayers` and `nfilters` variables in the `asreview-plugin-model-cnn-17-layer\asreviewcontrib\models\cnn.py` file. 

 

 