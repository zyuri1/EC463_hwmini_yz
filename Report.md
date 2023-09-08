The objective of this experiment was to design a measurement system on the Raspberry Pi Pico using MicroPython to gauge human response time when prompted by an LED flash. Two distinct methodologies were explored: a single-threaded approach and a cooperative multitasking method. The former, while straightforward, provided a linear and simple-to-understand execution flow. The cooperative multitasking method, though slightly more complex, introduced flexibility by allowing concurrent monitoring of results and capturing new measurements. Despite the Raspberry Pi Pico possessing dual cores, the current MicroPython implementation as of September 2021 utilizes only one. Thus, true parallel execution remains a challenge. In summary, both methodologies offer viable solutions, with the choice largely dependent on the specific application's requirements and the desired data collection frequency.

Single thread measurments: 
MPY: soft reboot
Response Time: 207 ms
Light Sensor Value when LED ON: 8866
Light Sensor Value at Button Press: 17988
Response Time: 214 ms
Light Sensor Value when LED ON: 8914
Light Sensor Value at Button Press: 17796
Response Time: 207 ms
Light Sensor Value when LED ON: 8594
Light Sensor Value at Button Press: 17700
Response Time: 207 ms
Light Sensor Value when LED ON: 8578
Light Sensor Value at Button Press: 17924
Response Time: 186 ms
Light Sensor Value when LED ON: 8802
Light Sensor Value at Button Press: 17812
Response Time: 213 ms
Light Sensor Value when LED ON: 8834
Light Sensor Value at Button Press: 17860

Multithread measurments: 
MPY: soft reboot
Response Time: 3036 ms
Light Sensor Value when LED ON: 8177
Light Sensor Value at Button Press: 17172
----------
Response Time: 231 ms
Light Sensor Value when LED ON: 8482
Light Sensor Value at Button Press: 17908
----------
Response Time: 221 ms
Light Sensor Value when LED ON: 8770
Light Sensor Value at Button Press: 17572
----------
Response Time: 196 ms
Light Sensor Value when LED ON: 8498
Light Sensor Value at Button Press: 17764
----------
Response Time: 212 ms
Light Sensor Value when LED ON: 8578
Light Sensor Value at Button Press: 17748
----------
Response Time: 202 ms
Light Sensor Value when LED ON: 8706
Light Sensor Value at Button Press: 17572
----------