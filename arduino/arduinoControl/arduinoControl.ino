/*
 * Created Date: Sunday, November 14th 2021
 * Author: Pawel Kremienowski
 * Author email: Kremienowski33@gmail.com
 * -----
 * Last modified: 
 * Modified by: Pawel Kremienowski
 */

const int BLUE_DIODE = 2;
const int RED_DIODE = 3;
const int YELLOW_DIODE = 4;

const String BLUE_ON = "b'blue on'";
const String RED_ON = "b'red on'";
const String YELLOW_ON = "b'yellow on'";
const String DIODES_OFF = "b'diodes off'";

String received = "";

void setup()
{
    Serial.begin(9600);
    pinMode(BLUE_DIODE, OUTPUT);
    pinMode(RED_DIODE, OUTPUT);
    pinMode(YELLOW_DIODE, OUTPUT);

    // turning off diodes at beggining
    turnAllDiodesOff();
}

void loop()
{
    if (Serial.available() > 0)
    {
        received = Serial.readStringUntil('\n');
        diodesAction(received);
    }

    delay(100);
}

void diodesAction(String command)
{
    if (command.equals(BLUE_ON))
    {
        digitalWrite(BLUE_DIODE, HIGH);
    }
    else if (command.equals(RED_ON))
    {
        digitalWrite(RED_DIODE, HIGH);
    }
    else if (command.equals(YELLOW_ON))
    {
        digitalWrite(YELLOW_DIODE, HIGH);
    }
    else if (command.equals(DIODES_OFF))
    {
        turnAllDiodesOff();
    }
    else
    {
        Serial.println("diodes action NONE");
    }
}

void turnAllDiodesOff()
{
    digitalWrite(BLUE_DIODE, LOW);
    digitalWrite(RED_DIODE, LOW);
    digitalWrite(YELLOW_DIODE, LOW);
}