# paper-megameta-hyperparameter-training
Hyperparameter-training for the Mega-Meta project

This repository stores the scripts and plugins that were used for the creation
of the three final project files. These final project files were created using a
classifier based on a [convolutional neural
network](https://github.com/JTeijema/asreview-plugin-model-cnn-17-layer),
optimized using [Optuna](https://github.com/optuna/optuna).

## content
The `Plugins` folder contains the 2 used ASReview plugins.
[`asreview-cnn-hpo`](https://github.com/BartJanBoverhof/asreview-cnn-hpo) was
used to find the optimal settings for each dataset, and
[`asreview-model-cnn-17-layer`](https://github.com/JTeijema/asreview-plugin-model-cnn-17-layer)
was used to implement these settings.

The `scripts` folder contains a Jupyter Notebook that can be run in [Google
Colab](https://colab.research.google.com/). This script installs the plugins
found in the `plugins` folder and then creates an ASReview lab instance that can
be used to employ these plugins, find the optimal hyperparameters, and create
the final project files.

## Step-by-step guide
This guide details how the CNN was optimized and trained.

1. The process started with 3 different excel files containing ASReview output. 


2. In Google Colab, upload and run the
   `cnn_training_script_for_use_in_google_colab.ipynb` file in found in the
   folder called `scripts`. This file is used to optimize the CNNs for the later
   processing.

    - A custom-made version of the HPO-CNN was used to determine the optimal
      hyperparameters for each of the project files. These hyperparameters were
      then applied to the CNN classifier model. 

        - To use this custom-made version of the HPO-CNN, upload the folder
          containing the HPO-CNN version to Colab. A quick way of doing this is
          by zipping-up the folder and uploading this zip file. 

        - The notebook contains code for unzipping, and then installing the
          plugin automatically. 

    - The notebook uses NGROK to access the ASReview frontend. A personal NGROK
      token is needed for the `NGROK_AUTH_TOKEN` variable. A link with
      instructions on where to get such a token can be found in the notebook.

    ```python
    !pip install pyngrok --quiet
    from pyngrok import ngrok

    # Terminate open tunnels if exist
    ngrok.kill()

    # Setting the authtoken (optional)
    # Get your authtoken from https://dashboard.ngrok.com/auth
    NGROK_AUTH_TOKEN = "fill token here"
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    ```

    - After running the notebook, there will be a link produced by NGROK. This
      link will open the ASReview frontend.  

    ```python
    ngrok.connect(port="80", proto="http")

    <NgrokTunnel: "http://d3c5-35-197-26-146.ngrok.io" -> "http://localhost:80">
    ```

    - In this front end, create a new project file with one of the Excel files.

    - When the training of the new project file is finished (after a long time),
      the still processing colab cell running ASReview will print the optimal
      parameters in the output.  

    ```
    Hpo trail:  77/80
    Hpo trail:  77/80
    Hpo trail:  77/80
    Hpo trail:  77/80
    FOUND HYPERPARAMETERS:  {'nlayers': 3, 'nfilters':  209}
    ```

3. These parameters are used to optimize the CNN used for the final project
   files. 

    - For the training of these project files, the parameters that resulted as
      an output of the HPO are used for the CNN. The output is set by filling in
      the results into the `nlayers` and `nfilters` variables in the
      `asreview-plugin-model-cnn-17-layer\asreviewcontrib\models\cnn.py` file. 

    ```python
    def _create_dense_nn_model(_size):
      def model_wrapper():
        backend.clear_session()

        nfilters = 209
        
        model = Sequential()
    ```




