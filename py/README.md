workflow:

- create file list with 
```
flist, labels = gen_file_list() #-> get file list and list of labels
```
- load images with 
```
imgs = loadbatch(flist=flist)
```
at this point shold be imgs.shape -> Nimgs, Nrows, Ncols, 3

- feed imgs and labels to neural network 
