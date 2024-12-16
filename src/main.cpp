#include <Arduino.h>
#include <BleMouse.h>
#include "movement_sequence.h"

// Initialize BLE mouse
BleMouse bleMouse("ESP32 HID Mouse", "Espressif", 100);

void executeSequence() {
    for (size_t i = 0; i < sizeof(sequence) / sizeof(sequence[0]); i++) {
        const MovementStep &step = sequence[i];
        switch (step.type) {
            case MovementStep::MOVE:
                // Move the mouse (relative movement)
                bleMouse.move(step.x, step.y);
                break;
            case MovementStep::LEFT_DOWN:
                // Press left mouse button
                bleMouse.press(MOUSE_LEFT);
                break;
            case MovementStep::LEFT_UP:
                // Release left mouse button
                bleMouse.release(MOUSE_LEFT);
                break;
            case MovementStep::WAIT:
                // Wait for the specified delay in milliseconds
                delay(step.delay_ms);
                break;
            default:
                // Handle any unexpected cases
                Serial.println("Unknown step type encountered.");
                break;
        }
    }
}

void setup() {
    Serial.begin(115200);
    bleMouse.begin();
    delay(2000);  // Allow time for BLE connection
}

void loop() {
    if (bleMouse.isConnected()) {
        Serial.println("Starting sequence...");
        executeSequence();
        Serial.println("Sequence complete.");
        while (true) {
            // Keep the loop idle after sequence execution
        }
    } else {
        Serial.println("Waiting for BLE connection...");
        delay(1000);
    }
}
