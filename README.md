# ESP32 Mouse HID Simulator

Este proyecto utiliza un microcontrolador ESP32 para simular un dispositivo de interfaz humana (HID) USB, concretamente un ratón. El objetivo principal es replicar interacciones humanas con el ratón en un entorno web, proporcionando una herramienta útil para pruebas automatizadas o simulaciones.

## Características
- Emulación de un dispositivo HID USB tipo ratón.
- Soporte para movimientos, clics y desplazamiento.
- Implementado en C++ y Python utilizando PlatformIO como entorno de desarrollo.

## Requisitos
1. **Hardware**:
   - Microcontrolador ESP32 compatible con USB HID.
   - Cable USB.
2. **Software**:
   - [PlatformIO](https://platformio.org/) instalado en VS Code.
   - Python 3.x.

## Instalación y Configuración
1. Clona este repositorio:
   ```bash
   git clone https://github.com/Lilmouse16/esp32_mouse_hid_simulator.git
   ```
2. Abre el proyecto en Visual Studio Code con la extensión PlatformIO instalada.
3. Configura el entorno según tu modelo de ESP32.
4. Carga el código en tu ESP32 usando el comando de PlatformIO:
   ```bash
   pio run --target upload
   ```
5. Configura los scripts en Python según la interacción deseada.

## Uso
1. Conecta el ESP32 a tu computadora vía USB.
2. Ejecuta el script de Python o personaliza el comportamiento desde el firmware.
3. Observa la simulación de movimientos y clics del ratón en el navegador web.

## Aplicaciones
- Pruebas automatizadas en interfaces web.
- Simulación de interacciones humanas.
- Desarrollo y depuración de herramientas de accesibilidad.

## Contribuciones
Si tienes ideas o mejoras para este proyecto, no dudes en abrir un *issue* o enviar un *pull request*.

## Licencia
Este proyecto está licenciado bajo la [MIT License](LICENSE).

---
