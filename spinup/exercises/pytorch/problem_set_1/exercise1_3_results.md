# Results for my exercise 1.3 TD3 implementation

# HalfCheetah-v2
|           Property|            Value|
|-------------------|-----------------|
|             Epoch |              10 |
|      AverageEpRet |             421 |
|          StdEpRet |            43.1 |
|          MaxEpRet |             493 |
|          MinEpRet |             326 |
|  AverageTestEpRet |             488 |
|      StdTestEpRet |            26.4 |
|      MaxTestEpRet |             517 |
|      MinTestEpRet |             421 |
|             EpLen |             150 |
|         TestEpLen |             150 |
| TotalEnvInteracts |           4e+04 |
|     AverageQ1Vals |            11.7 |
|         StdQ1Vals |            25.8 |
|         MaxQ1Vals |            87.9 |
|         MinQ1Vals |           -48.9 |
|     AverageQ2Vals |            11.7 |
|         StdQ2Vals |            25.8 |
|         MaxQ2Vals |            88.6 |
|         MinQ2Vals |           -48.6 |
|            LossPi |           -13.6 |
|             LossQ |            9.23 |
|              Time |             433 |

# InvertedPendulum-v2
|           Property|            Value|
|-------------------|-----------------|
|             Epoch |              10 |
|      AverageEpRet |             150 |
|          StdEpRet |               0 |
|          MaxEpRet |             150 |
|          MinEpRet |             150 |
|  AverageTestEpRet |             150 |
|      StdTestEpRet |               0 |
|      MaxTestEpRet |             150 |
|      MinTestEpRet |             150 |
|             EpLen |             150 |
|         TestEpLen |             150 |
| TotalEnvInteracts |           4e+04 |
|     AverageQ1Vals |            40.5 |
|         StdQ1Vals |            18.8 |
|         MaxQ1Vals |            57.6 |
|         MinQ1Vals |           -3.26 |
|     AverageQ2Vals |            40.5 |
|         StdQ2Vals |            18.8 |
|         MaxQ2Vals |            57.6 |
|         MinQ2Vals |           -3.56 |
|            LossPi |           -44.7 |
|             LossQ |            5.21 |
|              Time |             427 |

# Walker2d-v2
Something interesting I observed was a peak in average episode return on epoch 6 of 176. The return diminished as training progressed. From 176 to 152 to 104, then increasing on epoch 9 to 129 and finally the average return was 139 on epoch 10. I'm unsure what cased this dip in performance in the second half of training. 
|           Property|            Value|
|-------------------|-----------------|
|             Epoch |              10 |
|      AverageEpRet |             139 |
|          StdEpRet |            59.9 |
|          MaxEpRet |             291 |
|          MinEpRet |            92.4 |
|  AverageTestEpRet |             151 |
|      StdTestEpRet |            77.6 |
|      MaxTestEpRet |             316 |
|      MinTestEpRet |            72.8 |
|             EpLen |             109 |
|         TestEpLen |             107 |
| TotalEnvInteracts |           4e+04 |
|     AverageQ1Vals |            56.4 |
|         StdQ1Vals |            18.9 |
|         MaxQ1Vals |             142 |
|         MinQ1Vals |            -120 |
|     AverageQ2Vals |            56.4 |
|         StdQ2Vals |            18.9 |
|         MaxQ2Vals |             134 |
|         MinQ2Vals |            -125 |
|            LossPi |           -59.4 |
|             LossQ |            33.2 |
|              Time |             437 |
