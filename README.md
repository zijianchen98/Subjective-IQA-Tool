# Subjective-IQA-Tool
An image quality assessment scoring tool

## Introduction
It can be used for subjects to subjectively rate images and is able to output the score in ".txt" format.
![Overview of the interface](https://github.com/zijianchen98/Subjective-IQA-Tool/blob/main/overview.png)

## Requirement
```
python>=3.7
pillow>=9.4.0
tkinter within the python
The monitor resolution of this version is >= 2560x1440 
```

## Getting Started
### Usage
Enter this command on the command line
```
python Subjective-IQA-Tool.py
```
### Steps
First, change the `FilePath` in  `Subjective-IQA-Tool.py` to your own image folder. Then, execute `python Subjective-IQA-Tool.py`. After entering the UI and clicking the `Begin test` button, you can start scoring the first image. 
```
Drag the slider and click the `Submit` button
Click the `next image` button
Drag the slider and click the `Submit` button
......

```
### Interface modification
The place and size of each component can be modified in the code to fit your monitor
```
Resolution of the interface: root.geometry('2560x1440')
Button, Text, and Slider
```

## Output
The output is a ".txt" file
```
image_path:score
1.png:46.8
2.png:28.2
3.png:44.0
```


## Citation
**If you use this tool in your research, please cite**:
```
@inproceedings{
  
}
```
