# predict-the-lotery 🍀

## This is a little experiment to predict "La Tinka" lottery using DBSCAN algorithm 

#### 📢 Disclaimer 📢
  This is ONLY an experiment, it is not by any means something that allows you to predict the results of any lottery game. This is obviously a wrong thing to predict. Lotteries in general made a huge effort to prove that their process is actually random. If the lottery is doing its job, it will be impossible.
  The only way that lottery results are predictable is if they are tampering with the result and you *discover* the method.

## Why did you do it?
I was bored  🫤

## What did I do?
1. With `extractor.py` I scrapped the cumulative frequency table for the 46 balls for 2022 from the *Tinka* website and saved it in `raw_data.html`.
2. Then, I execute `loader.py` to clean the data and convert it and dump it in `tinka.csv`.
3. `grid_plot.py` creates a heatmap for the cumulative frequency  `tinka_945_2022_12.png`, just to see if the geometric distribution of the numbers on the card when you play has some pattern 🤨 (i didn't see any, maybe you know better).
4. Using the frequencies as weights, `process.py` generates 1000 rows of 6-number sequences without replacement (to simulate lottery trials).
5. Finally, `predictor.py` use DBSCAN to detect clusters and returns the `model.components_` of each cluster (Maybe the centroid is a better option).
6. Everything is orchestrated by the `main.py` script, using the `subprocess` module. I also include a `run.bat` script because Windows was annoying me with permissions on my own laptop 🙃
7. I also included a `param_extractor.py` script to help to select the best values for `eps` and `min_samples`, calculating the number of clusters, size and a number of outliers.

## Why so many scripts?
I hate monolitic scripts 😶

## Final comments
- Remember, this is more numerology than anything else 🙊
- 100% PYTHON 3.10.9 🐍
- I'm sure that you can use other methods, maybe Markov Chains or an RNN 🎯
- Some results????

```
python predictor.py 

Number of clusters: 5
Number of outliers: 278
Cluster 0: 655 points, center: [35. 27. 25. 12.  9. 10.]
Cluster 1: 50 points, center: [ 7. 17. 13.  6. 41. 18.]
Cluster 2: 6 points, center: [44. 38. 11. 16. 31. 32.]
Cluster 3: 7 points, center: [15. 28. 41. 26.  8. 25.]
Cluster 4: 4 points, center: [16. 38. 27. 14. 10. 21.]

Process finished with exit code 0
```

