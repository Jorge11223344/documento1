from docx import Document

# Cargar plantilla
doc = Document("Contrato_Plantilla.docx")

# Datos de ejemplo
datos = {
    "FECHA": "28 de junio de 2025",
    "NOMBRE_PRESTAMISTA": "Jorge Iván Muñoz Acuña",
    "RUT_PRESTAMISTA": "10679836-2",
    "DIRECCION_PRESTAMISTA": "Av. Laguna Grande 1120 casa 36, San Pedro de la Paz",
    "NOMBRE_REPRESENTANTE": "Jorge Iván Muñoz Acuña",
    "NOMBRE_EMPRESA": "JIMACOMEX SpA",
    "RUT_EMPRESA": "76.146.748-0",
    "DIRECCION_EMPRESA": "Av. Laguna Grande 1120 casa 36, San Pedro de la Paz",
    "MONTO": "$10.000.000",
    "PLAZO": "12 meses",
    "FECHA_VENCIMIENTO": "28 de Junio de 2025",
    "FORMA_PAGO": "transferencia electrónica",
    "BANCO": "Banco Chile",
    "TIPO_CUENTA": "Cuenta Corriente",
    "NUMERO_CUENTA": "2280528105",
    "INTERES": "no devengará intereses",
    "INTERES_MORA": "2%",
}

# Reemplazar etiquetas
for p in doc.paragraphs:
    for key, value in datos.items():
        if f"{{{{{key}}}}}" in p.text:
            p.text = p.text.replace(f"{{{{{key}}}}}", value)

# Guardar contrato final
doc.save("Contrato_Mutuo_Completado.docx")
print("Contrato generado correctamente.")
