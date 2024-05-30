# C.AR.D.I.A
### Client-Side Script: Federated Learning Client for Heart Disease Prediction

The `client.py` script functions as a client in a Federated Learning (FL) system aimed at predicting heart disease. Utilizing the Flower (FLwr) framework, it supports decentralized model training. The script features a Keras Feedforward Neural Network (FFNN) model, a custom `CifarClient` class for interfacing with Flower, and functions for training and evaluating the model. The client loads a subset of the heart disease dataset, updates its local FFNN model during training rounds, and participates in the collaborative learning process. This client script is essential to the larger FL system, designed to operate on decentralized devices, with the goal of collectively enhancing the FFNN model's accuracy while maintaining data privacy.

### Server-Side Script: Federated Learning Server for Heart Disease Prediction

The `server.py` script is the server-side component of a Federated Learning (FL) system for heart disease prediction. It uses the Flower (FLwr) framework to manage federated training across multiple clients. The script defines a Keras Feedforward Neural Network (FFNN) model, sets up the Federated Averaging (FedAvg) strategy, and includes functions for evaluation and configuration. By aggregating local updates from FL clients, the server improves the FFNN model's performance over several training rounds. The federated learning process adjusts training and evaluation configurations dynamically and visualizes the evolution of loss and accuracy across rounds. This server-side script is a key part of the distributed FL system, promoting collaborative learning for heart disease prediction.

### Instructions

1. **Navigate to the Folder**: Open the Command Prompt (cmd) in the folder containing your files.
2. **Install Necessary Tools**: Run `pip install -r requirements.txt` in the Command Prompt to install the required dependencies.
3. **Initiate Server and Client Scripts**:
   - Open another Command Prompt in the same folder.
   - Start the server script with `python server.py` to activate the server on the designated port (port 8080).
   - Open three additional Command Prompt instances (adjust based on the minimum client count set in `server.py`).
   - In each instance, run `python client.py`.

   Once all instances are running, the final results will be displayed in the server.py Command Prompt, showcasing the outcomes of each round and the overall result.

### Results

- **Accuracy Achieved**: 89.98%
- **Dataset Used**: [Kaggle Heart Dataset](https://www.kaggle.com/datasets/zhaoyingzhu/heartcsv)

### Conclusion

This project marks a significant advancement in cardiovascular risk prediction by merging AI capabilities with the privacy-preserving features of Federated Learning (FL). The proposed FL model achieved high accuracy and demonstrated adaptability to various deployment scenarios, addressing gaps in existing predictive techniques. It laid the groundwork for personalized and confidential healthcare interventions, highlighting the potential of AI integration in healthcare, especially for early detection and prevention of cardiovascular diseases. The model preserved healthcare data privacy while achieving up to 89.9% accuracy.

### Future Work

Future improvements to the FL model may include exploring diverse datasets and expanding its scope to predict a broader range of medical conditions, contributing to the ongoing evolution of predictive healthcare technologies.
