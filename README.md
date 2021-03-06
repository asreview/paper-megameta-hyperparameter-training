[![DOI](https://zenodo.org/badge/424153223.svg)](https://zenodo.org/badge/latestdoi/424153223)

# Hyperparameter-training for the Mega-Meta project

The repository is part of the so-called, Mega-Meta study on reviewing factors
contributing to substance use, anxiety, and depressive disorders. The study
protocol has been pre-registered at
[Prospero](https://www.crd.york.ac.uk/prospero/display_record.php?ID=CRD42021266297).
The procedure for obtaining the search terms, the exact search query, and
selecting key papers by expert consensus can be found on the [Open Science
Framework](https://osf.io/m5uhy/). 

The screening was conducted in the software ASReview ([Van de Schoot et al.,
2020](https://www.nature.com/articles/s42256-020-00287-7) using the protocol
as described in [Hofstee et al. (2021)](https://osf.io/3znar/). The server
installation is described in [Melnikov
(2021)](https://github.com/valmelnikov/asreview_server_setup), 
and the post-processing is described by [van de Brand et al., 2021](https://github.com/asreview/paper-megameta-postprocessing-screeningresults). 
The data can be found on DANS [LINK NEEDED].

This repository stores the scripts and plugins that were used for the creation
of the three final project files. These final project files were created using a
classifier based on a [convolutional neural
network](https://github.com/JTeijema/asreview-plugin-model-cnn-17-layer),
optimized using [Optuna](https://github.com/optuna/optuna).

## Content
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

## Step-by-step quickguide
1. Create a project file from one of the input files.
2. Select the HPO-CNN optimizer as classifier for the created project file.
3. Train the project file to recieve the optimal CNN hyper parameters. The
   optimal parameters appear in the console used to start ASReview.
4. Plug these parameters into the CNN model (not the HPO-CNN model).
5. Train the CNN model.
6. Start screening records with the optimized CNN model.

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

4. Install this newly created CNN. Using this new optimized CNN, create the
   projects files for screening.


## Funding
This project is funded by a grant from the Centre for Urban Mental Health, University of Amsterdam, The Netherlands

## Licence
The content in this repository is published under the MIT license.

## Contact
For any questions or remarks, please send an email to the [ASReview-team](mailto:asreview@uu.nl).
