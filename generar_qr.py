import qrcode
import os

print("Generando código QR...")

# URL de tu página en GitHub Pages
url = "https://arirodriguez001.github.io/san-valentin/"

# Crear código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Generar imagen del QR
img = qr.make_image(fill="black", back_color="white")

# Guardar en la misma carpeta donde ejecutas el script
img_path = os.path.join(os.getcwd(), "codigo_qr.png")
img.save(img_path)

print(f"Código QR guardado en: {img_path}")

# Intentar abrir la imagen automáticamente
try:
    os.startfile(img_path)  # Solo funciona en Windows
except AttributeError:
    print("No se puede abrir la imagen automáticamente en este sistema.")
