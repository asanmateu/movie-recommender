# Movie Recommendations System

Notebook containing a detailed exploratory data analysis and a NLP vector based recommendations system with Python3 and Scikit-Learn using a Kaggle dataset containing movies hosted by Netflix, Hulu, Prime Video, and Disney+.

Dataset: https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney / Guidance by Avinash Navlani

## 1. Dataset Exploration

![1](https://user-images.githubusercontent.com/62403518/103226745-13d4c800-492d-11eb-9cd3-1589d7b69c4a.png)


## 2. Handling Missing Values

1. Drop columns with >50% NaN values
2. Drop NaN rows
3. Reset index
4. Convert data types

![2](https://user-images.githubusercontent.com/62403518/103226733-11726e00-492d-11eb-84c9-c7dad42a99f6.png)
![3](https://user-images.githubusercontent.com/62403518/103226730-11726e00-492d-11eb-8ffd-92b9e68e059c.png)


## 3. Exploratory Data Analysis

### **Statistical exploration includes:**

1. Distribution plots
2. Distribution of movies on each streaming platform
3. Movie distributions according to:
    * Genre
    * Country
    * Language
4. IMDb distribution on each platform
5. Runtime analysis per platform and age group

![4](https://user-images.githubusercontent.com/62403518/103226729-10d9d780-492d-11eb-991b-7ed626a0cae1.png)
![5](https://user-images.githubusercontent.com/62403518/103226728-10d9d780-492d-11eb-8a6e-fbc3910e9c90.png)
![6](https://user-images.githubusercontent.com/62403518/103226727-10414100-492d-11eb-8569-547431b69769.png)
![7](https://user-images.githubusercontent.com/62403518/103226712-0d465080-492d-11eb-90d9-c313ce0e2c8a.png)
![8](https://user-images.githubusercontent.com/62403518/103226716-0e777d80-492d-11eb-8f2e-e6ab9bc17a3e.png)
![9](https://user-images.githubusercontent.com/62403518/103226719-0f101400-492d-11eb-94f7-1fe877583e8a.png)
![10](https://user-images.githubusercontent.com/62403518/103226721-0fa8aa80-492d-11eb-9039-aa708197c0ba.png)
![11](https://user-images.githubusercontent.com/62403518/103226723-10414100-492d-11eb-8b25-1c2b41c84454.png)
![12](https://user-images.githubusercontent.com/62403518/103226747-13d4c800-492d-11eb-8de3-9e62406827f8.png)
![13](https://user-images.githubusercontent.com/62403518/103226744-133c3180-492d-11eb-846f-e248dd1d5073.png)


## 4. Recommendations Systems

1. Quantitatice system
2. Quant-text hybrid system

![14](https://user-images.githubusercontent.com/62403518/103227330-6498f080-492e-11eb-9262-029cf6c9154b.png)
![15](https://user-images.githubusercontent.com/62403518/103226735-120b0480-492d-11eb-9f25-da3dcd1ad903.png)
![16](https://user-images.githubusercontent.com/62403518/103226737-120b0480-492d-11eb-8b6b-8b2c453fc025.png)
![17](https://user-images.githubusercontent.com/62403518/103227388-8c885400-492e-11eb-9516-d7a67f02920f.png)
![18](https://user-images.githubusercontent.com/62403518/103226739-12a39b00-492d-11eb-830e-5309c89fa64c.png)
![19](https://user-images.githubusercontent.com/62403518/103226740-133c3180-492d-11eb-8403-b2e290e1772a.png)
![20](https://user-images.githubusercontent.com/62403518/103226742-133c3180-492d-11eb-8aef-9d114c9d8e6b.png)
