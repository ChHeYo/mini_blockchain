# mini_blockchain

This is a mini-sized blockchain. <br/>
The blockchain module has three key components - transaction, block and blockchain classes. <br/>
You can run the simulation by running the 'main.py' file.

```python
python main.py
```

<br/>

### Things to Note:

* Usually transactions are in JSON format but this project does not include distributed system (or at least not yet)
* Each block and each transaction has merkle root so that it not only serves as an id for each block but strengthens integrity of transactions
* Blockchain starts with the genesis block which will be automatically created whenever it is instantiated

<br/>

### ScreenShot

![Screenshot](https://github.com/ChHeYo/mini_blockchain/blob/master/raw/demo_shot.png)
