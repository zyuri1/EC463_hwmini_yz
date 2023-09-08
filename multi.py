import machine
import time
import _thread

# Pin definitions
LED_PIN = machine.Pin(25, machine.Pin.OUT)
BUTTON_PIN = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
LIGHT_SENSOR_PIN = machine.ADC(machine.Pin(26))

lock = _thread.allocate_lock()

results = []

def measure_response_time():
    while True:
        LED_PIN.on()
        start_time = time.ticks_ms()
        light_sensor_value_when_led_on = LIGHT_SENSOR_PIN.read_u16()

        while BUTTON_PIN.value() == 1:
            pass

        end_time = time.ticks_ms()
        light_sensor_value_when_button_pressed = LIGHT_SENSOR_PIN.read_u16()
        LED_PIN.off()

        response_time = end_time - start_time
        
        with lock:
            results.append((response_time, light_sensor_value_when_led_on, light_sensor_value_when_button_pressed))
        time.sleep(5)

_thread.start_new_thread(measure_response_time, ())

try:
    while True:
        with lock:
            for r in results:
                print("Response Time:", r[0], "ms")
                print("Light Sensor Value when LED ON:", r[1])
                print("Light Sensor Value at Button Press:", r[2])
                print("----------")
            results.clear()  # Clear after printing
        time.sleep(5)
except KeyboardInterrupt:
    pass

