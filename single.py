import machine
import time

# Define pins
LED_PIN = machine.Pin(25, machine.Pin.OUT)
BUTTON_PIN = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
LIGHT_SENSOR_PIN = machine.ADC(machine.Pin(26))

def measure_response_time():
    LED_PIN.on()  # Turn the LED on
    start_time = time.ticks_ms()
    light_sensor_value_when_led_on = LIGHT_SENSOR_PIN.read_u16()
    
    while BUTTON_PIN.value() == 1:  # Wait for button press
        pass
    
    end_time = time.ticks_ms()
    light_sensor_value_when_button_pressed = LIGHT_SENSOR_PIN.read_u16()
    LED_PIN.off()  # Turn the LED off
    
    response_time = end_time - start_time
    return response_time, light_sensor_value_when_led_on, light_sensor_value_when_button_pressed

# Main loop
for _ in range(10):  # Take 10 measurements
    time.sleep(5)  # Wait for 5 seconds between measurements
    response, light_on, light_press = measure_response_time()
    print("Response Time:", response, "ms")
    print("Light Sensor Value when LED ON:", light_on)
    print("Light Sensor Value at Button Press:", light_press)

